# MediaWiki 独立盲测操作

工作流在专用分支 `codex/blind-wiki` 上运行。公网入口仅供读取当前测试页和修订，写入由隔离的 GitHub Actions 作业内完成。每次运行的临时地址都会变化，作业退出后失效。请在评审人可以同步扫描的时段启动。

## 基线复查

在专用分支修改 `blind-wiki/request.json`，设置 `"mode": "baseline"`。每次可更新 `run_id`，便于在提交历史区分运行。等待 Actions 作业出现 `wiki-ready-` 开头的制品。下载其中的 `wiki-asset.json`，追加到五入口配置的 `assets`。这个模式只保留约两分钟的公开基线读取窗口。先把文件和 v17 程序准备好，再启动。

## 正式投放

1. 由独立评审人完成样本选择、预期标签和版本计划。MediaWiki 的固定资产 ID 为 `blind-wiki`，计划编号为 `wiki-01` 至 `wiki-24`，位置文件名为 `page-2.wiki`。工作流会先确认页面 ID 为 2，再允许投放。标签和预期答案由评审人私下保管。
2. 准备 24 个 UTF-8 文本文件 `blind-wiki/revisions/wiki-01.wiki` 至 `wiki-24.wiki`，每个对应一项计划发布。仅使用未签发、无访问能力的合成样本，按本次计划在文件中放置正例与该版分配的负例。保留原有内容和行号。工作流会在末尾追加一行版本注释。
3. 核对六入口并封存标签。确定开始后，由持有发布权限的一方把 24 个文件和 `"mode": "blind"` 的 `blind-wiki/request.json` 提交到专用分支。盲测样本目录公开可读，封存清单与预期标签保留在评审电脑。
4. 在运行的 Actions 页面下载 `wiki-ready-` 制品，把其中的 `wiki-asset.json` 作为本轮 MediaWiki 的配置项，加到五入口配置。启动正式扫描后检查干净修订可读取。就绪制品上传后会预留 8 分钟，然后开始投放。未赶上准备窗口时，按原样保留记录，另开一轮。
5. 24 个新修订完成后，下载 `wiki-blind-revision-metadata`。把各个 `wiki-XX.json` 中的 `query.pages[0].revisions[0].revid` 填到对应的 `receipts.csv` 行。保存实际扫描导出的 `alerts.json` 与 `events.json`。作业结束后临时链接不可用，因此投放期间需核对告警定位。

## 用一条命令合并配置或导入回执

把[五入口配置](https://github.com/ziyil55333-dotcom/cloud-credential-watch-test/blob/codex/review-handoff/review-handoff/five-baseline-preflight.json)、脚本和本次下载的制品放到评审目录。将就绪制品在本地命名为 `wiki-ready.zip`。在评审目录打开 PowerShell 并执行第一条命令。启动扫描前核对本轮 Wiki 的地址和页面 ID。已有内容不同的 `blind-config.json` 时，先保留旧批次，再另开评审目录。

```powershell
py -3.12 .\assemble-blind-review.py config .\five-baseline-preflight.json .\wiki-ready.zip .\blind-config.json
```

投放结束后，将修订制品在本地命名为 `wiki-blind-revision-metadata.zip`，关闭正打开 `receipts.csv` 的表格，再执行第二条命令。脚本核对同一页面的 24 个递增修订号，只填写 Wiki 行。已有不一致的回执或缺失修订时保留原始 CSV。

```powershell
py -3.12 .\assemble-blind-review.py receipts .\wiki-blind-revision-metadata.zip .\receipts.csv
```

[合并与导入脚本](assemble-blind-review.py)

在 `baseline` 模式下看到零告警，只能用于基线核对。正式盲测由评审人选择、封存、监督投放并交回首轮记录。

