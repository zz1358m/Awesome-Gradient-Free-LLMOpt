# ICLR 2027 提示词与智能体范围收紧审查：批次 2

本批次依据仓库保存的 OpenReview 官方摘要逐篇判断；未进行新检索。决定仅用于范围调整，不评价论文有效性。

## 统计

- `keep_unaffected`：15
- `keep_agent_model_training`：0
- `defer_prompt_core`：15
- `defer_agent_no_model_training`：25
- `defer_agent_training_unverified`：1

## 逐篇决定

### 1. [Ranking-Aware Prompt Optimization for Multimodal Clinical Diagnosis](https://openreview.net/forum?id=4JLvdwVQnj)

- 决定：`defer_prompt_core`
- 依据：核心对象是多模态临床诊断提示词；Ranking-PE 以成对排序反馈演化候选提示词。
- 实际更新对象：候选提示词；不更新诊断模型参数。
- 方法/训练算法：基于经验 AUROC 的 pair-level Pareto prompt evolution。
- 反向传播：摘要未说明底层 MLLM 或反思模型训练；提示词搜索本身不需要反向传播。
- 待核实：医学视觉骨干曾通过 SFT/预训练获得，但它不是本文提示词搜索中更新的对象。

### 2. [RBEPO: From Root-Cause Diagnosis to Branching Evolutionary Prompt Optimization](https://openreview.net/forum?id=XbT1YBExr4)

- 决定：`defer_prompt_core`
- 依据：RBEPO 的核心是按失败根因生成、评估、组合提示词重写分支。
- 实际更新对象：提示词及跨迭代重写经验。
- 方法/训练算法：根因聚类、分支式演化提示优化和 racing。
- 反向传播：摘要明确不更新模型参数；未说明固定调用模型自身的训练。
- 待核实：无。

### 3. [Proximity, Precendence and Position: A Minimum Linear Arrangement Account of Ordering Effects in LLM Prompts](https://openreview.net/forum?id=dp6Z7up2zP)

- 决定：`defer_prompt_core`
- 依据：核心研究对象是 in-context demonstrations 的排列顺序，即固定内容提示词的离散优化。
- 实际更新对象：提示词中 demonstrations 的顺序。
- 方法/训练算法：带 precedence 约束的 minimum linear arrangement。
- 反向传播：无模型参数训练；属于上下文排列优化。
- 待核实：无。

### 4. [Providing Context: Enriching Graph Learning Using Language Model Priors](https://openreview.net/forum?id=nGF3lnQ3Qd)

- 决定：`defer_prompt_core`
- 依据：核心机制是将 LM-embedded global graph prompts 作为图语义条件，通过 cross-attention 注入 GNN；虽非提示搜索，仍以提示表示为主要研究对象。
- 实际更新对象：外部图描述提示表示及 GINAT 图网络参数。
- 方法/训练算法：prompt-conditioned message passing 与常规图表示学习；摘要未给出优化器。
- 反向传播：图网络需要训练，但摘要未明确反向传播细节。
- 待核实：LM embedding 是否冻结未明确。

### 5. [Prompt Reinjection for Spatial Reasoning in MMDiTs: Signal Amount, Depth Allocation, and Content-Specific Repair](https://openreview.net/forum?id=fmAQLVOhLg)

- 决定：`defer_prompt_core`
- 依据：核心机制是 MMDiT 内部逐层 prompt-token reinjection，并系统选择注入位置、深度和权重；属于提示信号适配。
- 实际更新对象：推理时 prompt token 的注入位置、层分配和注入权重配置。
- 方法/训练算法：受控消融和稀疏 prompt reinjection 调度。
- 反向传播：摘要未报告模型参数训练。
- 待核实：是否存在额外校准训练未说明。

### 6. [Predicting Where Recall Fails: The Fact Matters More Than the Entity in Black-Box Language Models](https://openreview.net/forum?id=BhrfhXyPMR)

- 决定：`keep_unaffected`
- 依据：这是黑盒语言模型事实召回可靠性的测量研究；没有提示优化或智能体工件演化。
- 实际更新对象：不适用；研究预查询统计特征与错误的关系。
- 方法/训练算法：统计分析和重复采样。
- 反向传播：无所提模型训练。
- 待核实：无。

