# ICLR 2027 提示词与智能体范围审查：批次 1

本批次逐篇依据仓库已有 OpenReview 官方摘要审查，共 56 条。未发起新检索。决定只反映 2026-10-12 用户指定的目录范围，不评价论文有效性或学术质量。

## 统计

- 保留：不受本次范围影响：14 条
- 保留：智能体模型参数训练证据明确：1 条
- 暂缓：提示词/提示参数为核心对象：12 条
- 暂缓：智能体未训练模型参数：27 条
- 暂缓：智能体参数训练证据待核实：2 条

## 逐篇决定

### 1. What Do Evolutionary Coding Agents Evolve?

- 决定：暂缓：智能体未训练模型参数
- 具体依据：EvoTrace/EvoReplay研究进化编码智能体生成、重放和筛选程序的搜索轨迹；摘要没有训练智能体语言模型参数。
- 更新对象：程序、局部搜索状态与评测记录；未更新智能体模型参数。
- 方法/训练算法：进化式程序生成、重放、固定结构参数调优和事后分析。
- 反向传播：摘要未说明训练语言模型；LLM作为生成器和评审器调用。
- 待核实：固定结构参数调优针对生成程序而非语言模型权重。
- 原始来源：[OpenReview](https://openreview.net/forum?id=a2ZN4PGsoR)
- 官方摘要证据：Recent work pairs LLMs with evolutionary search to iteratively generate, modify, and select code using task-specific feedback.
These systems have produced strong results in mathematical discovery and algorithm design, yet a fundamental question remains: what do they actually evolve?
Progress is typically summarized by the best score a run reaches under a task-specific evaluator, but that score can reflect several different mechanisms: new algorithmic structure, re-tuning an existing strategy, recombining ideas already in the model's internal knowledge, or overfitting to the evaluator.
Distinguishing these mechanisms requires inspecting the search process itself, not only its final outcome.
We introduce EvoTrace, a dataset of 121 evolutionary coding runs spanning four frameworks, five models, and 16 tasks across mathematics and algorithm design, comprising 10,672 unique programs.
We also develop EvoReplay, which reconstructs local search states and supports held-out rescoring, same-prompt replay, and fixed-structure parameter tuning.
Using a multi-label LLM judge validated against blind human re-annotation, we assign parent--child edits to nine recurring categories.
The most frequent edit categories are not those most strongly associated with beating the parent. The median run reintroduces about 30\% of its added lines from code deleted earlier in the same lineage, and these edits more often repair weak parents than advance the run best.
Fixed-structure tuning can recover improvements otherwise reached through later LLM edits, exposed-evaluator gains can reverse on held-out instances, and same-prompt replay often recovers much of the original score without reproducing the winning code.
These results show that benchmark gains in evolutionary coding agents can arise from qualitatively different mechanisms, only some of which correspond to new algorithmic structure.

### 2. TEMPA: Temporally Extended Memory for Policy Adaptation

- 决定：暂缓：智能体未训练模型参数
- 具体依据：TEMPA明确声明部署后模型参数冻结，通过可执行记忆片段、经验优势和路由器适配行为。
- 更新对象：可执行记忆片段、经验统计和路由决策；LLM参数冻结。
- 方法/训练算法：半马尔可夫规划、经验优势选择和自适应路由。
- 反向传播：摘要明确模型参数冻结；未报告对LLM反向传播。
- 待核实：路由器是否含可训练参数未说明，但摘要所述适配对象是策略外部记忆。
- 原始来源：[OpenReview](https://openreview.net/forum?id=N7EPk5dvDX)
- 官方摘要证据：Large language model (LLM) agents must learn from online experience to improve their behavior, even though their parameters remain frozen after deployment.
Reusing complete episode trajectories as prompt context can incur additional token costs, while
estimating individual action values from experience is challenging under sparse and delayed rewards.
These challenges motivate policy adaptation through planning over action segments at an intermediate temporal granularity. We introduce
TEMPA (Temporally Extended Memory for Policy Adaptation), a gradient-free framework
that adapts an agent's policy over actor actions and executable memory segments.
It partitions interaction at reward events and stores the resulting reward-to-reward segments as executable options. These segments are selected using empirical advantages.
A router uses evidence from exploratory trials to choose between executing the selected segment and invoking the LLM actor. TEMPA reuses multi-step behaviors without separate credit estimates for constituent actions and reduces repeated actor inference during memory execution.We formulate memory exploitation as finite-horizon semi-Markov planning and establish a
conditional sublinear bound on exploration loss relative to the incumbent policy.
Experiments on Jericho and ScienceWorld show that TEMPA achieves
higher average scores and stronger late-episode performance.
Its total inference token consumption is roughly 56\% lower
than the mean across the seven baselines.
Ablations support the contributions of reward-based segmentation,
continuation values, adaptive routing, and persistent execution.

### 3. SpecEvo: Speculative Evolution with Large Language Models for Cost-Efficient Scientific Discovery

- 决定：暂缓：智能体未训练模型参数
- 具体依据：SpecEvo用固定的轻量与前沿模型生成、精炼候选程序并把搜索证据蒸馏成持久指导，未报告更新这些模型参数。
- 更新对象：候选程序、种群与自然语言搜索指导。
- 方法/训练算法：多模型推测—汇总式进化搜索。
- 反向传播：摘要未报告模型训练或反向传播。
- 待核实：Advisor的“distills”指证据汇总，未证明参数蒸馏。
- 原始来源：[OpenReview](https://openreview.net/forum?id=LOHzPGrcTQ)
- 官方摘要证据：LLM-driven evolutionary search is a promising paradigm for scientific discovery, but existing methods remain costly and slow, often applying expensive reasoning uniformly while underusing evidence from failed, redundant, and saturated trials. We introduce Speculative Evolution (SpecEvo), a multi-LLM framework that coordinates lightweight and frontier models through continual consolidation of search evidence. Lightweight models power both parallel Speculators, which generate and refine candidate programs, and an Advisor, which distills accumulated successes, failures, and saturated directions into persistent guidance for subsequent exploration. At sparse checkpoints, a frontier-model Navigator inspects the evolving population and intervenes through synthesis, surgical refinement, or reframing according to search stagnation. This speculate-then-consolidate workflow delegates routine exploration and evidence consolidation to inexpensive models while reserving frontier reasoning for strategic interventions whose benefits extend across many subsequent low-cost evaluations. Across 176 tasks spanning four scientific and algorithmic discovery domains, SpecEvo matches or outperforms frontier-model baselines while reducing API cost by up to 80%, achieves up to 1.5× greater evaluation efficiency than cost-efficient baselines on equation discovery, and improves over the strongest CO-Bench baseline by 3.8%. These results support trajectory-conditioned model coordination as an effective approach to cost-efficient scientific discovery.

### 4. Remembering Through Change: Provenance-Preserving Hypergraph Memory for Multimodal Agents

- 决定：暂缓：智能体未训练模型参数
- 具体依据：MHG-Mem的核心是多模态超图记忆及其智能体检索遍历，没有语言模型或策略模型参数训练证据。
- 更新对象：实体/事实节点、超边、演化状态和检索路径。
- 方法/训练算法：超图记忆构建与基于工具的智能体搜索。
- 反向传播：摘要未报告模型训练或反向传播。
- 待核实：状态合成器的实现细节未说明。
- 原始来源：[OpenReview](https://openreview.net/forum?id=X52294nnHl)
- 官方摘要证据：Long-term memory for multimodal agents remains challenging, as it must preserve fine-grained visual evidence while tracking entity evolution across sessions. Existing abstraction-based memories compress images into text, often discarding visually discriminative details, whereas pixel-preserving memories retain raw observations but struggle to reliably associate diverse observations with persistent entity identities and track their evolving states. To address these limitations, we propose MHG-Mem, a multimodal hypergraph memory that jointly organizes entity identity, state evolution, and provenance to visual evidence. Specifically, MHG-Mem represents distinct entity mentions and their observed facts as individual nodes, grouping identity-consistent mentions and facts through occurrence hyperedges. It then synthesizes aspect-specific evolution states from these grouped observations and links them to supporting entities, facts, and source evidence through evolutionary and evidential hyperedges. To navigate this structured memory, we introduce hypergraph-based agentic search, which adaptively selects an entry layer, traverses typed hyperedges across memory levels, and inspects source observations when fine-grained verification is required. These designs support both detailed visual verification and reasoning over cross-session state changes. Extensive experiments across three benchmarks demonstrate the effectiveness of MHG-Mem, improving performance by 8.20-9.98% over the strongest baseline.

### 5. RB-Prompt: Detecting and Repairing Prompt Saturation in Reflective Optimization

- 决定：暂缓：提示词/提示参数为核心对象
- 具体依据：RB-Prompt明确以不改变模型权重的反思式提示优化为对象，搜索和修复保存的提示词。
- 更新对象：自然语言提示词及其指令长度。
- 方法/训练算法：分支回退、反思式规则删并、长度惩罚与贝叶斯选择。
- 反向传播：摘要明确不改变模型权重。
- 待核实：无。
- 原始来源：[OpenReview](https://openreview.net/forum?id=uVKMqFVBDG)
- 官方摘要证据：Prompt optimization adapts large language models to new tasks without changing their weights. Reflective optimizers rewrite prompts using feedback on model errors, but can keep adding instructions after performance stops improving. We call this prompt saturation: search spends evaluation budget on longer prompts with little gain. We address this problem with RB-PROMPT, which detects saturation from recent scores and instruction growth. It returns to a branch’s best saved prompt and asks reflection to remove or combine unnecessary rules. Search continues with a penalty for added instruction length and Bayesian selection guided by past rewrite gains. We evaluate on HotpotQA, GSM8K, and an existing document extraction task at a major global automotive manufacturer, using three model families. Under matched task-evaluation budgets, RB-PROMPT achieves the highest or joint-highest score in all nine settings, with the largest gains on HotpotQA and extraction. It achieves higher scores while using 40–45% fewer optimization tokens than TextBO-GEPA. Comparisons from the same saved states isolate the repair’s benefit over continued reflection. We show that adding repair to GEPA and TextBO-GEPA improves performance without changing their parent-selection rules. These findings support adaptive branch repair as a reusable component of reflective prompt optimization.

### 6. Profiling Compression, Disrupting Distributions: Structured Adversarial Attacks on Token-Compressed Large Vision-Language Models

- 决定：保留：不受本次范围影响
- 具体依据：CLOUD核心是针对压缩LVLM的结构化对抗攻击：优化替代模型配置、攻击支持集和输入扰动，不是提示词优化或智能体训练范围。
- 更新对象：替代模型配置、视觉token支持集和对抗输入扰动。
- 方法/训练算法：贝叶斯优化、DPP支持集构造与最优传输目标。
- 反向传播：摘要未说明受害LVLM训练；是否训练替代模型池未说明。
- 待核实：具体梯度计算路径待原文确认，但不属于本次提示词/智能体范围。
- 原始来源：[OpenReview](https://openreview.net/forum?id=zLqQFeOCf2)
- 官方摘要证据：Visual token compression offers a promising pathway to improve the efficiency of large vision-language models (LVLMs). However, it creates a fundamental mismatch for adversarial attacks: compression acts on token representations, whereas attack success is evaluated at the sequence level. Existing attacks typically identify tokens likely to survive compression and optimize perturbations over this predicted survivor set. Yet this strategy overlooks two challenges: token utility varies across compression schemes, and independent survival scores cannot capture the joint attack effect of retained tokens. To address these challenges, we propose Compression-Aware Profiling with Coordinated Distributional Disruption (CLOUD), a novel framework for conducting adversarial attacks that remain effective across distinct token-compression schemes. The key idea is to profile compression-dependent attack utility with a surrogate pool and then coordinate support construction with distributional perturbation. Specifically, we first introduce a utility-guided surrogate probing module, which applies Bayesian optimization over the surrogate configuration space to characterize compression-aware attack responses. Subsequently, we construct a dynamic cache to aggregate token-retention patterns and representation shifts across surrogates to calibrate the attack budget. Guided by these profiles, we leverage a determinantal point process (DPP)  to construct a diverse support set by balancing compression resilience with complementary evidence coverage. Additionally, we maximize the discrepancy between clean evidence and its post-compression adversarial counterpart from the perspective of optimal transport (OT). This coordinated objective encourages the attack effect to persist after token reduction. Experiments across multiple LVLM backbones and compression schemes show that CLOUD consistently outperforms strong baselines. Code is available at https://anonymous.4open.science/r/CLOUD_For_Token_Compression_Robustness.

### 7. Phase Geometry of Reasoning: Predicting and Controlling Evidence Integration in Large Language Models

- 决定：保留：不受本次范围影响
- 具体依据：CPIR分析和干预LLM证据整合轨迹并做校准，不以提示词优化或智能体系统为核心。
- 更新对象：证据顺序、掩蔽、极性和强度等推理干预。
- 方法/训练算法：受控干预、状态空间拟合与校准评估。
- 反向传播：合成环境中的比较模型包含拟合；Qwen和DeepSeek判断模型是否冻结未逐项说明。
- 待核实：模型拟合细节待原文确认，但不触发本次范围收紧。
- 原始来源：[OpenReview](https://openreview.net/forum?id=ut4zYIin58)
- 官方摘要证据：Large language models often produce different probabilistic judgments when equivalent evidence is reordered, reframed, or combined, yet the latent thought dynamics responsible for these changes remain poorly understood. We operationalize a thought as an atomic, belief-changing state transition induced by processing one evidence item, and represent reasoning as a trajectory through a latent state space. We hypothesize that these trajectories follow complex-valued, noncommutative dynamics in which phase-dependent interference determines how successive thoughts combine. To test this hypothesis, we introduce Complex Probabilistic Interventional Reasoning (CPIR), a controlled framework that traces model judgments across three-step reasoning sequences with known priors and likelihood ratios. CPIR intervenes on individual thought updates through evidence masking, polarity reversal, strength modification, order permutation, paraphrasing, and compositionally held-out combinations of these operations. We compare a complex-valued state-space model with normative Bayesian inference, logistic interaction models, nonlinear real-valued recurrent models, and parameter-matched controls. On five frozen synthetic environments with planted complex-coherent dynamics, CPIR identifies the correct compositional family and predicts held-out domains, paraphrases, and longer sequences, reducing joint-holdout logit RMSE from 0.072 to 0.023 relative to the strongest real-valued baseline. When transferred to Qwen3-14B and DeepSeek-V3.2 judgments, the same prespecified procedure discovers target-specific real and heterogeneous predictive regimes, demonstrating selective model assignment across targets. Extending CPIR to sequential LLM evaluation, repeatability and competence controls reveal that the observed cross-order reversal rate (11.1\%) is matched by same-order variation (10.0\%) for the competence-qualified judge, motivating checklist elicitation that reduces reversals to 0.7\%. At equal inference cost, averaging opposite criterion orders improves Brier score from 0.156 to 0.146 over averaging two same-order evaluations, with the gain concentrated in probabilistic calibration. Together, these results show that CPIR can recover structured thought composition, discriminate among compositional regimes, and improve the stability and calibration of sequential LLM evaluation.

### 8. Optimizing Content Policies against Unauthorized Use by Large Language Models

- 决定：暂缓：提示词/提示参数为核心对象
- 具体依据：PACT用模型引导进化搜索改写保护前提与响应指令的表达结构，本质是文本政策/指令优化，模型与外部任务保持不变。
- 更新对象：保护前提、响应指令及其层级文本政策。
- 方法/训练算法：前提条件生成与反馈驱动的进化搜索。
- 反向传播：摘要未报告更新LLM参数。
- 待核实：“policy”是内容使用文本政策，不是训练出的神经策略模型。
- 原始来源：[OpenReview](https://openreview.net/forum?id=xuYAIX5ouE)
- 官方摘要证据：Large language models (LLMs) are increasingly relying on content provided by users or crawled from external sources to carry out tasks.
However, source owners may share or publish material without authorizing their contents for use by LLMs.
We propose **Policy Adaptation for Content Protection (PACT)**, a method for optimizing content-use policies that enable source owners to unilaterally restrict such unwanted LLM use.
PACT formulates content-use restriction as policy induction over the hierarchical policy structure that connects protection premises to response directives governing the model's response.
Within this formulation, premise-conditioned generation constructs the response directives, while model-guided evolutionary search uses response feedback to jointly refine the premise and directive structure.
The search adjusts how the restriction is expressed while keeping the protected content and external task unchanged.
We evaluate the resulting policies on question answering and summarization across four sensitive content domains and five models.
On unseen content, the policies achieve 91.78\%-100\% answer suppression under Global Protection.
The policies also support targeted protection and generalize across models, with policies optimized using GPT-5.6-Sol exceeding 80\% suppression on all four other models under Global Protection.
These findings suggest that content-use policies can help source owners limit unwanted LLM use, while distinguishing generalization to new content from transfer to another model.

### 9. Modular Discovery of General Game-Playing Algorithms with Large Language Models

- 决定：暂缓：智能体未训练模型参数
- 具体依据：多智能体LLM系统共同进化C++搜索机制和规则合成启发式；神经policy-value表示仅作为冻结比较对象。
- 更新对象：C++程序化搜索机制和领域启发式。
- 方法/训练算法：LLM提议/重构代码的多智能体进化搜索。
- 反向传播：摘要明确评测时神经表示冻结；未报告训练LLM智能体。
- 待核实：PPO训练只描述部分游戏表示/比较设置，不是所提智能体模型训练。
- 原始来源：[OpenReview](https://openreview.net/forum?id=7Ukbo7ZShy)
- 官方摘要证据：General Game Playing across arbitrary games from rules alone remains challenging due to differing algorithmic requirements across game classes and strict decision-time constraints. Rather than hand-designing search heuristics for specific domains, can we leverage Large Language Models (LLMs) to discover general game-playing algorithms? Because language models can propose and refactor structured code, they provide an expressive proposal engine for exploring the space of algorithmic designs. We introduce a multi-agent LLM meta-learning system to co-evolve game-agnostic procedural search mechanisms in C++ alongside domain heuristics synthesized directly from game rules. Controlling the compute budget, we benchmark the discovered mechanisms across more than 400 diverse environments, including OpenSpiel training and held-out games, procedural simulation engines, and games with deep neural policy-value representations trained via PPO. Evaluated via AlphaRank stationary distributions and Soft Condorcet Optimization (SCO) against 15 established MCTS baselines, the discovered search mechanisms consistently achieve top-tier ratings and pairwise ballot majorities over most baselines across independent evolutionary runs, generalizing to unseen human-designed and procedurally synthesized games and remaining competitive with baselines on frozen neural network representations.

### 10. MiniRep: Robust Reputation-Based Aggregation for Multi-Agent Debate

- 决定：暂缓：智能体未训练模型参数
- 具体依据：MiniRep优化多智能体辩论中的信誉评估与答案聚合，不训练参与辩论的语言模型。
- 更新对象：代理信誉、当前行为评分与聚合权重/决策。
- 方法/训练算法：信誉感知的稳健聚合和攻击评测。
- 反向传播：摘要未报告模型训练或反向传播。
- 待核实：聚合系统内部是否含拟合组件未说明。
- 原始来源：[OpenReview](https://openreview.net/forum?id=EvAw2OPG25)
- 官方摘要证据：Autonomous agents powered by large language models (LLMs) are rapidly evolving into an open agentic ecosystem. To support trustworthy collaboration, industry initiatives increasingly assess agent reputation from past behavior and provide performance leaderboards. However, reputation derived from past performance may not reliably predict an agent's behavior on new tasks, particularly when malicious agents can adapt their behavior and influence other agents during collaboration.

We study reputation in multi-agent debate (MAD), where multiple agents answer the same query,  debate to improve their answers, and aggregate them into a final output. We present MiniRep, a reputation-based aggregation system for MAD under malicious agents. To ground our threat model in established research, we construct an attack taxonomy drawing on reputation-system attacks and software-testing mutation operators, covering strategic exploitation of reputation and subtle corruption of agent proposals. Guided by this taxonomy, MiniRep evaluates agents based on both their behavior on the current task and their reputation over time, while preventing groups of agents with highly similar responses from dominating the final decision. We assess MiniRep across diverse tasks, LLM-agent compositions, corruption placements, and attack types drawn from our taxonomy. Our experimental results show that, MiniRep outperforms both conventional MAD aggregation and conventional reputation-based approaches on MATH no matter being attacked or not. Also, under a heterogeneous 10-agent setting on MATH, MiniRep outperforms all baselines in all 28 attack conditions.

### 11. LinkEvo: Learning When to Recombine Modular Prompts

- 决定：暂缓：提示词/提示参数为核心对象
- 具体依据：LinkEvo明确是模块化提示遗传优化，变异和重组instruction body。
- 更新对象：模块化指令块/提示词。
- 方法/训练算法：受限种群遗传优化、受控块替换和上下文加权门控收益。
- 反向传播：摘要未报告更新执行模型参数。
- 待核实：无。
- 原始来源：[OpenReview](https://openreview.net/forum?id=OQNjPFbr1Z)
- 官方摘要证据：Genetic prompt optimization improves modular language-model systems by evolving instruction bodies while preserving their interfaces, tools, and control flow.
However, recombination can disrupt dependencies between modules, and the value of inheriting an instruction block changes with its recipient context and evaluation cost.
We introduce LinkEvo, a bounded-population genetic optimizer that measures interactions through controlled block substitutions, builds candidate groups from these measurements, and allocates mutation and crossover effort using context-weighted signed gate gains under an explicit adaptation budget.
Across six benchmarks and six executor families, LinkEvo achieved positive observed differences in 34 of 36 settings against uniform genetic-action allocation and 33 against GEPA with merging, with median gains of 1.59 and 0.82 percentage points, respectively, and Qwen3.6 retrieval gains over GEPA with merging of 1.20 points on HotpotQA and 1.33 on HoVer.
These results identify a practical role for optimization history in learning which instruction combinations to inherit and when their predicted utility warrants further evaluation, supporting gains across several model families while exposing small mixed differences on reasoning tasks.

### 12. Large Language Models as Prior Elicitors for Sample-Efficient Black-Box Optimization

- 决定：暂缓：智能体未训练模型参数
- 具体依据：LLM agent只负责生成候选解的两两偏好以构造BO函数先验；研究没有训练或持久更新该语言模型。
- 更新对象：外部黑箱目标的概率先验、偏好数据和候选解。
- 方法/训练算法：智能体偏好诱导、贝叶斯偏好学习与GP-LCB。
- 反向传播：贝叶斯偏好模型会拟合；摘要未报告LLM参数训练。
- 待核实：偏好学习模型的参数不是语言智能体策略参数。
- 原始来源：[OpenReview](https://openreview.net/forum?id=tj6MpVTUHZ)
- 官方摘要证据：Many scientific and engineering applications require optimizing complex decisions whose outcomes can only be evaluated through costly simulations, experiments, or high-fidelity models, giving rise to black-box optimization (BBO) under tight evaluation budgets. Existing BBO methods typically learn from objective evaluations collected on the target task and therefore rely heavily on costly observation-driven exploration. Large language models (LLMs), with broad cross-domain knowledge, offer a potential opportunities to alleviate this dependence. This study introduces a different perspective on using LLMs for BBO: rather than using LLMs to assist sampling, we elicit embedded domain knowledge of LLMs to explicitly form a probabilistic distribution over objective functions.  Specifically, we develop an LLM-enhanced Bayesian optimization framework that first elicits a probabilistic prior over the objective function from LLMs and then incorporates this prior into Bayesian optimization. The key idea is to develop an agentic preference elicitation method, where an LLM agent is established to analyze the problem context and to generate pairwise preferences between candidate solutions, thereby deriving a probabilistic distribution through Bayesian preference learning before expensive evaluations are collected. Theoretically, we show that the elicited distribution contracts predictive uncertainty and information gain and, under an explicit alignment condition, yields a no-larger finite-budget GP-LCB simple-regret bound than the reference prior. We further establish controlled sensitivity to corrupted preferences and show that an initially biased prior can be corrected as sufficiently informative objective observations accumulate. Experiments on six real-world benchmarks demonstrate improved sample efficiency, with the largest gains under limited evaluation budgets.

### 13. InterEvolve: Self-Evolving Agentic Search via Retrieval–Understanding Interaction

- 决定：暂缓：智能体未训练模型参数
- 具体依据：InterEvolve明确无需额外模型训练或任务微调，只通过检索—理解一致性和查询验证改善智能体搜索。
- 更新对象：检索状态评估和改写后的查询。
- 方法/训练算法：RUPA进度评估与QRV查询精炼验证。
- 反向传播：摘要明确无额外模型训练/微调。
- 待核实：无。
- 原始来源：[OpenReview](https://openreview.net/forum?id=DIvAq35uE6)
- 官方摘要证据：State assessment in self-evolving agentic search poses significant challenges, as inaccurate evaluations can mislead the evolutionary trajectory and trap the system in redundant or mis-evolved loops.
In this paper, we observe that humans mitigate such failures via retrieval-understanding interaction.
During multi-turn search, they use prior understanding to form expectations about retrieval results and assess the consistency between results and expectations to resist misdirection from search outputs.
Inspired by this behavior, we propose InterEvolve, an agentic search framework that improves the accuracy of state assessment without requiring additional model training or task-specific fine-tuning.
Specifically, InterEvolve comprises two main components: the Retrieval–Understanding Progress Assessor (RUPA) and the Query Refinement Validator (QRV).
RUPA leverages retrieval–understanding consistency to assess whether each search iteration progresses in a productive direction.
Moreover, QRV constrains retrieval discrepancies between the original and refined queries, ensuring reliable query refinement and preventing misdirected evolution.
Extensive experiments on the MMEB-v2 benchmark (78 datasets) across 4 popular retrieval backbones demonstrate that InterEvolve consistently outperforms the naive agentic search baseline in all model combinations.
Notably, agentic search relying on weaker models like Qwen3.8-27B for state assessment suffers from misdirected evolution, degrading from 74.96 to 74.14 below single-turn retrieval.
InterEvolve recovers this degradation and further improves it to 75.48, demonstrating its robustness safeguard.
The code will be released if the paper is accepted.

### 14. HypoEvolve: Genetic Algorithms Enable Multi-Agent LLMs to Discover Scientific Hypotheses

- 决定：暂缓：智能体未训练模型参数
- 具体依据：HypoEvolve用遗传算法协调LLM科学智能体更新假设种群，未报告更新任何智能体模型参数。
- 更新对象：科学假设种群。
- 方法/训练算法：生成式遗传算法、专业化智能体评议和外部证据评测。
- 反向传播：摘要未报告模型训练或反向传播。
- 待核实：无。
- 原始来源：[OpenReview](https://openreview.net/forum?id=xWGRBqGz2h)
- 官方摘要证据：Scientific agents increasingly contribute to hypothesis discovery by synthesizing evidence, assessing proposals, and developing new explanations. Recent systems bring scientific agents and evolutionary search together to develop hypotheses through cycles of critique, comparison, and revision. However, how different forms of agent collaboration affect hypothesis quality remains an open question. Answering this question requires separating the effects of agents' scientific capabilities from those of their collaboration. A suitable framework must therefore preserve the agents' scientific roles and support different rules for combining, revising, and retaining hypotheses. Building on this perspective, we introduce HypoEvolve, which makes collaboration explicit through successive updates to a hypothesis population. Specifically, we propose to use a generational genetic algorithm to coordinate specialized large language model (LLM) agents that integrate mechanistic arguments, reconsider assumptions, and assess evidence and testability. Each generation specifies how scientific judgments and new proposals reshape the population, which makes the effects of collaboration on hypothesis quality directly testable. Moreover, we design our evaluation around scientifically meaningful hypotheses that explain how a proposed intervention could work. Drug repurposing connects these explanations to target-level biological claims that can be assessed against external evidence. Specifically, we adapt DepMap and Open Targets into complementary external measures grounded in experimental, genetic, and clinical evidence. The evaluation spans 34 cancer types, with HypoEvolve achieving the highest scores against six baselines on both measures. DepMap selectivity reaches 0.171, compared with 0.115 for the strongest baseline. Gains over single-pass generation also generalize to held-out cancer types. HypoEvolve advances a vision of autonomous science in which AI research teams achieve a capacity for discovery beyond that of individual models.

### 15. HISTORY IS NOT STATE: CAUSAL DIAGNOSTICS FOR SUFFICIENT-STATE FAILURES IN LANGUAGE AGENTS

- 决定：暂缓：智能体未训练模型参数
- 具体依据：MarkovLens是语言智能体历史—状态—决策链的因果诊断框架，干预状态表示但不训练智能体模型参数。
- 更新对象：任务充分状态、历史表示和诊断统计。
- 方法/训练算法：受控状态干预和四项因果诊断。
- 反向传播：摘要未报告模型训练或反向传播。
- 待核实：不属于模型参数优化方法。
- 原始来源：[OpenReview](https://openreview.net/forum?id=RaQJnQBy6u)
- 官方摘要证据：Language agents are increasingly deployed in interactions where user goals, ev-idence,
and environment states evolve over time. Final accuracy alone does
not reveal where failures enter the history-to-state-to-decision chain. We pro-pose
MarkovLens, a causal diagnostic framework that uses task-sufffcient states
as intervention targets: canonical, non-leaking representations under which the
target decision should be independent of the surface history, given the current
query and decision context. We introduce four diagnostics: the sufffcient-state
gap (SSG), Markov invariance violation (MIV), state update error (SUE), and
obsolete-state attraction (OSA). On a 96-state balanced User Constraint Update
grid, qwen2.5:7b improves from 0.833 raw-history accuracy to 1.000 gold-state
accuracy (SSG = +0.167, 95% CI [0.130, 0.206]), while mistral:7b ex-hibits
the opposite compact-state pattern (0.917 to 0.833, SSG = −0.083, 95% CI
[−0.151, −0.023]). This opposite sign is not a contradiction: interface-equalized
controls show that explicit-state rendering is itself part of the mechanism. Cross-task
results extend the diagnostic beyond user constraints: on a 48-group Code
Requirement Drift slice, qwen2.5:7b again shows a positive SSG (0.755 to
1.000, SSG = +0.245, 95% CI [0.135, 0.354]), while mistral:7b remains di-rectionally
negative but statistically unstable. Tool/Environment Mutation shows
that compact states can hurt while dialogue-style states can recover performance,
and OSA calibration supports strong stale-state attraction for qwen2.5:7b but
not equally for mistral:7b. MarkovLens is therefore a diagnostic microscope
rather than a leaderboard or universal repair: it localizes whether models fail to
infer the current state, fail to use an explicit state interface, or remain attracted to
stale states.

### 16. Fusion is the New Mutation: Bandit-Guided Evolution on Workflow Graphs

- 决定：暂缓：智能体未训练模型参数
- 具体依据：DAGO以bandit选择要融合的已有workflow，由LLM生成子workflow；持久更新的是图和bandit奖励模型，不是语言智能体模型。
- 更新对象：workflow代码/提示、谱系DAG和LinUCB统计。
- 方法/训练算法：上下文bandit选亲与多亲workflow融合。
- 反向传播：LinUCB在线更新；摘要未报告LLM参数训练。
- 待核实：bandit奖励模型不是语言智能体策略模型。
- 原始来源：[OpenReview](https://openreview.net/forum?id=rdupqcKSju)
- 官方摘要证据：Automated agentic workflow optimization relies on costly evaluations, making it essential to allocate a limited evaluation budget effectively. Multi-parent fusion can reuse designs from previously discovered workflows, but identifying promising parent combinations requires learning from limited fusion feedback. We introduce \textbf{DAGO} (Directed Acyclic Graph Optimization), a contextual-bandit-guided framework that learns which parent workflows to fuse under a limited evaluation budget. DAGO formulates each candidate parent combination as an \textbf{arm}, represented by pretrained embeddings of its constituent workflows' code and prompts. A diagonal LinUCB policy learns a shared reward model across arms and balances exploitation of arms with high predicted offspring quality against uncertainty-driven exploration. After an arm is selected, an LLM generates a child workflow through summary-guided fusion, and the child's validation score serves as the reward for updating the bandit. A shared directed acyclic graph maintains discovered workflows and their multi-parent lineage, providing an expanding pool of parents for subsequent arm proposals. Across six benchmarks covering mathematical reasoning, code generation, and question answering, DAGO achieves the highest macro-average score among the evaluated baselines. Under matched validation-evaluation budgets, it improves over AFlow from 80.3 to 81.7 while reducing aggregate search expenditure by 11.2\%. Ablation studies show that LinUCB-guided arm selection outperforms both random selection and its exploration-free variant, supporting the value of feedback-driven selection and exploration--exploitation balance.

### 17. Discovering Multiagent Learning Algorithms with Large Language Models

- 决定：暂缓：智能体未训练模型参数
- 具体依据：AlphaEvolve搜索并蒸馏MARL求解器代码，核心产物是闭式算法而非训练LLM编码智能体参数。
- 更新对象：CFR/PSRO算法代码和闭式求解器。
- 方法/训练算法：进化编码搜索、消融和算法蒸馏。
- 反向传播：摘要未报告训练LLM；求解器评测可能内部运行学习算法。
- 待核实：“training set”是搜索适应度环境集合，不证明LLM参数训练。
- 原始来源：[OpenReview](https://openreview.net/forum?id=rcijc7IjDd)
- 官方摘要证据：Much of the advancement in Multi-Agent Reinforcement Learning (MARL) for imperfect-information games has historically depended on the manual, iterative refinement of algorithmic baselines. Recently, evolutionary coding agents powered by Large Language Models (LLMs) have emerged as powerful tools to automate this discovery process.
In this work, we deploy one of such agentic frameworks, AlphaEvolve, to navigate the design spaces of two distinct game-theoretic paradigms: counterfactual regret minimization (CFR) and policy-space response oracles (PSRO).
This automated search yielded two algorithms: Volatility-Adaptive Discounted (VAD-) CFR and Smoothed Hybrid Optimistic Regret (SHOR-) PSRO, which are consistently competitive with state-of-the-art human-designed baselines across an 18-game evaluation suite spanning Poker, Goofspiel, Liar's Dice, Blotto, and Battleship variants.
However, because the LLM optimizes for fitness on a specific training set, it often constructs highly synergistic, complex mechanisms tailored to those environments. Through systematic train-only ablation criteria, we distill these discoveries into two minimal closed-form solvers: Warm-started Optimistic Predictive (WOP-)CFR and Projection Matching (PM-)PSRO. Ten independent search runs confirm that the distilled cores recur while the overfitted machinery differs across runs. Distillation isolates this stable algorithmic core, achieving superior held-out performance at drastically reduced structural complexity: WOP-CFR improves on scaled variants within family and maintains parity out of family, while PM-PSRO improves in both regimes and most strongly out of family.

### 18. Discovering Efficient and Explainable Communication Topologies for LLM-based Multi-Agent Systems via Causal Inference

- 决定：暂缓：智能体未训练模型参数
- 具体依据：E2-Explainer解释并裁剪LLM多智能体通信拓扑，更新的是拓扑解释器/子图而非语言智能体政策参数。
- 更新对象：通信边归因、紧凑子图和摊销解释器。
- 方法/训练算法：Granger式遮蔽归因与解释器蒸馏。
- 反向传播：摘要称摊销解释器被distill，可能训练解释器；未报告训练LLM智能体参数。
- 待核实：解释器的结构和训练细节待核实，但与代理政策模型更新不同。
- 原始来源：[OpenReview](https://openreview.net/forum?id=cVG2eV2lua)
- 官方摘要证据：The performance of large language model (LLM)-based multi-agent systems (MAS) largely depends on effective communication topologies. Existing topology generation methods, however, typically learn communication topologies through black-box optimization driven solely by task-level rewards. While effective, such optimization provides little insight into why particular communication edges are selected, making it difficult to identify the critical communication subgraphs responsible for successful collaboration. To address this limitation, we propose E2-Explainer, a model-agnostic framework for providing interpretable explanations of communication topologies produced by arbitrary topology generators. Specifically, we formulate topology explanation as a causal attribution problem that identifies compact communication subgraphs supported by edge-level evidence of task preservation. We obtain this evidence with a Granger-style objective that measures how masking each communication channel changes the task outcome and the stability of the final response. The resulting budgeted subgraphs are then distilled into an amortized explainer, enabling efficient post-hoc explanation without repeated edge-level evaluations at deployment. Extensive experiments on multiple reasoning and coding benchmarks demonstrate that E2-Explainer identifies critical communication subgraphs that preserve successful collaboration. These subgraphs can also be executed directly to prune redundant communication edges, substantially reducing communication costs while maintaining competitive task performance.

### 19. Confirmation Is Not Attestation: How Agent Memory Mints Fresh Authority

- 决定：暂缓：智能体未训练模型参数
- 具体依据：论文研究持久记忆引用确认的授权缺口并改造签发规则，不训练语言智能体模型。
- 更新对象：记忆记录、确认对象绑定和授权签发证据。
- 方法/训练算法：匹配任务实验、来源敏感签发和开放式模型评审。
- 反向传播：摘要未报告模型训练或反向传播。
- 待核实：无。
- 原始来源：[OpenReview](https://openreview.net/forum?id=jvwoKSo6Uq)
- 官方摘要证据：Persistent memory lets agents reuse saved values without asking users to repeat them. This convenience creates an authorization ambiguity: approving “use my saved address” confirms an operation over a record, but does not necessarily attest the hidden value resolved from that record. We study this referential-confirmation gap in matched retail and airline tasks with official state mutations. Across 21 entities, a conventional issuer commits externally supplied values in 21/21 cases even though the confirmation is valid and the resulting capabilities are fresh, scoped, and single-use. Two changes eliminate the effect while preserving 21/21 clean completion: showing and binding the exact candidate value, or requiring authenticated source evidence during issuance. We replace the deterministic confirmation oracle with open-ended review by three models. Among 63 hidden-reference decisions, 54 explicitly delegate, two request clarification, and seven affirm without delegation; six of those seven express an expected-value restriction. Conventional issuance nevertheless commits all seven paired external alternatives, whereas source-sensitive issuance rejects all seven. Complete-value review accepts all 63 correct values and no alternatives. The boundary persists across an independent LangGraph implementation, visible warnings, conversational planning, and five memory transformations. A valid confirmation response therefore becomes an authorization fact only when the system records which concrete object the response and its supporting evidence bind.

### 20. CoEvolve: Traceable Reflective Memory Evolution for Prompt Optimization

- 决定：暂缓：提示词/提示参数为核心对象
- 具体依据：CoEvolve明确是反思式提示优化器，把自然语言反思记忆作为候选并进化。
- 更新对象：反思标识集合、持久反思存储与优化后的提示政策。
- 方法/训练算法：Distill、结构化记忆变异、共享评估和亲本相对选择。
- 反向传播：摘要未报告更新基础模型权重。
- 待核实：“Distill”是失败到文本政策的整理，未证明神经参数蒸馏。
- 原始来源：[OpenReview](https://openreview.net/forum?id=wbQy4kEPym)
- 官方摘要证据：Reflective prompt optimization turns model failures into reusable natural-language guidance, but free-form memory is difficult to attribute, repair, and control as it grows. We introduce \method{}, a prompt optimizer that represents each candidate as a traceable set of reflection identifiers and evolves this memory under an explicit budget. The system couples candidate lineage with a persistent reflection store and combines automatic failure-to-policy Distill, structured memory mutations, shared evaluation, and parent-relative memory-growth-aware selection. In five-run, equal-budget locked-test comparisons spanning financial tagging and arithmetic, multi-hop question answering, and differential diagnosis, CoEvolve-Distill leads on FINER, HotpotQA, and DDXPlus. An independent-split protocol reduces the selection optimism gap from 0.023 to 0.007--0.011. Removing persistent state causes the largest ablation loss and variability, whereas score-only selection preserves quality but uses substantially more policy tokens. In controlled recovery episodes, full provenance improves harmful-memory identification and recovery while retaining at least 0.978 of task score. These results support treating reflective memory as an explicit, auditable optimization object rather than unstructured prompt text.

### 21. Characterizing Abductive Reasoning Failures in Large Language Models with Elenchos

- 决定：暂缓：智能体未训练模型参数
- 具体依据：Elenchos评估LLM智能体在黑箱形式环境中的溯因推理并做诊断消融，没有模型参数优化。
- 更新对象：交互探针、假设归因和评测诊断。
- 方法/训练算法：黑箱交互评测与干预式消融。
- 反向传播：摘要未报告模型训练或反向传播。
- 待核实：无。
- 原始来源：[OpenReview](https://openreview.net/forum?id=WiY7GTwHkb)
- 官方摘要证据：Large language models (LLMs) are highly capable of reasoning from known rules to their consequences, but their ability to reason in the opposite direction -- from observed behavior to the rules that produced it -- remains poorly understood. Recent work has characterized this transition from observations to hypotheses about underlying rules as an ``abductive jump'' and argued that it remains challenging for current reasoning systems. To investigate this challenge, we introduce \emph{Elenchos}, a framework for evaluating abductive inference in controlled executable formal environments, instantiated here in a dependently typed $\lambda$-calculus kernel. Given a pair of kernels, exactly one of which is sound and the other intentionally mutated, agents interact with both through a black-box interface to determine which of the two kernels is sound and identify the mutations responsible for observed behavioral differences.

Evaluating frontier and mid-tier LLMs on Elenchos reveals a striking dissociation between detecting an alteration and identifying its cause: models frequently determine which kernel is sound and gather probes that uniquely distinguish competing mutations, yet often fail to identify the mutations responsible for the observed behavioral differences. To isolate the mechanisms driving this breakdown, we conduct diagnostic ablation studies on GPT-5.4 (high reasoning). These show that forward simulation of mutated systems is substantially harder than simulation of the sound system, but that simulation accuracy does not predict attribution accuracy during interactive reasoning. Remarkably, when the predicted consequences of competing hypotheses are provided explicitly, the model identifies the responsible mutation with near-perfect accuracy. Together, these results point to two interacting bottlenecks in abductive reasoning: deriving the behavioral consequences of competing hypotheses and integrating those consequences with accumulated evidence during interactive attribution.

### 22. BudgetWeaver: Learning the Downstream Value of Agent Reads and Memory Mutations under Shared Budgets

- 决定：保留：智能体模型参数训练证据明确
- 具体依据：BudgetWeaver学习记忆操作策略，且摘要明确分别拟合Llama-3.1-8B-Instruct controllers，构成语言控制器参数训练证据。
- 更新对象：Llama-3.1-8B-Instruct记忆控制器/操作策略参数，以及运行中的记忆状态。
- 方法/训练算法：离线价值细化、读与NOOP配对结果、成本准入与控制器拟合。
- 反向传播：摘要确认控制器被拟合，但未说明优化器及是否反向传播。
- 待核实：需原文核实具体微调形式、可训练层和是否端到端训练。
- 原始来源：[OpenReview](https://openreview.net/forum?id=I1lt2QZWPr)
- 官方摘要证据：Every optional-memory action changes two things at once: the current context and the evidence--budget state inherited by later decisions. A write can preserve verified progress, an eviction can remove a stale hypothesis, and a summary can make later evidence affordable. Controllers that score each operation only for its immediate use miss this intertemporal choice when every read and mutation spends the same token--latency budget. BudgetWeaver learns the downstream value of a seven-operation sequence over NOOP, retrieval, reranking, graph traversal, summarization, writing, and eviction. Its policy combines remaining budget and memory state with paired read-versus-NOOP endpoint outcomes, support-aware offline value refinement, predicted-cost admission, and realized-cost accounting. We isolate the controller by fixing prompts, candidates, operators, retrievers, stores, schemas, and guards across all matched policies. At the predeclared medium operating point, BudgetWeaver improves native success over tuned full-interface non-RL control by 1.8--2.6 points on LOCOMO v2, SWE-bench Lite v1.1, and OdysseyBench v1.3; every paired interval excludes zero and all three tests remain significant after Holm correction. Relative to always-retrieve, success rises by 3.7--4.9 points while paired full-run token use falls by 4.1k--5.4k and end-to-end p95 latency falls by 1.6--2.7 seconds. Removing persistent mutations costs 1.3--2.8 points, with the largest descriptive effects in contradiction-heavy and longest-horizon episodes, and separately fitted Llama-3.1-8B-Instruct controllers retain a 1.7--2.6-point lead over tuned non-RL control. These results make downstream memory-state value an actionable control signal: coordinating reads and mutations improves success while reducing complete-run resource use.

### 23. Breaking Homogeneity: Diversifying Persona Sets for Creative LLM Outputs

- 决定：暂缓：提示词/提示参数为核心对象
- 具体依据：论文以persona集合条件化来诱导输出，并进化生成persona；persona是输入文本/提示组件而非模型参数。
- 更新对象：persona文本集合。
- 方法/训练算法：子集选择、空间填充采样和进化persona生成。
- 反向传播：摘要未报告更新模型参数。
- 待核实：无。
- 原始来源：[OpenReview](https://openreview.net/forum?id=lD3w05aIiT)
- 官方摘要证据：Language models often produce homogeneous responses to open-ended tasks; such homogeneity can spawn groupthink---the convergence of ideas toward a singular and potentially suboptimal decision. We formulate persona diversification as a set-level conditioning problem and study two orthogonal design choices: selecting versus generating personas, and space-filling versus frontier-seeking diversity. We instantiate this design space with four methods spanning coverage and dispersion subset selections, uniform-coverage sampling, and evolutionary persona generation. Evaluations on the Alternative Uses Task (AUT), Infinity-Chat, and Divergent Association Task (DAT) show the benefits of the proposed methods across tasks and creativity objectives. On AUT, evolutionary persona generation increases response diversity by 78.8\%, originality by 26.1\%, flexibility by 49.5\%, and holistic creativity by 13.9\% over task-only prompting, while maintaining 98.5\% validity; on Infinity-Chat, it nearly doubles persona-induced response separation relative to random personas. Moreover, evolutionary personas compose with creativity-optimized prompting, further increasing its response diversity by 18.6\% and creativity by 6.3\%. These results establish persona-set geometry as a task-agnostic mechanism for eliciting divergent LLM outputs, and support persona diversification as a reusable complement to prompt optimization.

### 24. Behavioral Capacity Certificates for Quantized Language Models

- 决定：保留：不受本次范围影响
- 具体依据：BCC研究量化语言模型的行为容量证书、位宽筛选和认证权重操作，非提示词或智能体研究。
- 更新对象：量化位宽、权重编码、激活/KV-cache规则。
- 方法/训练算法：前向筛选、margin证书和复杂度界。
- 反向传播：前向筛选无需Hessian；未报告训练模型参数。
- 待核实：不属于本次范围。
- 原始来源：[OpenReview](https://openreview.net/forum?id=BLtMieC3Ds)
- 官方摘要证据：Activation and key--value cache precision change what a quantized language model
computes without altering its stored weights. Direct weight-code bounds, however,
assign identical complexity to deployments that behave differently and charge
separately for weight codes that behave identically. Behavioral Capacity
Certificates (BCC) charge for behavior using the aggregate prior mass of complete
implementations---weights, scales, activation and cache rules---that induce the
same bounded loss. When quantization merges implementations, this shared mass
lowers the complexity penalty, and a break-even law determines when the saving
survives the cost of validating it. BCC supports a three-step deployment
workflow, and our experiments verify each step. First, a forward-only screen
shortlists per-layer bit-widths by how often candidate perturbations preserve the
reference predictions, with quality comparable to Hessian-guided selection at
lower preprocessing cost. Second, margin-certified cells identify weights that can be pruned or
sign-flipped without changing the deployed behavior: every permitted
combination preserves all declared predictions, and on OLMoE-1B-7B and
SmolLM2-1.7B, independent probes bound the probability that any permitted
combination changes a prediction on new text. Third, BCC bounds the population loss of the deployed model,
nonvacuously for complete decoders and more tightly than the
compressed-code route. At equal cache memory, giving keys higher
precision than values yields lower NLL and higher prediction
agreement on GPT-2, Qwen2.5, and SmolLM2, together with a tighter
complexity bound in the GPT-2 audit.

### 25. BOReFT: Manifold Steering of Language Models for Black-box Optimization

- 决定：保留：不受本次范围影响
- 具体依据：BOReFT在冻结语言模型中学习低维隐藏状态干预空间并以BO搜索，是非智能体的内部表示适配，不是提示词核心。
- 更新对象：冻结LM的低维隐藏状态干预空间和外部候选。
- 方法/训练算法：表示微调式空间学习与贝叶斯优化。
- 反向传播：摘要明确LM冻结；低维干预空间如何学习及是否反传待核实。
- 待核实：可训练干预参数的精确形式待原文确认。
- 原始来源：[OpenReview](https://openreview.net/forum?id=M38068rlvo)
- 官方摘要证据：Language models are increasingly used as proposal models for black-box search, from program optimization to molecular design. Existing approaches typically improve proposals through iterative prompting or parameter updates, offering limited control over how completely and efficiently the model's search space is explored. Continuous optimization methods, such as Bayesian optimization, provide a principled way to search but require a suitable domain to operate over. To address this, we introduce BOReFT, which learns a compact, low-dimensional space of hidden-state interventions in a frozen language model, and uses this space as the search domain for Bayesian optimization with an external scoring function. Empirically, we find that the learned domain spans semantic regions and exhibits smoothness properties that support search. Theoretically, we show that semantic coverage and interpolation control the best score available in the learned space, and that decoding from this space yields a standard stochastic-bandit observation model for adaptive search. We evaluate BOReFT on the interpretable word search task "Semantle" and on three more real-world discovery tasks in de novo molecule property optimization. Compared to strong LLM baselines, BOReFT finds in Semantle a higher number of hidden targets and, on two out of three molecular objectives, achieves higher property scores. Consequently, our method provides a principled new bridge between discrete proposal spaces of LLM-based search and continuous black-box optimization.

### 26. Autonomous Red Teaming for Utility-Preserving Indirect Prompt Injection via Fine-Grained Diagnosis

- 决定：暂缓：提示词/提示参数为核心对象
- 具体依据：EPOA迭代优化间接提示注入payload，优化对象是植入外部内容的恶意指令文本。
- 更新对象：IPI payload和载体轨迹。
- 方法/训练算法：四块诊断、轨迹历史条件化候选生成与黑箱迭代。
- 反向传播：摘要未报告训练受害或优化器模型参数。
- 待核实：无。
- 原始来源：[OpenReview](https://openreview.net/forum?id=kbGIuuTWP0)
- 官方摘要证据：Indirect prompt injection (IPI) embeds malicious instructions in external content to redirect tool-using language agents toward unauthorized actions. Effective red teaming must therefore identify payloads that induce the target behavior without disrupting the legitimate user task. However, existing adaptive attacks typically rely on scalar end-to-end outcomes or coarse holistic feedback, offering limited insight into why an attempt fails or how it should be improved. We introduce EPOA, an adaptive black-box framework that provides fine-grained, evidence-grounded guidance for iterative IPI optimization. At its core, the EPOA Judge decomposes observable attack progress into four ordered diagnostic blocks: Exposure, Provenance Promotion, Objective Adoption, and Action Binding. For each evaluated payload, it determines which blocks are supported by observable execution evidence; an optimizer then uses this structured diagnosis, together with the accumulated trajectory history, to generate the next candidate. This diagnose-and-refine process explores multiple carrier trajectories within a fixed query budget.
We evaluate EPOA on AgentDojo across four victim models and three defense settings. EPOA achieves competitive utility-preserving attack performance across all 12 model-defense combinations, obtaining an average utility-preserving attack success rate of 33.5%, compared with 31.6% for IterInject and 28.9% for PAIR. It also achieves a 55.1% attack success rate and 74.3% task utility. These results support the effectiveness of fine-grained, evidence-grounded diagnosis for adaptive IPI optimization across the evaluated models and defenses.

### 27. Optimizing Denoising Trajectories in dLLMs: A Lightweight Evolutionary Heuristic Approach

- 决定：保留：不受本次范围影响
- 具体依据：该工作以CMA-ES优化dLLM推理时去噪调度器的393个参数，是非智能体模型组件参数优化。
- 更新对象：上下文均值场神经调度器的393个参数。
- 方法/训练算法：CMA-ES进化优化。
- 反向传播：摘要称CMA-ES优化，未报告反向传播。
- 待核实：参数是否随模型检查点持久保存待原文核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=kny8uL2w7v)
- 官方摘要证据：Diffusion Large Language Models (dLLMs) have recently emerged as a promising alternative to conventional Auto-Regressive (AR) Large Language Models (LLMs). By leveraging bidirectional attention and parallel decoding, dLLMs enable more efficient generation. However, they require a carefully designed denoising scheduler at inference time (absent during training) whose choice significantly impacts generation quality. While confidence-based heuristic schedulers have shown strong empirical performance, they suffer from two critical failure modes: EOS Overflow and Proximal Bias. Through in-depth analysis of the Transformer's attention patterns, we reveal that these failures stem from certain positions assigning disproportionately high attention weights to invalid tokens (e.g., [MASK] and [EOS]), which produce misleading confidence signals. Building on this insight, empirical evidence shows that valid attention scores can provide complementary guidance to conventional confidence-based heuristics, yet no single metric consistently excels across all scenarios, implying that the optimal denoising trajectory is highly context-dependent. To address this problem, we propose a lightweight evolutionary heuristic scheduler optimized using the Covariance Matrix Adaptation Evolution Strategy (CMA-ES). Our scheduler dynamically integrates multiple heuristic features with a contextual mean-field embedding, while requiring only 393 trainable parameters. Evaluated on LLaDA and Dream across four reasoning and planning benchmarks, our method consistently outperforms strong baselines, including conventional heuristics, block auto-regressive methods, and recent State-Of-The-Art (SOTA) approaches. To the best of our knowledge, it represents the most parameter-efficient neural scheduler to date. Our code is available at anonymous repository https://anonymous.4open.science/r/Evo-Denoiser-CE0D .

### 28. Lost in Adaptation: Layer-Selective Recovery of Temporal Reasoning in Video-Language Models

- 决定：保留：不受本次范围影响
- 具体依据：MERIT用CMA-ES搜索VLM/LLM检查点层级插值配方，属于非智能体的模型合并修复，不是提示词。
- 更新对象：语言骨干各自注意力层的检查点插值选择。
- 方法/训练算法：感知约束CMA-ES配方搜索。
- 反向传播：摘要明确不学习新参数；未报告反向传播。
- 待核实：输出是插值模型配方而非新训练参数。
- 原始来源：[OpenReview](https://openreview.net/forum?id=xjhDSxr3GE)
- 官方摘要证据：Multimodal adaptation can weaken temporal reasoning (TR) in video-language models (VLMs) even when the visual evidence needed for an answer is correctly perceived. This weakened competence, however, remains partly recoverable from the model's paired pre-adaptation language checkpoint. We introduce MERIT, a gradient-free framework that selectively restores this competence across the language backbone while protecting temporal perception (TP). It assigns each self-attention layer a VLM-dominant or LLM-dominant interpolation and uses the Covariance Matrix Adaptation Evolution Strategy (CMA-ES) to search the recipe space under a perception-constrained objective. Across three VLM families and five video benchmarks, MERIT improves reasoning-aligned performance in all 15 model--benchmark evaluations while preserving TP across all three Video-MME settings. Recipes selected using 232 diagnostic examples transfer to four unseen benchmarks, with relative gains up to 27.8%, and outperform full-backbone, uniform-attention, and alpha-tuned random-layer merging. Interventional masking shows that MERIT-selected layers are disproportionately important for TR, while frame-level attribution reveals increased reliance on temporally distributed, causally relevant evidence. These results show that adaptation-induced reasoning degradation can be repaired post hoc through selective reuse of pre-adaptation competence, without learning new parameters or adding inference overhead.

### 29. WikiEvolve: Coupling Foundational and Experiential Knowledge in Self-Evolving Agents

- 决定：暂缓：智能体未训练模型参数
- 具体依据：WikiEvolve让固定wiki与累积经验记忆指导候选解进化，摘要没有训练智能体模型参数。
- 更新对象：候选解、固定知识库和累积经验记忆。
- 方法/训练算法：经验驱动进化搜索和记忆选择。
- 反向传播：摘要未报告模型训练或反向传播。
- 待核实：无。
- 原始来源：[OpenReview](https://openreview.net/forum?id=evK7w4wFCc)
- 官方摘要证据：Self-evolving agents can improve solutions for various tasks by iteratively proposing them based on past experience (e.g., proposed algorithms and their utilities), evaluating their utilities, and using evolutionary search to select the best solution. However, as these agents might only make minor modifications and do finite exploration, useful solutions can remain undiscovered, limiting the effectiveness of experience-based evolution. To address this limitation, we introduce WikiEvolve, a novel  framework that couples a fixed foundational wiki with an accumulating experiential memory. The foundational wiki provides established foundational knowledge from literature to enrich candidate solutions, while the experiential memory records past experience to guide future selection. Across distributed constraint optimization (DCOP) and Bayesian optimization (BO) tasks, our framework usually improves the final solution utility over experience-based evolution. Moreover, our experiments show how the amount of foundational knowledge influences the final solutions. These results demonstrate that combining a structured foundational wiki with an experiential memory enables self-evolving agents to break out of trial-and-error traps and discover solutions beyond what pure experience can reach.

### 30. Which Tasks Stay Vulnerable? Cross-Goal Persistence of Prompt-Injection Risk in LLM Agents

- 决定：暂缓：智能体未训练模型参数
- 具体依据：CASPER测量冻结任务风险排序在不同注入目标间的持续性，属于智能体安全评测，未训练智能体模型。
- 更新对象：任务脆弱性排序和防御预算分配。
- 方法/训练算法：留一恶意目标测量、相关分析和置换检验。
- 反向传播：摘要明确冻结排序；未报告模型参数训练。
- 待核实：无。
- 原始来源：[OpenReview](https://openreview.net/forum?id=MZodbg4BOZ)
- 官方摘要证据：Indirect prompt injection in LLM agents is usually summarized by aggregate attack success rate, but this hides whether the same benign user tasks remain vulnerable when the attacker changes objectives. We ask whether task susceptibility is persistent: can risk estimated from previously observed malicious goals predict failures under a held-out goal? We introduce CASPER, a leave-one-malicious-goal-out measurement protocol that estimates a task-level susceptibility profile from observed goals and evaluates the frozen ranking on an unseen attacker objective. Across AgentDojo and InjecAgent, spanning GPT, Llama, and Qwen models, we observe consistent cross-goal persistence. In four primary settings, median Spearman correlations range from 0.602 to 0.682, all 74 evaluable held-out goals have positive association, and task-identity permutation tests reach the resolution floor of 10,000 permutations. This structure is not determined by aggregate attack success rate. Qwen3.6-27B retains a predictive task ranking at only 9.4\% ASR, while a MiniMax-M3 condition with 53.1\% ASR and substantial outcome variation shows little cross-goal alignment. Near floor and ceiling conditions can instead make the ranking statistically unidentifiable. Finally, historical task risk improves held-out failure coverage over random allocation under limited defense budgets. These results show that prompt-injection vulnerability can contain a persistent task-specific component across attacker objectives, and that measuring this structure provides information that aggregate ASR alone does not capture.

### 31. Where Autonomy Belongs: A Separation of Powers for Agentic Program Evolution

- 决定：暂缓：智能体未训练模型参数
- 具体依据：EvoTrias重构编码智能体的治理、提议和评审权限及运行时接口，进化的是程序候选而非智能体模型参数。
- 更新对象：程序候选、治理证据、评审器和系统接口。
- 方法/训练算法：结构化治理、开放提议与受保护评审的程序进化。
- 反向传播：摘要未报告模型训练或反向传播。
- 待核实：无。
- 原始来源：[OpenReview](https://openreview.net/forum?id=7WJBskIhxM)
- 官方摘要证据：LLM-driven program evolution rests on three decisions: govern directs the search from accumulated evidence, propose constructs the next candidate, and judge settles validity and fitness. All three appear in every system, and existing work splits into two lines over who makes each. Controller-centric systems strengthen govern and neglect the autonomy of propose, which caps what evolution can reach. Agent-centric systems let a coding agent take over both govern and propose, at a cognitive and computational cost. Neither line protects the independent authority of judge, so benchmark reliability suffers. These failures share one root: autonomy is misallocated across the three decisions. We address this problem with EvoTrias, a separation-of-powers architecture in which each decision has one owner: Structured Governance for what spans evolution rounds, Open Proposal for construction inside a task, and Protected Judgment behind a private evaluator. These owners exchange typed contracts only, and runtime hooks reinforce the boundaries. This separation also lets EvoTrias run as a plugin that turns an existing coding agent into an evolution system. EvoTrias sets a new state of the art on mathematical, systems, and algorithm-design benchmarks. Three further results show what each owner buys: separating Governance from Proposal cuts token cost by 64\%, Open Proposal extends evolution to a 680K-line industrial repository, and Protected Judgment keeps benchmark scores faithful to transfer.

### 32. When Correct Memory Goes Wrong: Fuzzing Persistent Memory Use in LLM Agents

- 决定：暂缓：智能体未训练模型参数
- 具体依据：U-Fuzz从记忆检查点出发变异查询或记忆状态以发现智能体故障，不训练语言智能体参数。
- 更新对象：查询、记忆状态、测试种子和变异轨迹。
- 方法/训练算法：覆盖义务约束的迭代模糊测试。
- 反向传播：摘要未报告模型训练或反向传播。
- 待核实：无。
- 原始来源：[OpenReview](https://openreview.net/forum?id=fvUewMH9lG)
- 官方摘要证据：Persistent memory helps LLM agents carry information across long interactions, but correct memory can still be used incorrectly when queries change or memory states evolve. Existing work mainly studies memory content errors or evaluates fixed test cases, leaving memory-use failures hard to discover systematically. We formulate this issue as a fuzzing problem and categorize such failures into query-related and memory-state failures. We then develop U-Fuzz, which starts from memory checkpoints as test seeds, mutates queries or memory states under explicit mutation obligations, validates each mutant, and uses observed memory behavior to guide iterative testing while keeping failure labels outside the search. We evaluate U-Fuzz across several memory systems against diverse fuzzing
baselines, and further test an output-only setting with API-based LLMs where memory retrieval is hidden. Across these settings, U-Fuzz consistently uncovers more confirmed memory-use failures, showing that its search remains effective across different memory architectures and even when only final responses are observable.

### 33. What Should the Reflector See? An Empirical Study of Evidence in Reflective Prompt Optimization

- 决定：暂缓：提示词/提示参数为核心对象
- 具体依据：论文直接比较反思式提示优化的九种证据配置，并在搜索中修订指令。
- 更新对象：自然语言指令和反思证据配置。
- 方法/训练算法：单亲Pareto搜索与反思式提示改写。
- 反向传播：摘要未报告更新任务模型或反思器参数。
- 待核实：无。
- 原始来源：[OpenReview](https://openreview.net/forum?id=7e7pAnM0JR)
- 官方摘要证据：Reflective prompt optimization revises instructions using examples of a model’s behavior, but which evidence the reflector should receive remains unclear. We compare nine reflection strategies within a single-parent Pareto-guided search, varying evidence composition, visibility of examples, candidate selection and domain-knowledge policy. Using Qwen3.5-9B as both task model and reflector, we complete 45 optimization runs on five datasets and report test accuracy averaged over three final evaluations. No strategy dominates across tasks. Failure-only evidence produces the largest average improvement, driven by a 33.7-point gain on LiveBench-Math, whereas balanced evidence and validated blind generation share the best mean accuracy rank. Balanced evidence is not uniformly better than failure-only evidence, and explicit knowledge retention helps multi-hop question answering but hurts some other tasks in these runs. Empirical selection with natural evidence outperforms an LLM judge on average, although their computational costs differ. The results highlight task dependence and the need to distinguish calibration improvement from held-out performance, with repeated optimization runs still needed for stronger conclusions.

### 34. Vision-Language Models Can Report Which Image's Visual-Token Activations Were Perturbed

- 决定：保留：不受本次范围影响
- 具体依据：论文研究VLM内部视觉token激活扰动的可报告性和线性可解码性，是模型分析/干预，不是提示词或智能体研究。
- 更新对象：decoder侧视觉token激活和探针方向。
- 方法/训练算法：激活扰动、线性探针和steering对照。
- 反向传播：探针需要拟合；VLM检查点是否冻结未明确陈述。
- 待核实：不触发本次范围。
- 原始来源：[OpenReview](https://openreview.net/forum?id=wGTQG3yhOp)
- 官方摘要证据：Can a vision-language model (VLM) report which of two images had its internal visual-token activations perturbed while the visible inputs themselves remain unchanged? We study this question in three instruction-tuned VLM checkpoints by perturbing decoder-side activations at candidate-associated visual-token positions and asking the model which candidate was affected. Because successful localization could simply reflect damaged visual information, we separately test whether measured visual functions remain intact and use controls to probe simpler explanations. At operating points satisfying both the category criterion and a secondary counting guard, localization rises from \(0.499\) to \(0.688\) in Qwen2.5-VL and from \(0.505\) to \(0.656\) in Qwen3-VL, with both effects surviving whole-window multiplicity correction. Idefics3 shows a smaller but statistically detectable effect. Norm-restored and crossover controls show that activation-norm inflation and fixed display-side preference are not sufficient explanations, while matched-quality and visible-corruption comparisons bound stronger perturbation-specific interpretations. Finally, in Qwen3-VL, perturbation identity is near-ceiling linearly decodable at both \(p=.30\) and \(p=.60\), yet the fitted probe directions have sharply different steering efficacy: little targeted steering at \(p=.30\) but material bidirectional steering at \(p=.60\), where the counting guard no longer holds. We call this phenomenon perturbation reportability: candidate-specific internal perturbation information can become behaviorally reportable, while linear availability and steering efficacy remain distinct under the tested intervention procedure.

### 35. VAPOR: Automatic Prompt Optimization for Vision-Language Models via Visual Reflection

- 决定：暂缓：提示词/提示参数为核心对象
- 具体依据：VAPOR明确是VLM自动提示优化，构建并路由层级专家提示。
- 更新对象：视觉决策规则、负约束和专家提示系统。
- 方法/训练算法：视觉反思、行为验证、聚类和提示路由。
- 反向传播：摘要未报告更新VLM参数。
- 待核实：无。
- 原始来源：[OpenReview](https://openreview.net/forum?id=H1G5NrhRUc)
- 官方摘要证据：Automatic prompt optimization (APO) has emerged as a gradient-free alternative to fine-tuning for adapting vision-language models (VLMs). However, existing APO methods inherit a modality mismatch: they optimize visual decision-making through language-only feedback. This mismatch is especially limiting in few-shot settings with fuzzy visual boundaries, where failures often arise not from missing task instructions but from misidentified visual evidence. We propose $\textbf{VAPOR}$, an automatic prompt optimization framework that closes this feedback gap through visual reflection. VAPOR compares per-example reasoning trajectories between erroneous and corrected predictions, distills their differences into atomic visual decision rules, and records negative constraints that suppress recurring spurious rationales. We treat model-generated rationales as candidate diagnostic signals rather than faithful explanations, and admit a rule into the optimized prompt only after behavioral verification. Rather than appending all discovered rules into a monolithic prompt, VAPOR builds a hierarchical expert prompt system over dual visual-semantic clusters, routing each input to specialized guidance matched to its visual regime. On three multimodal benchmarks with ambiguous visual decision boundaries, VAPOR achieves up to 12\% absolute gains over established APO baselines. Our analysis shows that visual reflection produces more compact, stable, and interpretable prompts, reframing APO for VLMs as a problem of grounding language search in visual evidence.

### 36. Uncovering Robustness Weaknesses in LLM Agents via Persona Evolution with Task-Integrity Constraints

- 决定：暂缓：提示词/提示参数为核心对象
- 具体依据：Tiper进化的是持久用户persona和行为策略，用文本用户模拟暴露智能体弱点；未训练被测智能体模型。
- 更新对象：用户persona文本与用户行为策略。
- 方法/训练算法：反思引导行为变异和任务约束Pareto选择。
- 反向传播：摘要未报告模型参数训练。
- 待核实：persona是条件输入/模拟政策，按提示词相关对象暂缓。
- 原始来源：[OpenReview](https://openreview.net/forum?id=O4HXAtmx7v)
- 官方摘要证据：Interactive-agent evaluations commonly rely on standardized LLM-based user simulators that exhibit broadly cooperative behavior, potentially overlooking failures that arise under diverse but realistic user interactions. This can lead to overly optimistic estimates of agent robustness and provide limited failure signals for training agents that generalize across users. Existing approaches largely rely on predefined user behaviors, which may miss agent- or domain-specific weaknesses, while failure-oriented search can reduce task success by invalidating the underlying task rather than exposing genuine robustness failures. To fill this gap, we introduce Tiper, a task-integrity-preserving persona evolution method that automatically discovers agent-specific user policies exposing robustness weaknesses while keeping the underlying task valid and solvable.
Tiper evolves persistent user personas through reflection-guided behavioral mutations and task-wise Pareto selection under a task-integrity constraint. Across four interactive-agent benchmarks, Tiper yields lower held-out avg@3 scores in all 12 GPT-5.4 settings, with observed reductions of 5.8-33.7 percentage points, and in all 28 agent--domain pairs spanning seven agents, with a median observed reduction of 22.9 points. Further analysis yields a behavior-to-failure taxonomy that connects discovered user behaviors to recurring agent failure modes. Together, these results show that Tiper enables more diagnostic robustness evaluation of interactive agents and provides informative failure analysis for future agent robustness improvement.

### 37. Thermal Plume Attack: Physics-Inspired Attacks on Infrared Vision-Language Models

- 决定：保留：不受本次范围影响
- 具体依据：Thermal Plume Attack用CMA-ES优化红外物理扰动配置，是非智能体VLM黑箱攻击。
- 更新对象：热羽流温度场及形状/物理配置。
- 方法/训练算法：CMA-ES黑箱优化。
- 反向传播：未训练被攻击VLM；摘要未报告反向传播。
- 待核实：无。
- 原始来源：[OpenReview](https://openreview.net/forum?id=97XCQK26JE)
- 官方摘要证据：Infrared vision-language models (IR-VLMs) support classification, image captioning, and visual question answering in low-visibility environments, yet their robustness to non-contact thermal variations remains underexplored. We propose Thermal Plume Attack, a physics-inspired black-box framework that models a rising thermal plume and optimizes its configuration with CMA-ES. A shared temperature field couples refractive displacement with radiance variation, yielding a structured thermal perturbation. Experiments on person/vehicle crops from the FLIR and LLVIP datasets show effective top-1 flips for LanguageBind Thermal and IRGPT. Evaluations across four CLIP backbones adapted to infrared data and matched controls further reveal that this sensitivity is not confined to a single scorer or architecture. These results establish Thermal Plume Attack as a controlled testbed for studying IR-VLM behavior under structured thermal variations.

### 38. The Seven-Year Itch of Lifelong Agents: When Perfect Memory Prevents Adaptation

- 决定：暂缓：智能体未训练模型参数
- 具体依据：FAM调整长期记忆中旧经历影响当前个性化的方式，保留外部记忆并传递状态，未报告训练语言模型参数。
- 更新对象：历史episode、记忆权重/权限和handoff状态。
- 方法/训练算法：漂移用户建模与有限感知记忆控制。
- 反向传播：摘要未报告模型训练或反向传播。
- 待核实：FAM具体控制规则是否含拟合参数未说明。
- 原始来源：[OpenReview](https://openreview.net/forum?id=2e5z57jIPK)
- 官方摘要证据：Long-lived AI agents rely on memory to personalize over time, yet the user they remember may change. An assistant can accurately retain years of past preferences and still make poor decisions for the user now if obsolete evidence continues to shape current responses. We call this crossover the \emph{seven-year itch} of lifelong agents: beyond some interaction history, retaining more behaviorally active memory can reduce current-state adaptation. We characterize the effect with a drifting-user model that separates the benefit of averaging more observations from the bias created by stale evidence. This analysis motivates \FAM{} (Finitude-Aware Memory), which preserves historical episodes while adapting how strongly they influence current personalization; commitments follow a protected path, and a compact handoff state carries forward still-valid information. We evaluate the resulting design with \itch{}, a controlled benchmark spanning eight forms of user change, six LLM backbones, and repeated runs. The study reframes long-term memory as a temporal-validity problem: the challenge is not only to remember the past, but to decide how much authority the past should retain over the present.

### 39. TabEvo: LLM-Guided Evolution of Dataset-Conditional Programs for Tabular In-Context Learning

- 决定：暂缓：智能体未训练模型参数
- 具体依据：TabEvo的LLM agent循环与进化搜索编辑表格学习程序；被拟合的是程序中的GP、残差学习器等，不是语言智能体模型。
- 更新对象：meta-DAG程序及其程序内预测组件。
- 方法/训练算法：LLM代码编辑、MAP-Elites和逐表拟合。
- 反向传播：程序组件会训练；摘要未报告训练LLM agent。
- 待核实：程序内模型参数不等于语言智能体策略参数。
- 原始来源：[OpenReview](https://openreview.net/forum?id=l1YqHcNb2s)
- 官方摘要证据：A tabular in-context learner is a function $f (D, X^∗)$ from a labelled table and query rows to predictions, which tabular foundation models implement with a transformer pretrained on millions of synthetic tables. We show that the same function can be an explicit program found by large language model (LLM) guided search. TabEvo represents a learner as a meta-DAG: a directed graph whose edges carry code that fits a transformation or a predictor on the rows of the table at hand, whose nodes merge the resulting blocks, and whose head combines prediction blocks by cross-fitted non-negative stacking, so that no component reads a prediction made with its own label. An LLM agent loop grows a program one accepted edit at a time; an evolutionary search then edits it through parent-specific structured diffs,
every child fitted on 15 development tables before entering a MAP-Elites archive. The resulting program has four exact Gaussian-process views of the input space, two residual learners, repeat-detecting gates and a gradient-boosted lane. Frozen and evaluated under a pre-registered protocol on 71 tables against 45 baseline configurations, it is within one point, by our equivalence rule, of six of the nine
foundation models on 22 of the 26 fresh TabArena tables, 0.7 to 0.9 points behind TabFM and LimiX, and level with bagged CatBoost, RealMLP and a Super Learner of trained models, with no pretraining; on 24 fresh regression tables it is ahead of every trained model and of the Super Learner, about one point behind the newest foundation models. As a program it can be tested and edited: with two thousand mostly irrelevant features it keeps an R2 of 0.86 where the foundation models fall to 0.33–0.39, and an automated edit-and-test loop halved its graph and made it 6.5× faster at a 0.3-point cost in accuracy and no detected change in ROC-AUC.

### 40. TCP-MCP: Landscape-Guided Co-Evolution of Prompts and Communication Topologies for Multi-Agent Systems

- 决定：暂缓：提示词/提示参数为核心对象
- 具体依据：TCP-MCP将多智能体提示词与通信拓扑作为统一基因共同进化，提示词是核心优化对象。
- 更新对象：代理提示词和通信图。
- 方法/训练算法：结构感知进化搜索、景观探测和Pareto诊断。
- 反向传播：摘要未报告更新DeepSeek骨干参数。
- 待核实：无。
- 原始来源：[OpenReview](https://openreview.net/forum?id=llCtjFLimR)
- 官方摘要证据：Effective multi-agent systems cannot be designed by selecting prompts or communication graphs in isolation. Agent behavior depends on the information an agent receives, while the usefulness of a communication edge depends on how the receiving agent interprets and uses that information. We propose TCP-MCP (Topology-Coupled Prompting for Multi-Agent Collaborative Problem-Solving), a co-evolution framework that searches agent prompts and communication topologies as a unified genome. TCP-MCP couples this executable representation with a structure-aware evolutionary search procedure, using an initialization-time landscape probe to calibrate early search behavior and Pareto-front diagnostics to adapt exploration under three objectives: task performance, token cost, and structural complexity. Using the same DeepSeek-V3.2 backbone across all methods, TCP-MCP achieves 82.66%, 89.96%, 96.61%, and 77.31% accuracy on MMLU-Pro, MMLU, GSM8K, and WorkBench, respectively. Across the four benchmarks, it consistently outperforms automated graph-generation baselines and achieves competitive accuracy relative to debate-style systems, while using up to 5.71× fewer tokens than those systems at the reported operating points. These results show that jointly evolving prompts and communication structure provides a practical route to cost-aware and task-adaptive multi-agent system design in controlled evaluations.

### 41. Stride: Scale-Aware Multi-Agent Evolutionary Refinement for Infographic Generation

- 决定：暂缓：智能体未训练模型参数
- 具体依据：Stride明确在冻结图像生成器上通过多智能体规划、候选生成和验证器单调接受优化输出，没有训练代理模型参数。
- 更新对象：候选图像、修订计划和验证分数。
- 方法/训练算法：尺度路由、多候选生成和单调接受的演化策略。
- 反向传播：摘要明确生成器冻结；未报告训练composer/retoucher/verifier。
- 待核实：无。
- 原始来源：[OpenReview](https://openreview.net/forum?id=qT1Thc0dst)
- 官方摘要证据：Infographic generation challenges text-to-image models because a single image must satisfy numerous visual, textual, and semantic constraints. Iterative agentic refinement with a multimodal verifier is a natural remedy, but existing methods face a scale mismatch: local edits cannot correct global composition errors, while full regeneration may destroy already-correct regions. We introduce **Stride**, a constraint-grounded multi-agent framework that treats refinement over any frozen generator as a history-aware evolution strategy. Stride separates constraint evaluation—whether each requirement is satisfied—from visual grounding—where and how it is violated. It then routes global revisions to a composer subagent and local corrections to a retoucher subagent. Each subagent conducts internal planning and generates multiple candidates, while Stride accepts a candidate only when it improves the verifier score, reducing regression across iterations. Because stochastic generators and imperfect verifiers make any single step unreliable, it is this combination of scale-aware routing, per-step redundancy, and monotonic acceptance that yields stable improvement across iterations. With fully open-weight generator–verifier systems, Stride outperforms proprietary systems including Nano-Banana-2.0 and Seedream-5.0-Pro on BizGenEval, matches GPT-Image-2.0 and surpasses Seedream-5.0-Pro on IGenBench, and achieves a new state-of-the-art score on WISE, while substantially outperforming existing agentic methods across all evaluated benchmarks.

### 42. Stable Loci Addressing: A Shared-State Architecture for Referential Stability in Evolving Long-Term LLM Memory

- 决定：暂缓：智能体未训练模型参数
- 具体依据：SLA是零可训练参数的共享状态记忆寻址架构，并在冻结DeltaNet上集成。
- 更新对象：持久间接寻址、共享记忆记录和指针状态。
- 方法/训练算法：精确写入律、证书和验证解引用。
- 反向传播：摘要明确零可训练参数且DeltaNet冻结。
- 待核实：无。
- 原始来源：[OpenReview](https://openreview.net/forum?id=xqdq8GKNoE)
- 官方摘要证据：Long-term memory for large language models (LLMs) is usually treated as a retrieval problem: given a query, find the relevant stored information. But a memory that changes over time faces another problem. Once a computation refers to a record, later updates should not make that reference silently point elsewhere. We call this requirement referential stability and show that exact revisitation requires retained information about the earlier choice. We introduce Stable Loci Addressing (SLA), which unifies persistent indirection, rebinding, and structured locus operations within one shared-state memory interface without a separate per-record reverse-locator layer. Shared writes can therefore affect other references. We derive exact RLS and Delta one-write laws, an exact cumulative native-Delta law, and a necessary-and-sufficient Top-1 certificate. Experiments span semantic conflict, learned cue embeddings, long mutation sequences, LongMemEval content and structural evolution, cross-bank maintenance, and zero-trainable-parameter integration with a frozen DeltaNet. Raw semantic keys can initialize correctly yet fail after relocation. Verified dereference prevents wrong-record returns, and the certificate tracks failure. On 70 LongMemEval-S knowledge-update questions, stale predecessor evidence lowers answer accuracy by 68.6 percentage points, while SLA exactly matches updated-pointer semantics. Together, these results show static retrieval accuracy is insufficient for evolving shared memory and establish referential stability as a distinct, testable correctness criterion.

### 43. Sprune: Training-Free Credit-and-Act for Agentic Workflows

- 决定：暂缓：智能体未训练模型参数
- 具体依据：Sprune明确training-free，通过Owen value和移动平均在workflow中归档、恢复、改写组件，不训练代理模型。
- 更新对象：workflow算子、提示、边和运行分数。
- 方法/训练算法：排列采样Owen值、EMA积累与credit-and-act。
- 反向传播：摘要明确training-free。
- 待核实：包含提示改写，但核心是workflow组件信用控制，归入智能体无模型训练。
- 原始来源：[OpenReview](https://openreview.net/forum?id=5uwgUxmb6F)
- 官方摘要证据：Agentic workflows are graphs of operators, prompts, and edges that pass drafts between operators. Automated methods improve such workflows mostly by searching over candidate graphs and returning one, which leaves open how much each component contributes and discards components that later tasks may still need. A growing number of methods instead tie actions to per-component credit, but this coupling has not been named or treated as a design space of its own. We call it credit-and-act (CrAct) and describe it by three parts: a credit estimator, an accumulation rule, and an action set. We then present Sprune, a training-free CrAct method that values operators, prompts, and edges jointly with Owen values over three a priori unions, estimated by permutation sampling and smoothed into running scores by an exponential moving average. The running score archives weak components without deleting them, restores them when their score recovers, and, in a second variant, selects prompts to rewrite and decides whether operators proposed by a language model stay. Because every action reads this score, the attribution that Sprune reports is the signal behind its decisions. Across six benchmarks in code generation, mathematical reasoning, and question answering and three open-weight backbones, Sprune is competitive with seven workflow-search methods that share its backbone. An analysis of the credit recorded in nearly a thousand runs, most of them from the hyperparameter search, shows that operators carry most of the credit, that credit rankings are stable across seeds on five of the six benchmarks, and that most operators ending with the highest credit had been archived and restored along the way. Code is available at https://anonymous.4open.science/r/sprune-iclr.

### 44. Solve, Recover, Reuse: LLM Reasoning Across Workflows with Corrupted Contexts

- 决定：保留：不受本次范围影响
- 具体依据：ETG是生成跨workflow和污染条件关联任务的评测框架，摘要虽分析training effects，但核心不是优化提示词或智能体模型。
- 更新对象：评测任务、workflow与污染上下文。
- 方法/训练算法：演化任务生成和跨条件分析。
- 反向传播：摘要提到训练结果，但未说明训练算法或参数模块。
- 待核实：若原文存在具体模型训练，仅属评测因素；本次不据此判定智能体训练。
- 原始来源：[OpenReview](https://openreview.net/forum?id=mSO30AmGJA)
- 官方摘要证据：Large language models (LLMs) increasingly operate in complex workflows and noisy contexts. It's important to have a comprehensive understanding of how model performance varies across workflow and corruption types, and whether both harmful and beneficial transitions arise under these challenges.
We introduce an \textbf{Evolutionary Task Generator (ETG)} that generates a series of linked tasks across workflows and  corruptions, providing a framework to systematically experiment and analyze: 1) model performance changes across workflows and corruptions,  2) the bidirectional transitions under corrupted contexts, and 3) training effects across workflows and corruptions. Across frontier LLMs, we find that model rankings and performance change substantially across workflows, e.g., DeepSeek-V4-Flash drops from 0.75 in direct solving to 0.20 in downstream reuse. Instance-level analysis shows that both harmful and beneficial transitions arise under corrupted contexts. Training results show that direct-solving gains may not transfer across workflows, and may even degrade model performance under complex workflows with corrupted contexts.
Our results highlight the importance of examining LLMs reasoning through the lens of complex workflows and corrupted contexts, and suggest a more constructive direction when such noise is unavoidable in practice: resist the harmful and leverage the beneficial.

### 45. Sensitivity-Guided Mixed-Precision Quantization for Large Language Models

- 决定：保留：不受本次范围影响
- 具体依据：SGMPQ按扰动探针敏感度分配LLM权重量化精度，属于模型量化，不是提示词或智能体研究。
- 更新对象：各层权重量化位宽。
- 方法/训练算法：扰动探针排序与混合精度分配。
- 反向传播：PTQ不训练语言智能体；摘要未报告反向传播。
- 待核实：无。
- 原始来源：[OpenReview](https://openreview.net/forum?id=UubS9jd0J4)
- 官方摘要证据：Post-training quantization (PTQ) is essential for deploying large language models (LLMs) on resource-constrained hardware, but its impact on specific capabilities is poorly characterized. We present a capacity-controlled study of how weight-only quantization affects multi-step reasoning versus factual recall and commonsense inference, across six models (0.5B–8B; Qwen2.5, Qwen3, and Phi-3.5 families). We introduce the Reasoning Fragility Ratio (RFR), a diagnostic metric that quantifies capability-asymmetric degradation, and SGMPQ, a mixed-precision scheme that assigns 8-bit precision to the layers ranked most quantization-sensitive by a perturbation probe, with a capability-conditioned ratio as the ranking signal. Our evaluation uses real benchmarks (GSM8K, ARC-Challenge, HellaSwag, held-out perplexity) with Wilson confidence intervals and exact McNemar tests, and compares SGMPQ 8/4 (≈5.2 average bits) against capacity-matched controls: uniform W5/W6, a random mixed-precision control at the identical budget (replicated over five allocation seeds), and—decisively—two capability-agnostic sensitivity rankings at the same budget, plus GPTQ and AWQ at matched budgets. Three findings emerge. First, the quantizer dominates where it matters: GPTQ beats RTN by up to 63 accuracy points exactly where RTN breaks (W4 on the 3B base and Coder-3B models), rescuing Qwen2.5-Coder-3B, which RTN destroys outright, while the two quantizers converge on robust models at W5. Second, on robust models the bit budget masks placement: at equal ≈5.2 bits, sensitivity-guided placement is statistically indistinguishable from random placement on the two small instruct models, worse on the 3B base model, and better on the two largest models—though with five allocation seeds the permutation design (sign-flip floor p=0.0625) cannot reach conventional significance even if the advantage is real on every seed. Third, placement matters exactly where uniform quantization fails: on Coder-3B, both perturbation-probe-guided allocations tested preserve the model (59.4–64.2% GSM8K) where all five independently drawn random allocations collapse (0.4–2.4%; uniform W5 also rescues it), and the capability ratio itself is beneficial on one model (8B: +6.0 pp) but actively harmful on another (3B: -33.4 pp vs. the agnostic ranking). We release per-item results, sensitivity maps, and the full evaluation stack, and conclude that sensitivity-guided mixed precision is a targeted repair tool for quantization-brittle models—but no ranking signal we tested (capability ratio or agnostic) transfers safely across models, so any allocation must be validated against random-placement controls on the target model.

### 46. SemanticBBOBench: A Benchmark for Semantic Black-Box Optimization with Large Language Models

- 决定：保留：不受本次范围影响
- 具体依据：SemanticBBOBench是带语义上下文的LLM黑箱优化基准，不以提示词优化或智能体系统为核心。
- 更新对象：外部科学工程黑箱问题及语义上下文。
- 方法/训练算法：基准构建和上下文水平控制实验。
- 反向传播：摘要未报告模型训练。
- 待核实：不触发本次范围。
- 原始来源：[OpenReview](https://openreview.net/forum?id=BfRhheMOI7)
- 官方摘要证据：Black-box optimization is central to many scientific and engineering disciplines. While numerical methods such as Bayesian optimization (BO) can successfully optimize black-box problems, these methods struggle to incorporate the semantic context that often accompanies real-world experimental problems, including domain knowledge, prior experiments, and expert intuition. Using this information could substantially reduce experimental costs and improve outcomes. Large language models (LLMs) can reason over both semantic and numerical data, offering a pathway for bringing this context into the optimization loop. We present SemanticBBOBench, a black-box optimization benchmark designed for testing LLM-based methods with semantic context. It provides a uniform framework containing 42 optimization problems spanning diverse scientific and engineering domains, each paired with a curated context at multiple controlled levels of detail and types of information. Our experiments show that semantic context provides its greatest benefit early in the optimization process, enabling substantially stronger initial configurations when few numerical observations are available. We also show that misleading semantic information can persistently bias LLM-based search. These results highlight both the potential and limitations of LLM-based black-box optimization and establish SemanticBBOBench as a framework for developing methods that use such information effectively.

### 47. Semantic Behavioral Watermarking: Paraphrase-Robust and Forgery-Resistant Provenance for LLM Agents

- 决定：暂缓：智能体未训练模型参数
- 具体依据：SBW在agent高层动作选择上施加语义簇水印与密钥分桶，改变解码选择但未训练agent模型参数。
- 更新对象：动作语义簇、密钥分桶和水印选择。
- 方法/训练算法：历史条件化语义分桶与logit/选择控制。
- 反向传播：摘要未报告模型训练或反向传播。
- 待核实：编码器是否微调未说明；不构成agent政策模型训练证据。
- 原始来源：[OpenReview](https://openreview.net/forum?id=z3M8weP6Mn)
- 官方摘要证据：Behavioral watermarking embeds an owner identifier in an LLM agent's high-level action choices, giving provenance without touching output tokens. Prior agent watermarks bind the signal to raw strings and break in two ways. AgentMark's own robustness test paraphrases the observation alone and bit-recovery falls to 16.8%; its released script holds the per-step key fixed, so that experiment measures distribution drift, not the key desynchronization its context-hash design separately admits. All three prior schemes also bind the watermark to the exact action symbol, so renaming a tool desynchronizes decoding even when the observation is untouched — the axis we measure and close. And every prior agent watermark studies only removal: none asks whether an adversary can forge a trajectory that verifies as someone else's, a question answered affirmatively for text watermarks (Jovanović et al., 2024). We present Semantic Behavioral Watermarking (SBW): watermarking over semantic action clusters under history conditioning, with the public-cluster bin replaced by keyed collision-resistant binning whose fresh-bucket assignment is provably unpredictable in the random-oracle model. Across five agent models (3B–14B, four vendors) and three encoders the ordering holds on both benchmarks: on ToolBench (600 trajectories per model) detection under rewriting is 0.49–0.66 for cluster-level versus 0.05–0.17 for exact-symbol at a permutation-calibrated 1% FPR, at 72–83% choice agreement against 22–27% for logit biasing; on ALFWorld (100 episodes per model) it is 0.92–0.97 versus 0.00–0.01. Keyed binning takes adaptive forgery from 100% to the false-positive floor at the primary operating point (bge, r=64). We also mark the boundary that guarantee does not cover: when the adversary copies the victim's own steps, shuffled splicing is neutralized (0.000 on Qwen2.5-3B) but chained replay remains at 0.76–0.98 across the five models, reported as open. Paraphrase robustness costs about half of the per-step watermark capacity. Code is available at https://anonymous.4open.science/r/SBW-Agent-Watermark.

### 48. SemAdapt: Adaptive Semantic Watermarking with Paraphrase Robustness for Large Language Models

- 决定：保留：不受本次范围影响
- 具体依据：SemAdapt是一般LLM输出水印方法，用BO离线选控制器参数；非智能体且非提示优化。
- 更新对象：语义词汇桶、水印强度和控制器超参数。
- 方法/训练算法：多目标贝叶斯优化和语义水印注入。
- 反向传播：摘要未报告更新基础LLM权重。
- 待核实：控制器参数的拟合方式待原文确认。
- 原始来源：[OpenReview](https://openreview.net/forum?id=9fBck6CClD)
- 官方摘要证据：Watermarking large language model (LLM) outputs is a promising approach for establishing content provenance and mitigating misuse. However, LLM-generated text can be easily paraphrased by users or automated tools, disrupting token-level watermark statistics and reducing detection reliability. Although existing methods attempt to improve robustness against such paraphrases, they often do so without adequately considering text quality, limiting their practical applicability.
We propose SemAdapt, an adaptive semantic watermarking method for robust LLM watermarking under paraphrasing. SemAdapt injects watermark signals at the level of semantic vocabulary buckets rather than individual tokens, and refines the vocabulary partition using lexical substitutions observed under paraphrasing. To balance detectability, paraphrase robustness, and text quality, SemAdapt further adapts watermark strength according to uncertainty over the same semantic bucket space, with controller parameters selected offline using multi-objective Bayesian optimization under noisy paraphrase evaluations.
Extensive experiments demonstrate that SemAdapt achieves consistently stronger robustness against diverse paraphrase attacks than existing baselines, while maintaining comparable text quality and detectability.

### 49. Self-Structuring Latent Action Spaces for Black-Box Instruction Optimization

- 决定：暂缓：提示词/提示参数为核心对象
- 具体依据：SLAE把instruction编码成离散基因型并用差分进化搜索，核心仍是黑箱指令优化。
- 更新对象：指令文本的脚手架和槽位语义动作。
- 方法/训练算法：整数编码差分进化、结构扩展和动作空间细化。
- 反向传播：摘要未报告更新基础模型参数。
- 待核实：无。
- 原始来源：[OpenReview](https://openreview.net/forum?id=nwDOqi2Qri)
- 官方摘要证据：Instruction optimization for large language models (LLMs) is a high-dimensional discrete black-box optimization problem in which reliable feedback comes only from costly model evaluations. Existing methods search directly in raw text or use LLMs as high-frequency mutation operators, which makes the search hard to analyze and ties generation-side cost to population size and optimization depth. We propose Self-Structuring Latent Action-Space Evolution (SLAE), which represents each instruction as an integer-coded genotype that selects a syntactic scaffold and slot-wise semantic actions and is mapped deterministically to text. Routine search runs in this categorical genotype space without LLM calls, while the space itself evolves: Dynamic Structural Evolution (DSE) adds newly discovered scaffolds, and Adaptive Action-Space Refinement ($\mathrm{A^2R}$) adds slot-level actions when search stagnates. Because genotype coordinates are nominal categories, we show that differential-evolution arithmetic on them depends on how categories are indexed and give a label-equivariant variation rule. Under matched evaluation budgets, SLAE with integer-coded differential evolution achieves the best results on all nine language understanding and generation benchmarks we evaluate. In controlled studies under the main experimental protocol, disabling the expansion mechanisms costs 8.7 accuracy points on AG News and 5.3 on a held-out task with a different model family, while on AG News these mechanisms account for about 0.1\% of the measured token budget.

### 50. Self-Improving Language Models with Bidirectional Evolutionary Search

- 决定：暂缓：智能体参数训练证据待核实
- 具体依据：BES在推理和post-training sample generation中重组候选轨迹，但摘要未明确是否用生成样本训练并持久更新语言模型参数。
- 更新对象：部分轨迹、候选解、子目标和验证反馈；是否更新模型权重不明。
- 方法/训练算法：双向进化搜索、轨迹重组和目标分解。
- 反向传播：摘要未给出模型训练/反向传播证据。
- 待核实：需原文核实所谓post-training实验是否实际训练模型参数，还是仅在post-training任务上搜索。
- 原始来源：[OpenReview](https://openreview.net/forum?id=DcvklOsaEP)
- 官方摘要证据：Search has been proposed as an effective method for self-improving language models and agentic systems, both for post-training sample generation and for inference. However, widely used methods such as best-of-N sampling and tree search face two fundamental limitations: they are guided by sparse verification signals, and they construct candidates primarily through autoregressive expansion, restricting exploration to regions with substantial model probability mass. To address these, we propose Bidirectional Evolutionary Search (BES), a search framework that couples forward candidate evolution with backward goal decomposition. In the forward search, BES augments standard expansion with evolution operators that recombine partial trajectories to generate candidates that are difficult to obtain from a single model rollout. In the backward search, BES recursively decomposes the original task into checkable sub-goals, producing dense intermediate feedback that guides forward search. We provide motivation illustrating that candidates generated by expansion-only search may be confined to a narrow entropy shell, while evolution operators may escape it.
  Experiments show that on challenging post-training tasks where mainstream post-training algorithms fail to improve, BES enables consistent gains. At inference time, BES outperforms existing open-source frameworks on three open problem solving benchmarks in both average and best-case performance, and outperforms majority voting and Monte Carlo Tree Search on mathematical reasoning and competitive programming benchmarks.

### 51. SageLLM-BO: High-Dimensional Bayesian Optimization via Large Language Model-Guided Search Geometry

- 决定：保留：不受本次范围影响
- 具体依据：SageLLM-BO让LLM选择外部高维BO搜索几何，核心是通用黑箱优化而非提示词或智能体系统训练。
- 更新对象：外部黑箱域的子空间/信赖域搜索几何。
- 方法/训练算法：LLM辅助几何选择与贝叶斯优化。
- 反向传播：摘要未报告训练LLM参数。
- 待核实：不触发本次范围。
- 原始来源：[OpenReview](https://openreview.net/forum?id=REys9S1BcO)
- 官方摘要证据：Bayesian Optimization (BO) is a powerful framework for optimizing expensive black-box functions, yet its performance deteriorates in high-dimensional settings. Instead of operating over the full domain, prior works aim to define a suitable search geometry, a structured region within which BO can operate more efficiently, typically in the form of a low-dimensional subspace and/or a local trust region. However, these methods often rely on problem-specific heuristics and predefined adaptation rules, limiting their robustness. Recent BO methods have shown that Large Language Models (LLMs) can assist the BO process, but they do not explicitly address high-dimensional search and can incur substantial inference costs in such settings. In this work, we propose SageLLM-BO, a novel high-dimensional BO algorithm that leverages the reasoning capabilities of LLMs in a cost-efficient manner to guide the search geometry selection, replacing fixed adaptation rules with adaptive LLM decisions informed by optimization indicators. We further introduce a methodology for constructing a set of example search geometries with their associated quality estimates, and various optimization indicators to guide the LLMs in selecting an effective search geometry. Extensive experiments on synthetic and real-world benchmarks demonstrate that SageLLM-BO consistently matches or outperforms state-of-the-art non-LLM and LLM-based high-dimensional BO methods while substantially reducing LLM cost.

### 52. STRATA: Spatiotemporal Alignment of Agentic Memory for Long-Horizon Preference Tracking

- 决定：暂缓：智能体未训练模型参数
- 具体依据：STRATA构建三层记忆图，并由LLM agent在推理时调用工具遍历；没有模型参数训练。
- 更新对象：偏好演化链、记忆图和推理时检索路径。
- 方法/训练算法：时空记忆表示与工具调用遍历。
- 反向传播：摘要明确操作发生在inference time；未报告模型训练。
- 待核实：无。
- 原始来源：[OpenReview](https://openreview.net/forum?id=pE9wfA0TJa)
- 官方摘要证据：Large language model assistants increasingly maintain relationships with users across months or years, yet most memory systems still treat personalization as a retrieval problem. This framing fails when a user's preferences change over time, and the turns most semantically similar to a query are no longer the correct value. We argue long-term memory should instead be framed as a state inference problem by computing the value of an attribute at a given time from its past states. We present STRATA, a memory architecture organized into three complementary layers (Spatial, Temporal, and Spatiotemporal) that create a single traversable graph via casual and relational edges. Preferences are stored as evolutionary chains, mapping the trajectory of its value over time. At inference time, an LLM agent traverses the memory graph with tool calls both within and across layers to intelligently retrieve relevant context. On PersonaMem, STRATA attains a new SOTA of 61.6% accuracy compared to six baselines, and a second-best on LongMemEval of 86.4% overall, driven by a 6.8-point margin on multi-session recall questions. Tool call analysis reflects the agent exhibiting emergent routing based on dataset and question type. Controlled ablations show the memory representation is crucial for preference tracking questions, and that agentic, query-conditioned traversal at inference time - a property unique to STRATA - drives meaningful gains.

### 53. SM2-AHD: Search Experience Memory and Meta-Cognitive Reflection for LLM-Based Automatic Heuristic Design

- 决定：暂缓：智能体未训练模型参数
- 具体依据：SM2-AHD共同进化代码种群和外层启发式设计框架，记忆注入mutation prompt；未训练LLM代码生成器参数。
- 更新对象：启发式代码、搜索经验记忆、探索强度和算子权重。
- 方法/训练算法：代码进化、经验检索和元反思在线调节。
- 反向传播：摘要未报告模型训练或反向传播。
- 待核实：无。
- 原始来源：[OpenReview](https://openreview.net/forum?id=MBCkxr1718)
- 官方摘要证据：Automatic Heuristic Design (AHD) aims to construct high-quality heuristics with as little human intervention as possible; LLM-based AHD, which uses LLMs as code generators, has already produced heuristics that surpass hand-crafted ones through iterative search. Existing evolutionary methods, however, rely on a relatively fixed evolutionary framework and remain sensitive to the initial population and to the hyperparameters. We therefore propose SM2-AHD, a meta-level AHD framework in which the code population and the outer framework co-evolve throughout the search with two independent components. At the code level, Search Experience Memory (SEM) encodes each trajectory into a memory unit that carries its code lineage and failure attribution, and injects retrieved historical cases into the mutation prompt. At the level of the outer framework, Meta-Reflection periodically diagnoses verifiable search statistics and, under safety constraints, adjusts the exploration strength and the operator weights online. Experiments show that SM2-AHD outperforms several existing state-of-the-art methods across a range of heuristic design problems.

### 54. SGA: Stamp Guided Black-box Adversarial Attack against Vision-Language Models

- 决定：保留：不受本次范围影响
- 具体依据：SGA用混合整数CMA-ES优化视觉印章参数，是非智能体VLM黑箱攻击；固定文本后缀不是被优化的提示。
- 更新对象：印章形状、尺寸、位置、颜色和透明度。
- 方法/训练算法：混合整数CMA-ES查询优化。
- 反向传播：未训练受害VLM；摘要未报告反向传播。
- 待核实：固定scenario-agnostic后缀不是核心搜索对象。
- 原始来源：[OpenReview](https://openreview.net/forum?id=KUuqUEtSMZ)
- 官方摘要证据：Vision-language models (VLMs) have demonstrated remarkable multimodal capabilities, yet remain vulnerable to jailbreak attacks that circumvent safety alignment and elicit harmful answers. Existing visual attacks typically either optimize pixel-level adversarial perturbations with limited explicit semantics and white-box model access, or construct semantically meaningful multimodal inputs through specific content transformation and external model assistance. In this work, we investigate whether a simple visual cue with widely recognized semantics can itself serve as an effective attack medium. To this end, we propose \textbf{Stamp Guided Attack (SGA)}, a straightforward black-box adversarial attack framework that overlays an authorization-themed visual stamp onto the original image and augments the textual query with a fixed, scenario-agnostic priming suffix to induce a harmful response. SGA introduces the reusable checkmark as an explicit semantic hint and represents it with a compact, interpretable parameterization over its shape, size, position, color, and opacity. This formulation reduces attack generation to a low-dimensional black-box optimization problem, which is efficiently solved using a mixed-integer Covariance Matrix Adaptation Evolution Strategy (CMA-ES) through only input-output queries to the victim model. Extensive experiments on seven representative VLMs demonstrate the effectiveness and generalizability of SGA, achieving average Attack Success Rates (ASRs) of 78.78\% across five open-source models and 54.25\% across two closed-source models. The results reveal that VLMs are susceptible to high-level visual semantics introduced beyond the original image content, highlighting the importance of accounting for such cues in multimodal safety evaluation and alignment. Code is available at {\url{https://anonymous.4open.science/r/Stamp_Guided_Attack-7EFA/}}.

### 55. SEARCH WHAT YOU MUST, SOLVE WHAT YOU CAN: FEDERATED CONTINUOUS PROMPT ADAPTATION FOR BLACK-BOX VLMS

- 决定：暂缓：提示词/提示参数为核心对象
- 具体依据：FedMUSE核心之一是连续多模态提示搜索，使用分块ZO估计优化文本和视觉prompt参数，属于软提示适配。
- 更新对象：连续文本/视觉prompt潜在核及后续score-space残差。
- 方法/训练算法：分块零阶估计和闭式全局残差细化。
- 反向传播：冻结VLM且无内部梯度访问；提示参数通过ZO更新。
- 待核实：残差模块是否视为模型参数不改变其提示核心属性。
- 原始来源：[OpenReview](https://openreview.net/forum?id=wBmaKUqoBB)
- 官方摘要证据：Federated adaptation of pretrained vision–language models (VLMs) commonly relies on lightweight prompts, yet existing approaches typically require gradient or feature access to the frozen backbone. Such white-box access may be unavailable when VLMs are exposed through restricted inference interfaces or opaque runtimes, while distributed users still need to adapt them to private local data. We therefore study federated adaptation of black-box VLMs, where clients can interact with the model through continuous multimodal prompts and class-score feedback but cannot access model internals. Rather than treating black-box adaptation as a single optimization problem, we ask a simpler question: what must be searched, and what can be solved? We propose FedMUSE, which decomposes federated black-box VLM adaptation into two complementary components: multimodal prompt search for what must be optimized through queries, and global decision refinement for what can be solved explicitly from the returned score space. FedMUSE first introduces mean–contrast prompt search, which parameterizes textual and visual prompts through common and differential latent kernels and performs block-wise zeroth-order estimation to reduce cross-block interference. It then freezes the selected prompt predictor and performs global residual refinement in the resulting shared score space. Clients communicate additive sufficient statistics rather than locally fitted heads, allowing the server to recover the pooled residual solution exactly without collecting individual scores or labels. Across 13 classification benchmarks, FedMUSE achieves 70.15% mean accuracy, improving its prompt-only predictor by 5.16 percentage points while adding less than 0.34% training queries, with compact communication and single-call VLM inference. Code is available at https://anonymous.4open.science/r/FedMUSE-04C1.

### 56. ReHarness: Learning Reusable Harness Evolution Across Tasks

- 决定：暂缓：智能体参数训练证据待核实
- 具体依据：ReHarness称“学习可迁移进化策略”并将其用于worker harness适配，但摘要未说明该策略是否为可训练模型、其参数类型或训练算法。
- 更新对象：可迁移进化策略与任务特定programmable harness；模型参数状态不明。
- 方法/训练算法：离线多任务学习与少样本harness evolution，算法细节摘要未给出。
- 反向传播：是否有反向传播或模型参数训练未说明。
- 待核实：需原文核实 transferable evolution strategy 是文本/程序规则、统计策略还是训练出的神经模型。
- 原始来源：[OpenReview](https://openreview.net/forum?id=Gzda5HNz7Y)
- 官方摘要证据：Large Language Model (LLM) agents increasingly rely on programmable harnesses to coordinate reasoning, tool use, and execution. Existing harness evolution methods typically optimize a task-specific harness from scratch for each new task, requiring substantial task-specific data and evolution steps. In this work, we identify that harness evolution exhibits reusable structure across heterogeneous tasks: independently evolved harnesses repeatedly discover similar improvement strategies, although the resulting harnesses remain task-specific. Building on this insight, we propose ReHarness, a reusable harness evolution framework that learns how to evolve across tasks. ReHarness learns a transferable evolution strategy from multiple offline-given tasks and applies it to rapidly adapt task-specific worker harnesses to new tasks using only a few examples. Experiments across four LLMs and six benchmarks demonstrate that ReHarness consistently improves agent performance on four new tasks not used during the offline phase, while outperforming the task-specific evolution method Self-Harness on two tasks from the offline suite under the same data budget. Code and models will be made publicly available.
