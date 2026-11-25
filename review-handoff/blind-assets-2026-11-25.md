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

## 待完成

- **MediaWiki 正式运行** 评审人先封存标签。按启动说明提交 24 份新合成文件和 `mode=blind` 的请求，启动只读临时站点。取得 Actions 的 `wiki-asset.json` 后并入五入口配置。就绪后有 8 分钟启动扫描，随后工作流逐次写入修订。已核验的空白基线用于确认环境。
- **正式发布权限** 请核对 Gitee、文章和 OCI 发布协助人，以及 GitHub 和 APK 测试分支的评审人写权限。评审人保管样本与答案。发布协助人按约定只接收实际投放文件。
- **独立接入** 仍待评审人本人参与或见证并交回 `extension.json` 与三轮证据。已核验的 GitHub 单次公开复测可直接沿用。

六入口齐备且评审人完成封存后，再开始正式发布并逐次记录实际版本。
