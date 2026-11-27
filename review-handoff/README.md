# 独立评审交接站

这里记录云上凭据泄露检测与响应系统 v17 的评审进度。评审人从本页领取任务，并在 [results](results/) 登记进度、代发请求和结果。任务和证据都在 GitHub 交接。




| 任务 | 状态 | 已有证据或下一步 |
| --- | --- | --- |
| `github-public-retest` | 已核验 | 告警命中本次公开提交的指定位置，检测时延区间为 14.278–21.947 秒。[公开提交](https://github.com/ziyil55333-dotcom/cloud-credential-watch-test/commit/b7f60a7a4f1e1e72753d8bcc012fe1748ceb0d24) |
| `extension-review` | 已核验 | 公告源接入的三轮告警数为 0、1、1，首次告警时间和核心代码指纹核对通过。 |
| `blind-review` | 已封存，待启动观察 | 从本页第 3 节继续，按本轮同步安排投放并交回证据。[六入口准备记录](blind-assets-2026-11-25.md) |

## 给 Codex 的一条指令

> 请读取本仓库 `codex/review-handoff` 分支下 `review-handoff/README.md` 的最新版，查看当前批次的最新回执和项目方回复，从第一个未完成的步骤继续执行。完成进度、代发请求和复核文件直接提交到该批次的 GitHub 目录。需要我本人确认样本、签认或获得发布权限时，说明具体缺项并留在 GitHub 回执。

## 当前批次 `blind-20261126-172420`

评审人已于 2026-11-26 18:03（北京时间）封存。本轮 24 个 APK 已构建并通过签名校验。实际投放 **0/144**，MediaWiki 正式作业和六入口观察待启动。按 [11 月 27 日 19:00–22:00（北京时间）同步安排](results/blind-review/blind-20261126-172420/project-rollout-2026-11-27.md)从第 3 节继续。 [封存回执](results/blind-review/blind-20261126-172420/zhoumouai-blind-review-2026-11-26-preseal.md#封存及同步窗口) · [技术准备回执](results/blind-review/blind-20261126-172420/zhoumouai-blind-review-2026-11-26-operations-ready.md)

### 1. 恢复本轮工作目录

- 沿用本轮的本机登记目录和原始 v17 评审包。打开 v17 源码根目录运行命令。优先使用这一轮已能运行的 Python 环境。在 PowerShell 中，把 `$ReviewDir` 设为已有登记目录的绝对路径，把 `$Py` 设为该环境的 Python 可执行文件绝对路径。核对 `$ReviewDir` 内确实有 `sources.csv`、`releases.csv`、`labels.csv`、`receipts.csv` 和 `assemble.py`。
- 读取本轮的现有 CSV、配置及封存文件，先判断真实进度。已有 `seal.json` 的批次沿用封存版本。封存后的标签或扫描源码有变更时，保留原批次并另开一轮。
- 参考[六入口准备记录](blind-assets-2026-11-25.md)和[五入口配置](five-baseline-preflight.json)。`sources.csv` 登记 `blind-github`、`blind-gitee`、`blind-wiki`、`blind-article`、`blind-oci`、`blind-apk`，每个 ID 对应一个已登记的测试入口。

### 2. 评审人确认样本并封存

1. 只测试自有或授权的资产。样本全部使用未签发、无访问权限的合成值。Codex 可以辅助生成和整理，评审人本人选定样本并核对预期类型、正负标签、文件和行号。
2. 六入口各 24 个计划版本，共 144 次发布。12 类各选 10 个不同的正例身份，共 120 个。任选 24 个身份在另一发布中各复用一次，用相同合成值和 `unique_id`，形成 144 个正例位置，每次发布一个。再安排 120 个负例位置，覆盖全部 12 类。每种正例类型至少出现在两个入口。
3. `labels.csv` 填 `kind`、相对 `path`、从 1 开始的 `line`，正例另填 `unique_id`。`releases.csv` 保留 144 个计划编号。`receipts.csv` 的实际版本发布后填。类型名沿用评审包的《凭据类型清单》。OCI 先在本机核对实际层摘要和包内路径。APK 先核对实际包内路径。MediaWiki 路径固定为 `page-2.wiki`。
4. 评审人核对无误后，从 v17 源码根目录运行下列命令。两条命令均成功才算封存。把 `seal.json` 里的 `sealed_at` 和 `manifest_sha256` 记到 GitHub 回执。盲测答案和封存原件留在评审人本机，等整轮首次扫描结束后再提交。

```powershell
& $Py (Join-Path $ReviewDir 'assemble.py') $ReviewDir labels
if ($LASTEXITCODE -ne 0) { throw '标签表校验失败' }
& $Py -m credential_watch.assessment seal $ReviewDir --reviewer zhoumouai
if ($LASTEXITCODE -ne 0) { throw '封存未完成' }
Get-Content -Raw -Encoding UTF8 -LiteralPath (Join-Path $ReviewDir 'seal.json')
```

### 3. 协调发布并启动首次观察

- 在本批次回执追加封存时间、摘要、可同步操作的北京时间。GitHub 由评审人在专用分支投放。Gitee、文章、OCI 和 APK 如需项目方代发，写明入口、计划编号和具体操作。只有观察就绪后才交接可公开的投放文件，交接分支不作为扫描目标。
- MediaWiki 先在本机备齐 `wiki-01` 到 `wiki-24` 的 24 个 UTF-8 文件。待项目方和评审人确认同步窗口后，在专用分支提交本轮材料及 `mode=blind` 请求。按[MediaWiki 操作说明](https://github.com/ziyil55333-dotcom/cloud-credential-watch-test/blob/codex/blind-wiki/blind-wiki/blind-review.md)下载 `wiki-ready` 制品、合并六入口配置、确认页面 ID 为 2，并在预留的 8 分钟内启动扫描。正式投放期间核对 Wiki 定位，作业结束后临时地址失效。
- 合并后的 `blind-config.json` 应含六个资产并使用该批次的干净相对状态目录。用以下命令扫描干净基线，检查六个入口均读取成功且 `alerts.json` 为 `[]`。有失败或已出现测试样本时，在回执标出原因。基线通过后启动常驻扫描，并在回执写明已就绪，再安排各入口投放。

```powershell
$BlindConfig = Join-Path $ReviewDir 'blind-config.json'
& $Py -m credential_watch serve --config $BlindConfig --once
if ($LASTEXITCODE -ne 0) { throw '基线扫描失败' }
& $Py -m credential_watch export --config $BlindConfig --output (Join-Path $ReviewDir 'blind-baseline')
if ($LASTEXITCODE -ne 0) { throw '基线证据未导出' }
Get-Content -Encoding UTF8 -LiteralPath (Join-Path $ReviewDir 'blind-baseline/alerts.json')
```

基线核对完成后，在 v17 源码根目录启动并保持此窗口运行。

```powershell
& $Py -m credential_watch serve --config $BlindConfig
```

### 4. 投放并登记实际版本

按 `releases.csv` 在目标入口发布本次的合成材料，记录时间，将实际版本填回 `receipts.csv`。手工发布的入口逐次推进，每次核对扫描记录中的资产 ID、版本和处理结果。失败、超时、漏报均保留原始记录。有自动定时投放的 Wiki，保存作业制品和每版扫描结果。

| 入口 | 实际版本或定位 |
| --- | --- |
| GitHub、Gitee | 完整 40 位提交 SHA。文件位置写仓库内相对路径。 |
| MediaWiki | 本次作业的数字修订 ID。用修订制品导入 `receipts.csv`，路径为 `page-2.wiki`。 |
| 文章 | `条目ID@sha256:正文摘要`。按发布后的 HTML 字节计算 SHA-256，行号按源文。 |
| OCI | 实际推送的镜像清单摘要。标签路径仍使用 `层摘要:包内路径`。 |
| APK | `版本号@sha256:制品摘要`。版本号、URL 与 SHA-256 均以当次发布索引为准。 |

### 5. 提交首轮复核文件和回执

核对每个入口预定发布 24 次及其实际版本，结束常驻观察。立即导出首次运行并编译回执。实际发布或扫描有缺口时先保留现场证据，在 GitHub 回执注明计划编号和原因。

```powershell
& $Py -m credential_watch export --config $BlindConfig --output $ReviewDir
if ($LASTEXITCODE -ne 0) { throw '首轮告警未导出' }
& $Py (Join-Path $ReviewDir 'assemble.py') $ReviewDir receipts
if ($LASTEXITCODE -ne 0) { throw '实际版本回执不齐或不一致' }
```

整轮首次扫描结束后，评审人逐项检查文件可公开，再将以下复核文件提交到[本批次目录](results/blind-review/blind-20261126-172420/)。`manifest.json`、`seal.json`、`receipts.json`、`alerts.json` 保持首次执行原样。附上可公开的 `events.json` 和四张填好的 CSV。回执写明六入口各自的实际发布数、扫描成功数、失败或未执行数、缺项及文件链接。项目方从该目录直接读取并回填核验结果。

仓库和提交历史公开可读。凭据原值、登录信息、`.state` 缓存、本机绝对路径及其他非公开内容留在本机。不能公开的必需文件在回执注明缺项，并保留原件供后续核对。 [回执与复核文件要求](results/README.md)
