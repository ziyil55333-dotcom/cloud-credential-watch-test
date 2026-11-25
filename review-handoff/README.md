# 独立评审交接站

这里记录云上凭据泄露检测与响应系统 v17 的评审进度。评审人从本页领取任务，并在 [results](results/) 提交脱敏进度或结果摘要。

| 任务 | 状态 | 已有证据或下一步 |
| --- | --- | --- |
| `github-public-retest` | 已核验 | 告警命中本次公开提交的指定位置，检测时延区间为 14.278–21.947 秒。[公开提交](https://github.com/ziyil55333-dotcom/cloud-credential-watch-test/commit/b7f60a7a4f1e1e72753d8bcc012fe1748ceb0d24) |
| `extension-review` | 已核验 | 公告源接入的三轮告警数为 0、1、1，首次告警时间和核心代码指纹核对通过。 |
| `blind-review` | 待执行 | 核对六个受控测试入口，独立选样、封存、投放并交回证据。[六入口准备记录](blind-assets-2026-11-25.md) |

## 给独立评审人

1. 打开评审包的《独立评审操作手册》零基础版第 5 节，按[六入口准备记录](blind-assets-2026-11-25.md)核对 GitHub、Gitee、MediaWiki、知识文章、OCI 镜像和 APK 的地址、发布权限及干净基线。逐个记下发布人和基线状态。临时 MediaWiki 的当轮地址按[入口操作说明](https://github.com/ziyil55333-dotcom/cloud-credential-watch-test/blob/codex/blind-wiki/blind-wiki/blind-review.md)获取。
2. 按手册独立选定 120 个未签发、无访问权限的合成正例，覆盖 12 类，每类 10 个。另安排 24 个重复正例位置和 120 个负例位置。六个入口各安排 24 次发布，共 144 次。评审人确认样本和预期答案，按手册在首次扫描和正式投放前生成并保存 `manifest.json` 和 `seal.json`。
3. 核对观察程序已就绪后开始正式发布。按手册为每次发布记录实际提交号、修订号、摘要或其他可追溯版本标识。同一轮保留首次扫描的原始告警、事件和失败记录。需要项目负责人代为发布的入口，请先写明入口和所需操作。
4. 发回私下封存的证据包，至少包含 `manifest.json`、`seal.json`、`receipts.json`、`alerts.json` 和 `events.json`。在 [results](results/) 写一份脱敏 Markdown 回执，包含任务编号、日期、六入口进度、已发布数量、是否已封存和当前缺项。

本仓库公开可读。标准答案、样本值、完整证据包和本地路径通过双方约定的私下渠道交接。GitHub 只收脱敏摘要。