### 7. [Permutation Alignment and Depth in Weight-Tied Language Models](https://openreview.net/forum?id=hvniX9y4FG)

- 决定：`keep_unaffected`
- 依据：核心是权重绑定语言模型的置换对齐、权重平均与后续训练分析，不属于提示词或智能体范围。
- 实际更新对象：语言模型权重、对齐后的 midpoint。
- 方法/训练算法：置换对齐、权重平均、继续训练和蒸馏。
- 反向传播：继续训练和蒸馏通常依赖反向传播；摘要未详述实现。
- 待核实：具体优化器待原文核实。

### 8. [ParetoEvo: Pareto-Guided Evolutionary Tree Search for Automatic Heuristic Design with LLM Agents](https://openreview.net/forum?id=1Zv2iOm1Gb)

- 决定：`defer_agent_no_model_training`
- 依据：LLM agents 生成、评估和修改可执行启发式；搜索对象是启发式程序与树节点，不是 agent 模型参数。
- 实际更新对象：可执行启发式及搜索树。
- 方法/训练算法：PD-MCTS、Pareto 选择和反思式生成。
- 反向传播：摘要没有训练 Actor/Reflector LLM 参数的证据。
- 待核实：“update guidance”指后续生成指导，不足以证明参数更新。

### 9. [Paper Agent Network: Literature-Grounded Multi-Agent Program Discovery](https://openreview.net/forum?id=eTpwBeLmHO)

- 决定：`defer_agent_no_model_training`
- 依据：PAN 的持久 coding agents 通过工具、反馈和实现历史修订程序路线，更新的是可执行 artifact 与历史。
- 实际更新对象：程序实现、方法路线、共享报告与历史。
- 方法/训练算法：多智能体程序发现和基于评测的迭代修订。
- 反向传播：摘要没有语言/策略模型参数训练。
- 待核实：无。

### 10. [PRISM: Transparent Strategy Search for Privacy Risks in LLM Agents](https://openreview.net/forum?id=5lk0NlZc4f)

- 决定：`defer_prompt_core`
- 依据：核心搜索对象是攻击者 instruction；稀疏 tactic code 和闭式 Bayesian surrogate 用于选择待重写指令。
- 实际更新对象：攻击者指令及 tactic 表示。
- 方法/训练算法：闭式 Bayesian surrogate 加反思重写。
- 反向传播：未更新目标、重写或评判模型参数。
- 待核实：无。

### 11. [PINNForge: Execution-Grounded Evolutionary Design of Physics-Informed Neural Networks for PDE Solving via Large Language Models](https://openreview.net/forum?id=DXeChT9fBB)

- 决定：`defer_agent_no_model_training`
- 依据：LLM 驱动演化的是 PINN 配置和设计组件；PINN 会训练，但没有训练语言智能体/策略模型。
- 实际更新对象：PINN 架构、采样、约束、损失和优化配置。
- 方法/训练算法：generate-execute-evaluate-evolve。
- 反向传播：候选 PINN 训练会使用其自身优化过程；LLM 参数更新无证据。
- 待核实：PINN 的具体反向传播实现未在摘要说明。

### 12. [Ouroboros: A Self-Developing Coding Harness with Reviewed Core Evolution](https://openreview.net/forum?id=w0OSBRyfSU)

- 决定：`defer_agent_no_model_training`
- 依据：Ouroboros 演化 tools、context、prompts 和 harness core implementation；基座模型参数未被描述为训练对象。
- 实际更新对象：agent harness 代码、工具、上下文装配与提示词。
- 方法/训练算法：经审查 commit 的递归/经验驱动 core evolution。
- 反向传播：摘要没有语言模型参数训练。
- 待核实：系统可选择新 model API，但这不是训练模型参数。

### 13. [OrderCover: Structure-Aware Budgeted Search over Prompt-Component Orders](https://openreview.net/forum?id=hciep78aST)

