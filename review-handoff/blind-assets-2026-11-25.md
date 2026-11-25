# 盲测资产准备记录

2026-11-25　项目方预检。以下 4 个入口从公网读取并各完成一次基线扫描，均为零告警。发布操作及评审人见证仍须按评审手册排期。

| 入口 | 本次登记位置 | 基线版本 |
| --- | --- | --- |
| GitHub | [专用分支 `codex/blind-github`](https://github.com/ziyil55333-dotcom/cloud-credential-watch-test/tree/codex/blind-github) | `8b05f6e40bcf85d8eb8fc38e1345e2da96a66a29` |
| APK | [专用分支 `codex-blind-apk`](https://github.com/ziyil55333-dotcom/cloud-credential-watch-test/tree/codex-blind-apk/apk-acceptance)，[发布索引](https://raw.githubusercontent.com/ziyil55333-dotcom/cloud-credential-watch-test/codex-blind-apk/apk-acceptance/releases.json) | `1.0.0@sha256:804b3f4f2dbc80931de050056cad4e41bb2647e9ba9665e316d201ee2d80e02b` |
| 文章 | [独立 RSS](https://ziyil55333-dotcom.github.io/cloud-credential-watch-public-fixtures/blind-article/feed.xml)，发布目录 `blind-article/` | `blind-article-baseline@sha256:dab264c7085b29913f0c708078c00618e574c4c680e776a750ad5dd212b2a87f` |
| OCI | `https://ghcr.io/v2/ziyil55333-dotcom/cloud-credential-watch-public-fixtures`，标签 `blind-eval` | `sha256:0b7d7340cecda072b4a98ccc9030d8f04046220ee1fb1543900bc25d947144fc`，[发布记录](https://github.com/ziyil55333-dotcom/cloud-credential-watch-public-fixtures/actions/runs/45588441120) |

## 仍需完成

- **Gitee** 已找到首个干净提交 `01da4ea6536815472a8d838ad5e272ad91bec9d9`。该站点要求仓库负责人先完成页面验证，随后才能在此提交上开专用分支并验证读取。
- **MediaWiki** 原临时站点已失效。需要与评审人约定时段，启动可持续到投放结束的站点，并验证 API 地址、页面 ID、干净修订和编辑权限。
- **发布权限** GitHub 和 APK 均在现有测试仓库。文章和 OCI 位于另一测试仓库，评审前请核对实际发布协助人及权限。评审人保管样本与答案，发布协助人只接收实际投放文件。
- **独立接入** 仍待评审人本人参与或见证并交回 `extension.json` 与三轮证据。已核验的 GitHub 单次公开复测可直接沿用。

这些结果用于准备环境。六入口齐备且评审人完成封存后，再开始正式发布并逐次记录实际版本。
