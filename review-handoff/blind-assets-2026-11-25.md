# 盲测资产准备记录

2026-11-25 项目方预检。六个入口均已从公网读取并完成干净基线扫描，告警数均为零。下载 [五入口配置](five-baseline-preflight.json)，再按下文从本轮 MediaWiki 作业下载临时配置，合并为正式六入口配置。


| 入口 | 本次登记位置 | 基线版本 |
| --- | --- | --- |
| GitHub | [专用分支 `codex/blind-github`](https://github.com/ziyil55333-dotcom/cloud-credential-watch-test/tree/codex/blind-github) | `8b05f6e40bcf85d8eb8fc38e1345e2da96a66a29` |
| Gitee | [专用分支 `codex/blind-gitee`](https://gitee.com/n123_40_1/cloud-credential-watch-gitee-fixtures/tree/codex/blind-gitee) | `01da4ea6536815472a8d838ad5e272ad91bec9d9`，标签 `blind-clean-baseline-20261125` |
| APK | [专用发布目录](https://github.com/ziyil55333-dotcom/cloud-credential-watch-test/tree/codex-blind-apk/apk-acceptance)，[发布索引](https://raw.githubusercontent.com/ziyil55333-dotcom/cloud-credential-watch-test/codex-blind-apk/apk-acceptance/releases.json) | `1.0.0@sha256:804b3f4f2dbc80931de050056cad4e41bb2647e9ba9665e316d201ee2d80e02b` |
| 文章 | [独立 RSS](https://ziyil55333-dotcom.github.io/cloud-credential-watch-public-fixtures/blind-article/feed.xml)，发布目录 `blind-article/` | `blind-article-baseline@sha256:dab264c7085b29913f0c708078c00618e574c4c680e776a750ad5dd212b2a87f` |
| OCI | `https://ghcr.io/v2/ziyil55333-dotcom/cloud-credential-watch-public-fixtures`，标签 `blind-eval` | `sha256:0b7d7340cecda072b4a98ccc9030d8f04046220ee1fb1543900bc25d947144fc`，[发布记录](https://github.com/ziyil55333-dotcom/cloud-credential-watch-public-fixtures/actions/runs/45588441120) |
| MediaWiki | [专用分支与启动说明](https://github.com/ziyil55333-dotcom/cloud-credential-watch-test/tree/codex/blind-wiki/blind-wiki)，[空白基线复测](https://github.com/ziyil55333-dotcom/cloud-credential-watch-test/actions/runs/45592140742) | 页面 ID `2`，本次空白修订 `2`；正式运行生成新的临时 API |

## 正式评审与发布分工

1. **评审人先登记。** 按手册核对当前基线、发布人和权限，确认独立选择的合成样本与预期答案。封存后再启动当轮观察和正式投放。GitHub、APK 和 MediaWiki 使用上表登记的专用分支。Gitee、文章和 OCI 可由项目方已具权限的发布人协助。

2. **需要代发时。** 在 [回执目录](results/) 提交脱敏进度，注明渠道、批次、计划版本或数量，以及需要代办的操作。评审人仅通过私下渠道交付需投放的合成文件，自己保管标准答案和封存材料。发布人按评审人指定的顺序操作，并回传实际版本标识和发布时间。

3. **MediaWiki 在本轮启动。** 封存后，按上表的启动说明提交本轮 24 份合成文件和 `mode=blind` 请求。下载本轮 Actions 制品中的 `wiki-asset.json`，并入五入口配置。工作流留出 8 分钟启动观察，然后逐次写入修订。按说明保留本轮的 24 个修订号。

4. **交回本轮证据。** 私下交付四张填好的 CSV，以及 `manifest.json`、`seal.json`、`receipts.json`、`alerts.json` 和 `events.json`。GitHub 回执仅记录脱敏进度、缺项以及证据包交接状态。

[交接站首页](README.md)已登记公告源独立接入和 GitHub 单次公开复测的核验结果。六入口正式盲测是当前任务。
