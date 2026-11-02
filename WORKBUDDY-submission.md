# WorkBuddy 提交信息（照抄即可）

技能包：`dist/cross-border-buyer-matching-workbuddy.zip`（13.9 KB，官方上限 3 MB）
图标：`dist/icon-512.png`（512×512）

## 两条上传路线

### 路线 A：装进自己的 WorkBuddy 客户端（免审核，1 分钟）

1. 打开 WorkBuddy 桌面端，左侧→。
2. 点右上角→。
3. 选择 `cross-border-buyer-matching-workbuddy.zip`，导入后启用。
4. 新开对话，输入货物名称测试，例如：帮我找真无线蓝牙耳机在德国的卖家。

### 路线 B：发布到 WorkBuddy 技能市场（公开，其他人可安装，可收费）

1. 打开 https://open.workbuddy.cn/ ，微信扫码登录。
2. 首次入驻选，按指引完成开发者实名认证（必须本人完成）。
3. 进→→ 新建/上传，上传 zip 与图标。
4. 按下方字段表填写，提交审核（机器审核 + 人工审核，官方口径最长约 7 个工作日）。
5. 审核通过后进入市场；之后满足「已有 ≥1 个过审技能」等条件，可在开通付费（一次性买断或按月订阅，微信签约）。

## 字段表（提交表单照填）

| 字段 | 内容 |
|---|---|
| 技能标识 name | cross-border-buyer-matching |
| 显示名称 | 外贸跨境买家一键开发匹配 |
| 英文名称 | Cross-Border Buyer Matching |
| 版本 | 1.1.0 |
| 作者 | guwen123456 |
| 中文介绍 | 输入货物名称，搜索国外在售该货物的卖家并核验打分，输出可直接开发的买家名单与个性化英文开发信包。 |
| 英文介绍 | Type a product name to find overseas sellers of that product, verify and score them as buyers, reverse-match suppliers, and draft personalized outreach. |
| 分类建议 | 生产力 / 办公（页面有更贴切的贸易或商业类目时选类目） |
| 是否需要第三方 API 密钥 | 否 |
| 版本说明 v1.1.0 | 匹配方式明确为：输入货物名称 → 关键词扩展 → 搜索国外在售卖家（在售证据可核实才入选）→ 100 分评分 → 供应商反向匹配 → 不带价开发信。 |

## 提交前检查（已由 Muse 完成）

- zip 解压验证 9 个文件，结构符合官方：SKILL.md + references/ + scripts/ + templates/。
- SKILL.md frontmatter 必填字段齐全（name / display_name / display_name_en / description / description_zh / description_en / version / author）。
- 包内只有方法论与空白模板，无真实买家数据、无邮箱手机号、无密钥。
