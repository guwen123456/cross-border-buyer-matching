# 外贸跨境买家一键开发匹配 Skill

> Cross-Border Buyer Development & Matching — an Agent Skill

**输入货物名称即可启动**：在国外正在卖这件货物的公司，就是最值得开发的潜在买家。这个 Skill 让 AI Agent 按一套实战验证过的顺序，把「找买家」做成可直接执行的开发包：

1. **按货物名称搜索国外卖家** — 关键词扩展（英文名 / 同义词 / 品类词 / 规格词）后，在公开渠道搜索正在国外在售该货物的进口商 / 批发商 / 零售 / 电商卖家，每家留来源链接，在售证据可核实才入选
2. **核验评分** — 100 分制五维打分，理由必须落字，≥60 分才深挖
3. **个性化锚点** — 每家目标买家必须查到一个具体事实，填不出不发信
4. **供应商反向匹配** — 买家优先：先拿买家三要素（价格带 / 认证 / 试单量）形成需求单，再按硬项反向筛工厂
5. **开发信生成** — 首封不带价，卖核验、质检、拼单、包装四件服务，结尾只问三件事
6. **分波触达 + 回复处理** — 按时区分波、逐封人工审核、退信熔断、回复分类与 WhatsApp 索取话术

## 为什么是这个顺序

海外买家对价格高度透明，平台价随手可查。先向工厂泛询价、再拿价格找买家，是在拼必输的信息差。先联系买家拿到真实需求单，再带规格和数量反向询工厂，工厂面对的是订单机会，回复质量和议价地位完全不同。

## 文件结构

```
SKILL.md                        技能主文件（工作流、交付物、红线、复盘门槛）
references/scoring.md           买卖双方评分表与匹配逻辑
references/outreach-templates.md 开发信、跟进信、报价骨架、工厂询价、试点包话术
references/reply-playbook.md    回信分类 A–F 与 WhatsApp 索取模板
templates/                      buyers / suppliers / outreach_log / orders_profit 四张空表
examples/                       虚构示例数据（.invalid 域名，无真实公司信息）
scripts/match_buyers.py         一键匹配自检脚本（Python 标准库，零依赖）
```

## 快速开始

把这个仓库放进你的 Agent 的 skills 目录（Claude Code、Grok Build、Codex 等支持 Agent Skills 的工具均可），或直接让 Agent 先读 `SKILL.md`。

手动跑一次匹配自检：

```bash
python3 scripts/match_buyers.py examples/sample-buyers.csv examples/sample-suppliers.csv
```

输出：达标可发买家、被拦截的不完整条目（缺评分依据 / 缺个性化锚点 / 缺公开联系方式）、供应商候选与淘汰名单。示例数据中故意放了一家缺锚点的 71 分买家，脚本应把它拦下（退出码 2）。

## 红线（写在技能里，执行时不打折）

- 逐封人工审核，每天 ≤20 封，不群发；首批小量试发；累计硬退信 3 封立即暂停
- 不买名单、不批量抓取个人邮箱，只用官网公开商务联系方式
- 未核验的认证 / 产能 / 价格一律标「待核验」，不写进对外材料
- 不承诺回复率与成交，只承诺核验质量与开发信可直接用

## English summary

A buyers-first B2B lead development skill for cross-border trade. You start by typing a product name: the skill expands it into search keywords and finds overseas sellers of that exact product (importers, wholesalers, retailers and e-commerce sellers — the strongest potential buyers), verifies and scores them on a 100-point rubric (only ≥60 proceed), requires a concrete personalization anchor per buyer, matches suppliers in reverse from real buyer demand (price band, certifications, trial quantity), and drafts no-price first-touch outreach that sells verification, QC, consolidation and packaging instead of competing on transparent platform prices. Includes scoring rubrics, outreach and reply templates, CSV schemas, and a zero-dependency matching checker. All sample data is fictional.

## License

MIT

## WorkBuddy

WorkBuddy 专用包（官方 frontmatter）与提交信息见 `WORKBUDDY-submission.md`，zip 在本地 `dist/` 目录构建，结构已解压验证。