- 决定：`defer_prompt_core`
- 依据：核心是固定文本 prompt components 的排列搜索。
- 实际更新对象：提示词组件顺序。
- 方法/训练算法：结构覆盖与 Kendall-distance 分离的预算搜索。
- 反向传播：摘要明确不用 logits、gradients 或模型分数。
- 待核实：无。

### 14. [Online Automated Algorithm Design with Large Language models](https://openreview.net/forum?id=mm4pTeeEST)

- 决定：`defer_agent_no_model_training`
- 依据：多智能体按优化状态合成并执行算法；更新的是可执行算法与对运行证据的解释，不是模型参数。
- 实际更新对象：优化算法代码/决策规则。
- 方法/训练算法：在线多智能体 automated algorithm design。
- 反向传播：摘要没有 LLM/agent policy 参数训练。
- 待核实：无。

### 15. [NextEval: An Agent-Based Solver and Benchmark for Derivative-Free Optimization](https://openreview.net/forum?id=MsqBCJeXIT)

- 决定：`defer_agent_no_model_training`
- 依据：NextEval 的 LLM agent 选择工具、参数和预算，数值环境维护历史；未训练智能体模型。
- 实际更新对象：DFO 评估点、工具配置、预算与历史状态。
- 方法/训练算法：LLM agent 调度数值 DFO 方法。
- 反向传播：摘要没有模型参数更新。
- 待核实：无。

### 16. [Mirrorrefine: Mirror Reflection Generation via Multi-agent Refinement with Spatial Priors](https://openreview.net/forum?id=CygM5LTLej)

- 决定：`defer_agent_no_model_training`
- 依据：多智能体迭代更新 synthesis conditions 并选择图像操作；摘要明确迭代期间全部组件参数固定。
- 实际更新对象：合成条件、操作选择与生成图像。
- 方法/训练算法：多动作 evolutionary refinement。
- 反向传播：迭代时全部组件参数固定；RSG 是离线训练的辅助几何模块。
- 待核实：RSG 的离线训练不等于语言智能体模型训练。

### 17. [Meta-Delta: Evolving Knowledge through Global Review for LLM-Driven Optimization](https://openreview.net/forum?id=982s77OSTT)

- 决定：`keep_unaffected`
- 依据：Meta-Delta 是通用 LLM 驱动优化，联合演化候选解与 Delta Bank 知识；摘要未将其定义为语言智能体系统，也非提示词优化。
- 实际更新对象：任务候选解与结构化 Delta Cards。
- 方法/训练算法：局部更新与 Global Review。
- 反向传播：摘要未报告 LLM 参数训练。
- 待核实：具体任务候选可能是程序/科学定律，非 agent 模型。

### 18. [Measured Behavior, Recorded Zero: Measurement Failures in Self-Improving Coding Agents](https://openreview.net/forum?id=9UsBcc69Ua)

- 决定：`defer_agent_no_model_training`
- 依据：研究明确描述 frozen language model 周围的 scaffold evolution；更新的是 scaffold，且论文主要诊断测量失败。
- 实际更新对象：agent scaffold 代码与测量层。
- 方法/训练算法：进化式 scaffold 提案与评测。
- 反向传播：语言模型明确冻结。
- 待核实：无。

### 19. [Mask-On: Compact Activation-Calibrated Merging for Autoregressive and Diffusion Language Models](https://openreview.net/forum?id=db6NrHuZbK)

- 决定：`keep_unaffected`
- 依据：Mask-On 是语言模型权重更新的无梯度压缩/合并方法，不属于提示词或智能体范围。
- 实际更新对象：AR-to-diffusion 紧凑权重更新、ternary masks 与 scales。
- 方法/训练算法：闭式 scale fitting 和单 pruning parameter 搜索。
- 反向传播：摘要明确不使用 gradient-based optimization。
- 待核实：无。

### 20. [MODEPrompt: Taxonomy-Guided Pareto Evolution for Prompt Optimization](https://openreview.net/forum?id=CkuA2Se9vX)

- 决定：`defer_prompt_core`
- 依据：MODEPrompt 核心是按推理子群 Pareto 目标演化提示词。
- 实际更新对象：候选提示词、语义 patches 和 meta-rules。
- 方法/训练算法：多目标 evolutionary prompt optimization。
- 反向传播：摘要未给出语言模型参数更新。
- 待核实：无。

