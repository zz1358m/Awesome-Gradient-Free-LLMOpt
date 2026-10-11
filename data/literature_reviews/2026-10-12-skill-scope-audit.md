# ICLR 2027 skill 范围临时例外逐篇审计（2026-10-12）

## 结论

本报告只执行用户于 2026-10-12 新增的目录范围例外：主要研究对象或核心机制为技能生成、技能库、技能检索、技能优化/自演化、技能与 policy 共演化，或技能组合/技能基函数适配的论文，暂缓进入现行目录。机器人技能组合与适配同样适用。仅把 `skill` 当作普通词汇、背景例子、部署形式或泛指能力的论文不因此暂缓。

- 审查候选：37 条。
- 当前暂缓：34 条。
- 当前保留：3 条（Rent or Recompute、MILO、AIProver）。
- 证据范围：`data/papers.json` 中原目录记录及 `data/literature_reviews/2026-10-11-iclr2027.json` 保存的官方 OpenReview 投稿摘要；没有为本报告发起新检索。
- “暂缓”是用户当前的目录范围选择，不表示论文无效、不相关或学术质量判断。原始记录和证据应归档，以便用户解除例外后恢复。
- 已从现行目录和书目移出同一组 34 条；完整可恢复记录见 [`data/deferred_papers/2026-10-12-skills.json`](../deferred_papers/2026-10-12-skills.json)，集合验证见 [`2026-10-12-skill-deferral-validation.json`](2026-10-12-skill-deferral-validation.json)。

## 暂缓的 34 条

1. **TITRATE: Adapting Self-Distillation Weight and Skill Refresh to Training Dynamics**（原分类 `related_hybrid`；[OpenReview](https://openreview.net/forum?id=sCJWZK42vA)）
   决定：暂缓。摘要将版本化 skill bank、证据门控的复用/刷新控制器及技能与 policy learning 的闭环列为框架主体，技能库刷新属于核心机制。

2. **RideSkill: A Hierarchical Algorithm for Generalized Ride Sharing with LLM-Driven Automatic Evolution**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=fmCe2SzUjW)）
   决定：暂缓。核心组件包括学习得到的调度 skill repository、车辆到技能的 combiner，并由 LLM-based evolutionary method 联合训练；属于机器人/调度技能库演化。

3. **OR-Skill: Self Evolutionary Agent Skills for Optimization Modeling**（原分类 `related_hybrid`；[OpenReview](https://openreview.net/forum?id=oGepteMxUI)）
   决定：暂缓。论文让 agent 携带候选优化建模技能执行任务，再依据失败诊断进行 cascade evolution，直接以技能迭代修订为核心。

4. **MoS-VLA: A Vision-Language-Action Model with One-Shot Skill Adaptation**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=jeYa5D7gYZ)）
   决定：暂缓。机器人策略被表示为 learned basis functions 的连续混合，测试时梯度无关求解技能混合系数；属于技能基函数适配。

5. **When Small Evaluator Biases Become Permanent: Phase Transitions in Self-Evolving Agent Skill Libraries**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=zEFUowQZuR)）
   决定：暂缓。CRR 专门建模持久技能库中的评价选择、mutation/repair、检索强化、谱系与暴露偏差，研究对象就是递归更新的 skill library。

6. **Test Time Computing for Evolving Agent Skill Optimization**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=LUKh19HsU1)）
   决定：暂缓。EvoBranch 围绕已有 skill optimizer 增加分支修订、mutation/crossover 和 Top-M 选择，搜索对象明确是可复用技能。

7. **Socratic-SWE: Self-Evolving Coding Agents via Trace-Derived Agent Skills**（原分类 `related_hybrid`；[OpenReview](https://openreview.net/forum?id=xEKG0mb0Ny)）
   决定：暂缓。方法把 solver traces 蒸馏为结构化 repair skills，并用技能生成定向仓库修复任务；技能生成与使用是闭环课程的核心环节。

8. **Skills and Challenges Co-Evolve: Learnability-Aware Autocurricula for Agent Skill Evolution**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=PoxAW0RMer)）
   决定：暂缓。框架共同演化技能和可执行挑战群体，以挑战的可解性/可学习性为技能突变提供信号，属于技能自演化。

9. **SkillSmith: Co-Evolving Skills and Tools for Self-Improving Agent Systems**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=sATDr8QpEQ)）
   决定：暂缓。摘要明确提出 skill–tool co-evolution，并以技能间互补/冲突与 anti-pattern 指导技能和工具修改。

10. **SkillNEO: Non-Elitist Evolutionary Optimization of Agent Skills**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=DScGkPg0NR)）
    决定：暂缓。研究对象是无需更新模型权重的持久 agent skills，并以非精英式演化保留低分中间技能和历史轨迹。

