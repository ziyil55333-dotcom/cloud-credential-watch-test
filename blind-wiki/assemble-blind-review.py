"""Assemble v17 blind-review inputs from the authorized MediaWiki run."""

import argparse
import csv
import io
import json
from pathlib import Path
from tempfile import NamedTemporaryFile
from urllib.parse import urlsplit
from zipfile import BadZipFile, ZipFile


def metadata(source, filename):
    if source.suffix.casefold() == ".zip":
        with ZipFile(source) as archive:
            entries = [entry for entry in archive.infolist() if entry.filename == filename]
            if len(entries) != 1 or entries[0].file_size > 65536:
                raise ValueError(f"Expected one metadata file named {filename} in the ZIP.")
            data = archive.read(entries[0])
    else:
        path = source / filename if source.is_dir() else source
        data = path.read_bytes()
    return json.loads(data.decode("utf-8-sig"))


def build_config(five, wiki_source, destination):
    config = json.loads(five.read_text(encoding="utf-8-sig"))
    assets = config["assets"]
    kinds = {"github", "gitee", "article", "oci", "apk"}
    if len(assets) != len(kinds) or {asset["kind"] for asset in assets} != kinds:
        raise ValueError("The five-source configuration must contain each registered kind once.")
    wiki = metadata(wiki_source, "wiki-asset.json")
    endpoint = urlsplit(wiki["url"])
    if (wiki["kind"], wiki["id"], wiki["page_id"]) != ("wiki", "blind-wiki", 2) or (
        endpoint.scheme != "https" or not endpoint.hostname
        or endpoint.path != "/api.php" or endpoint.username is not None
        or endpoint.query or endpoint.fragment
    ):
        raise ValueError("Expected the HTTPS API for asset blind-wiki and page ID 2.")
    assets.append(wiki)
    if len({asset["id"] for asset in assets}) != len(assets):
        raise ValueError("The six asset IDs must be distinct.")
    config.update(state_dir=".state-blind-first", engine="combined", offline=False)
    content = json.dumps(config, ensure_ascii=False, indent=2) + "\n"
    try:
        with destination.open("x", encoding="utf-8", newline="\n") as output:
            output.write(content)
    except FileExistsError:
        if json.loads(destination.read_text(encoding="utf-8-sig")) != config:
            raise ValueError("An existing configuration differs. Keep it and use a new review directory.")
    print(f"Six registered assets written to {destination}.")


def add_wiki_receipts(metadata_source, ledger):
    if not metadata_source.is_dir() and metadata_source.suffix.casefold() != ".zip":
        raise ValueError("Use the release-metadata ZIP or its extracted directory.")
    versions = {}
    prior = 0
    for number in range(1, 25):
        name = f"wiki-{number:02d}"
        page, = metadata(metadata_source, f"{name}.json")["query"]["pages"]
        revision, = page["revisions"]
        rev_id = revision["revid"]
        if page["pageid"] != 2 or type(rev_id) is not int or rev_id <= prior:
            raise ValueError(f"{name} must identify page 2 and a strictly newer revision.")
        versions[name] = str(rev_id)
        prior = rev_id

    original = ledger.read_bytes()
    reader = csv.DictReader(io.StringIO(original.decode("utf-8-sig"), newline=""))
    rows = list(reader)
    if reader.fieldnames != ["channel", "planned_version", "actual_version"]:
        raise ValueError("Use the original three-column receipts.csv from the review kit.")
    wiki_rows = [row for row in rows if row["channel"] == "wiki"]
    if len(wiki_rows) != len(versions) or {row["planned_version"] for row in wiki_rows} != set(versions):
        raise ValueError("The ledger must contain one row per planned Wiki revision.")
    for row in wiki_rows:
        version = versions[row["planned_version"]]
        if row["actual_version"] not in ("", version):
            raise ValueError(f"{row['planned_version']} already refers to a different revision.")
        row["actual_version"] = version
    with NamedTemporaryFile("w", encoding="utf-8-sig", newline="", dir=ledger.parent, delete=False) as file:
        draft = Path(file.name)
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    try:
        if ledger.read_bytes() != original:
            raise ValueError("The ledger changed while it was being read. Close the spreadsheet and retry.")
        if draft.read_bytes() != original:
            draft.replace(ledger)
    finally:
        draft.unlink(missing_ok=True)
    print(f"Checked 24 Wiki revision IDs in {ledger}. Other entries are unchanged.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    config = commands.add_parser("config", help="merge the five-source config and current Wiki asset")
    config.add_argument("five_config", type=Path)
    config.add_argument("wiki_source", type=Path, help="wiki-ready ZIP, extracted directory, or wiki-asset.json")
    config.add_argument("output", type=Path)
    receipts = commands.add_parser("receipts", help="fill the 24 Wiki rows in the existing CSV")
    receipts.add_argument("wiki_metadata", type=Path, help="revision metadata ZIP or extracted directory")
    receipts.add_argument("ledger", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "config":
            build_config(args.five_config, args.wiki_source, args.output)
        else:
            add_wiki_receipts(args.wiki_metadata, args.ledger)
    except (BadZipFile, KeyError, OSError, TypeError, ValueError) as exc:
        parser.exit(2, f"{exc}\n")


if __name__ == "__main__":
    main()
