# 2026-10-12 提示词与智能体范围收紧报告

本次在基线 `a7b72b1` 的 389 条现行目录上逐篇审查。判断以缓存的官方 OpenReview 摘要、论文原始来源和既有方法事实为依据，不按标题、`prompt`、`agent`、`RL` 或 `self-evolution` 词面批量判定。六个批次报告保留全部 389 条逐篇语义决定。

## 结果

- 调整前：389 条；调整后：248 条。
- 移出并可恢复：141 条，其中提示词核心 45 条、智能体明确无模型参数训练 86 条、智能体参数训练证据待核实 10 条。
- 保留训练型智能体：28 条，其中关联训练类 5 条、混合类 20 条、ES/ZO 核心类 3 条。
- 既有 skill 核心暂缓的 34 条未恢复；本次不改写 2026-10-11 新增历史或此前 skill 暂缓历史。
- 完整可恢复记录：[`data/deferred_papers/2026-10-12-prompt-agent-scope.json`](../deferred_papers/2026-10-12-prompt-agent-scope.json)。

## 分类变化

| 分类 | 调整前 | 调整后 | 变化 |
|---|---:|---:|---:|
| `es_multi_turn` | 1 | 1 | +0 |
| `es_pretraining` | 1 | 1 | +0 |
| `es_single_turn` | 13 | 13 | +0 |
| `es_understanding` | 9 | 9 | +0 |
| `related_agent_training` | 0 | 5 | +5 |
| `related_closed_form` | 28 | 26 | -2 |
| `related_forward_gradient` | 1 | 1 | +0 |
| `related_hybrid` | 73 | 62 | -11 |
| `related_inference` | 11 | 7 | -4 |
| `related_prompt_agent` | 167 | 39 | -128 |
| `zo_alignment` | 1 | 1 | +0 |
| `zo_baselines` | 14 | 14 | +0 |
| `zo_directions` | 32 | 31 | -1 |
| `zo_multi_turn` | 1 | 1 | +0 |
| `zo_pretraining` | 3 | 3 | +0 |
| `zo_systems` | 24 | 24 | +0 |
| `zo_understanding` | 10 | 10 | +0 |

## 保留的训练型智能体

下表只把原始来源确认的语言模型、策略模型、适配器或等价智能体控制器参数更新计为“训练”。`纯 ES/ZO` 一栏仅在所提参数更新本身确属纯前向 ES/ZO 时标注；常规 RL/SFT/PPO 或细节未明的训练不会冒充无反传。