### 21. [MILO: Automated Harness Discovery via Orchestrated Multi-Agent Evolution](https://openreview.net/forum?id=AUiAVv2xU2)

- 决定：`defer_agent_no_model_training`
- 依据：MILO 共同演化完整 harness 与搜索策略；对象是 harness、lineage memory、mutators 和 curriculum，并无模型参数训练证据。
- 实际更新对象：agent harness 与外部搜索状态。
- 方法/训练算法：岛模型 meta-evolution。
- 反向传播：摘要没有 LLM 参数训练。
- 待核实：mutator/orchestrator agent 的“adapt”是搜索行为，不证明参数学习。

### 22. [MAPF-Evo: LLM-Driven Evolution of Heuristics for Conflict Elimination in Multi-Agent Path Finding](https://openreview.net/forum?id=jtF7cAh4OE)

- 决定：`defer_agent_no_model_training`
- 依据：LLM 驱动演化 MAPF-LNS 的 destroy heuristics；没有训练语言智能体模型。
- 实际更新对象：可解释 destroy heuristic 程序。
- 方法/训练算法：运行状态反馈驱动的启发式演化。
- 反向传播：摘要未报告 LLM 参数更新。
- 待核实：对比的 NNS 训练不属于所提 MAPF-Evo。

### 23. [Learning Compact State Abstractions for LLM Agents](https://openreview.net/forum?id=v5FgAqHn7s)

- 决定：`defer_agent_no_model_training`
- 依据：用固定 reference agent 的任务表现搜索递归状态抽象程序；更新的是程序而非 agent 参数。
- 实际更新对象：确定性递归状态抽象程序。
- 方法/训练算法：LLM-guided genetic algorithm。
- 反向传播：reference agent 明确固定。
- 待核实：无。

### 24. [Large Language Model Driven Operator Evolution: A Paradigm for Operator Pool Reconstruction and Adaptation](https://openreview.net/forum?id=wqsoOi2vaP)

- 决定：`keep_unaffected`
- 依据：这是 LLM 辅助的一般进化算子设计，用于受约束多目标优化；不是提示词研究或语言智能体。
- 实际更新对象：GA/DE 候选算子。
- 方法/训练算法：反馈驱动的 operator reconstruction。
- 反向传播：摘要未报告 LLM 参数训练。
- 待核实：无。

### 25. [LabBook: Harnessing Experimental History for Efficient LLM-Driven Discovery](https://openreview.net/forum?id=JUgAEHSCri)

- 决定：`defer_agent_no_model_training`
- 依据：LabBook 是 discovery agent 维护的外部实验记忆，驱动新程序生成；未训练 agent 模型参数。
- 实际更新对象：程序候选、实验日志与 LabBook 外部记忆。
- 方法/训练算法：单智能体迭代程序发现。
- 反向传播：摘要没有语言模型参数训练。
- 待核实：无。

### 26. [Is Flat Merging Enough? Evolutionary Search for Tree-Structured Model Merging](https://openreview.net/forum?id=9Ntfc5vVGp)

- 决定：`keep_unaffected`
- 依据：核心是语言/视觉模型合并结构的遗传编程搜索，会产生持久合并模型；非提示词或智能体。
- 实际更新对象：合并树拓扑、专家选择/复用及合并后模型。
- 方法/训练算法：genetic programming。
- 反向传播：不需重训；候选专家此前如何训练不是该方法核心。
- 待核实：内部合并算子细节待原文。

### 27. [Is Complex Agentic Memory Always Needed? Naive RAG Is Stronger Than We Thought](https://openreview.net/forum?id=MZ7kcOOYa3)

- 决定：`defer_agent_no_model_training`
- 依据：论文比较固定的 Raw-RAG 与复杂 agentic memory；核心状态是检索/记忆系统，不训练语言智能体参数。
- 实际更新对象：原始历史索引、检索与 reranking。
- 方法/训练算法：检索基准与证据分析。
- 反向传播：摘要没有 reader LLM 参数训练。
- 待核实：无。

