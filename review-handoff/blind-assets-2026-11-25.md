# 盲测资产准备记录

2026-11-25 项目方预检。以下五个入口从公网读取，各完成一次干净基线扫描，均为零告警。可下载 [五入口配置](five-baseline-preflight.json) 在 v17 上复核。它用于基线预检；MediaWiki 就绪后再补入正式六入口配置。

| 入口 | 本次登记位置 | 基线版本 |
| --- | --- | --- |
| GitHub | [专用分支 `codex/blind-github`](https://github.com/ziyil55333-dotcom/cloud-credential-watch-test/tree/codex/blind-github) | `8b05f6e40bcf85d8eb8fc38e1345e2da96a66a29` |
| Gitee | [专用分支 `codex/blind-gitee`](https://gitee.com/n123_40_1/cloud-credential-watch-gitee-fixtures/tree/codex/blind-gitee) | `01da4ea6536815472a8d838ad5e272ad91bec9d9`，标签 `blind-clean-baseline-20261125` |
| APK | [专用发布目录](https://github.com/ziyil55333-dotcom/cloud-credential-watch-test/tree/codex-blind-apk/apk-acceptance)，[发布索引](https://raw.githubusercontent.com/ziyil55333-dotcom/cloud-credential-watch-test/codex-blind-apk/apk-acceptance/releases.json) | `1.0.0@sha256:804b3f4f2dbc80931de050056cad4e41bb2647e9ba9665e316d201ee2d80e02b` |
| 文章 | [独立 RSS](https://ziyil55333-dotcom.github.io/cloud-credential-watch-public-fixtures/blind-article/feed.xml)，发布目录 `blind-article/` | `blind-article-baseline@sha256:dab264c7085b29913f0c708078c00618e574c4c680e776a750ad5dd212b2a87f` |
| OCI | `https://ghcr.io/v2/ziyil55333-dotcom/cloud-credential-watch-public-fixtures`，标签 `blind-eval` | `sha256:0b7d7340cecda072b4a98ccc9030d8f04046220ee1fb1543900bc25d947144fc`，[发布记录](https://github.com/ziyil55333-dotcom/cloud-credential-watch-public-fixtures/actions/runs/45588441120) |

## 待完成

- **MediaWiki** 原临时站点已失效。约定评审时段后启动临时站点，确认本轮 API 地址、页面 ID、干净修订和投放方式，再进行盲测封存。
- **正式发布权限** 请核对 Gitee、文章和 OCI 发布协助人，以及 GitHub 和 APK 测试分支的评审人写权限。评审人保管样本与答案。发布协助人按约定只接收实际投放文件。
- **独立接入** 仍待评审人本人参与或见证并交回 `extension.json` 与三轮证据。已核验的 GitHub 单次公开复测可直接沿用。

六入口齐备且评审人完成封存后，再开始正式发布并逐次记录实际版本。
