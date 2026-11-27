# 本轮发布协调

已收到 [封存回执](zhoumouai-blind-review-2026-11-26-preseal.md#封存及同步窗口) 和 [技术准备回执](zhoumouai-blind-review-2026-11-26-operations-ready.md)。本轮沿用已登记的 `manifest_sha256` 和 v17 版本。已签名的 24 个 APK 可作为本轮待发布制品。正式投放仍为 0/144。

## 2026-11-27 19:00–22:00（北京时间）

以评审人提出的时段安排本轮。到时先在本批次回执登记评审端是否在线、v17 是否可用、五入口配置及 Wiki 材料是否在手。项目方代发入口根据本批次的实际就绪记录推进。

1. **先启动 MediaWiki。** 评审端准备接收 `wiki-ready` 后，若 `zhoumouai` 已能写入 `codex/blind-wiki`，由他直接提交本轮 24 份修订及 `mode=blind` 请求并回填 Actions 链接。若专用分支拒绝写入，在本批次登记权限缺项，由项目方操作。作业只在评审端能立即接入时启动。 [MediaWiki 操作说明](https://github.com/ziyil55333-dotcom/cloud-credential-watch-test/blob/codex/blind-wiki/blind-wiki/blind-review.md)

2. **确认观察就绪。** 评审人下载本轮 `wiki-ready` 制品，合并 `wiki-asset.json`，在 8 分钟准备窗口内核对六入口基线并启动 v17 常驻扫描。把本轮 Actions 链接、观察就绪时间和存疑入口记到回执。

3. **交接和逐次投放。** 评审人用现有权限发布 GitHub。项目方协助 Gitee、文章、OCI 和 APK。APK 已有经签名校验的制品，核对实物摘要与索引后使用该制品。观察就绪后在交接分支提交需要代发且可公开的合成材料，标出计划编号和文件链接。发布方记录实际不可变版本和发布时间。手工发布的入口核对当次扫描结果再推进下一版。

本批次回执记录就绪、代发请求、失败和各渠道的实际完成数。预期标签和封存原件在首轮扫描结束后按交接站规则提交。 [回执规则](../../README.md)