### 28. [Improving LLM-driven program evolution with dynamic scope](https://openreview.net/forum?id=MXINrso5QC)

- 决定：`keep_unaffected`
- 依据：DyScope 优化 LLM 驱动程序演化的可编辑边界；摘要未把系统定义为语言智能体，也不属于提示词。
- 实际更新对象：程序、scope graph 与 transition contract。
- 方法/训练算法：动态范围控制的 program evolution。
- 反向传播：未训练 LLM 参数。
- 待核实：与 agent harness 的边界仅凭摘要不能成立，故本次范围不自动排除。

### 29. [Hill Sampling for Test-Time Scaling: A Simple and Better Alternative to Repeated Sampling, Evolution, and Training](https://openreview.net/forum?id=m1xdCQou1Z)

- 决定：`keep_unaffected`
- 依据：核心是冻结 LLM 的 test-time program sampling，并直接比较 LLM 权重 ES；属于推理时优化研究而非 agent harness/prompt。
- 实际更新对象：候选程序；比较分支另搜索模型权重。
- 方法/训练算法：hill climbing、重复采样与 ES 对照。
- 反向传播：主方法冻结 LLM；比较的 ES 分支更新模型权重且无需反传。
- 待核实：无。

### 30. [Harmony Harness: Multi-Objective Self-Evolution of Agent Harnesses](https://openreview.net/forum?id=cR0St8qS2n)

- 决定：`defer_agent_no_model_training`
- 依据：Harmony Harness 演化 agent harness 机制与基准适配，推理时组合外部工件；无模型参数训练。
- 实际更新对象：agent harness 及 Pareto 解集。
- 方法/训练算法：分解式多目标进化搜索。
- 反向传播：摘要未报告 LLM 参数更新。
- 待核实：无。

### 31. [HapBO: Harnessed α–π Bayesian Optimization via Expert Natural Language Priors](https://openreview.net/forum?id=45k9l8zWbL)

- 决定：`keep_unaffected`
- 依据：HapBO 将一次性自然语言先验编译成 BO belief function；不是 prompt optimization 或语言智能体。
- 实际更新对象：BO belief function 与 acquisition multiplier。
- 方法/训练算法：带有理论保证的 prior-guided BO。
- 反向传播：无语言模型参数训练。
- 待核实：无。

### 32. [HERA: Harness–Environment Co-Evolution for Reliable Agentic Abstention](https://openreview.net/forum?id=aqyvExE4ST)

- 决定：`defer_agent_no_model_training`
- 依据：HERA 演化 harness 与任务环境，并明确最佳 harness 跨模型迁移且无 model-specific optimization。
- 实际更新对象：agent harness、环境变异和任务。
- 方法/训练算法：harness-environment co-evolution。
- 反向传播：没有语言模型参数训练。
- 待核实：无。

### 33. [HEMO: Harness Self-Evolution for Multi-Objective Combinatorial Optimization](https://openreview.net/forum?id=FxMC3n6AdZ)

- 决定：`defer_agent_no_model_training`
- 依据：HEMO 更新的是 AOD harness 模块、持久 memory filesystem 和算子搜索编排，不是语言模型参数。
- 实际更新对象：harness state、搜索算子和外部记忆。
- 方法/训练算法：UCB 调度的模块级 self-evolution。
- 反向传播：摘要没有 LLM 参数更新。
- 待核实：无。

### 34. [Geometry of Large Language Model Controllability](https://openreview.net/forum?id=eVAaz2QSye)

- 决定：`defer_prompt_core`
- 依据：PGDE 的核心是用输出空间 pullback 距离筛选离散提示词跳转。
- 实际更新对象：离散提示词候选。
- 方法/训练算法：gradient-free pullback-guided discrete exploration。
- 反向传播：不更新模型参数；严格梯度属性仅针对离散搜索。
- 待核实：无。

### 35. [GP-Harness: Sequential Bayesian–Evolutionary Optimisation of LLM Harnesses](https://openreview.net/forum?id=0T5xZWy3I2)