11. **SkillGRACE: Group-Relative Advantage-Guided Contrastive Editing of Agent Skills**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=l9IMRiLRHo)）
    决定：暂缓。方法把同任务 rollout 优势转为生成和选择 skill patch 的对比证据，核心是外部技能编辑。

12. **Skill-R1: Agent Skill Evolution via Reinforcement Learning**（原分类 `related_hybrid`；[OpenReview](https://openreview.net/forum?id=1b8Jj09JxE)）
    决定：暂缓。论文训练 lightweight skill generator 为冻结任务 LLM 生成技能，并以代内/跨代 group-relative 目标优化技能生成器。

13. **Skill-MAP-Elites: Open-Ended Evolution of Agent Skills through Behavioral Niches**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=TvzNP3tmRz)）
    决定：暂缓。框架以执行行为生态位、局部精英和 behavior-level mutations 演化多文件技能工件，技能质量多样性搜索是主体。

14. **Skill-$\pi$: Skill-Policy Co-Evolution for Self-Improving Multimodal Reasoning**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=dXqMUjWpme)）
    决定：暂缓。共享 MLLM 共同执行技能选择、使用和演化，成功经验同时扩展技能库并更新参数化 policy，符合技能—policy 共演化定义。

15. **Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills**（原分类 `related_unverified`；[OpenReview](https://openreview.net/forum?id=07pvXM8POP)）
    决定：暂缓。虽独立梯度无关机制尚未确立，摘要明确由 dynamic skill controller 利用执行反馈更新并扩展 skill library；新例外覆盖混合或机制待核实的技能论文。

16. **Self-Regression-Test:Continuous Integration for Self-Evolving Agents That Rewrite Their Own Skills**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=OjV808LATw)）
    决定：暂缓。SRT 为每项可重写技能维护版本化回归谓词，并据测试决定技能更新的 commit、repair 或 rollback；技能工件更新是直接对象。

17. **Residual Skill Optimization for Text-to-SQL Ensembles**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=cEWctQOQL4)）
    决定：暂缓。DivSkill-SQL 在现有技能集未解样例上逐个优化新技能，目标是提高对 Pass@K 的边际贡献，属于技能集合优化。

18. **PackAgent: Evolving Three Coordinated Skills for State-Adaptive 3D Bin Packing**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=xVyJHWHTMw)）
    决定：暂缓。方法把决策分解为 reflection、item selection 和 placement scoring 三项技能，并由 LLM 离线联合演化可执行技能。

19. **PROTEUS: Provable Self-Evolution for Skill-Composing Language Agents**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=XnVVAhxbSu)）
    决定：暂缓。框架把 agent 自演化表述为 skill graph 上的约束随机优化，并维护 per-skill 能力后验及图变异/选择，技能组合是核心。

20. **Open-Ended Skill Speciation: Evolving New Abstractions for Agent Skills**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=AWQyYRvaOE)）
    决定：暂缓。OESS 演化不断扩展的技能 repertoire，通过物种划分和 macro-mutations 发现新的技能抽象。

21. **MAS-Skill: Skill-Guided Multi-Agent Systems via Collaborative Topology Transfer**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=1oiohnxg31)）
    决定：暂缓。论文把协作拓扑、角色、工具分配和综合策略封装为可复用技能，并通过遗传重组和突变形成技能库。

22. **Lifetime Learning of Skills: Evolving the Skill-Learning Algorithm Itself**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=IqsyZEhbYe)）
    决定：暂缓。外层种群演化控制技能构造、评估、预算、部署和回滚的可执行 meta-program，研究对象仍是 skill-learning lifecycle。

23. **Learning to Evolve: Skill–Policy Co-Evolution for Self-Evolving Agents**（原分类 `related_hybrid`；[OpenReview](https://openreview.net/forum?id=5LaVWdURJZ)）
    决定：暂缓。SCALE 以候选技能对长期 policy evolution 的影响评价技能，并将技能提取与 policy optimization 联结，符合技能—policy 共演化。

24. **GraphSkillEvo: Evolutionary Optimization of Graph-Structured Agent Skills**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=FrghfkhvZh)）
    决定：暂缓。方法将技能表示为图结构自然语言工件，再执行 population-based mutation 和 crossover，技能结构与优化均为核心。

25. **Execution-Grounded Credit Assignment for Self-Evolving Agents**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=V2OwjDmLOC)）
    决定：暂缓。方法对 instructions、tool code 和 skills 做 execution-grounded component-level credit assignment，并据此指导组件变化；技能更新是核心演化对象之一而非偶然提及。

