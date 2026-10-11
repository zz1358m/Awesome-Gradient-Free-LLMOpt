# ICLR 2027 梯度无关 LLM 论文：一手来源与覆盖核验记录

记录更新时间：2026-10-11T17:08:24+08:00

## 结论

本轮已经完成 31 个关键词/方法名的会议限定官方 OpenReview 搜索、分页补齐、跨查询去重、766 条候选逐条决定记录，以及当前目录条目的方法字段复核。当前目录共 **390** 条，其中本轮报告内 `included_or_updated` 为 **327** 条，逐条保留但未列入目录的候选为 **439** 条。

**仍不能证明取得 ICLR 2027 全量投稿。** 可验证覆盖下界为 **35,728 个独立 OpenReview ID**。详细每页 URL、offset、官方 count、返回数和缓存路径见 [`2026-10-11-iclr2027-search-manifest.json`](2026-10-11-iclr2027-search-manifest.json)；766 条逐项记录见 [`2026-10-11-iclr2027.json`](2026-10-11-iclr2027.json)。

## 官方检索证据

- 检索范围：`group=ICLR.cc/2027/Conference`、`source=forum`、`limit=1000`。
- 投稿 venue 标识：`ICLR.cc/2027/Conference/Submission`。
- 会议限定关键词：31 个；成功缓存 **85 页**、**61,901 条跨查询记录**，去重为 **29,623 个 ID**。
- 30 个查询已分页到官方 reported count；`Sample the Order, Not the Token` 因多词 OR 展开在 `count=10000` 且第 10 页仍满页，只能记作窗口封顶。
- 继续分页请求 65 次，均为 HTTP 200，本阶段未发生 429；先前 429 的缺页从缺失 offset 继续，没有重抓已成功页。
- `venueid` 全会搜索按 `cdate:asc` 与 `cdate:desc` 各缓存 10 页/10,000 条，两个窗口 **0 重叠**。正序最大 cdate 为 `1789215224711`，倒序最小 cdate 为 `1789748368818`，中间区间未取得。
- `after`、`before`、`fromdate`、`todate` 被服务忽略；新增 `sort=title:asc` 探测返回 HTTP 400：`No mapping found for [title] in order to sort on`。
- 完整 `notes?invitation=ICLR.cc/2027/Conference/-/Submission` 仍返回官方 `ChallengeRequiredError`。未绕过 challenge、CAPTCHA 或访问控制。

因此，**35,728 是可验证独立 ID 下界，不是会议总投稿数**；官方 `count=10000` 是搜索窗口上限，不能解释成会议总数。

## 审查与边界规则

- 主分类：模型权重、adapter、参数子空间、量化参数等由明确 ES/ZO/函数值机制持久更新。
- `related_hybrid`：梯度无关/外部搜索与一阶、RL、policy update 或 backward pass 并存。
- `related_inference`：无参数更新的推理时校准、顺序搜索、激活控制等；若另有训练分支，单独注明。
- `related_prompt_agent`：提示词、技能、工作流、harness、脚本、记忆、奖励、模型合并、系统配置等外部工件的真实梯度无关搜索。
- 不用缺少持久模型参数更新作为关联分类的排除理由；也不把 `evolving` 自动解释成遗传算法。
- 每个收录候选分别记录 `backpropagation`、`component_training_zh`、`persistent_model_parameter_update`、`persistent_updates_zh`、`updated_object` 与 `unverified_zh`。信息不足按组件标为待核实。
- 439 条未收录候选均保存题名、官方摘要、原始链接、日期字段、摘要方法证据及具体关联缺口；排除决定不以“没有持久参数更新”为由。

## 本轮关键纠错

- **Skill Self-Play**：保留边界收录并移至 `related_hybrid`。官方摘要只证明 RL loop 下 proposer、solver、skill controller 与 skill library 共同演化；没有证明独立 ES/遗传搜索，也没有证明冻结权重或无反传。
- **Skill-R1**：任务 LLM 据摘要 frozen，但轻量 skill generator 以 bi-level GRPO 训练，归 `related_hybrid`。
- **Hyper-ES**：先用梯度训练得到下降方向，再用 CMA-ES 合并，已从 `es_single_turn` 移至 `related_hybrid`。
- **FoRA、ZO-Curv、GS-Muon、ESRL、Evaluate Before You Commit、sequential ES–GRPO**：因明确存在一阶/RL/backward component，移至 `related_hybrid`。
- **ZO-LDSD / CZqew9w981**：采用官方当前题名 *Zero-Order Optimization via Learnable Direction Sampling for LLM Fine-Tuning*，旧题名作为别名保留；LLM 用 finite-difference ZO，direction policy 用 REINFORCE，因此列入 `related_hybrid`。
- **Sample the Order, Not the Token**：核心 OSE 是推理时 unmasking-order 搜索，无持久模型更新；附加 GRPO 分支另行标注，保留在 `related_inference`。
- **EvoG、GP-Harness、MODEPrompt、SkillNEO、GraphSkillEvo、ReHarness、MIMUS、BoLT**：均读取官方摘要并保留；搜索对象、训练组件与持久状态逐项区分。
- 对 61 条由比较性关键词机械触发的 `related_hybrid` 记录复审：31 条找到方法侧训练证据后保留，30 条保守移至 `related_prompt_agent`；没有把“摘要提到 RL/一阶基线”直接当作混合方法证据。
- 第三遍从模板排除项中恢复 31 条高置信边界稿，包括 GEAR、SeaEvo、BayesianAgent、DICE、BOTAS、SPOON、Meta-Rubrics、HIRE、OpenMLE、EdgeEdit 与 AT-AT。

## 投稿、作者与日期

- OpenReview 记录统一标为 `ICLR 2027 Conference Submission; decision pending`，没有录用徽标。
- 双盲投稿作者保持 `Anonymous`；未凭题名、方法名或第三方线索猜测作者。
- `openreview_created_at` / `submitted_at` 只表示记录创建/投稿时间，不当作首次公开日期。
- `first_public_date` 默认留空；只有更早 arXiv/作者页面可明确核实时才另行注明。

## 当前分类数量

- `es_multi_turn`：1
- `es_pretraining`：1
- `es_single_turn`：13
- `es_understanding`：9
- `related_hybrid`：55
- `related_inference`：17
- `related_prompt_agent`：204
- `zo_alignment`：1
- `zo_baselines`：15
- `zo_directions`：32
- `zo_multi_turn`：1
- `zo_pretraining`：3
- `zo_systems`：29
- `zo_understanding`：9

## 可复核文件

- 完整候选审查：[`2026-10-11-iclr2027.json`](2026-10-11-iclr2027.json)
- 分页与覆盖证据：[`2026-10-11-iclr2027-search-manifest.json`](2026-10-11-iclr2027-search-manifest.json)
- 权威目录：[`../papers.json`](../papers.json)
- 本地原始缓存：`/tmp/iclr2027-catalog-20261011-attempt4` 与 `/tmp/iclr2027-catalog-20261011-attempt5`

本记录支持“已完成上述可审计范围内的检索与逐项审查”，不支持“已全量覆盖 ICLR 2027 所有公开投稿”。