- 决定：`defer_agent_no_model_training`
- 依据：GP-Harness 围绕 fixed model 演化、重组并选择 harness。
- 实际更新对象：agent harness 图。
- 方法/训练算法：Gaussian-process Bayesian optimization 加 evolutionary generation。
- 反向传播：任务模型明确固定。
- 待核实：无。

### 36. [FrugalEvo: Towards Cost-Aware LLM-Guided Program Evolution](https://openreview.net/forum?id=QT9UN9GxWQ)

- 决定：`keep_unaffected`
- 依据：FrugalEvo 搜索数学/系统任务的程序解；LLM 是方案/代码生成器，不是被训练的 agent 模型，也非提示词优化。
- 实际更新对象：候选程序与演化缓存流程。
- 方法/训练算法：成本感知程序演化。
- 反向传播：摘要未报告 LLM 参数更新。
- 待核实：虽比较 multi-agent 方法，但自身核心不是 agent 模型训练。

### 37. [From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails](https://openreview.net/forum?id=2ieHfp0vhO)

- 决定：`defer_prompt_core`
- 依据：攻击核心是搜索最大化 guardrail 推理长度的自然语言 payload，属于对输入提示的优化。
- 实际更新对象：攻击 payload/注入文本。
- 方法/训练算法：beam search 与结构化 mutation。
- 反向传播：未训练目标 guardrail 或 proposer 模型参数。
- 待核实：无。

### 38. [From Operation to Interface: Where Harness Changes Enter a Fixed Model’s Tool Calls](https://openreview.net/forum?id=DSP0z2ufLg)

- 决定：`defer_agent_no_model_training`
- 依据：研究固定模型下不同 harness 对 tool-call 操作/接口的影响，明确讨论不触碰权重的 harness edits。
- 实际更新对象：prompts、tools、middleware 与调用历史。
- 方法/训练算法：干预与表征分析，不是模型训练。
- 反向传播：模型固定；activation steering 实验也未建立参数更新。
- 待核实：无。

### 39. [From Experience to Knowledge: Algorithm Design for Black-Box Optimization with Large Language Models](https://openreview.net/forum?id=QDfuYx1Rp8)

- 决定：`keep_unaffected`
- 依据：FETK 是面向黑盒优化的 EA architecture 设计与知识蒸馏，不属于 prompt 或语言智能体范围。
- 实际更新对象：EA 架构与自然语言设计知识。
- 方法/训练算法：三阶段经验收集、知识学习、复用。
- 反向传播：摘要未训练 LLM 参数。
- 待核实：无。

### 40. [FedPOB: Sample-efficient Federated Prompt Optimization via Bandits](https://openreview.net/forum?id=psls0Sg5LI)

- 决定：`defer_prompt_core`
- 依据：FedPOB 的明确目标是联邦黑盒 prompt optimization。
- 实际更新对象：提示词配置以及 bandit 统计参数。
- 方法/训练算法：Linear UCB / federated dueling bandits。
- 反向传播：不更新被调用 LLM 权重；“sharing model parameters”指 bandit 模型参数。
- 待核实：需避免将 bandit 参数误记为语言模型参数。

### 41. [Evolutionary Adversarial Attacks Meet LLMs: Semantic-aware Adaptive Optimization Against Vision-Language Pre-trained Models](https://openreview.net/forum?id=u82Fkl3jwy)

- 决定：`keep_unaffected`
- 依据：LEA 用 LLM 控制器协调对 VLM 的图像扰动进化；核心对象是对抗图像扰动，不是提示词或 agent harness。
- 实际更新对象：图像扰动、算子选择和搜索参数。
- 方法/训练算法：异构 evolutionary operator pool。
- 反向传播：受害模型黑盒且无梯度；未训练 LLM 控制器。
- 待核实：无。

### 42. [EvoMem: Memory-Augmented Evolution for Code Optimization](https://openreview.net/forum?id=nrx0FyO4my)

- 决定：`keep_unaffected`
- 依据：EvoMem 为 LLM 驱动程序搜索保存和检索 mutation knowledge；核心仍是程序优化，不是 agent 模型/harness。
- 实际更新对象：候选程序与跨运行外部 mutation memory。
- 方法/训练算法：memory-augmented evolutionary program search。
- 反向传播：未训练 LLM 参数。
- 待核实：若未来把该系统界定为 agent memory，需再按范围复核。

