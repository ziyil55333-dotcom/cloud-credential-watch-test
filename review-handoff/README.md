# 独立评审交接站

这里记录云上凭据泄露检测与响应系统 v17 的评审进度。评审人从本页领取任务，并在 [results](results/) 登记进度、代发请求和结果。任务和证据都在 GitHub 交接。


| 任务 | 状态 | 已有证据或下一步 |
| --- | --- | --- |
| `github-public-retest` | 已核验 | 告警命中本次公开提交的指定位置，检测时延区间为 14.278–21.947 秒。[公开提交](https://github.com/ziyil55333-dotcom/cloud-credential-watch-test/commit/b7f60a7a4f1e1e72753d8bcc012fe1748ceb0d24) |
| `extension-review` | 已核验 | 公告源接入的三轮告警数为 0、1、1，首次告警时间和核心代码指纹核对通过。 |
| `blind-review` | 待执行 | 核对六个受控测试入口，独立选样、封存、投放并交回证据。[六入口准备记录](blind-assets-2026-11-25.md) |

## 给独立评审人

1. 打开评审包《独立评审操作手册》零基础版第 5 节，按[六入口准备记录](blind-assets-2026-11-25.md)核对测试地址、发布权限及干净基线。在 [results](results/) 为本轮写一份进度回执。需要项目方代发时，在回执注明入口、批次、计划编号和所需操作。
2. 独立选定 12 类共 120 个未签发、无访问权限的合成正例，另安排 24 个重复正例位置和 120 个负例位置。六个入口各安排 24 次发布。首次扫描和正式投放前先在本机生成 `manifest.json` 和 `seal.json`，在 GitHub 回执记下 `manifest_sha256` 和封存时间。预期标签留在评审人本机，等整轮首次扫描结束后再公开。
3. 确认观察程序就绪后，按计划发布并记录实际提交号、修订号、摘要或其他可追溯版本标识。保留首次扫描结果和失败记录。临时 MediaWiki 的本轮地址和证据导入方法见[入口操作说明](https://github.com/ziyil55333-dotcom/cloud-credential-watch-test/blob/codex/blind-wiki/blind-wiki/blind-review.md)。
4. 整轮首次扫描结束后，经评审人逐项检查，将能公开的合成实验复核文件提交到 `codex/review-handoff` 分支的 `review-handoff/results/blind-review/` 下，以批次编号分目录。至少提交原样的 `manifest.json`、`seal.json`、`receipts.json` 和 `alerts.json`，并按[回执说明](results/README.md)提交可公开的 `events.json` 和四张登记表。进度回执填六入口实际完成数、缺项和结果目录链接。项目方从该链接读取证据并在同一回执目录登记核验结果。

本仓库和提交历史公开可读。实验只用自有或授权测试入口和未签发的合成数据。登记表只用公开测试资产标识、相对路径和评审账号或编号。包含真实凭据、登录信息、本机路径或其他非公开内容的文件留在本机。封存和首轮证据保持原样，如某份必需文件不能公开，在回执写明缺项。