| 论文 | 分类 | 更新对象与证据 | 算法及反传边界 | 来源 |
|---|---|---|---|---|
| BudgetWeaver: Learning the Downstream Value of Agent Reads and Memory Mutations under Shared Budgets | `related_agent_training` | Llama-3.1-8B-Instruct记忆控制器/操作策略参数，以及运行中的记忆状态。 | 离线价值细化、读与NOOP配对结果、成本准入与控制器拟合。；反传：摘要确认控制器被拟合，但未说明优化器及是否反向传播。 | [原始来源](https://openreview.net/forum?id=I1lt2QZWPr) |
| Code to Control: Synthesizing Parameterized Reactive Controllers | `related_agent_training` | 参数化 Python controller 的连续策略参数。 | 环境反馈驱动的 derivative-free parameter search。；反传：控制器参数搜索不依赖反传；LLM 本身是否训练未说明。 | [原始来源](https://openreview.net/forum?id=z62vbEOWDO) |
| Adaptive Exploratory Landscape Analysis for LLM-based Meta-Black-Box Optimization | `related_agent_training` | AdaELA self-/cross-attention 选择模型参数。 | neuroevolution strategy；摘要另称可进一步 fine-tuning。；反传：neuroevolution 本身无需反传；后续 fine-tuning 是否反传未说明。 | [原始来源](https://openreview.net/forum?id=Ke3tLwqK3L) |
| Beyond Scripted Search: Sample-Efficient Reward Discovery via Agentic Black-box Optimization | `related_agent_training` | 下游 RL policy 参数；外部还更新 reward function 和搜索 workspace。 | LLM agent 黑盒奖励搜索；候选评估采用 full RL training run。；反传：RL policy training 通常依赖反传，但摘要未明确优化器，故具体反传实现待核实。 | [原始来源](https://openreview.net/forum?id=JZSS6Stlhv) |
| EvoForge: Agentic Online Hyperparameter Tuning for Pretraining | `related_agent_training` | GPT-2 124M 预训练模型参数及训练超参数。 | 单轨迹 agentic online hyperparameter tuning + distributed pretraining。；反传：预训练明确发生，通常反传；摘要未列优化器细节。 | [原始来源](https://openreview.net/forum?id=LAmTBYPHye) |
| Recursive Self-Improvement through Multi-Agent Self-Supervision | `related_hybrid` | 单一基础模型在优化工作流的执行轨迹上做监督微调，模型权重持久更新；工作流图另经外部进化搜索。反向传播实现未明说。 | 官方摘要明确交替进行 multi-agent workflow evolutionary optimization 与在自生成轨迹上的 supervised fine-tuning。；反传：— | [原始来源](https://openreview.net/forum?id=lHLch9v09X) |
| Noisy Replicator-Mutator Dynamics in Multi-Agent Learning | `related_hybrid` | 多智能体 policy 通过 policy-gradient/PRPG 更新；摘要未给出具体反传实现和参数化范围。 | 论文从 stochastic policy-gradient updates 推导多智能体动力学，并据此构造 PRPG，属于策略参数训练而非只改文本工件。；反传：— | [原始来源](https://openreview.net/forum?id=qtwq8fbHB0) |
| MA-RL-VLA: Counterfactual Credit-Aware PPO for Multi-Agent Reinforcement Fine-Tuning of Vision-Language-Action Models | `related_hybrid` | VLA policy 参数由 PPO 持久更新；精确动作枚举用于信用分配，不等同于整个流程无反向传播。 | MA-RL-VLA 将反事实信用权重置入 PPO 两个分支，明确训练多智能体 VLA 导航策略。；反传：— | [原始来源](https://openreview.net/forum?id=MtYTLgYRmu) |
| Learning to Elicit: Co-Evolving Routing and Information Disclosure in Societies of Language Agents | `related_hybrid` | 智能体 routing/disclosure policy 由 RL 与蒸馏持久训练；各模块是否共享语言模型参数及反传细节待正文核实。 | Co-Adapt 用 RL 与 privileged on-policy distillation 学习联系路由和私有信息披露。；反传：— | [原始来源](https://openreview.net/forum?id=xupjJh9hXG) |
| Good Agentic Friends Do Not Just Give Verbal Advice: They Can Update Your Weights | `related_hybrid` | parameter generator 参数被训练；receiver 基座冻结，但生成的 LoRA 扰动在单次生成中改变模型参数状态。训练算法和反传边界待核实。 | TFlow 明确训练 parameter generator，由 sender 隐状态生成 receiver-specific 低秩 LoRA 扰动。；反传：— | [原始来源](https://openreview.net/forum?id=tDrV3iV2Zb) |
| Beyond Cooperative Simulators: Generating Realistic User Personas for Robust Evaluation of LLM Agents | `related_hybrid` | persona generation program 是外部搜索工件；下游语言 agent 明确经过 fine-tuning，具体参数子集和反传实现未说明。 | PPol 的 persona 程序由进化 coding agent 搜索；摘要另明确用 PPol 数据 fine-tuning agents 并报告真人交互提升。；反传：— | [原始来源](https://openreview.net/forum?id=HJaoIZVSzM) |
| AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety | `related_hybrid` | attacker 与 defender 的语言智能体策略由 RL 持久更新；task weighting 是信用/课程机制，具体反传实现待核实。 | AgentSafeEvo 是 attacker–defender co-evolutionary RL，摘要明确攻击者和防御者均学习任务/执行策略。；反传：— | [原始来源](https://openreview.net/forum?id=9wUe4gLzDm) |
| Explicit Trajectory Diversity for RL-Based Post-Training of LLM Agents | `related_hybrid` | 单一 LLM agent policy 经 group-based RL 持久更新；trajectory descriptors 是用户指定的行为表示，不是被训练的模型。 | TJPO 在 single-policy group-based RL 中以 trajectory-level signals 直接优化智能体 policy。；反传：— | [原始来源](https://openreview.net/forum?id=WDqlWS75gR) |
| EviGate: Evidence-Gated Inheritance for Self-Evolving Program-Repair Agents | `related_hybrid` | 通过门控的参数子代可持久继承；摘要未说明 parameter adaptation 的优化器、参数范围或反传实现。 | EviGate 官方摘要明确包含 parameter adaptation，并仅在 promotion、regression、safety checks 后保留 parameter children。；反传：— | [原始来源](https://openreview.net/forum?id=gU0o6s2tHP) |
| CoHARL: Co-Evolving Agent Policies and Executable Harnesses with Reinforcement Learning | `related_hybrid` | shared LLM policy 由 RL 持久更新；harness proposer 修订代码，proposer 自身是否训练待核实。 | CoHARL 明确在 harness population 上用 population-based RL 训练 shared policy。；反传：— | [原始来源](https://openreview.net/forum?id=Iiw1WtkMkZ) |
| AIProver: Agentic Auto-Formalization of Mathematical Research via Certificate-Driven Evolving Harness | `related_hybrid` | 119B 模型参数通过 fine-tuning 和 alternating RL 持久更新；harness control flow 另由证书驱动进化搜索。具体反传实现待核实。 | AIProver 明确 jointly post-trains a 119B open-weight language model，并交替进行模型 fine-tuning/RL 与 HarnessEvolve。；反传：— | [原始来源](https://openreview.net/forum?id=R9kJupcBxE) |
| $\pi$-Play: Multi-Agent Self-Play via Privileged Self-Distillation without External Labeled QA Data | `related_hybrid` | 语言模型/策略通过 token-level self-distillation 持久更新；摘要未说明优化器和反向传播实现。 | π-Play 将 QCP 转为 token-level supervision 做 self-distillation，以持续改进搜索智能体模型。；反传：— | [原始来源](https://openreview.net/forum?id=KOqQs63l7Q) |
| $R_Q$-Evolve: LLMs Evolve Their Own Generator Programs for Self-Improvement | `related_hybrid` | Solver 模型参数经 group-relative RL 持久更新；generator-program archive 经 mutation、fitness ranking 与 retention 更新。 | R_Q-Evolve 同时突变 generator programs，并用 group-relative RL 训练 Solver。；反传：— | [原始来源](https://openreview.net/forum?id=B8oWwVLeGz) |
| GEAR: Co-evolving Grounded VLM Agents with Environment-Aligned Rubrics | `related_hybrid` | VLM policy 与 rubricator 均为训练组件；摘要未说明参数子集和各自是否/如何反向传播。自然语言 rubrics 是外部工件。 | GEAR 官方摘要明确 jointly optimizes a VLM policy and a rubricator，并与 RL 轨迹分布共同演化。；反传：— | [原始来源](https://openreview.net/forum?id=0AdawuC1tj) |
| Heterogeneous Agentic Coevolution | `related_hybrid` | specialist foundation model 与 agent policy 均持久训练；interaction harness 另经 evolutionary search，具体反传路径待核实。 | HACE 明确以 supervised learning 改进 specialist，并以 on-policy RL 训练 LLM agent。；反传：— | [原始来源](https://openreview.net/forum?id=E1rsriszaM) |
| Self-Evolving Algorithm-Design Agents: Escaping In-Context Evolutionary Stagnation via Population-Curated Policy Optimization | `related_hybrid` | agent policy 参数经 PCPO 持久更新；算法 population 是外部工件。摘要未交代梯度/反传实现。 | PCPO 提出 parametric self-evolution，以 hybrid policy update 将自生成算法内化到 algorithm-design agent。；反传：— | [原始来源](https://openreview.net/forum?id=Y3u3Z56znq) |
| Meta-Rubrics: Learning to Discover Rubrics at Deployment for Efficient Task Adaptation | `related_hybrid` | rubric generator 与 LLM judge 参数经 RL 持久训练；部署期自然语言 rubric/候选排序是外部状态，反传实现待核实。 | Meta-Rubrics 明确用 branched-rollout RL jointly optimizes rubric generator and LLM judge。；反传：— | [原始来源](https://openreview.net/forum?id=g5tssaW2qj) |
| OpenMLE: Training LLMs for Evolutionary Search in Machine Learning Engineering | `related_hybrid` | 程序修订语言模型通过 SFT 和 RL 持久更新；OpenMLE-Evo 的长期 population/search state 另行更新。 | OpenMLE-Train 明确先 execution-verified SFT、再以执行奖励 RL post-train 单一模型，之后把它作为进化搜索 variation engine。；反传：— | [原始来源](https://openreview.net/forum?id=nSuEq47kb9) |
| HarnessNet: From Engineered Harnesses to a Unified Neural Controller for Self-Evolving Agents | `related_hybrid` | LLM 权重冻结；作为智能体执行策略的 HarnessNet 神经控制器参数持久训练，且不穿过 LLM/环境求梯度。第二阶段优化细节待正文核实。 | HarnessNet 保持 LLM 冻结，但明确训练持久 neural feedback controller：先模仿 engineered harness，再按同任务多次尝试结果改进。；反传：— | [原始来源](https://openreview.net/forum?id=cFcaAi8dtG) |
| Don't Retrain, Remix: Adaptation of Web Agents using Mixture Hypernetworks | `related_hybrid` | 源 LoRA 与 router 预先训练；目标域以一次 router 前向持久合成/配置新 adapter，基础模型不做目标域反向传播。 | WebMix 用预训练 LoRA bank 与 router 在部署时合成为新 adapter；虽无目标域梯度更新，但明确形成用于智能体推理的新模型适配参数。；反传：— | [原始来源](https://openreview.net/forum?id=Eq74LwgkjR) |
| Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Memory Requirements | `es_multi_turn` | 官方摘要原文明确写明“forward-only full-parameter optimization”以及“a full-parameter ES framework supporting both train-time fine-tuning and on-the-fly adaptation”。 | 以完整长程智能体轨迹的环境总奖励评价参数扰动，用 Evolution Strategies 更新全量语言模型参数；按摘要，该 ES 分支无需 backpropagation。摘要中的 Agentic RL/GRPO 是比较对象，不据此归入所提 ES 方法。；反传：— | [原始来源](https://openreview.net/forum?id=LfIpbuIKLb) |
| Dimension Is Free, Horizon Is Not: When Evolution Strategies Rival Policy Gradients for LLM Fine-Tuning | `es_understanding` | 官方摘要将 ES 定义为扰动参数的估计器，并报告使用 Qwen2.5-7B-Instruct 在 27 个 NLP、数学推理和智能体任务上进行 ES–PG 对比。 | ES 通过参数扰动和整条轨迹总回报估计语言模型更新；PG/GRPO 通过动作采样与 token 级信用训练模型。论文分析两类梯度估计器的有效参数维数与有效信用分配时域，不应把比较用 PG 的反传属性归给 ES。；反传：— | [原始来源](https://openreview.net/forum?id=59ufz75SkM) |
| Beyond the Capability Boundary: Zeroth-Order Optimization for Self-Evolving LLM Agents | `zo_multi_turn` | 官方摘要明确写明“perturb LoRA parameters of LLMs”、以损失差估计梯度并“update the LoRA parameters”，以及用更新后的 LLM 采样轨迹用于 supervised fine-tuning。 | 第一阶段以 answer perplexity 为损失，通过参数扰动和损失差进行零阶 LoRA 更新；第二阶段以成功轨迹执行 SFT。ZO 阶段不需要反传，但 SFT 通常是一阶训练，摘要未明确其具体反传实现，故不把整个闭环称为无反向传播。；反传：— | [原始来源](https://openreview.net/forum?id=qqOjD3pcxL) |

## 全部移出记录

提示词核心即使包含提示参数、残差模块或其他训练，也因主要研究对象属于本次暂缓范围而移出；智能体“明确无训练”组只包含原始来源能确认持久更新对象是模型外文本/程序/系统状态等的工作；证据不足者单列为待核实，不强行断言没有模型训练。

| 论文 | 原分类 | 原因组 | 论文特定依据 | 来源 |
|---|---|---|---|---|
| Private Zeroth-Order Optimization with Public Data | `zo_directions` | 提示词核心 | 暂缓：目录记录和原始论文页面所述文本实验以 RoBERTa-base 的 prompt-tuning 为模型适配对象，优化的是提示参数；这属于用户明确要求移出现行目录的软提示核心研究。论文的差分隐私 ZO 方法本身有效，本决定仅是当前目录范围调整。 | [原始来源](https://proceedings.neurips.cc/paper_files/paper/2025/hash/54de3c17e1a2457658a22ad801c721db-Abstract-Conference.html) |
| What Do Evolutionary Coding Agents Evolve? | `related_prompt_agent` | 智能体明确无模型参数训练 | EvoTrace/EvoReplay研究进化编码智能体生成、重放和筛选程序的搜索轨迹；摘要没有训练智能体语言模型参数。 | [原始来源](https://openreview.net/forum?id=a2ZN4PGsoR) |
| TEMPA: Temporally Extended Memory for Policy Adaptation | `related_prompt_agent` | 智能体明确无模型参数训练 | TEMPA明确声明部署后模型参数冻结，通过可执行记忆片段、经验优势和路由器适配行为。 | [原始来源](https://openreview.net/forum?id=N7EPk5dvDX) |
| SpecEvo: Speculative Evolution with Large Language Models for Cost-Efficient Scientific Discovery | `related_prompt_agent` | 智能体明确无模型参数训练 | SpecEvo用固定的轻量与前沿模型生成、精炼候选程序并把搜索证据蒸馏成持久指导，未报告更新这些模型参数。 | [原始来源](https://openreview.net/forum?id=LOHzPGrcTQ) |
| Remembering Through Change: Provenance-Preserving Hypergraph Memory for Multimodal Agents | `related_prompt_agent` | 智能体明确无模型参数训练 | MHG-Mem的核心是多模态超图记忆及其智能体检索遍历，没有语言模型或策略模型参数训练证据。 | [原始来源](https://openreview.net/forum?id=X52294nnHl) |
| RB-Prompt: Detecting and Repairing Prompt Saturation in Reflective Optimization | `related_prompt_agent` | 提示词核心 | RB-Prompt明确以不改变模型权重的反思式提示优化为对象，搜索和修复保存的提示词。 | [原始来源](https://openreview.net/forum?id=uVKMqFVBDG) |
| Optimizing Content Policies against Unauthorized Use by Large Language Models | `related_prompt_agent` | 提示词核心 | PACT用模型引导进化搜索改写保护前提与响应指令的表达结构，本质是文本政策/指令优化，模型与外部任务保持不变。 | [原始来源](https://openreview.net/forum?id=xuYAIX5ouE) |
| Modular Discovery of General Game-Playing Algorithms with Large Language Models | `related_prompt_agent` | 智能体明确无模型参数训练 | 多智能体LLM系统共同进化C++搜索机制和规则合成启发式；神经policy-value表示仅作为冻结比较对象。 | [原始来源](https://openreview.net/forum?id=7Ukbo7ZShy) |
| MiniRep: Robust Reputation-Based Aggregation for Multi-Agent Debate | `related_prompt_agent` | 智能体明确无模型参数训练 | MiniRep优化多智能体辩论中的信誉评估与答案聚合，不训练参与辩论的语言模型。 | [原始来源](https://openreview.net/forum?id=EvAw2OPG25) |
| LinkEvo: Learning When to Recombine Modular Prompts | `related_prompt_agent` | 提示词核心 | LinkEvo明确是模块化提示遗传优化，变异和重组instruction body。 | [原始来源](https://openreview.net/forum?id=OQNjPFbr1Z) |
| Large Language Models as Prior Elicitors for Sample-Efficient Black-Box Optimization | `related_prompt_agent` | 智能体明确无模型参数训练 | LLM agent只负责生成候选解的两两偏好以构造BO函数先验；研究没有训练或持久更新该语言模型。 | [原始来源](https://openreview.net/forum?id=tj6MpVTUHZ) |
| InterEvolve: Self-Evolving Agentic Search via Retrieval–Understanding Interaction | `related_prompt_agent` | 智能体明确无模型参数训练 | InterEvolve明确无需额外模型训练或任务微调，只通过检索—理解一致性和查询验证改善智能体搜索。 | [原始来源](https://openreview.net/forum?id=DIvAq35uE6) |
| HypoEvolve: Genetic Algorithms Enable Multi-Agent LLMs to Discover Scientific Hypotheses | `related_prompt_agent` | 智能体明确无模型参数训练 | HypoEvolve用遗传算法协调LLM科学智能体更新假设种群，未报告更新任何智能体模型参数。 | [原始来源](https://openreview.net/forum?id=xWGRBqGz2h) |
| HISTORY IS NOT STATE: CAUSAL DIAGNOSTICS FOR SUFFICIENT-STATE FAILURES IN LANGUAGE AGENTS | `related_prompt_agent` | 智能体明确无模型参数训练 | MarkovLens是语言智能体历史—状态—决策链的因果诊断框架，干预状态表示但不训练智能体模型参数。 | [原始来源](https://openreview.net/forum?id=RaQJnQBy6u) |
| Fusion is the New Mutation: Bandit-Guided Evolution on Workflow Graphs | `related_prompt_agent` | 智能体明确无模型参数训练 | DAGO以bandit选择要融合的已有workflow，由LLM生成子workflow；持久更新的是图和bandit奖励模型，不是语言智能体模型。 | [原始来源](https://openreview.net/forum?id=rdupqcKSju) |
| Discovering Multiagent Learning Algorithms with Large Language Models | `related_prompt_agent` | 智能体明确无模型参数训练 | AlphaEvolve搜索并蒸馏MARL求解器代码，核心产物是闭式算法而非训练LLM编码智能体参数。 | [原始来源](https://openreview.net/forum?id=rcijc7IjDd) |
| Discovering Efficient and Explainable Communication Topologies for LLM-based Multi-Agent Systems via Causal Inference | `related_prompt_agent` | 智能体明确无模型参数训练 | E2-Explainer解释并裁剪LLM多智能体通信拓扑，更新的是拓扑解释器/子图而非语言智能体政策参数。 | [原始来源](https://openreview.net/forum?id=cVG2eV2lua) |
| Confirmation Is Not Attestation: How Agent Memory Mints Fresh Authority | `related_prompt_agent` | 智能体明确无模型参数训练 | 论文研究持久记忆引用确认的授权缺口并改造签发规则，不训练语言智能体模型。 | [原始来源](https://openreview.net/forum?id=jvwoKSo6Uq) |
| CoEvolve: Traceable Reflective Memory Evolution for Prompt Optimization | `related_prompt_agent` | 提示词核心 | CoEvolve明确是反思式提示优化器，把自然语言反思记忆作为候选并进化。 | [原始来源](https://openreview.net/forum?id=wbQy4kEPym) |
| CoER: Defending against Adaptive Indirect Prompt Injection via Adversarial Co-Evolution and Refinement | `related_hybrid` | 提示词核心 | CoER 的核心任务是 adaptive indirect prompt injection：攻击者反复生成/适配注入内容，虽同时以 BA-RL 和 fine-tuning 训练 defender，仍命中“提示词相关暂缓”例外。 | [原始来源](https://openreview.net/forum?id=SUxaNjKUP8) |
| Characterizing Abductive Reasoning Failures in Large Language Models with Elenchos | `related_prompt_agent` | 智能体明确无模型参数训练 | Elenchos评估LLM智能体在黑箱形式环境中的溯因推理并做诊断消融，没有模型参数优化。 | [原始来源](https://openreview.net/forum?id=WiY7GTwHkb) |
| Breaking Homogeneity: Diversifying Persona Sets for Creative LLM Outputs | `related_prompt_agent` | 提示词核心 | 论文以persona集合条件化来诱导输出，并进化生成persona；persona是输入文本/提示组件而非模型参数。 | [原始来源](https://openreview.net/forum?id=lD3w05aIiT) |
| Autonomous Red Teaming for Utility-Preserving Indirect Prompt Injection via Fine-Grained Diagnosis | `related_prompt_agent` | 提示词核心 | EPOA迭代优化间接提示注入payload，优化对象是植入外部内容的恶意指令文本。 | [原始来源](https://openreview.net/forum?id=kbGIuuTWP0) |
| ACE-Guard: Automated Co-Evolutionary Guardrails for LLM Security via Inference-Time Natural Language Gradients | `related_hybrid` | 提示词核心 | ACE-Guard 的核心是 prompt injection 防御与 natural-language prompt steering，且摘要明确 ΔΘ=0；属于提示词核心。 | [原始来源](https://openreview.net/forum?id=8YtHcGc4sq) |
| You Only Reprogram Once: Rethinking Prolonged Training for Visual Reprogramming | `related_closed_form` | 提示词核心 | 论文以 visual reprogramming 为研究对象：主方案从冻结模型响应构造下游映射，扩展方案直接优化 visual prompt；其适配对象是输入/视觉提示而非模型参数。 | [原始来源](https://openreview.net/forum?id=1Ijpq0Nino) |
| Test-Time Safety Alignment | `related_inference` | 提示词核心 | 核心机制是在测试时用零阶安全分数优化输入 embeddings，属于软提示/输入提示优化。 | [原始来源](https://openreview.net/forum?id=dcWHMLpYZE) |
| WikiEvolve: Coupling Foundational and Experiential Knowledge in Self-Evolving Agents | `related_prompt_agent` | 智能体明确无模型参数训练 | WikiEvolve让固定wiki与累积经验记忆指导候选解进化，摘要没有训练智能体模型参数。 | [原始来源](https://openreview.net/forum?id=evK7w4wFCc) |
| Which Tasks Stay Vulnerable? Cross-Goal Persistence of Prompt-Injection Risk in LLM Agents | `related_prompt_agent` | 智能体明确无模型参数训练 | CASPER测量冻结任务风险排序在不同注入目标间的持续性，属于智能体安全评测，未训练智能体模型。 | [原始来源](https://openreview.net/forum?id=MZodbg4BOZ) |
| Where Autonomy Belongs: A Separation of Powers for Agentic Program Evolution | `related_prompt_agent` | 智能体明确无模型参数训练 | EvoTrias重构编码智能体的治理、提议和评审权限及运行时接口，进化的是程序候选而非智能体模型参数。 | [原始来源](https://openreview.net/forum?id=7WJBskIhxM) |
| When to Prompt, When to Update: Context-Parameter Allocation for Language Agents | `related_hybrid` | 提示词核心 | 论文直接研究 prompt information 与 parameter writes 的分配，并以 controller 投影/维护 prompt state；即使会触发参数更新，也属于提示词核心。 | [原始来源](https://openreview.net/forum?id=OTIZLTbN5q) |
| When Correct Memory Goes Wrong: Fuzzing Persistent Memory Use in LLM Agents | `related_prompt_agent` | 智能体明确无模型参数训练 | U-Fuzz从记忆检查点出发变异查询或记忆状态以发现智能体故障，不训练语言智能体参数。 | [原始来源](https://openreview.net/forum?id=fvUewMH9lG) |
| What Should the Reflector See? An Empirical Study of Evidence in Reflective Prompt Optimization | `related_prompt_agent` | 提示词核心 | 论文直接比较反思式提示优化的九种证据配置，并在搜索中修订指令。 | [原始来源](https://openreview.net/forum?id=7e7pAnM0JR) |
| VAPOR: Automatic Prompt Optimization for Vision-Language Models via Visual Reflection | `related_prompt_agent` | 提示词核心 | VAPOR明确是VLM自动提示优化，构建并路由层级专家提示。 | [原始来源](https://openreview.net/forum?id=H1G5NrhRUc) |
| Uncovering Robustness Weaknesses in LLM Agents via Persona Evolution with Task-Integrity Constraints | `related_prompt_agent` | 提示词核心 | Tiper进化的是持久用户persona和行为策略，用文本用户模拟暴露智能体弱点；未训练被测智能体模型。 | [原始来源](https://openreview.net/forum?id=O4HXAtmx7v) |
| The Seven-Year Itch of Lifelong Agents: When Perfect Memory Prevents Adaptation | `related_prompt_agent` | 智能体明确无模型参数训练 | FAM调整长期记忆中旧经历影响当前个性化的方式，保留外部记忆并传递状态，未报告训练语言模型参数。 | [原始来源](https://openreview.net/forum?id=2e5z57jIPK) |
| TabEvo: LLM-Guided Evolution of Dataset-Conditional Programs for Tabular In-Context Learning | `related_prompt_agent` | 智能体明确无模型参数训练 | TabEvo的LLM agent循环与进化搜索编辑表格学习程序；被拟合的是程序中的GP、残差学习器等，不是语言智能体模型。 | [原始来源](https://openreview.net/forum?id=l1YqHcNb2s) |
| TCP-MCP: Landscape-Guided Co-Evolution of Prompts and Communication Topologies for Multi-Agent Systems | `related_prompt_agent` | 提示词核心 | TCP-MCP将多智能体提示词与通信拓扑作为统一基因共同进化，提示词是核心优化对象。 | [原始来源](https://openreview.net/forum?id=llCtjFLimR) |
| Stride: Scale-Aware Multi-Agent Evolutionary Refinement for Infographic Generation | `related_prompt_agent` | 智能体明确无模型参数训练 | Stride明确在冻结图像生成器上通过多智能体规划、候选生成和验证器单调接受优化输出，没有训练代理模型参数。 | [原始来源](https://openreview.net/forum?id=qT1Thc0dst) |
| Stable Loci Addressing: A Shared-State Architecture for Referential Stability in Evolving Long-Term LLM Memory | `related_prompt_agent` | 智能体明确无模型参数训练 | SLA是零可训练参数的共享状态记忆寻址架构，并在冻结DeltaNet上集成。 | [原始来源](https://openreview.net/forum?id=xqdq8GKNoE) |
| Sprune: Training-Free Credit-and-Act for Agentic Workflows | `related_prompt_agent` | 智能体明确无模型参数训练 | Sprune明确training-free，通过Owen value和移动平均在workflow中归档、恢复、改写组件，不训练代理模型。 | [原始来源](https://openreview.net/forum?id=5uwgUxmb6F) |
| Semantic Behavioral Watermarking: Paraphrase-Robust and Forgery-Resistant Provenance for LLM Agents | `related_prompt_agent` | 智能体明确无模型参数训练 | SBW在agent高层动作选择上施加语义簇水印与密钥分桶，改变解码选择但未训练agent模型参数。 | [原始来源](https://openreview.net/forum?id=z3M8weP6Mn) |
| Self-Structuring Latent Action Spaces for Black-Box Instruction Optimization | `related_prompt_agent` | 提示词核心 | SLAE把instruction编码成离散基因型并用差分进化搜索，核心仍是黑箱指令优化。 | [原始来源](https://openreview.net/forum?id=nwDOqi2Qri) |
| Self-Improving Language Models with Bidirectional Evolutionary Search | `related_prompt_agent` | 智能体参数训练证据待核实 | BES在推理和post-training sample generation中重组候选轨迹，但摘要未明确是否用生成样本训练并持久更新语言模型参数。 | [原始来源](https://openreview.net/forum?id=DcvklOsaEP) |
| Safe Alone, Unsafe Together: Compositional Curvature Safety Alignment for Prompt Robustness | `related_hybrid` | 提示词核心 | 论文核心对象是 compositional prompt transformations、prompt safety lattice 与 prompt robustness；参数子空间修复不改变其提示词核心范围。 | [原始来源](https://openreview.net/forum?id=uXUOE1j8px) |
| STRATA: Spatiotemporal Alignment of Agentic Memory for Long-Horizon Preference Tracking | `related_prompt_agent` | 智能体明确无模型参数训练 | STRATA构建三层记忆图，并由LLM agent在推理时调用工具遍历；没有模型参数训练。 | [原始来源](https://openreview.net/forum?id=pE9wfA0TJa) |
| SM2-AHD: Search Experience Memory and Meta-Cognitive Reflection for LLM-Based Automatic Heuristic Design | `related_prompt_agent` | 智能体明确无模型参数训练 | SM2-AHD共同进化代码种群和外层启发式设计框架，记忆注入mutation prompt；未训练LLM代码生成器参数。 | [原始来源](https://openreview.net/forum?id=MBCkxr1718) |
| SEARCH WHAT YOU MUST, SOLVE WHAT YOU CAN: FEDERATED CONTINUOUS PROMPT ADAPTATION FOR BLACK-BOX VLMS | `related_prompt_agent` | 提示词核心 | FedMUSE核心之一是连续多模态提示搜索，使用分块ZO估计优化文本和视觉prompt参数，属于软提示适配。 | [原始来源](https://openreview.net/forum?id=wBmaKUqoBB) |
| Rent or Recompute?: Learning-Augmented Placement of Agent KV Caches Across Memory and Shared Storage Tiers | `related_hybrid` | 智能体明确无模型参数训练 | 核心是 agent KV-cache 在 GPU/主存/存储层之间的放置策略；语言智能体和 LLM 参数均不更新。 | [原始来源](https://openreview.net/forum?id=5MJgRASpik) |
| ReHarness: Learning Reusable Harness Evolution Across Tasks | `related_prompt_agent` | 智能体参数训练证据待核实 | ReHarness称“学习可迁移进化策略”并将其用于worker harness适配，但摘要未说明该策略是否为可训练模型、其参数类型或训练算法。 | [原始来源](https://openreview.net/forum?id=Gzda5HNz7Y) |
| Ranking-Aware Prompt Optimization for Multimodal Clinical Diagnosis | `related_prompt_agent` | 提示词核心 | 核心对象是多模态临床诊断提示词；Ranking-PE 以成对排序反馈演化候选提示词。 | [原始来源](https://openreview.net/forum?id=4JLvdwVQnj) |
| RBEPO: From Root-Cause Diagnosis to Branching Evolutionary Prompt Optimization | `related_prompt_agent` | 提示词核心 | RBEPO 的核心是按失败根因生成、评估、组合提示词重写分支。 | [原始来源](https://openreview.net/forum?id=XbT1YBExr4) |
| Proximity, Precendence and Position: A Minimum Linear Arrangement Account of Ordering Effects in LLM Prompts | `related_prompt_agent` | 提示词核心 | 核心研究对象是 in-context demonstrations 的排列顺序，即固定内容提示词的离散优化。 | [原始来源](https://openreview.net/forum?id=dp6Z7up2zP) |
| Providing Context: Enriching Graph Learning Using Language Model Priors | `related_prompt_agent` | 提示词核心 | 核心机制是将 LM-embedded global graph prompts 作为图语义条件，通过 cross-attention 注入 GNN；虽非提示搜索，仍以提示表示为主要研究对象。 | [原始来源](https://openreview.net/forum?id=nGF3lnQ3Qd) |
| Prompt Reinjection for Spatial Reasoning in MMDiTs: Signal Amount, Depth Allocation, and Content-Specific Repair | `related_prompt_agent` | 提示词核心 | 核心机制是 MMDiT 内部逐层 prompt-token reinjection，并系统选择注入位置、深度和权重；属于提示信号适配。 | [原始来源](https://openreview.net/forum?id=fmAQLVOhLg) |
| Positional Inference for Stronger Attacks on Language Models | `related_hybrid` | 提示词核心 | 论文优化 adversarial token 的 prefix/infix/suffix 位置，并转移 position posterior；优化对象是攻击 prompt 的 token placement。 | [原始来源](https://openreview.net/forum?id=uh7b7doBNd) |
| ParetoEvo: Pareto-Guided Evolutionary Tree Search for Automatic Heuristic Design with LLM Agents | `related_prompt_agent` | 智能体明确无模型参数训练 | LLM agents 生成、评估和修改可执行启发式；搜索对象是启发式程序与树节点，不是 agent 模型参数。 | [原始来源](https://openreview.net/forum?id=1Zv2iOm1Gb) |
| Paper Agent Network: Literature-Grounded Multi-Agent Program Discovery | `related_prompt_agent` | 智能体明确无模型参数训练 | PAN 的持久 coding agents 通过工具、反馈和实现历史修订程序路线，更新的是可执行 artifact 与历史。 | [原始来源](https://openreview.net/forum?id=eTpwBeLmHO) |
| PRISM: Transparent Strategy Search for Privacy Risks in LLM Agents | `related_prompt_agent` | 提示词核心 | 核心搜索对象是攻击者 instruction；稀疏 tactic code 和闭式 Bayesian surrogate 用于选择待重写指令。 | [原始来源](https://openreview.net/forum?id=5lk0NlZc4f) |
| PINNForge: Execution-Grounded Evolutionary Design of Physics-Informed Neural Networks for PDE Solving via Large Language Models | `related_prompt_agent` | 智能体明确无模型参数训练 | LLM 驱动演化的是 PINN 配置和设计组件；PINN 会训练，但没有训练语言智能体/策略模型。 | [原始来源](https://openreview.net/forum?id=DXeChT9fBB) |
| P$^2$O: Joint Policy and Prompt Optimization | `related_hybrid` | 提示词核心 | P²O 明确交替进行 prompt evolution 与 policy update，GEPA 搜索 reasoning prompts；提示词优化是核心组成。 | [原始来源](https://openreview.net/forum?id=XywNH2Ca3U) |
| Ouroboros: A Self-Developing Coding Harness with Reviewed Core Evolution | `related_prompt_agent` | 智能体明确无模型参数训练 | Ouroboros 演化 tools、context、prompts 和 harness core implementation；基座模型参数未被描述为训练对象。 | [原始来源](https://openreview.net/forum?id=w0OSBRyfSU) |
| OrderCover: Structure-Aware Budgeted Search over Prompt-Component Orders | `related_prompt_agent` | 提示词核心 | 核心是固定文本 prompt components 的排列搜索。 | [原始来源](https://openreview.net/forum?id=hciep78aST) |
| Online Automated Algorithm Design with Large Language models | `related_prompt_agent` | 智能体明确无模型参数训练 | 多智能体按优化状态合成并执行算法；更新的是可执行算法与对运行证据的解释，不是模型参数。 | [原始来源](https://openreview.net/forum?id=mm4pTeeEST) |
| NextEval: An Agent-Based Solver and Benchmark for Derivative-Free Optimization | `related_prompt_agent` | 智能体明确无模型参数训练 | NextEval 的 LLM agent 选择工具、参数和预算，数值环境维护历史；未训练智能体模型。 | [原始来源](https://openreview.net/forum?id=MsqBCJeXIT) |
| Mirrorrefine: Mirror Reflection Generation via Multi-agent Refinement with Spatial Priors | `related_prompt_agent` | 智能体明确无模型参数训练 | 多智能体迭代更新 synthesis conditions 并选择图像操作；摘要明确迭代期间全部组件参数固定。 | [原始来源](https://openreview.net/forum?id=CygM5LTLej) |
| Measured Behavior, Recorded Zero: Measurement Failures in Self-Improving Coding Agents | `related_prompt_agent` | 智能体明确无模型参数训练 | 研究明确描述 frozen language model 周围的 scaffold evolution；更新的是 scaffold，且论文主要诊断测量失败。 | [原始来源](https://openreview.net/forum?id=9UsBcc69Ua) |
| MODEPrompt: Taxonomy-Guided Pareto Evolution for Prompt Optimization | `related_prompt_agent` | 提示词核心 | MODEPrompt 核心是按推理子群 Pareto 目标演化提示词。 | [原始来源](https://openreview.net/forum?id=CkuA2Se9vX) |
| MILO: Automated Harness Discovery via Orchestrated Multi-Agent Evolution | `related_prompt_agent` | 智能体明确无模型参数训练 | MILO 共同演化完整 harness 与搜索策略；对象是 harness、lineage memory、mutators 和 curriculum，并无模型参数训练证据。 | [原始来源](https://openreview.net/forum?id=AUiAVv2xU2) |
| MAPF-Evo: LLM-Driven Evolution of Heuristics for Conflict Elimination in Multi-Agent Path Finding | `related_prompt_agent` | 智能体明确无模型参数训练 | LLM 驱动演化 MAPF-LNS 的 destroy heuristics；没有训练语言智能体模型。 | [原始来源](https://openreview.net/forum?id=jtF7cAh4OE) |
| Learning Compact State Abstractions for LLM Agents | `related_prompt_agent` | 智能体明确无模型参数训练 | 用固定 reference agent 的任务表现搜索递归状态抽象程序；更新的是程序而非 agent 参数。 | [原始来源](https://openreview.net/forum?id=v5FgAqHn7s) |
| LabBook: Harnessing Experimental History for Efficient LLM-Driven Discovery | `related_prompt_agent` | 智能体明确无模型参数训练 | LabBook 是 discovery agent 维护的外部实验记忆，驱动新程序生成；未训练 agent 模型参数。 | [原始来源](https://openreview.net/forum?id=JUgAEHSCri) |
| Is Complex Agentic Memory Always Needed? Naive RAG Is Stronger Than We Thought | `related_prompt_agent` | 智能体明确无模型参数训练 | 论文比较固定的 Raw-RAG 与复杂 agentic memory；核心状态是检索/记忆系统，不训练语言智能体参数。 | [原始来源](https://openreview.net/forum?id=MZ7kcOOYa3) |
| Harmony Harness: Multi-Objective Self-Evolution of Agent Harnesses | `related_prompt_agent` | 智能体明确无模型参数训练 | Harmony Harness 演化 agent harness 机制与基准适配，推理时组合外部工件；无模型参数训练。 | [原始来源](https://openreview.net/forum?id=cR0St8qS2n) |
| HERA: Harness–Environment Co-Evolution for Reliable Agentic Abstention | `related_prompt_agent` | 智能体明确无模型参数训练 | HERA 演化 harness 与任务环境，并明确最佳 harness 跨模型迁移且无 model-specific optimization。 | [原始来源](https://openreview.net/forum?id=aqyvExE4ST) |
| HEMO: Harness Self-Evolution for Multi-Objective Combinatorial Optimization | `related_prompt_agent` | 智能体明确无模型参数训练 | HEMO 更新的是 AOD harness 模块、持久 memory filesystem 和算子搜索编排，不是语言模型参数。 | [原始来源](https://openreview.net/forum?id=FxMC3n6AdZ) |
| Geometry of Large Language Model Controllability | `related_prompt_agent` | 提示词核心 | PGDE 的核心是用输出空间 pullback 距离筛选离散提示词跳转。 | [原始来源](https://openreview.net/forum?id=eVAaz2QSye) |
| GP-Harness: Sequential Bayesian–Evolutionary Optimisation of LLM Harnesses | `related_prompt_agent` | 智能体明确无模型参数训练 | GP-Harness 围绕 fixed model 演化、重组并选择 harness。 | [原始来源](https://openreview.net/forum?id=0T5xZWy3I2) |
| From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails | `related_prompt_agent` | 提示词核心 | 攻击核心是搜索最大化 guardrail 推理长度的自然语言 payload，属于对输入提示的优化。 | [原始来源](https://openreview.net/forum?id=2ieHfp0vhO) |
| From Operation to Interface: Where Harness Changes Enter a Fixed Model’s Tool Calls | `related_prompt_agent` | 智能体明确无模型参数训练 | 研究固定模型下不同 harness 对 tool-call 操作/接口的影响，明确讨论不触碰权重的 harness edits。 | [原始来源](https://openreview.net/forum?id=DSP0z2ufLg) |
| FedPOB: Sample-efficient Federated Prompt Optimization via Bandits | `related_prompt_agent` | 提示词核心 | FedPOB 的明确目标是联邦黑盒 prompt optimization。 | [原始来源](https://openreview.net/forum?id=psls0Sg5LI) |
| EvoG: A Modular Framework for Evolutionary Optimization of Agentic Workflows | `related_prompt_agent` | 智能体明确无模型参数训练 | EvoG 明确优化 agentic workflow 图；四组件和共享历史更新候选工作流，无模型参数训练证据。 | [原始来源](https://openreview.net/forum?id=0MiTxo4j9d) |
| EvoDisco: Strategy Discovery for Self-Evolving Agent Memory | `related_prompt_agent` | 智能体参数训练证据待核实 | EvoDisco 声称 learnable policy 按双层 fitness 更新，但摘要未说明该 policy 是参数化模型还是外部规则/状态，不能认定训练语言/策略模型参数。 | [原始来源](https://openreview.net/forum?id=FmXVyNi3hK) |
| Escaping Alignment: A Physical Trap Model of Best-of-N Jailbreaking | `related_prompt_agent` | 提示词核心 | BoN jailbreak 的核心对象是 unsafe prompt 的随机 augmentation 与 completion 采样。 | [原始来源](https://openreview.net/forum?id=x7eAMFALle) |
| Elicitation or Expansion? Demystifying Gains from Agent Harness Optimization | `related_prompt_agent` | 智能体明确无模型参数训练 | 论文明确研究不更新模型权重的 harness optimization，并分析其 elicitation/expansion 效应。 | [原始来源](https://openreview.net/forum?id=bSBejKazyx) |
| EVOUNDO: RECOVERABILITY-CONSTRAINED SELF-EVOLUTION FOR LLM AGENT HARNESSES | `related_prompt_agent` | 智能体明确无模型参数训练 | EvoUndo 的对象是 prompts、tools、middleware、resources 和 harness 自修改及其可恢复性，不是模型参数。 | [原始来源](https://openreview.net/forum?id=IFmd4fBKfS) |
| EEVEE: Post-Deployment Prompt Learning across Heterogeneous Tasks | `related_prompt_agent` | 提示词核心 | EEVEE 明确联合演化 router 与 prompt configurations，核心仍是 post-deployment prompt learning。 | [原始来源](https://openreview.net/forum?id=tHX0Ublg85) |
| E$^{2}$MEND: Evidence-guided Evolution for Memory Enhancement via Bottleneck Diagnosis | `related_prompt_agent` | 智能体明确无模型参数训练 | E2MEND 变异和回滚的是 versioned memory-strategy artifacts，runtime 锁定；未训练语言智能体模型。 | [原始来源](https://openreview.net/forum?id=EcMoDY6gpg) |
| Does Prompt Sensitivity Improve Cross-Family Degradation Prediction? | `related_prompt_agent` | 提示词核心 | 论文以十种 instruction wording 的 prompt sensitivity 为核心变量，研究其跨模型家族预测价值；虽然不优化提示词，仍属于提示词核心研究。 | [原始来源](https://openreview.net/forum?id=uVn7IU6iPN) |
| Direction-Indexed Evolutionary Red-Teaming of Large Language Models | `related_prompt_agent` | 提示词核心 | DIER 演化 roles、pretexts、personas 等 jailbreak framings，本质是攻击提示工件搜索。 | [原始来源](https://openreview.net/forum?id=TWCBAEspBn) |
| Designing and Evolving Multi-Agent Systems via a Typed Intermediate Representation | `related_prompt_agent` | 智能体明确无模型参数训练 | meta-agent 生成 typed IR 来设计 MAS；经验演化 refine design policy，但摘要明确不更新任何模型参数。 | [原始来源](https://openreview.net/forum?id=6YccHf9cEN) |
| DarwinX: Evolving Agent Harnesses through Natural Selection | `related_prompt_agent` | 智能体明确无模型参数训练 | DarwinX 明确在 model fixed 条件下演化 instructions、tools、memory 和 control-flow harness。 | [原始来源](https://openreview.net/forum?id=XVvUgp3Bu8) |
| DARWIN: Evolving Jailbreak Adversary and Guardrail for LLM Safety Evaluation and Protection | `related_hybrid` | 提示词核心 | DARWIN-Attack 以遗传变异、选择和组合持续优化 jailbreak attack strategies/prompt variants；虽训练 guardrail，仍属提示词/越狱提示搜索核心。 | [原始来源](https://openreview.net/forum?id=UmzQqgrCPV) |
| Customize Your Memory: Scenario-Adaptive and Evolvable Memory Modeling for LLM Agents | `related_prompt_agent` | 智能体明确无模型参数训练 | ScenarioModelMem 演化的是动态 memory policy 和外部记忆建模结构；摘要没有训练语言/策略模型参数。 | [原始来源](https://openreview.net/forum?id=qm5Z3S6e4g) |
| Component-Aware Feedback for Self-Evolving Programs | `related_prompt_agent` | 智能体明确无模型参数训练 | LLM 充当 mutator，核心更新对象是多组件程序及其归因记忆；摘要没有训练或持久更新语言模型参数。 | [原始来源](https://openreview.net/forum?id=PtpPmfGxts) |
| Competition Discovers, Cooperation Consolidates: Social Rewards Shape Self-Evolving LLM Agents | `related_prompt_agent` | 智能体明确无模型参数训练 | 自演化来自交互轨迹筛选并写入持久外部记忆；摘要没有模型参数训练。 | [原始来源](https://openreview.net/forum?id=plmHDI1b7d) |
| CompEvolve: Competitive Evolution of LLM Agent Harness Regularized by Behavioral Diversity and Generalization Judging | `related_prompt_agent` | 智能体明确无模型参数训练 | CompEvolve 明确进化 prompt、控制流和多智能体 harness，而非模型权重。 | [原始来源](https://openreview.net/forum?id=4IVbz5H9ER) |
| Collective Alignment in LLM Multi-Agent Systems: Disentangling Bias from Cooperation via Statistical Physics | `related_prompt_agent` | 智能体明确无模型参数训练 | 该多智能体研究只查询固定 LLM 更新晶格二元状态并测量群体现象，没有训练智能体模型参数。 | [原始来源](https://openreview.net/forum?id=Qj9Mbp6dCi) |
| CoDeL: Co-Evolutionary Defense against Indirect Prompt Injection in LLM-based Agents | `related_hybrid` | 提示词核心 | CoDeL 的 co-evolving prober 搜索 injection rounds、attack methods 与 payloads，核心是 indirect prompt injection；LoRA-GDPO defender 训练不解除提示词暂缓规则。 | [原始来源](https://openreview.net/forum?id=ywkbERYvpx) |
| Co-Evolving LLM Agents and Bayesian Optimizers for Automated Feature Engineering | `related_prompt_agent` | 智能体明确无模型参数训练 | CoEvolve 更新特征变换、双记忆、FE-MDP/DSGO 代理状态；摘要没有训练 LLM agent 的模型参数，辅助 surrogate 更新不等同代理政策训练。 | [原始来源](https://openreview.net/forum?id=Oal3lWxqBY) |
| Characterizing and Improving Bijection Attacks through Prompt-Level Perturbation | `related_prompt_agent` | 提示词核心 | 核心对象是双射编码 prompt 及 prompt-level perturbation，SLS 直接搜索可成功越狱的提示编码。 | [原始来源](https://openreview.net/forum?id=Jq6I5yUXXR) |
| CUDA-Harness: Harnessing Agentic CUDA Kernel Generation and Optimization from Natural Language | `related_prompt_agent` | 智能体明确无模型参数训练 | CUDA-Harness 的智能体生成、验证和演化 CUDA kernel 程序；摘要没有模型参数更新。 | [原始来源](https://openreview.net/forum?id=PdZhD2bbqe) |
| COMIC: Agentic Sketch Comedy Generation | `related_prompt_agent` | 智能体参数训练证据待核实 | COMIC 明确演化剧本和渲染候选，但“与观众偏好对齐的 LLM critics”是否通过模型参数训练获得，摘要没有说明。 | [原始来源](https://openreview.net/forum?id=Rfj9wv4EDR) |
| CB-Orchestrator: Adaptive Workflow Optimization for LLM Agents via Contextual Bandits | `related_prompt_agent` | 智能体明确无模型参数训练 | 两阶段方法只进化工作流池并用 contextual bandit 选择工作流，未训练 agent 模型参数。 | [原始来源](https://openreview.net/forum?id=YEDtlblPEM) |
| Breaking the Pseudo-Multi-Agent Illusion: A Parasite–Immune Multi-Agent Trading Framework | `related_hybrid` | 智能体参数训练证据待核实 | PI-MAT 以固定视角的 LLM alpha agents 生成信号，并称在线反馈驱动的 meta-learning arbiter 调整信号和资金；摘要未说明 arbiter 是否为可训练参数模型。 | [原始来源](https://openreview.net/forum?id=xiaccTalhi) |
| Beyond Successful Experience Reuse: Inducing Revision Knowledge from Evolving Experience for LLM Agents | `related_prompt_agent` | 智能体明确无模型参数训练 | CEA 从演变经验恢复程序适用条件与状态到程序映射，摘要没有模型参数训练。 | [原始来源](https://openreview.net/forum?id=oFY9G0m3ts) |
| BehEvolve: Behavior-Guided Evolution of Multi-Agent Program Policies under Sparse Task Feedback | `related_prompt_agent` | 智能体明确无模型参数训练 | BehEvolve 的持久改进对象是多智能体程序政策、代码修改和调度分支，不是语言模型参数。 | [原始来源](https://openreview.net/forum?id=GhCb2ZuoHN) |
| Bandit Limited Discrepancy Search for Agent Harness Configuration | `related_prompt_agent` | 智能体明确无模型参数训练 | BLDS-AF 搜索 agent-DAG 的 agent type、模型选择、推理预算等 harness 配置，不更新所选模型参数。 | [原始来源](https://openreview.net/forum?id=u4uHWlP1gE) |
| BRAID: Evolving Evaluators for Reliable and Effective Self-Evolving Agents | `related_prompt_agent` | 智能体明确无模型参数训练 | BRAID 明确是 training-free，演化评估器候选与任务代理分支等外部实现。 | [原始来源](https://openreview.net/forum?id=N0mDtvLk4W) |
| Automated Discovery Has No Universally Superior Harness | `related_prompt_agent` | 智能体明确无模型参数训练 | 该研究比较并自适应分配自动发现 harness 的档案、父代选择和预算组件，未训练语言智能体参数。 | [原始来源](https://openreview.net/forum?id=2ONrI9JEqu) |
| AttriOpt: Attribution-Based Credit Assignment for Evolutionary API-Calling Optimization | `related_prompt_agent` | 智能体明确无模型参数训练 | AttriOpt 进化 LLM 生成的 API workflow，并更新统计归因分数；没有训练 agent 模型参数。 | [原始来源](https://openreview.net/forum?id=NFtZmpfvFx) |
| AscendAgent: Evolving Context to Fit the Harness in CANN Kernel Optimization | `related_prompt_agent` | 智能体明确无模型参数训练 | AscendAgent 明确模型权重、workflow 和 evaluator 固定，只演化 kernel 程序图和外部可复用知识。 | [原始来源](https://openreview.net/forum?id=gtuspdBfQo) |
| Agentic Bayesian Optimization through Surrogate-Augmented Autoresearch | `related_prompt_agent` | 智能体明确无模型参数训练 | Sara 调整 BO 评估选择、边界和问题表述，概率 surrogate 存于外部 backend；摘要未训练 LLM agent 参数。 | [原始来源](https://openreview.net/forum?id=ZIF61XReMF) |
| Adaptive Transfer for Cost-Aware Bayesian Optimization of LLM Agent Configurations | `related_prompt_agent` | 智能体明确无模型参数训练 | ALT 搜索 reasoning effort、工具权限和资源等 agent 配置，执行固定配置获得轨迹；不训练 agent 模型。 | [原始来源](https://openreview.net/forum?id=UjDZ0KzZ4X) |
| Adaptive Scenario Selection for Screening Overeager Behavior in Coding Agents | `related_prompt_agent` | 智能体明确无模型参数训练 | ASSBF 只改变筛查场景和 Thompson-sampling 预算，执行固定 framework–model pairs，没有智能体模型训练。 | [原始来源](https://openreview.net/forum?id=E6IQGL7SaC) |
| AdaGEPA: Adaptive Feedback Allocation for Reflective Prompt Optimization | `related_prompt_agent` | 提示词核心 | AdaGEPA 的目标就是通过反馈分配反复优化 prompt。 | [原始来源](https://openreview.net/forum?id=GxTIfjjhA4) |
| Active Learning for Communication Structure Optimization in LLM-Based Multi-Agent Systems | `related_prompt_agent` | 智能体明确无模型参数训练 | 方法更新多智能体通信图参数分布和任务选择状态，不是语言/策略模型参数。 | [原始来源](https://openreview.net/forum?id=esnxNWIVMO) |
| APEX-Data: Automated Prompt Engineering eXpert with Dynamic Data Selection | `related_prompt_agent` | 提示词核心 | APEX-Data 明确与数据分层联合执行 prompt search，核心产物仍是优化后的 prompt。 | [原始来源](https://openreview.net/forum?id=urjXCbKVzH) |
| AGAR: A REINFORCEMENT LEARNING SUBSTRATE FOR LLM PROGRAM EVOLUTION | `related_prompt_agent` | 智能体明确无模型参数训练 | AGAR 进化候选程序和 modular-prefix controller，且明确 backend model 不做梯度训练。 | [原始来源](https://openreview.net/forum?id=npY9pJqb57) |
| A Closer Look at Agentic BBO: Benchmarking LLM Agents for Black-Box Optimization | `related_prompt_agent` | 智能体明确无模型参数训练 | AgenticBBO-Bench 执行固定 LLM agents 做黑盒候选搜索并评估工具/先验，不训练其模型参数。 | [原始来源](https://openreview.net/forum?id=aAcE9xwrev) |
| SeaEvo: Strategy as State for LLM-Driven Evolution | `related_prompt_agent` | 智能体明确无模型参数训练 | SeaEvo 持久化程序候选的文本策略描述和群体状态，未更新 LLM 参数。 | [原始来源](https://openreview.net/forum?id=39Hpdbjdtz) |
| BayesianAgent: Guiding Agentic Evolution with Bayesian Optimization | `related_prompt_agent` | 智能体明确无模型参数训练 | BayesianAgent 用 GP/Thompson sampling 分配候选扩展实验，改进的是可执行方案而非 LLM 参数。 | [原始来源](https://openreview.net/forum?id=CzDLiwNxO8) |
| Stateful Search with Stateless Agents: Scaling Long-Horizon Automated Research | `related_prompt_agent` | 智能体明确无模型参数训练 | AES 由 harness 保存候选和测量结果并重建上下文，持久状态明确位于代理对话之外。 | [原始来源](https://openreview.net/forum?id=DK9rlpEHBf) |
| Gödel Ecology: Productivity-Guided Continuous Co-Evolution of Agents and Evaluators for Collective Recursive Self-Improvement | `related_prompt_agent` | 智能体参数训练证据待核实 | 摘要只说进化 agent/evaluator implementations，没有说明这些 implementation 是模型权重、adapter，还是 prompt/代码等外部工件。 | [原始来源](https://openreview.net/forum?id=N4GJVmrzsF) |
| From Knobs to Actions: Agentic Bayesian Optimization for Self-Improving System Tuning | `related_prompt_agent` | 智能体明确无模型参数训练 | EvoTune 用 agentic BO 调节数据库、Spark/LLM inference engine 的系统配置，未训练语言智能体模型。 | [原始来源](https://openreview.net/forum?id=am1vQQwJJ1) |
| SPOON: Strategy-based Prompt Optimization for Multi-Agent LLM Games | `related_prompt_agent` | 提示词核心 | SPOON 把多智能体策略直接表示为文本规则并做 strategy-based prompt optimization，且明确不更新模型权重。 | [原始来源](https://openreview.net/forum?id=cAhKtc1zVk) |
| A Risk-Bounded Gate for Self-Improving Agents: Selecting Modifications as a Mean–Variance Knapsack | `related_prompt_agent` | 智能体明确无模型参数训练 | 方法选择 memory、reflection、judge、cache、restart 和 prompt add-ons 等外部修改，测试使用 frozen LLM packer。 | [原始来源](https://openreview.net/forum?id=fPPQnFGSYd) |
| $\text{Turing}^2$: Scaling Turing-Style Evaluation to Optimize Human Simulation in Dialogue | `related_prompt_agent` | 提示词核心 | Turing² 明确通过 prompt optimization 共同改进 user simulator 与 Machine-Turing judge，并明确不更新模型参数。 | [原始来源](https://openreview.net/forum?id=jdJFvMPRZK) |
| HIRE: Hippocampal Replay for Test-Time Agentic Reinforcement Learning | `related_inference` | 智能体明确无模型参数训练 | HIRE 是智能体测试时强化学习，但官方摘要明确不更新模型参数；它通过 replay 与优势重加权适配冻结策略。 | [原始来源](https://openreview.net/forum?id=kbCX1FVPSj) |
| The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators | `related_prompt_agent` | 智能体参数训练证据待核实 | RQGM 共同演化 coder/writer/reviewer/grader，但摘要未说明被改写的是模型权重、adapter、prompt 还是代码。 | [原始来源](https://openreview.net/forum?id=o3txFJw4JR) |
| AIM: Agentic Idea Management for Automated Research | `related_prompt_agent` | 智能体明确无模型参数训练 | AIM 管理研究想法、解候选和实验预算，摘要没有训练语言智能体模型参数。 | [原始来源](https://openreview.net/forum?id=rnK26MhdGM) |
| AscendOptimizer: Episodic Agent for Ascend NPU Operator Optimization | `related_prompt_agent` | 智能体明确无模型参数训练 | AscendOptimizer 更新 tiling/data-movement 配置、kernel 程序和执行经验，而非代理模型参数。 | [原始来源](https://openreview.net/forum?id=wtVho001dF) |
| TABRSI: A RECURSIVE SELF-IMPROVING MULTI- AGENT SYSTEM FOR TABLE UNDERSTANDING AND REASONING | `related_prompt_agent` | 智能体明确无模型参数训练 | DGM/HGM-Flow 演化的是角色代码、拓扑和推理模式等可执行多智能体流水线工件，没有模型参数训练证据。 | [原始来源](https://openreview.net/forum?id=ypByqdkzf3) |
| AT-AT: Automatic Tool Optimization from Agent Traces | `related_prompt_agent` | 智能体明确无模型参数训练 | AT-AT 明确保持 agents fixed，只编辑共享工具描述和实现。 | [原始来源](https://openreview.net/forum?id=pp2JaGrr0r) |
| Self-Evolution Should Be Stable, Not Frozen: Lyapunov-Gated Recursive Self-Improvement | `related_prompt_agent` | 智能体参数训练证据待核实 | EVOLYAPUNOV 接纳 agent/improver 自修改，但摘要未说明自修改究竟包含模型权重还是外部 prompt、代码或记忆。 | [原始来源](https://openreview.net/forum?id=3t0j2Y05EH) |
| SCAMP: Black-Box Knowledge Poisoning Attack on Multimodal Retrieval-Augmented Generation | `related_prompt_agent` | 智能体参数训练证据待核实 | SCAMP 更新图文投毒对和视觉原型；Visual/Text Attacker、Competing Agents 与 Evaluators 是否另行训练模型参数，摘要未说明。 | [原始来源](https://openreview.net/forum?id=O26AmnGkFD) |
| Diagnosing Failure Regimes in LLM Agent Memory with Extraction-Pass Disagreement | `related_inference` | 智能体明确无模型参数训练 | RRC 是 LLM agent memory 的 training-free 配置层，通过多次记忆整合分歧路由投票预算、检索深度和回答策略。 | [原始来源](https://openreview.net/forum?id=vpahOt8lBU) |
| In-Context Robot Learning with VLM Agents | `related_prompt_agent` | 智能体明确无模型参数训练 | GPT-Policy 是 VLM agent，但摘要明确只做部署期上下文适配，不做梯度更新或任务参数持久修改。 | [原始来源](https://openreview.net/forum?id=LIa6SeOhH9) |
| Code-Probe-Adapt: Interactive Heuristic Learning for Self-Evolving Agents | `related_prompt_agent` | 智能体明确无模型参数训练 | COPA 通过 REPL 探测和修订 code-as-policy heuristic，摘要明确整体无需梯度更新。 | [原始来源](https://openreview.net/forum?id=zeF8echOqR) |
| scCoLLM: An LLM-Based Model Using Context-Space Adaptation for Single-Cell Analysis under Domain Shift | `related_inference` | 提示词核心 | scCoLLM 把适配从参数空间转为 context space，检索并组装 Bio-Context 供固定 GPT 条件生成，核心属于上下文/提示构造。 | [原始来源](https://openreview.net/forum?id=ICtYd1vctM) |
| Eliciting Model Behaviors by Optimizing the Latent Posterior | `related_hybrid` | 提示词核心 | Posterior Prefix Tuning 优化 hard-prompt 分布以诱导模型行为，优化对象明确是 prompt。 | [原始来源](https://openreview.net/forum?id=hw82nCsx4L) |
| Suppressing a Rejected Action Costs a KL: Closed-Form Test-Time Updates for LLM Agents | `related_closed_form` | 智能体参数训练证据待核实 | TALE 面向 LLM agent 的失败动作恢复，并对输出侧表示施加低秩编辑；但摘要没有说明该表示是否是可训练模型参数、适配器参数或仅为会话内状态，不能据 model editing 推断参数训练。 | [原始来源](https://openreview.net/forum?id=e4pspmOVIV) |

## 未确认事项

- “智能体参数训练证据待核实”10 条保持在可恢复归档中，不出现在现行目录；需要正文明确被更新的是模型权重/adapter/神经 policy，还是 prompt、程序、实现或外部状态后再决定。
- 部分保留训练型论文的原始摘要确认了 SFT、RL、PPO、policy update 或 parameter adaptation，但没有逐项给出优化器和反向传播实现；报告据实标为未说明，不把全系统描述为纯 ES/ZO。
- `Rent or Recompute?` 仅训练 idle-gap predictor；它服务 KV-cache 放置，不是语言智能体 policy、LLM、LoRA 或 adapter，因此属于明确无智能体模型参数训练。

## 完整覆盖与可恢复性

- [批次 1](2026-10-12-prompt-agent-scope-batch-1.md)：56 条。
- [批次 2](2026-10-12-prompt-agent-scope-batch-2.md)：56 条。
- [批次 3](2026-10-12-prompt-agent-scope-batch-3.md)：55 条。
- [批次 4](2026-10-12-prompt-agent-scope-batch-4.md)：73 条。
- [批次 5](2026-10-12-prompt-agent-scope-batch-5.md)：40 条。
- [批次 6](2026-10-12-prompt-agent-scope-batch-6.md)：109 条。

上述批次合计 389 条且互斥。归档逐条保存原 catalog record、原 BibTeX、原 review record、来源、官方摘要、原分类、scope decision 和明确移出原因。集合与书目校验结果见 [`2026-10-12-prompt-agent-scope-validation.json`](2026-10-12-prompt-agent-scope-validation.json)。