### 43. [EvoG: A Modular Framework for Evolutionary Optimization of Agentic Workflows](https://openreview.net/forum?id=0MiTxo4j9d)

- 决定：`defer_agent_no_model_training`
- 依据：EvoG 明确优化 agentic workflow 图；四组件和共享历史更新候选工作流，无模型参数训练证据。
- 实际更新对象：agent workflow、候选 lineage 和执行历史。
- 方法/训练算法：模块化 evolutionary optimization。
- 反向传播：摘要没有 LLM 参数更新。
- 待核实：无。

### 44. [EvoDisco: Strategy Discovery for Self-Evolving Agent Memory](https://openreview.net/forum?id=FmXVyNi3hK)

- 决定：`defer_agent_training_unverified`
- 依据：EvoDisco 声称 learnable policy 按双层 fitness 更新，但摘要未说明该 policy 是参数化模型还是外部规则/状态，不能认定训练语言/策略模型参数。
- 实际更新对象：记忆操作选择/实例化 policy 与 memory state。
- 方法/训练算法：双层 fitness 的在线 policy update。
- 反向传播：是否使用反向传播、ES 或规则更新均未说明。
- 待核实：需核实 policy 表示、可训练参数、更新算法及其是否属于 agent policy model。

### 45. [Escaping Alignment: A Physical Trap Model of Best-of-N Jailbreaking](https://openreview.net/forum?id=x7eAMFALle)

- 决定：`defer_prompt_core`
- 依据：BoN jailbreak 的核心对象是 unsafe prompt 的随机 augmentation 与 completion 采样。
- 实际更新对象：攻击提示词变体。
- 方法/训练算法：Best-of-N 随机增强采样及物理 barrier 建模。
- 反向传播：不更新目标模型参数。
- 待核实：无。

### 46. [Elicitation or Expansion? Demystifying Gains from Agent Harness Optimization](https://openreview.net/forum?id=bSBejKazyx)

- 决定：`defer_agent_no_model_training`
- 依据：论文明确研究不更新模型权重的 harness optimization，并分析其 elicitation/expansion 效应。
- 实际更新对象：context、tool use 与 execution workflow。
- 方法/训练算法：harness 前后对照和 pass@k 分析。
- 反向传播：明确不更新模型权重。
- 待核实：无。

### 47. [EVOUNDO: RECOVERABILITY-CONSTRAINED SELF-EVOLUTION FOR LLM AGENT HARNESSES](https://openreview.net/forum?id=IFmd4fBKfS)

- 决定：`defer_agent_no_model_training`
- 依据：EvoUndo 的对象是 prompts、tools、middleware、resources 和 harness 自修改及其可恢复性，不是模型参数。
- 实际更新对象：agent harness 自修改与 recovery calculus。
- 方法/训练算法：反事实状态下的合成、诊断和验证。
- 反向传播：摘要未报告语言模型参数训练。
- 待核实：无。

### 48. [EEVEE: Post-Deployment Prompt Learning across Heterogeneous Tasks](https://openreview.net/forum?id=tHX0Ublg85)

- 决定：`defer_prompt_core`
- 依据：EEVEE 明确联合演化 router 与 prompt configurations，核心仍是 post-deployment prompt learning。
- 实际更新对象：提示词配置与外部 router。
- 方法/训练算法：router-prompt co-evolution。
- 反向传播：摘要未证明更新 LLM 权重；router 是否为参数模型及训练方式未说明，但不改变 prompt 核心暂缓决定。
- 待核实：需核实 router 的表示与持久参数。

### 49. [E$^{2}$MEND: Evidence-guided Evolution for Memory Enhancement via Bottleneck Diagnosis](https://openreview.net/forum?id=EcMoDY6gpg)

- 决定：`defer_agent_no_model_training`
- 依据：E2MEND 变异和回滚的是 versioned memory-strategy artifacts，runtime 锁定；未训练语言智能体模型。
- 实际更新对象：记忆提取、检索、typed state 等策略工件。
- 方法/训练算法：诊断驱动的 bounded evolution。
- 反向传播：摘要没有模型参数训练。
- 待核实：无。