26. **EvoORSkill: When Optimization Skills Evolve, Who Checks The Math?**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=htz6wPMz4Z)）
    决定：暂缓。论文在 evolving skill hypergraph 中共同演化带版本的运筹技能及其 revision strategies，并以数学检查控制更新。

27. **EvoGenome: Genotype-Phenotype Evolution for Compositional Agent Skills**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=KerlEXgtZe)）
    决定：暂缓。框架把复合 agent skills 表示为带类型、功能定义且可独立遗传的单位，再进行变异、交叉、专门化和移植。

28. **DIVE: Unlocking Self-Improvement in Frozen Language Models Through Diversity-Driven Skill Evolution**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=ogu2wTp6nS)）
    决定：暂缓。DIVE 让冻结 LLM 从经验和 verifier 反馈演化多个持久自然语言技能种群，并选取互补技能集合。

29. **CtrlSkill: A Control-Theoretic View of Controllable Skill Self-Evolution**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=R22SK8XC1h)）
    决定：暂缓。框架把外部 skill policy 更新组织为证据反馈环路，提出带适用条件的技能并决定采用、延后或拒绝。

30. **Cross-Model Reproductive Fitness: Evolving Transferable Skills across Model Hosts**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=L18vEjanZr)）
    决定：暂缓。CMRF 将 model–harness 组合视为异质 host，直接按跨 host 效用选择和迁移技能，核心是可迁移技能演化。

31. **COBRA-Skills: Contextual Bandit-Guided Evolution for Agent Skill Optimization**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=6XFoqlavXz)）
    决定：暂缓。方法把技能优化建模为动态候选空间上的预算序贯优化，以 contextual bandit 分配执行评估并持续改进技能群体。

32. **AgentPSO: Evolving Agent Reasoning Skill via Multi-agent Particle Swarm Optimization**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=wDZ9eU8YuD)）
    决定：暂缓。AgentPSO 将自然语言技能作为粒子状态，依据个体/全局最佳技能与同伴轨迹形成语义更新方向，直接优化推理技能。

33. **A Kinetic Theory of the Gated Self-Evolving LLM Agent**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=23VDi5bfRj)）
    决定：暂缓。论文研究 agent 在 validation gate 下重写自身 skills，并在 DSH 技能插件库上建立群体动力学模型；skill-plugin 改写是理论对象。

34. **Discover and Internalize: A Continual Co-Evolving Training Loop for Self-Improvement Agents**（原分类 `related_hybrid`；[OpenReview](https://openreview.net/forum?id=FT2AzenhGs)）
    决定：暂缓。框架把 skills 作为 behavioral hypotheses，先演化与组合技能，再将有前景行为内化进模型权重，属于技能搜索与 policy 内化共演化。

## 保留的 3 条边界命中

35. **Rent or Recompute?: Learning-Augmented Placement of Agent KV Caches Across Memory and Shared Storage Tiers**（原分类 `related_hybrid`；[OpenReview](https://openreview.net/forum?id=5MJgRASpik)）
    决定：保留。核心是 idle agent session 的 KV cache 在 GPU、host memory、storage 和 recompute 之间的多状态放置，以及 idle-gap predictor 驱动的 learning-augmented ski-rental policy。摘要中的 “predictor has no skill” 只是普通语言中的预测能力，不涉及技能工件。

36. **MILO: Automated Harness Discovery via Orchestrated Multi-Agent Evolution**（原分类 `related_prompt_agent`；[OpenReview](https://openreview.net/forum?id=AUiAVv2xU2)）
    决定：保留。MILO 演化的是完整 agent harness 和搜索过程：island lineage memory、重写 entire harness 的 mutator 及做 grafting/speciation 的 orchestrator 是核心。“prompts or skills”只用于描述既有方法优化 harness 局部组件，MILO 并未把技能设为主要对象。

37. **AIProver: Agentic Auto-Formalization of Mathematical Research via Certificate-Driven Evolving Harness**（原分类 `related_hybrid`；[OpenReview](https://openreview.net/forum?id=R9kJupcBxE)）
    决定：保留。论文交替进行 119B 模型的 verifier-driven reinforcement post-training 与 HarnessEvolve 对完整 tool-calling control flow 的证书引导演化；“as a Claude Code and Codex skill”是部署/评测表述，不是技能生成、技能库或技能优化机制。

## 可恢复性与解释边界

暂缓集合应与归档的完整 `data/papers.json` 原记录和对应 BibTeX 条目一一对应。历史 2026-10-11 报告仍应保留这些论文曾被收录和如何审查的事实；本报告仅说明 2026-10-12 起当前有效目录的范围变化。以后恢复时，应由用户明确解除临时例外，再从归档记录恢复，不能把标题中的 `skill` 作为自动黑名单或反向恢复依据。
