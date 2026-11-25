# MediaWiki 盲测入口

在 `codex/blind-wiki` 上修改 `blind-wiki/request.json` 可启动一次临时作业。使用实际新 `run_id` 区分提交。公开 API 仅读取。站点随本次作业结束。

- **干净基线** 将 `mode` 设为 `baseline`。打开 Actions 本次运行，在 `wiki-ready-` 制品中下载 `wiki-asset.json`，并将其作为第六个资产加入本地配置。该次基线发布后保留约两分钟。
- **正式盲测** 评审人先选样、核对并封存。MediaWiki 用 `blind-wiki` 作为资产 ID，计划编号为 `wiki-01` 至 `wiki-24`，位置文件名为 `page-2.wiki`。分别把这 24 个未签发的合成输入存入 `blind-wiki/revisions/wiki-01.wiki` 至 `wiki-24.wiki`。标签和标准答案由评审人私下保管。最后提交包含 `"mode": "blind"` 的本次 `request.json`。
- **启动后** 从 `wiki-ready-` 制品拿到本次 API 和页面 ID，加入六入口扫描配置。工作流确认页面 ID 为 2，留出 8 分钟，再逐次发布 24 版。投放期间当场核对告警链接。
- **回执** 下载 `wiki-blind-revision-metadata`。各 `wiki-XX.json` 的 `query.pages[0].revisions[0].revid` 是相应计划编号的实际版本，连同首次扫描告警一并留存。

测试内容必须是未签发的合成样本，分支公开可读。日志、标准答案、真实凭据和账号信息留在评审人手中。

## 合并配置与导入回执

打开[详细操作与命令](blind-review.md#用一条命令合并配置或导入回执)，使用[脚本](assemble-blind-review.py)从 Actions ZIP 生成六入口配置，并按版本号填入 24 条 Wiki 回执。