### 50. [Does Prompt Sensitivity Improve Cross-Family Degradation Prediction?](https://openreview.net/forum?id=uVn7IU6iPN)

- 决定：`defer_prompt_core`
- 依据：论文以十种 instruction wording 的 prompt sensitivity 为核心变量，研究其跨模型家族预测价值；虽然不优化提示词，仍属于提示词核心研究。
- 实际更新对象：无持久更新；只计算不同提示措辞下的统计特征。
- 方法/训练算法：交叉验证和 permutation reference。
- 反向传播：无模型训练。
- 待核实：无。

### 51. [Do Vision-Language Models Use the Regions They Cite? A Step-Specific Intervention Test](https://openreview.net/forum?id=JwUvLVBgt7)

- 决定：`keep_unaffected`
- 依据：这是 VLM 区域引用的逐步干预检验；prompt/step 仅为测量上下文，不进行提示优化或 agent 演化。
- 实际更新对象：无；固定 reasoning steps 上进行区域扰动。
- 方法/训练算法：似然变化与成对顺序统计检验。
- 反向传播：无模型参数训练。
- 待核实：无。

### 52. [Direction-Indexed Evolutionary Red-Teaming of Large Language Models](https://openreview.net/forum?id=TWCBAEspBn)

- 决定：`defer_prompt_core`
- 依据：DIER 演化 roles、pretexts、personas 等 jailbreak framings，本质是攻击提示工件搜索。
- 实际更新对象：攻击 framing/library。
- 方法/训练算法：response-direction indexed evolutionary ranking。
- 反向传播：方向不进入模型激活且不更新目标模型参数。
- 待核实：无。

### 53. [Designing and Evolving Multi-Agent Systems via a Typed Intermediate Representation](https://openreview.net/forum?id=6YccHf9cEN)

- 决定：`defer_agent_no_model_training`
- 依据：meta-agent 生成 typed IR 来设计 MAS；经验演化 refine design policy，但摘要明确不更新任何模型参数。
- 实际更新对象：MAS typed IR、角色/目标/instructions 与外部经验。
- 方法/训练算法：experience-guided evolutionary design。
- 反向传播：摘要明确 updating no model parameters。
- 待核实：“design policy”是外部生成策略，不能据词面当作参数化 policy model。

### 54. [DebtMerge: Long-Horizon Expert Evolution for Continual Model Merging](https://openreview.net/forum?id=h2B3uQpSxt)

- 决定：`keep_unaffected`
- 依据：DebtMerge 优化并产生持久语言/视觉模型合并结果；不是提示词或智能体研究。
- 实际更新对象：专家选择、merge recipe、结构和集成几何。
- 方法/训练算法：Lyapunov debt control 加 evolutionary transfer optimization。
- 反向传播：不联合重训；候选专家既有训练不属于本文更新。
- 待核实：无。

### 55. [DarwinX: Evolving Agent Harnesses through Natural Selection](https://openreview.net/forum?id=XVvUgp3Bu8)

- 决定：`defer_agent_no_model_training`
- 依据：DarwinX 明确在 model fixed 条件下演化 instructions、tools、memory 和 control-flow harness。
- 实际更新对象：agent harness 与 archive/shared memory。
- 方法/训练算法：population-based natural selection。
- 反向传播：模型明确固定。
- 待核实：无。

### 56. [Customize Your Memory: Scenario-Adaptive and Evolvable Memory Modeling for LLM Agents](https://openreview.net/forum?id=qm5Z3S6e4g)

- 决定：`defer_agent_no_model_training`
- 依据：ScenarioModelMem 演化的是动态 memory policy 和外部记忆建模结构；摘要没有训练语言/策略模型参数。
- 实际更新对象：静态记忆结构与动态记忆策略。
- 方法/训练算法：验证驱动的 mutation、crossover、pruning。
- 反向传播：无语言模型参数训练证据。
- 待核实：“policy”表现为可演化的记忆配置；是否参数化未说明，但摘要机制支持外部工件解释。
