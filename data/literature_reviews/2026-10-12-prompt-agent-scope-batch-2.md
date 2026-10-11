# 2026-10-12 提示词与智能体范围审查：批次 2（语义修正版）

本批次逐篇审查 56 条。语义修正版按真实机制判定，不以是否自称 agent/harness、原类别名或关键词规避范围。

## 统计

- `defer_agent_no_model_training`：33 条
- `defer_agent_training_unverified`：1 条
- `defer_prompt_core`：15 条
- `keep_unaffected`：7 条

## 逐篇决定

### 1. Ranking-Aware Prompt Optimization for Multimodal Clinical Diagnosis

- 决定：`defer_prompt_core`
- 原分类：`related_prompt_agent`
- 论文特定依据：核心对象是多模态临床诊断提示词；Ranking-PE 以成对排序反馈演化候选提示词。
- 模型参数/组件边界：候选提示词；不更新诊断模型参数。
- 训练算法：基于经验 AUROC 的 pair-level Pareto prompt evolution。
- 反向传播：摘要未说明底层 MLLM 或反思模型训练；提示词搜索本身不需要反向传播。
- 待核实：医学视觉骨干曾通过 SFT/预训练获得，但它不是本文提示词搜索中更新的对象。
- 原始来源：https://openreview.net/forum?id=4JLvdwVQnj
- 官方摘要证据：Multimodal large language models (MLLMs) are rapidly advancing clinical diagnosis, yet their adaptation pipelines remain anchored to accuracy-based objectives. Clinical data are heavily class-imbalanced: a constant-majority predictor can score above $90\%$ accuracy while being clinically useless. We therefore evaluate and optimize for AUROC, a threshold-free score that ranks positives above negatives and is invariant to class balance.
We focus on prompt optimization in MLLMs. Reflective methods such as GEPA use a binary *scores matrix* with one row per evaluation instance and one column per candidate prompt; cells record per-instance correctness, so the column average is accuracy and drives candidate selection.

We introduce *pair-level Pareto prompt evolution* (Ranking-PE), which replaces each correctness row with a pairwise-ordering row over (positive, negative) instance pairs: the cell is $1$ if the candidate scores the positive higher than the paired negative. The column average then equals empirical AUROC (by the Wilcoxon–Mann–Whitney identity). We apply this swap at all three layers the prompt evolution search reads from—the scores matrix that decides Pareto dominance, the per-example feedback to the reflection LM, and final candidate selection—at no extra model calls and with no surrogate loss.
Across three diseases on MIMIC, accuracy-based prompt evolution can degrade ranking; Ranking-PE reverses this, beating the accuracy-based recipe by $+5.8$ AUROC pp on fine-tuned Qwen3-VL-8B and $+16.2$ pp on MedGemma-4B. Ablations examine each design component and show that a medical-grade visual backbone—via vision-encoder-tuned SFT or medical pretraining—is a prerequisite that prompt search cannot replace—our recipe extends reflective prompt evolution from text-only data to multimodal clinical decision-making.

### 2. RBEPO: From Root-Cause Diagnosis to Branching Evolutionary Prompt Optimization

- 决定：`defer_prompt_core`
- 原分类：`related_prompt_agent`
- 论文特定依据：RBEPO 的核心是按失败根因生成、评估、组合提示词重写分支。
- 模型参数/组件边界：提示词及跨迭代重写经验。
- 训练算法：根因聚类、分支式演化提示优化和 racing。
- 反向传播：摘要明确不更新模型参数；未说明固定调用模型自身的训练。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=XbT1YBExr4
- 官方摘要证据：With the widespread deployment of large language models in agentic systems and domain-specific tasks, using execution feedback to enable system self-evolution has attracted increasing attention. Automatic prompt optimization provides a lightweight path for systems to continually improve task performance without updating model parameters. However, identifying problems from execution feedback does not necessarily reveal effective repair strategies; joint rewrites across multiple directions obscure the actual effects and reuse potential of individual repairs. We propose RBEPO (Root-cause-guided Branching Evolutionary Prompt Optimization), a prompt optimization framework centered on cross-instance failure modes that jointly organizes targeted branching search and mechanism-level experience accumulation. RBEPO infers repair directions through per-instance error analysis and cross-instance root-cause clustering, generates and evaluates targeted rewrite branches for individual failure modes, and integrates effective, complementary repairs. Building on these evaluated rewrites, the method distills rewrite attempts and their evaluation results into cross-iteration experience to guide subsequent rewrites. To control the resulting candidate-evaluation cost, prompt-edit fragility-guided racing is introduced. Across multiple tasks and models, RBEPO consistently achieves higher test scores than the compared baselines: its average score is approximately 3.35 points higher than that of the strongest baseline in aggregate, while its final prompts are on average only about 1/6 as long. Comparisons of evaluation strategies further show that this strategy reduces the total sample-evaluation volume to about 38\% of full evaluation while maintaining performance close to that of full evaluation.

### 3. Proximity, Precendence and Position: A Minimum Linear Arrangement Account of Ordering Effects in LLM Prompts

- 决定：`defer_prompt_core`
- 原分类：`related_prompt_agent`
- 论文特定依据：核心研究对象是 in-context demonstrations 的排列顺序，即固定内容提示词的离散优化。
- 模型参数/组件边界：提示词中 demonstrations 的顺序。
- 训练算法：带 precedence 约束的 minimum linear arrangement。
- 反向传播：无模型参数训练；属于上下文排列优化。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=dp6Z7up2zP
- 官方摘要证据：In-context learning is highly sensitive to the ordering of demonstrations, but the root factors of context ordering remain undiscovered. Existing work treats a demonstration set as an unordered bag and searches over permutations based on a certain metric, without modeling the underlying relational structure. We give a structural account of order sensitivity built on three key properties of an arrangement: proximity (how far apart dependent facts sit), precedence (whether each fact appears after the facts it depends on), and position (where a fact sits in the context). We model proximity and precedence using minimum linear arrangement (MinLA), with precedence as a hard constraint and isolate position through controlled experiments. We treat the MinLA-constrained order as an oracle and measure how much of the total order effect it recovers relative to the worst achievable order. This provides a direct measure of how well our account explains observed behavior. On small-scale instances with known ground-truth ordering accuracy, it recovers 81\% of the order effect in the referential domain and 63\% in the associative domain. Across two domains with different dependency semantics — referential (GSM8K arithmetic, where a step reuses an unresolved prior value) and associative (synthetic narratives, where a sentence names a concept introduced earlier) — orders that are both MinLA-optimal and precedence-legal outperform the natural order by +34.5\% accuracy in arithmetic and +16.3\% in narrative on Llama-3.2-3B-Instruct, while MinLA optimization without the legality constraint does not reliably help. Decomposing the order effect into clustering (proximity) and direction (precedence), direction accounts for 61\% of it in arithmetic and clustering for 56\% in narrative, consistent with a referential-versus-associative account of how each domain encodes dependency. A third, independent, U-shaped position effect, isolated under experimental control, connects our results to lost-in-the-middle phenomena reported in previous work only observationally.

### 4. Providing Context: Enriching Graph Learning Using Language Model Priors

- 决定：`defer_prompt_core`
- 原分类：`related_prompt_agent`
- 论文特定依据：核心机制是将 LM-embedded global graph prompts 作为图语义条件，通过 cross-attention 注入 GNN；虽非提示搜索，仍以提示表示为主要研究对象。
- 模型参数/组件边界：外部图描述提示表示及 GINAT 图网络参数。
- 训练算法：prompt-conditioned message passing 与常规图表示学习；摘要未给出优化器。
- 反向传播：图网络需要训练，但摘要未明确反向传播细节。
- 待核实：LM embedding 是否冻结未明确。
- 原始来源：https://openreview.net/forum?id=nGF3lnQ3Qd
- 官方摘要证据：We introduce GINAT, a graph-language augmentation framework that improves message-passing GNNs by conditioning their edge messages on LM-embedded global graph descriptions. Unlike text-attributed graph methods that rely on node/edge-attached text, GINAT leverages external prompts that capture graph semantics independently of the downstream task. These prompts are injected into message passing through a cross-attention mechanism that preserves permutation equivariance, enabling global contextual guidance within standard MPNN computation. Across a broad suite of node- and graph-level benchmarks, GINAT yields consistent gains over strong GNN baselines, reaching up to 23% average relative improvement. Ablations show that the gains arise from the semantic content of prompts rather than random vectors, and an analysis of the learned context scaling reveals where and how strongly different backbones and layers rely on language-conditioned information. Overall, GINAT establishes LM-embedded prompts as a practical, interpretable graph-language signal to strengthen graph representation learning. Our code is available at https://anonymous.4open.science/r/GINAT-1312/

### 5. Prompt Reinjection for Spatial Reasoning in MMDiTs: Signal Amount, Depth Allocation, and Content-Specific Repair

- 决定：`defer_prompt_core`
- 原分类：`related_prompt_agent`
- 论文特定依据：核心机制是 MMDiT 内部逐层 prompt-token reinjection，并系统选择注入位置、深度和权重；属于提示信号适配。
- 模型参数/组件边界：推理时 prompt token 的注入位置、层分配和注入权重配置。
- 训练算法：受控消融和稀疏 prompt reinjection 调度。
- 反向传播：摘要未报告模型参数训练。
- 待核实：是否存在额外校准训练未说明。
- 原始来源：https://openreview.net/forum?id=fmAQLVOhLg
- 官方摘要证据：Multimodal diffusion transformers (MMDiTs) forget prompt semantics as depth grows, and spatial relations suffer most. Prompt Reinjection (PR) counters this by repairing every text token at every layer, but neither the number of repaired positions nor the choice of layers has been examined; we therefore treat PR as a probe of its own redundancy. Repair saturates early: eight real positions match full-scale repair, and the injection weight, not the token count, controls the response; past a bounded window, amplification collapses performance on SD3. Most repaired positions are padding, which joint attention does not mask and which carries no signal. Depth adds a secondary trend at the default weight: with span-matched controls, dense repair over the early half matches full PR while late-only repair is no better than baseline, and several allocations perform comparably. As one instantiation, an early-full/late-sparse schedule (Layer-Adaptive Sparse Prompt Reinjection, LASP) reaches 40.1\% on GenEval Position, matches full PR with a third of the token-layer pairs, and remains robust where full PR collapses; we make no optimality claim. The injected content matters---noise, a permutation, or a constant removes the gain---and the pattern transfers to T2I-CompBench and directionally to FLUX.1-Schnell.

### 6. Predicting Where Recall Fails: The Fact Matters More Than the Entity in Black-Box Language Models

- 决定：`keep_unaffected`
- 原分类：`related_prompt_agent`
- 论文特定依据：复核保留：这是黑盒模型事实召回失败的统计测量研究，不执行提示/上下文适配或反馈式工件优化。
- 模型参数/组件边界：不适用；研究预查询统计特征与错误的关系。
- 训练算法：统计分析和重复采样。
- 反向传播：无所提模型训练。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=BhrfhXyPMR
- 官方摘要证据：Language models recall some facts reliably and fabricate others, and the standard predictor of where recall fails is entity popularity, which assigns one score to every fact about an entity. We ask whether factual reliability is a property of the entity or of the fact. Holding the entity fixed, we probe multiple numeric facts about the same entity and period in four knowledge domains (Major League Baseball, the National Hockey League, national economic indicators, and corporate finance), covering thirty statistics and seven models from six laboratories. The fact matters more than the entity. In the sports domains, the statistic being asked explains about half of the variance in answer error and the player about 5%. Entity popularity has no held-out predictive value, whereas prose redundancy, the Wikipedia mention rate of a statistic computed before any query, reaches a held-out $R^2$ of 0.41–0.44 and predicts error on statistics withheld from fitting ($R^2$ of 0.33–0.40), where features of the numbers themselves, such as their dispersion and magnitude, do not. Ordering statistics by prose redundancy places the least mentioned tier lowest in all four domains (fact-level exact permutation test, combined $p < 10^{-5}$); deviation correlation falls from +0.894 to +0.163 in baseball and from +0.990 to +0.853 in national statistics. A second pre-query measure, reconstructibility from co-occurring facts, indicates which low-redundancy facts are consistent with inference from headline statistics. For the least mentioned baseball statistics, models fabricate values while refusing fewer than 1% of questions, whereas for a season beyond their training data the non-answer rate rises to 24.8%. For two frontier models, the spread of repeated samples locates this boundary without ground truth, with an AUC of 0.952. The assessment needs only public text and API access to the model.

### 7. Permutation Alignment and Depth in Weight-Tied Language Models

- 决定：`keep_unaffected`
- 原分类：`related_prompt_agent`
- 论文特定依据：复核保留：研究语言模型权重置换对齐、平均、继续训练与蒸馏，属于真实模型参数/合并分析。
- 模型参数/组件边界：语言模型权重、对齐后的 midpoint。
- 训练算法：置换对齐、权重平均、继续训练和蒸馏。
- 反向传播：继续训练和蒸馏通常依赖反向传播；摘要未详述实现。
- 待核实：具体优化器待原文核实。
- 原始来源：https://openreview.net/forum?id=hvniX9y4FG
- 官方摘要证据：Averaging the weights of two independently trained language models can yield a far worse model, even after their hidden units are permuted into correspondence. We ask how much of this damage permutation alignment removes, and how to interpret the remaining damage in weight-tied (looped) models, whose depth can vary at runtime. We measure fifteen pairs of 35M-parameter looped models at 16 and 192 loops, before and after a permutation alignment that respects the shared weights, recording the quality of the averaged (midpoint) model and both endpoints. Before alignment, the median barrier (the ratio of midpoint to better-endpoint perplexity) is 1.8 dex (base-10 log units) higher for eight pairs trained mostly with random loop counts than for six trained at a fixed 16 loops; after alignment the gap is under 0.05 dex. A shared residual remains: with the best of four alignment methods, midpoint perplexity is at least 12 times the better endpoint's on every pair. Equal-norm random perturbations reproduce its typical size; perturbations along the aligned weight difference's leading directions cause more damage than orthogonal ones on every pair tested. At 192 loops, endpoint quality sets the barrier: it falls where endpoints become unusable and persists between depth-stable ones. Continuing training from the aligned midpoint for 30% of the original budget removes over 90% of its residual on two depth-stable pairs, and distilling a probability-mixture teacher keeps deep-runtime degradation below 0.05 dex, versus 0.40 dex for plain continuation. Relative barriers should thus be reported with absolute endpoint quality and runtime depth.

### 8. ParetoEvo: Pareto-Guided Evolutionary Tree Search for Automatic Heuristic Design with LLM Agents

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：LLM agents 生成、评估和修改可执行启发式；搜索对象是启发式程序与树节点，不是 agent 模型参数。
- 模型参数/组件边界：可执行启发式及搜索树。
- 训练算法：PD-MCTS、Pareto 选择和反思式生成。
- 反向传播：摘要没有训练 Actor/Reflector LLM 参数的证据。
- 待核实：“update guidance”指后续生成指导，不足以证明参数更新。
- 原始来源：https://openreview.net/forum?id=1Zv2iOm1Gb
- 官方摘要证据：Combinatorial optimization (CO) generally relies on human-designed heuristics to obtain high-quality solutions when exact search is computationally prohibitive. Large language model (LLM)-based automatic heuristic design (AHD) reduces this reliance by iteratively generating, evaluating, and revising executable heuristics. However, evaluating heuristics primarily by average solution quality can overlook execution cost and difficult-instance performance. Moreover, attained objective values do not necessarily reveal a heuristic’s potential for further evolution. To address these limitations, we propose ParetoEvo, a Pareto-guided evolutionary tree-search framework that combines objective trade-offs with evidence of search potential. We develop Pareto-dominance Monte Carlo tree search (PD-MCTS) to allocate evaluations through vector-valued subtree returns over average quality, execution time, and worst-instance quality. To complement descendant-based evidence with earlier indications of search potential, we propose adaptive productivity control (APC) to grant additional expansions when productive creation empirically predicts productive subsequent search. To adapt revisions to search experience, reflection-conditioned Actor and Reflector LLM agents use evaluated transitions to update guidance for subsequent heuristic generation. Experiments across diverse CO tasks demonstrate improvements in solution quality, execution efficiency, and worst-instance performance over LLM-based AHD baselines, alongside faster convergence and higher final Pareto-front quality.

### 9. Paper Agent Network: Literature-Grounded Multi-Agent Program Discovery

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：PAN 的持久 coding agents 通过工具、反馈和实现历史修订程序路线，更新的是可执行 artifact 与历史。
- 模型参数/组件边界：程序实现、方法路线、共享报告与历史。
- 训练算法：多智能体程序发现和基于评测的迭代修订。
- 反向传播：摘要没有语言/策略模型参数训练。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=eTpwBeLmHO
- 官方摘要证据：Using a research paper in program search requires turning its methods into executable candidates and adapting them to a target task. A paper can initialise an approach whose implementation continues to develop through evaluation and findings from other approaches. We introduce the Paper Agent Network (PAN), a literature-grounded multi-agent system that organises this process around persistent coding agents. Each agent starts from a selected paper and develops a revisable method route through tool use, evaluator feedback, and accumulated implementation history. A shared result board and queued reports connect these routes; a progress-based controller allocates work and introduces reserve agents. The design separates admitting an improved artifact from sharing a finding that may
inform later work. We evaluate the complete system on 23 tasks spanning mathematics, systems, engineering, planning, scientific code, and prediction against four open program-evolution frameworks. The reported comparison contains twelve best or tied-best results. Two process analyses make method and information use concrete. A denoising construction appears in executable artifacts, and a peer’s scheduling report motivates a change to a route that improves through later work. The 17-task literature comparison shows that the positive denoising case does not imply a general benefit from literature access. These observations establish method and information use within the implemented system; interaction’s independent performance contribution remains unresolved. Persistent paper-informed
routes provide a concrete setting for studying how published methods are implemented, exchanged, and adapted during computational problem solving.

### 10. PRISM: Transparent Strategy Search for Privacy Risks in LLM Agents

- 决定：`defer_prompt_core`
- 原分类：`related_prompt_agent`
- 论文特定依据：核心搜索对象是攻击者 instruction；稀疏 tactic code 和闭式 Bayesian surrogate 用于选择待重写指令。
- 模型参数/组件边界：攻击者指令及 tactic 表示。
- 训练算法：闭式 Bayesian surrogate 加反思重写。
- 反向传播：未更新目标、重写或评判模型参数。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=5lk0NlZc4f
- 官方摘要证据：Discovering privacy attacks on LLM agents by search is expensive: each candidate attacker instruction must be evaluated in a simulated multi-agent conversation, and the search framework of Zhang & Yang (2026) decides what to try next inside one reflect-and-rewrite LLM call, with no explicit representation of tactics and no surrogate-based rule for choosing among proposals before they are simulated. PRISM is a drop-in replacement for that proposal step. It represents each instruction as a sparse code over named tactic primitives learned from its text, fits a closed-form Bayesian surrogate of leak velocity (the benchmark’s metric; higher means a stronger attack), and uses the surrogate to choose which previously evaluated instructions the parallel search threads revise next; the rewrite itself remains the baseline’s own LLM call, and the simulator, judge, metric, data splits and per-step simulation and optimizer-call budgets are unchanged. On the benchmark’s 100 held-out scenarios, run entirely on open-weight models, the attack instructions transferred from PRISM’s search reach a mean leak velocity of 0.277 against 0.188 for the baseline’s (paired difference +0.089, 95% bootstrap interval [+0.025, +0.153] over scenarios). We also measure a property of the benchmark’s selection rule, which breaks ties among equally scored candidates uniformly at random: from a defended starting point in our environment all 30 candidates had zero observed leakage in 87 of 100 steps, so the observed scores did not distinguish candidates within those steps. A game-theoretic defense construction is derived and evaluated offline on released trajectories; the comparative defense searches stopped before it could activate, so no live comparison of defense proposers is reported.

### 11. PINNForge: Execution-Grounded Evolutionary Design of Physics-Informed Neural Networks for PDE Solving via Large Language Models

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：LLM 驱动演化的是 PINN 配置和设计组件；PINN 会训练，但没有训练语言智能体/策略模型。
- 模型参数/组件边界：PINN 架构、采样、约束、损失和优化配置。
- 训练算法：generate-execute-evaluate-evolve。
- 反向传播：候选 PINN 训练会使用其自身优化过程；LLM 参数更新无证据。
- 待核实：PINN 的具体反向传播实现未在摘要说明。
- 原始来源：https://openreview.net/forum?id=DXeChT9fBB
- 官方摘要证据：Physics-informed neural networks (PINNs) require coordinated choices across representation, architecture, sampling, constraints, loss construction, and optimization, yet effective configurations can vary substantially across partial differential equations (PDEs). Existing automated design methods search over these choices, but training outcomes are still used primarily to rank candidates rather than to inform subsequent designs. We develop PINNForge, an execution-grounded large language model (LLM)-driven evolutionary framework that treats observed PINN training behavior as a cross-generation design signal. PINNForge initializes diverse configurations from PDE-related prior knowledge, executes them, retains globally strong configurations, and feeds their execution evidence and accumulated run-level experience back to the LLM. The LLM then revises and recombines coupled design components or explores new combinations within a generate--execute--evaluate--evolve loop. Across 25 PDE benchmarks, PINNForge achieves the lowest mean MSE on 24 tasks among RoPINN, PINNsFormer, PINNsAgent, and PINNForge. Removing knowledge guidance, execution feedback, or evolutionary search increases the median task-wise MSE ratio to 3.74×, 12.10×, and 10.10×, respectively, relative to full PINNForge. Anonymous code: https://anonymous.4open.science/r/PINNForge/

### 12. Ouroboros: A Self-Developing Coding Harness with Reviewed Core Evolution

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：Ouroboros 演化 tools、context、prompts 和 harness core implementation；基座模型参数未被描述为训练对象。
- 模型参数/组件边界：agent harness 代码、工具、上下文装配与提示词。
- 训练算法：经审查 commit 的递归/经验驱动 core evolution。
- 反向传播：摘要没有语言模型参数训练。
- 待核实：系统可选择新 model API，但这不是训练模型参数。
- 原始来源：https://openreview.net/forum?id=w0OSBRyfSU
- 官方摘要证据：Long-horizon agents are model–harness systems, yet most harnesses remain fixed after design. We present Ouroboros — a self-developing agent harness whose tools, context assembly, prompts and core implementation improve through reviewed commits that become the runtime for later work. Core evolution proceeds in two modes. In recursive free evolution, improvement is itself a task and completion can schedule the next evolution cycle. In experience-driven core evolution, ordinary work and social interaction expose bugs, rough edges, and inefficient context construction leading to reviewed structural changes. On Terminal-Bench 2.1, an Opus 5 run scores **86.97%** (86.74% after trajectory audit), the best result reported on this benchmark. An Opus 5 run on OSWorld-Verified reaches **90.69%**, above the best previously reported score, and a five-rollout CL-Bench campaign sets a new state of the art at **0.2301** **(all three comparisons as of August 2026)**. Hope is the longest-running publicly documented Ouroboros deployment: a 161-day living-agent experiment in free evolution under governed human communication across seven surfaces, where people surface faults and proposals but the agent decides which changes to pursue. Because a self-developing agent may rewrite its own code and select new model APIs, operational safety is a primary design problem: guardrails must remain authoritative under evolutionary pressure. Benchmark campaigns use frozen seeds, while Hope continues live evolution on a separate lineage.

### 13. OrderCover: Structure-Aware Budgeted Search over Prompt-Component Orders

- 决定：`defer_prompt_core`
- 原分类：`related_prompt_agent`
- 论文特定依据：核心是固定文本 prompt components 的排列搜索。
- 模型参数/组件边界：提示词组件顺序。
- 训练算法：结构覆盖与 Kendall-distance 分离的预算搜索。
- 反向传播：摘要明确不用 logits、gradients 或模型分数。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=hciep78aST
- 官方摘要证据：Prompt optimization typically rewrites instructions or selects demonstrations, although reordering existing components can change model behavior while keeping their text fixed. We formulate fixed-content prompt-order optimization and introduce OrderCover, a budgeted method that selects candidate permutations using structural feature coverage and Kendall-distance separation. Candidate construction uses only permutation structure, without labels, logits, gradients, or model scores. We evaluate OrderCover through complete landscapes across 10 tasks and 7 models, held-out application prompts, and composition with GEPA and MIPROv2. In the controlled suite, OrderCover improves the original Anchor by 3.35 percentage points, recovers 82.99% of the available Anchor-to-Oracle headroom, and exceeds budget-matched Random by 0.46 points. On application prompts, it improves Anchor in 12 of 15 cells, although the aggregate confidence interval includes zero. After content optimization, order search adds 1.48 points on average across 24 cells and improves 19 of them. Order headroom persists for strong starting orders and after content optimization, although the advantage over budget-matched Random is modest. OrderCover offers a transparent, content-preserving post-processing step for prompts whose components can be moved as whole units.

### 14. Online Automated Algorithm Design with Large Language models

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：多智能体按优化状态合成并执行算法；更新的是可执行算法与对运行证据的解释，不是模型参数。
- 模型参数/组件边界：优化算法代码/决策规则。
- 训练算法：在线多智能体 automated algorithm design。
- 反向传播：摘要没有 LLM/agent policy 参数训练。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=mm4pTeeEST
- 官方摘要证据：Large language models (LLMs) enable automated algorithm design (AAD) through reasoning and code synthesis. However, most existing LLM-based AAD methods separate algorithm design from target optimization, deploying a fixed design even as the optimization state evolves. Conventional adaptive optimizers can respond to such changes, but their adjustments remain confined to predefined parameters, operators, or strategies. To address these limitations, we introduce online LLM-based AAD, a novel optimization paradigm that treats the algorithm itself as a state-dependent decision variable. At each stage, LLM agents synthesize an algorithm with new decision rules from the current optimization state. Executing the generated algorithm advances the search and provides feedback for subsequent designs, coupling algorithm design with target optimization without requiring a separate offline algorithm pretraining stage. To implement this paradigm, we propose OnDesign, a multi-agent framework that reconciles competing design perspectives to synthesize executable algorithms and uses execution feedback to refine how runtime evidence is interpreted for subsequent designs. We evaluate OnDesign across two mainstream black-box optimization paradigms on three scenarios: Bayesian optimization, evolutionary continuous optimization, and evolutionary mixed-variable optimization. Extensive experiments on six benchmark suites and one engineering problem across multiple problem dimensions demonstrate superior overall performance over conventional optimizers and offline LLM-based AAD methods.

### 15. NextEval: An Agent-Based Solver and Benchmark for Derivative-Free Optimization

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：NextEval 的 LLM agent 选择工具、参数和预算，数值环境维护历史；未训练智能体模型。
- 模型参数/组件边界：DFO 评估点、工具配置、预算与历史状态。
- 训练算法：LLM agent 调度数值 DFO 方法。
- 反向传播：摘要没有模型参数更新。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=MsqBCJeXIT
- 官方摘要证据：Derivative-free optimization (DFO) addresses problems where derivatives are unavailable or costly to obtain. This setting often arises in simulation-based and experimental applications, where evaluating their black-box objective can itself be costly. Thus, it remains a central challenge in DFO to effectively exploit accumulated observations to select informative evaluation points under a limited budget. In this light, we introduce the NextEval solver, an agent-based DFO solver, which integrates the capabilities of the large language model (LLM) to guide the sequential selection of evaluation points. Specifically, we establish a system which combines an LLM agent with a numerical environment. The environment provides tools for analyzing past evaluations and executing numerical methods, while maintaining a shared evaluation history and method-specific state to support continuation across method switches. Using observations and tool feedback, the LLM agent selects tools, configures their parameters, and allocates the evaluation budget, while numerical methods compute and evaluate candidate points. Building on this system, we also introduce NextEval Bench, a benchmark protocol for comparing agent configurations on shared DFO tasks using the same numerical tools under matched evaluation budgets and information constraints. Numerical results on low-dimensional DFO problems demonstrate that the NextEval solver outperforms the state-of-the-art DFO baselines in function-evaluation efficiency.

### 16. Mirrorrefine: Mirror Reflection Generation via Multi-agent Refinement with Spatial Priors

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：多智能体迭代更新 synthesis conditions 并选择图像操作；摘要明确迭代期间全部组件参数固定。
- 模型参数/组件边界：合成条件、操作选择与生成图像。
- 训练算法：多动作 evolutionary refinement。
- 反向传播：迭代时全部组件参数固定；RSG 是离线训练的辅助几何模块。
- 待核实：RSG 的离线训练不等于语言智能体模型训练。
- 原始来源：https://openreview.net/forum?id=CygM5LTLej
- 官方摘要证据：Advancing visual generation toward world modeling requires more than photorealism: generated views must remain consistent with the underlying scene. In
mirror-reflection synthesis, this requires inferring reflected content and spatial
layout from the source scene, beyond the text–image alignment emphasized by
general-purpose prompt-refinement methods. We propose MirrorRefine, a multiagent framework for mirror-reflection generation through multi-action evolutionary refinement. Starting from a generated or supplied image, the Reflection Optimization Controller analyzes the original request and visible content outside the
mirror to infer intended reflected content and construct action-specific synthesis
conditions, rather than treating potentially erroneous reflections as reliable targets.
The Quality Evaluator provides a vision–language model with coarse reflectionlayout priors predicted by an offline-trained Reflection Spatial Geometry (RSG)
module. Together with textual conditions, these priors guide the diagnosis of geometric, appearance, and illumination inconsistencies in the synthesized image.
Based on this diagnosis, the evaluator selects among image generation, mirrorregion inpainting, and targeted editing, and returns structured revision suggestions
to the controller. The controller updates the synthesis conditions and coordinates
the selected operation, after which the resulting image is reassessed to guide subsequent refinement. All component parameters, including those of RSG, remain
fixed during iterative refinement. Experiments on MirrorBenchV2, MSD, and CCMirror show complementary strengths: among the compared systems, the online configuration leads the reported geometry, lighting, and appearance scores, while
the local configuration achieves the highest PSNR on MSD and CC-Mirror.

### 17. Meta-Delta: Evolving Knowledge through Global Review for LLM-Driven Optimization

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：固定 LLM 根据实验反馈反复生成候选并修订 Delta Bank 中的结构化搜索知识；持久更新的是候选解、Delta Cards、适用条件和证据，不是模型参数。
- 模型参数/组件边界：候选解与 Delta Bank；LLM 参数未训练。
- 训练算法：局部更新与 Global Review。
- 反向传播：摘要未报告 LLM 参数训练。
- 待核实：具体任务候选可能是程序/科学定律，非 agent 模型。
- 原始来源：https://openreview.net/forum?id=982s77OSTT
- 官方摘要证据：LLM-driven evolutionary optimization accumulates experience about which changes improve a candidate solution. As search progresses, this experience must be interpreted in context: lessons may have limited scope, accumulated guidance may conflict, and repeated refinement may leave alternatives unexplored. We introduce **Meta-Delta**, a framework that jointly evolves candidate solutions and the knowledge guiding their generation. A **Delta Bank** stores structured **Delta Cards** with search lessons, applicability conditions, and supporting evidence. Routine local updates incorporate what each experiment teaches, while Global Review examines the Bank and broader search history to reconsider existing guidance and propose directions for subsequent testing. The updated Bank guides new experiments, whose outcomes further refine its knowledge. Empirically, Meta-Delta achieves the best or tied-best result on 10 of 11 tasks across mathematical, scientific, and systems optimization. On scientific law discovery, it achieves the highest mean numeric-fit score on SCILAWS-REAL, ties for the highest scientific-validity score at displayed precision, and achieves the highest mean structure score on SCILAWS-PARALLEL. Global Review ablations provide evidence that broader knowledge revision helps sustain progress, and case studies show how revised knowledge changes subsequent search and the structure of discovered scientific laws. These results support treating search knowledge as an evolving component of long-horizon optimization.

### 18. Measured Behavior, Recorded Zero: Measurement Failures in Self-Improving Coding Agents

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：研究明确描述 frozen language model 周围的 scaffold evolution；更新的是 scaffold，且论文主要诊断测量失败。
- 模型参数/组件边界：agent scaffold 代码与测量层。
- 训练算法：进化式 scaffold 提案与评测。
- 反向传播：语言模型明确冻结。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=9UsBcc69Ua
- 官方摘要证据：Self-improving coding agents evolve a scaffold around a frozen language model and select variants using benchmark performance. We study whether that selection signal reliably reflects what the agent and the search actually did. On the 59-task Polyglot subset used by the Huxley–Gödel Machine (HGM), the default self-hosted setup records zero tool use at 7B, 14B, and 32B, yet the 14B transcripts contain dispatchable tool calls on 30/59 tasks. Recovering those calls changes tool use from 0/59 to 32/59 while resolve rate remains 0/59. In two evolutionary runs, all 14 proposed children are invalid Python and are archived with the same utility (0.0) that a valid child solving no tasks would receive. Replacing the proposal model with a frontier hosted model changes validity from 0/14 to 14/14 while preserving the same destructive edit pattern. Across ten configurations, resolve rates remain between 0/59 and 4/59. These results do not show that scaffold evolution fails. They show that, in this deployment regime, the recorded objective can collapse distinct behavioral states and can therefore obscure whether a search step acted, failed, or produced an executable candidate. We provide a network-level measurement layer and a set of inexpensive controls for evaluating self-improving agents.

### 19. Mask-On: Compact Activation-Calibrated Merging for Autoregressive and Diffusion Language Models

- 决定：`keep_unaffected`
- 原分类：`related_prompt_agent`
- 论文特定依据：复核保留：方法依据激活校准构造并应用模型合并 mask，持久结果是合并模型权重，属于非智能体模型合并。
- 模型参数/组件边界：AR-to-diffusion 紧凑权重更新、ternary masks 与 scales。
- 训练算法：闭式 scale fitting 和单 pruning parameter 搜索。
- 反向传播：摘要明确不使用 gradient-based optimization。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=db6NrHuZbK
- 官方摘要证据：Autoregressive (AR) and diffusion language models offer complementary generation behaviors, but retaining both pretrained endpoints requires storing two full parameter sets. We propose Mask-On, a gradient-free method that represents both modes using an unchanged AR backbone and a compact AR-to-diffusion update. Building on support/sign encoding, Mask-On compresses AR-to-diffusion weight changes into ternary masks and output-channel scales, calibrated by matching the diffusion endpoint's linear-layer outputs on collected activations. Closed-form scale fitting reduces the search to a single pruning parameter without gradient-based optimization or downstream task-specific tuning. Across four AR--diffusion model pairs and four benchmarks spanning diverse domains, we demonstrate that direct parameter merging does not consistently preserve both generation modes, whereas compact mode-specific updates support more consistent diffusion retention alongside an unchanged AR checkpoint. Mask-On achieves the highest average diffusion-mode accuracy among the compared merging methods on all four models, with an update substantially smaller than a full diffusion checkpoint. Experiments on Fast dLLM v2 show similar quality--throughput trend to the diffusion endpoint across six decoding configurations. A simple training-free experiment using the original AR checkpoint further improves diffusion-draft accuracy by up to 3.26 percentage points on GSM8K, illustrating how access to both modes can support complementary generation.

### 20. MODEPrompt: Taxonomy-Guided Pareto Evolution for Prompt Optimization

- 决定：`defer_prompt_core`
- 原分类：`related_prompt_agent`
- 论文特定依据：MODEPrompt 核心是按推理子群 Pareto 目标演化提示词。
- 模型参数/组件边界：候选提示词、语义 patches 和 meta-rules。
- 训练算法：多目标 evolutionary prompt optimization。
- 反向传播：摘要未给出语言模型参数更新。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=CkuA2Se9vX
- 官方摘要证据：Large language models (LLMs) are highly sensitive to prompts specifying task instructions, making automatic prompt optimization (APO) important for reliable performance. Existing APO methods typically guide search using scalar validation scores, which can obscure performance imbalances across heterogeneous reasoning patterns and produce prompts with competitive overall accuracy but low worst-group accuracy.
We propose MODEPrompt, a reflective multi-objective evolutionary framework that induces a task-specific taxonomy of mutually exclusive reasoning subgroups from development questions without using answer labels, and treats subgroup accuracies as distinct Pareto objectives. MODEPrompt introduces semantic differential evolution, which contrasts Pareto-front and non-front prompts to extract directional semantic patches that guide mutation and crossover. It further induces outcome-grounded meta-rules from trial acceptance outcomes and subgroup-level score changes, accumulating useful search experience across iterations.
Extensive experiments across diverse benchmarks show that MODEPrompt achieves strong overall performance, improves worst-group accuracy, and reduces performance disparities across reasoning subgroups. Further analyses support the stability, semantic interpretability, and performance relevance of the induced taxonomy.

### 21. MILO: Automated Harness Discovery via Orchestrated Multi-Agent Evolution

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：MILO 共同演化完整 harness 与搜索策略；对象是 harness、lineage memory、mutators 和 curriculum，并无模型参数训练证据。
- 模型参数/组件边界：agent harness 与外部搜索状态。
- 训练算法：岛模型 meta-evolution。
- 反向传播：摘要没有 LLM 参数训练。
- 待核实：mutator/orchestrator agent 的“adapt”是搜索行为，不证明参数学习。
- 原始来源：https://openreview.net/forum?id=AUiAVv2xU2
- 官方摘要证据：Modern agentic systems typically consist of an artificial intelligence (AI) model and a harness, a software layer that manages its control flow and interactions with the environment. Agent performance on long-horizon tasks is often strongly influenced by its harness design. Yet building effective harnesses requires significant human effort due to the combinatorial design space, and this effort must be repeated as models are updated. To automate harness design, existing methods provide limited exploration of this search space. Most optimize only parts of the harness, such as prompts or skills, while others struggle to escape local optima due to their fixed search strategies and exploitative bias in LLM-driven search.

In this paper, we present MILO (Meta-evolutionary Island Orchestration), a framework for automated harness discovery that co-evolves the harness and its own search strategy. Three components drive the search: (i) a hierarchical lineage memory of island-based trees that uses rejected mutations as negative evidence to prune unpromising paths and steer toward promising lineages; (ii) per-island mutator agents that combine global search history with feedback on parent weaknesses to rewrite entire harnesses; and (iii) an orchestrator agent that adapts the search by grafting and speciating lineages, reassigning mutators, and revising the curriculum. Together, they make MILO a meta-evolutionary harness-discovery framework that self-adapts its memory, mutators, and curriculum to balance exploration and exploitation. Across three long-horizon benchmarks, Terminal-Bench 2.1, PaperBench, and DeepSWE, MILO-discovered harnesses outperform eight state-of-the-art harnesses and six search methods with frontier (Opus 4.8) and open-weight (gpt-oss-120b) backbones. With Opus 4.8, it improves resolution rate over its initial harness by $+12.0$\%, $+28.3$\% and $+10.3$\%, respectively, versus the best prior search gains $+4.5$\% (GEPA), $+18.3$\% (Meta-Harness) and $0$\% (no improvement observed). On Terminal-Bench 2.1, it reaches $86.1 \pm 2.0$\%, above the official leaderboard's top entry ($83.8 \pm 2.3$\%), while consuming 26\% fewer tokens than its initial harness. On EinsteinArena's open problems, MILO-evolved harnesses tighten the best-known upper bounds for Erdős minimum-overlap ($0.3808586 \to 0.3808568$) and the first and third autocorrelation inequalities ($1.50274365 \to 1.50274360$, $1.45081 \to 1.44889$).

### 22. MAPF-Evo: LLM-Driven Evolution of Heuristics for Conflict Elimination in Multi-Agent Path Finding

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：LLM 驱动演化 MAPF-LNS 的 destroy heuristics；没有训练语言智能体模型。
- 模型参数/组件边界：可解释 destroy heuristic 程序。
- 训练算法：运行状态反馈驱动的启发式演化。
- 反向传播：摘要未报告 LLM 参数更新。
- 待核实：对比的 NNS 训练不属于所提 MAPF-Evo。
- 原始来源：https://openreview.net/forum?id=jtF7cAh4OE
- 官方摘要证据：Large Neighborhood Search (LNS) is one of the leading approaches for solving large-scale Multi-Agent Path Finding (MAPF), but its performance depends heavily on destroy heuristics—the strategy for selecting which agents to replan. Existing methods mostly rely on hand-crafted, fixed heuristics that cannot adapt well to different problem instances, whereas learning-based methods such as Neural Neighborhood Search (NNS) require training a separate model for each map type, which limits their generality. Therefore, we propose a Large Language Model (LLM) driven evolutionary framework (MAPF-Evo) that automatically designs interpretable destroy heuristics for LNS. By feeding the solver's runtime state back to the LLM, MAPF-Evo evolves heuristics that leverage detailed conflict-structure information to balance solution quality and speed. Experiments on five types of map (40 scenarios in total) show that, compared with the recent best method, MAPF-LNS2, adding the heuristic evolved by MAPF-Evo to the original heuristic pool reduces average remaining conflicts by about 45.0% and improves resolution speed by 11.6%. Gains are especially significant on structurally complex maps such as maze and room. This work is the first to introduce LLM-driven heuristic design into LNS-based MAPF solving, offering a more general and less manually tuned solution to this problem.

### 23. Learning Compact State Abstractions for LLM Agents

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：用固定 reference agent 的任务表现搜索递归状态抽象程序；更新的是程序而非 agent 参数。
- 模型参数/组件边界：确定性递归状态抽象程序。
- 训练算法：LLM-guided genetic algorithm。
- 反向传播：reference agent 明确固定。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=v5FgAqHn7s
- 官方摘要证据：LLM agents commonly use the full interaction history as a proxy for state, retaining all past observations and actions regardless of whether they remain relevant. We instead ask what information an agent actually needs to carry forward. We define agent state as a compact abstraction of interaction history that preserves the competence of a fixed reference agent, with the minimal such abstraction as the ideal. Because matching the reference agent's behavior is unnecessarily restrictive and difficult for black-box policies, we define sufficiency through task performance rather than behavior matching. We represent state abstractions as deterministic recursive programs and search over them using an LLM-guided genetic algorithm. Across ALFWorld and ScienceWorld, the learned abstractions preserve near-reference task success while reducing mean policy input by up to 71\% and 57\%, respectively. The resulting programs are directly inspectable, providing an explicit account of what information is retained, updated, and discarded during interaction.

### 24. Large Language Model Driven Operator Evolution: A Paradigm for Operator Pool Reconstruction and Adaptation

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：LLM 根据候选算子的搜索表现反馈反复重构进化算子并参与主搜索；更新的是算子程序、算子池与搜索参数，没有模型参数训练证据。
- 模型参数/组件边界：进化算子程序、算子池与搜索参数；LLM 参数未训练。
- 训练算法：反馈驱动的 operator reconstruction。
- 反向传播：摘要未报告 LLM 参数训练。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=wqsoOi2vaP
- 官方摘要证据：Evolutionary search performance strongly depends on operator design, while most existing methods remain limited to predefined operators or search behaviors. This paper proposes a feedback-driven operator evolution framework that uses large language models (LLMs) to reconstruct search behaviors within a bounded parameter space. Candidate operators combine random exploration, constraint improvement, objective convergence, and diversity restoration, while offspring generation retains the original GA/DE variation interfaces. Candidate operators are evaluated according to their search performance, which provides feedback for LLM-based reconstruction. Reconstructed candidates are evaluated again before participating in main evolution, while the original operator remains available throughout the search. The framework is integrated into representative constrained multiobjective evolutionary algorithms. Experiments are conducted on the LIR-CMOP and DAS-CMOP benchmarks, together with the real-world problem sets RWMOP and MOOPF. Experimental results show improved overall performance across the tested problems.

### 25. LabBook: Harnessing Experimental History for Efficient LLM-Driven Discovery

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：LabBook 是 discovery agent 维护的外部实验记忆，驱动新程序生成；未训练 agent 模型参数。
- 模型参数/组件边界：程序候选、实验日志与 LabBook 外部记忆。
- 训练算法：单智能体迭代程序发现。
- 反向传播：摘要没有语言模型参数训练。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=JUgAEHSCri
- 官方摘要证据：Evolutionary approaches to LLM-driven discovery often generate new programs
from a small set of selected ancestors. This keeps contexts manageable but can
omit useful evidence from other experiments, whereas including the full
experimental history produces long, redundant contexts. We introduce a
simple, single-agent discovery harness built around \textbf{LabBook}, an
agent-maintained memory that serves two complementary roles: guiding retrieval of relevant
evidence from a complete experimental log and informing the generation of new
solutions. At each iteration, the same agent combines its memory with retrieved
evidence and jointly produces the next program and an updated LabBook. This separates complete history retention from
selective context construction, without requiring an explicit population or
branching search structure. On 49 Frontier-CS problems, LabBook improves the observed quality–cost trade-off over the evaluated evolutionary baselines with two backbones, while remaining competitive across nine additional mathematical, systems, and heuristic-design tasks.

### 26. Is Flat Merging Enough? Evolutionary Search for Tree-Structured Model Merging

- 决定：`keep_unaffected`
- 原分类：`related_prompt_agent`
- 论文特定依据：复核保留：遗传编程搜索 checkpoint 合并树并生成持久合并模型，搜索对象直接决定模型权重组合，不是 LLM 生成外部程序的代理闭环。
- 模型参数/组件边界：合并树拓扑、专家选择/复用及合并后模型。
- 训练算法：genetic programming。
- 反向传播：不需重训；候选专家此前如何训练不是该方法核心。
- 待核实：内部合并算子细节待原文。
- 原始来源：https://openreview.net/forum?id=9Ntfc5vVGp
- 官方摘要证据：Model merging provides an efficient way to integrate independently fine-tuned models without costly retraining or access to their original training data. Most existing methods, however, focus primarily on designing merging operators while combining a fixed set of candidate experts through a typically flat aggregation structure. This leaves a largely overlooked structural design space: how experts should be organized, which experts should participate, and whether experts should be reused throughout the merging process. Through systematic empirical studies, we show that, even when the candidate experts and merging operator are held fixed, changing only the merging structure can substantially affect performance, with markedly different sensitivities across operator families.
Identifying effective configurations in this structural space is challenging, as merging topology, expert selection, and expert reuse jointly define a large discrete and combinatorial search space. We therefore propose EvoTM, an evolutionary framework based on genetic programming for optimizing tree-structured model merging. EvoTM represents a complete merging procedure as a hierarchical tree, where leaves correspond to expert models and internal nodes apply a given merging operator. Structure-aware evolutionary operators jointly explore tree topology and expert composition, naturally accommodating expert selection and reuse within a unified framework.
Experiments across diverse merging operators and both vision and language models show that EvoTM can improve over conventional flat merging in multiple settings. Further analyses reveal operator-dependent structural sensitivities and provide additional insights into how different classes of merging operators respond to tree-structured composition. These results highlight merging structure as a complementary and previously underexplored design dimension of model merging.

### 27. Is Complex Agentic Memory Always Needed? Naive RAG Is Stronger Than We Thought

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：论文比较固定的 Raw-RAG 与复杂 agentic memory；核心状态是检索/记忆系统，不训练语言智能体参数。
- 模型参数/组件边界：原始历史索引、检索与 reranking。
- 训练算法：检索基准与证据分析。
- 反向传播：摘要没有 reader LLM 参数训练。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=MZ7kcOOYa3
- 官方摘要证据：LLM memory is widely used in long-term conversation understanding. Existing agentic memory systems often manage memories through mutation, structural organization, learned retrieval strategies, or other complex operations. Is this complexity always necessary? We study Raw-RAG, a naive RAG baseline using dense retrieval and reranking over raw history to supply evidence to a reader LLM. Across LoCoMo, LongMemEval, MEME, and MemoryAgentBench, Raw-RAG ranks first among the compared memory systems in six of seven benchmark--model settings, outperforming the strongest compared agentic memory system by 0.13--5.53 points in those settings. We then investigate why raw-history retrieval remains competitive in these settings. Evidence analysis shows that its higher coverage of necessary evidence can offset lower utilization. Useful evidence includes both answer values and the relations and dependency paths needed to derive them. Even complete access to transformed memory stores leaves an accuracy gap relative to raw evidence, highlighting the importance of preserving raw information. These findings challenge the need for complex agentic memory systems in the evaluated conversation tasks and establish naive RAG as an essential baseline.

### 28. Improving LLM-driven program evolution with dynamic scope

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：DyScope 让 LLM proposer 在执行反馈下持续改写程序并更新可编辑边界、scope graph 与 transition state；这些均是外部程序/控制状态，未训练模型参数。
- 模型参数/组件边界：候选程序、scope graph、编辑边界与 transition state；LLM 参数未训练。
- 训练算法：动态范围控制的 program evolution。
- 反向传播：未训练 LLM 参数。
- 待核实：与 agent harness 的边界仅凭摘要不能成立，故本次范围不自动排除。
- 原始来源：https://openreview.net/forum?id=MXINrso5QC
- 官方摘要证据：LLM-driven program evolution typically searches over candidate programs while treating the extent that each mutation may change as a fixed generation interface. This creates a structural tension: narrow editing boundaries preserve locality and attribution but can make dependency-spanning improvements unreachable, whereas broad boundaries admit coordinated changes at the cost of a larger proposal space and weaker attribution. Because the appropriate side of this trade-off can change over a lineage, a fixed boundary can become either a reachability ceiling or an unnecessarily broad search interface. We introduce \textbf{DyScope}, which turns the permitted editing boundary into explicit, executable, and verifiable search state. A structural scope graph defines available regions, and each boundary action jointly specifies a target, dependency width, mutation regime, and transition guard. Trajectory evidence can retain productive local scope, widen to dependencies, redirect the target, contract after a broad transition, or invoke recovery. Before generation, the selected boundary changes the context exposed to the proposer and the set of reachable transformations. After generation, an executable transition contract compares the requested boundary with the realized parent--child diff, protects invariant regions, and records whether the transition is admissible. DyScope therefore adapts and verifies program transitions rather than only proposing programs. Feedback supplies evidence for updating boundary state; specific thresholds and rankings instantiate the selection policy rather than define the abstraction. DyScope attains 96.67\%, 99.39\%, and 98.83\% on AIME 2026, HumanEval, and MBPP, respectively. In the matched boundary-policy comparison, dynamic scope reaches 90.18\% versus 82.15\% for fixed scope. These results identify the editing boundary as an adaptive dimension of program search rather than a static implementation choice. By making changes to an evolving system selectable, enforceable, and traceable, DyScope provides a concrete control interface toward auditable recursive self-improvement.

### 29. Hill Sampling for Test-Time Scaling: A Simple and Better Alternative to Repeated Sampling, Evolution, and Training

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：冻结 LLM 反复基于当前最佳程序采样编辑并以验证结果保留候选；核心持久对象是 best-so-far 程序，论文还显示零学习率搜索优于 ES 权重学习。
- 模型参数/组件边界：最佳程序与采样上下文；冻结 LLM 权重不更新。
- 训练算法：hill climbing、重复采样与 ES 对照。
- 反向传播：主方法冻结 LLM；比较的 ES 分支更新模型权重且无需反传。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=m1xdCQou1Z
- 官方摘要证据：Large language models (LLMs) can improve solutions to verifiable scientific and algorithmic problems by spending additional computation at test time. Recent systems achieve strong results with increasingly elaborate evolutionary search harnesses or by updating model parameters during test-time training. We ask how much of this machinery is necessary. We introduce Hill Sampling, a form of hill-climbing optimization that repeatedly samples candidate programs from a frozen LLM, retains the best program found so far, and conditions all subsequent samples on that program. We evaluate the method on circle packing, sums and differences of sets, and Erdos' minimum-overlap problem using three open-weight models. Hill Sampling sets a new state of the art on circle packing among published methods, improves over the AlphaEvolve reference on Erdos' minimum-overlap problem, and achieves strong results on sums and differences of finite sets. The circle-packing and Erdos results require only hours of wall-clock time on eight NVIDIA H100 GPUs. We compare Hill Sampling against what is, to our knowledge, the largest application by parameter count of evolution strategies (ES) to LLM weights at test time. Surprisingly, when evaluating a method by the best program it generates, we find that learning model weights via ES is worse than invoking ES with a learning rate set to zero, i.e., using random weight-space perturbations to search for better models. Moreover, repeated sampling outperforms both ES methods, and Hill Sampling is the strongest of all. These results suggest a simple test-time compute allocation strategy: repeatedly sample edits to the best verified solution found so far before introducing additional complexity, such as adding archives, diversity mechanisms, evolutionary scaffolds, or test-time parameter learning.

### 30. Harmony Harness: Multi-Objective Self-Evolution of Agent Harnesses

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：Harmony Harness 演化 agent harness 机制与基准适配，推理时组合外部工件；无模型参数训练。
- 模型参数/组件边界：agent harness 及 Pareto 解集。
- 训练算法：分解式多目标进化搜索。
- 反向传播：摘要未报告 LLM 参数更新。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=cR0St8qS2n
- 官方摘要证据：Recent work on self-evolving LLM agents treats the agent harness as an optimization target that can be iteratively improved through execution feedback. Existing approaches, however, largely optimize a single objective and evolve the harness as a monolithic artifact, limiting their ability to handle competing goals and to separate transferable design from environment-specific adaptation. We introduce Harmony Harness, a framework for multi-objective, compositional harness evolution. Harmony Harness formulates harness evolution as a multi-objective optimization problem and uses decomposition-based evolutionary search to maintain solutions across different regions of the Pareto frontier, avoiding reliance on a hand-designed structural diversity metric for repository-scale harnesses. In parallel, we introduce factorized evolution operators that separately refine general-purpose harness mechanisms and benchmark-specific adaptations, together with a dynamic composition workflow that integrates them at inference time. Across SecRepoBench and BaxBench, Harmony Harness consistently outperforms strong harness-evolution baselines, with gains exceeding 10\% on both benchmarks. Our results show that explicitly modeling both objective trade-offs and harness structure yields substantially stronger and more transferable agent evolution than existing single-objective, monolithic approaches.

### 31. HapBO: Harnessed α–π Bayesian Optimization via Expert Natural Language Priors

- 决定：`keep_unaffected`
- 原分类：`related_prompt_agent`
- 论文特定依据：复核保留：LLM 至多一次性把自然语言先验编译成确定性 belief function；优化环内没有 LLM 调用或基于反馈的工件自改。
- 模型参数/组件边界：BO belief function 与 acquisition multiplier。
- 训练算法：带有理论保证的 prior-guided BO。
- 反向传播：无语言模型参数训练。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=45k9l8zWbL
- 官方摘要证据：Bayesian Optimization (BO) can be substantially more sample-efficient when informed by prior knowledge about the problem. In practice, however, such knowledge is often available only in natural language, e.g., expert intuitions or documentation, rather than as the explicit probability distribution landscape that prior-guided BO methods may require. Leveraging it effectively demands both an expressive mapping from language to priors and robustness to information that may be misleading. We propose HapBO (Harnessed $\alpha$-$\pi$ Bayesian Optimization), which elicits beliefs once from a human expert, a large language model (LLM), or both, and deterministically compiles a structured specification into a reusable belief function ($\pi: \mathcal{X} \to[0,1]$), with a rich representation not restricted to a Gaussian family. Building on $\alpha$-$\pi$BO, HapBO applies this belief function through a bounded positive multiplier on any nonnegative acquisition, preserving positive acquisition support and requiring no LLM calls during optimization. We prove that, for the Expected Improvement acquisition function (EI), HapBO preserves the standard simple-regret rate up to a bounded factor, even under adversarial beliefs. We evaluate HapBO on 40 HPOBench tasks, a synthetic suite in 6–15 dimensions and two real-world applications: cortical neurostimulation and constrained solar design. HapBO achieves the lowest aggregate HPOBench regret and strong real-world task performance, with zero in-loop token cost. In real-world applications it improves the optimization outcome even at budgets of 8-30 queries, and at a small fraction of the wall-clock and token costs of other LLM-based methods.

### 32. HERA: Harness–Environment Co-Evolution for Reliable Agentic Abstention

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：HERA 演化 harness 与任务环境，并明确最佳 harness 跨模型迁移且无 model-specific optimization。
- 模型参数/组件边界：agent harness、环境变异和任务。
- 训练算法：harness-environment co-evolution。
- 反向传播：没有语言模型参数训练。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=aqyvExE4ST
- 官方摘要证据：Large language model (LLM) agents are increasingly capable of acting in com-
plex tool-use environments, yet they often fail to recognize when tasks are in-
feasible and no valid solution exists. Recent work has formalized this reliabil-
ity gap as the problem of agentic abstention, and existing approaches typically
optimize a model or agent harness against a fixed set of tasks, leading to lim-
ited generalization to unseen failure modes. We introduce HERA, a framework
for harness–environment co-evolution for agentic abstention. HERA consists of
(i) a pipeline to automatically construct verifiable pairs of feasible and infeasible
tasks by applying controlled environment mutations that transform solvable tasks
into cases requiring abstention, and (ii) a co-evolution procedure in which perfor-
mance failures on previous tasks are used to drive harness adaptation and generate
new execution environments and tasks geared towards previous weaknesses. On
held-out evaluation tasks, an evolved harness from HERA improves abstention
accuracy from 61.7% to 83.3% while maintaining feasible task performance, out-
performing all compared methods. The resulting best harness transfers across 19
other LLMs, improving abstention accuracy by 15.3 percentage points on average
without any model-specific optimization, and enabling smaller models to match
the performance of more powerful models at an estimated 85% lower cost.

### 33. HEMO: Harness Self-Evolution for Multi-Objective Combinatorial Optimization

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：HEMO 更新的是 AOD harness 模块、持久 memory filesystem 和算子搜索编排，不是语言模型参数。
- 模型参数/组件边界：harness state、搜索算子和外部记忆。
- 训练算法：UCB 调度的模块级 self-evolution。
- 反向传播：摘要没有 LLM 参数更新。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=FxMC3n6AdZ
- 官方摘要证据：Automatic operator design (AOD) has increasingly adopted large language models (LLMs) to generate problem-specific search and variation operators for multi-objective combinatorial optimization (MOCO). Yet most methods evolve the operators while leaving the process that discovers them fixed. This limits adaptation as new Pareto trade-offs and operator interactions change where and how the search should proceed. We introduce **HEMO**, which makes the AOD harness itself a self-evolving optimization target. HEMO maintains a persistent harness state and updates one module at a time, revising the logic that determines which experience to retrieve, which operators to improve, which parents to select, and how to formulate the orchestration of search steps. Downstream solution quality and runtime guide these updates, while a discounted UCB scheduler directs adaptation toward promising modules as their utility changes. A persistent memory filesystem preserves candidate outcomes and diagnostic feedback across harness states, enabling successive states to build on accumulated optimization experience. Experiments across eight MOCO tasks and two structurally distinct evolutionary backbones demonstrate strong performance against conventional evolutionary, neural, and LLM-based AOD baselines, together with effective transfer to related tasks. HEMO extends automatic operator design beyond evolving individual operators to improving the search process that discovers them.

### 34. Geometry of Large Language Model Controllability

- 决定：`defer_prompt_core`
- 原分类：`related_prompt_agent`
- 论文特定依据：PGDE 的核心是用输出空间 pullback 距离筛选离散提示词跳转。
- 模型参数/组件边界：离散提示词候选。
- 训练算法：gradient-free pullback-guided discrete exploration。
- 反向传播：不更新模型参数；严格梯度属性仅针对离散搜索。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=eVAaz2QSye
- 官方摘要证据：Prompt engineering remains a brittle, heuristic practice governed by a fundamental *Controllability Dilemma*: extreme vulnerability to minor lexical variations (*Paraphrase Sensitivity*) alongside a persistent propensity to ignore explicit structural instructions (*Instruction Neglect*). In this paper, we reveal that this dilemma originates from a severe topological mismatch between the superficial prompt text space and the model's true operational Hilbert output space, invalidating the implicit isometric assumption of current prompt optimizers. To resolve this, we formalize prompting as the dynamic selection of a function within a continuous Hilbert space, equipping the prompt manifold with a pullback Riemannian metric tensor induced by functional output divergence over task distributions. Through this geometric lens, we mathematically prove that multi-head attention saturation induces a topological partition of the prompt manifold, driving Instruction Neglect via rank-deficient $\epsilon$-null foliations and Paraphrase Sensitivity via unbounded transversal sectional curvature across deep Transformer layers. Operationalizing these theoretical insights, we introduce **Pullback-Guided Discrete Exploration (PGDE)**, a gradient-free algorithm that leverages empirical pullback distances as a zero-order geometric filter to dynamically enforce distant functional jumps and local variance bounds. Empirical evaluations across 7B to 70B parameter models demonstrate that PGDE significantly outperforms state-of-the-art baselines on strict instruction following (IFEval, +8.6% absolute accuracy gain on Llama-3-8B) and mathematical reasoning (GSM8K), while reducing search wall-clock latency by over 50% by early-rejecting functionally inert proposals and suppressing output variance under paraphrasing by 82%.

### 35. GP-Harness: Sequential Bayesian–Evolutionary Optimisation of LLM Harnesses

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：GP-Harness 围绕 fixed model 演化、重组并选择 harness。
- 模型参数/组件边界：agent harness 图。
- 训练算法：Gaussian-process Bayesian optimization 加 evolutionary generation。
- 反向传播：任务模型明确固定。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=0T5xZWy3I2
- 官方摘要证据：Large language model agents rely on harnesses that organise planning,
tool use, verification, and failure recovery around a fixed model.
Automatic harness search can generate more candidates than can be
evaluated on long-horizon tasks, making the choice of which candidates
to evaluate a central challenge.
We introduce \methodname{}, which combines evolutionary candidate
generation with Bayesian optimisation to guide this choice.
Starting from eight adapted open-source harnesses, programmatic
mutation and recombination generate candidate pools.
A Gaussian-process surrogate over graph features uses previous
evaluations to predict candidate fitness and uncertainty, and
expected improvement selects one candidate for evaluation in each
round.
Within each benchmark, all harnesses use a shared executor, with
the task model, tool interfaces, evaluator, and per-task execution
limits held fixed.
With 20 new-candidate evaluations per run, \methodname{} achieves
64.6\% mean success on a held-out 24-task Terminal-Bench~2.0 subset
and a 43.3\% mean resolved rate on the official 300-instance
SWE-bench Lite test set across six search seeds, including runs
that fall back to an initial harness.
These results improve on the initial harness selected by its
performance on the search tasks by 10.4 and 8.0 percentage points,
respectively, and on budget-matched surrogate-free evolution
by 4.9 and 4.6 points.
Online ablations favour graph features over dimension-matched
text features and uncertainty-aware acquisition over
posterior-mean selection.

### 36. FrugalEvo: Towards Cost-Aware LLM-Guided Program Evolution

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：强/弱 LLM 在评估反馈下探索策略、实现并迭代精炼代码，harness 维护种群与缓存；持久更新的是程序解、种群和搜索状态，没有模型参数训练证据。
- 模型参数/组件边界：程序、种群、策略文本与缓存状态；所调用 LLM 未训练。
- 训练算法：成本感知程序演化。
- 反向传播：摘要未报告 LLM 参数更新。
- 待核实：虽比较 multi-agent 方法，但自身核心不是 agent 模型训练。
- 原始来源：https://openreview.net/forum?id=QT9UN9GxWQ
- 官方摘要证据：LLM-guided evolutionary methods, such as AlphaEvolve, have emerged as powerful approaches for challenging computational optimization problems, such as circle packing. However, prior work typically optimizes performance gain over a fixed number of iterations. We argue that practical optimization should maximize gain per unit cost. To this end, we propose FrugalEvo, a cost-aware evolutionary framework where a stronger, higher-cost LLM explores solution strategies, and a cheaper LLM implements them and iteratively refines the resulting code. We also design a cache-efficient evolution process, where our harness and prompts maximize the sharing of prefixes across different evolution steps, to improve cache reuse. To measure solution quality throughout a fixed cost budget, we introduce Budget-Aware Area Under the Curve (BA-AUC), defined as the area under the best-so-far evaluation score curve over cumulative LLM cost, up to the budget. Across 10 mathematical and systems optimization tasks, FrugalEvo matches or surpasses state-of-the-art baselines, including OpenEvolve, ShinkaEvolve, AdaEvolve, and EvoX, in final solution quality and achieves higher BA-AUC on 9 tasks. It also achieves higher average performance than these baselines on 10 algorithmic optimization tasks from ALE-Bench-Lite. Notably, on circle packing, FrugalEvo achieves new state-of-the-art performance with GPT-5.6 Terra and Luna for only 1.68 USD and with GLM-5.3 and its Flash variant for only 0.55 USD, matching or surpassing all baselines, including multi-agent methods such as CORAL and SwarmResearch, which cost approximately 50 USD on average.

### 37. From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails

- 决定：`defer_prompt_core`
- 原分类：`related_prompt_agent`
- 论文特定依据：攻击核心是搜索最大化 guardrail 推理长度的自然语言 payload，属于对输入提示的优化。
- 模型参数/组件边界：攻击 payload/注入文本。
- 训练算法：beam search 与结构化 mutation。
- 反向传播：未训练目标 guardrail 或 proposer 模型参数。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=2ieHfp0vhO
- 官方摘要证据：LLM-based guardrails have emerged as an effective defense against prompt injection and jailbreak attacks in autonomous agents. However, we reveal that the very reasoning and task-following capabilities enabling this protection introduce a novel vulnerability: attackers can inject crafted data to trap the guardrail in extended reasoning loops, effectuating a systematic denial-of-service (DoS) attack. To systematically expose this threat, we design a beam-search optimization framework that crafts natural-language payloads to maximize guardrail reasoning length, utilizing an LLM proposer guided by a strategy bank. Based on the observation of guardrail's schema-following nature, we also provide another attack framework driven by mechanism-aware structural mutations with less computational load. The attack efficacy is evaluated in two parts. First, standalone evaluations cover 10 target guardrail models across safety templates and agent benchmarks. Payloads optimized on an open-source surrogate successfully transfer to leading model backbones including Claude, GPT and Gemini, achieving a 13--63$\times$ length amplification. Second, evaluations in web, code, computer-use and multi-agent deployments show up to 148$\times$ guardrail-latency amplification. In a shared-guardrail supervisor experiment with sequential access, attacked workers may reduce throughput by 23.3\% and delayed benign workers by 113--146 seconds. These findings motivate explicit reasoning-cost bounds and reliable verdict recovery.

### 38. From Operation to Interface: Where Harness Changes Enter a Fixed Model’s Tool Calls

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：研究固定模型下不同 harness 对 tool-call 操作/接口的影响，明确讨论不触碰权重的 harness edits。
- 模型参数/组件边界：prompts、tools、middleware 与调用历史。
- 训练算法：干预与表征分析，不是模型训练。
- 反向传播：模型固定；activation steering 实验也未建立参数更新。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=DSP0z2ufLg
- 官方摘要证据：Procedures that improve a coding agent without touching its weights edit its prompts, tools and middleware and keep the edits that raise task success, but task success alone does not reveal which aspects of tool use an edit changes. We study gpt-oss-20b under six harnesses on SWE-bench Verified and separate each classifiable tool-call attempt into an operation category (such as search or read) and an invocation interface (shell or API-style). In TOOLS, the layer-20 state at the first generated-token position adds +11.8 accuracy points for the operation but +1.0 for the interface beyond a structured call-history baseline, and an operation decoder transfers across most harnesses and across interfaces. At file-read-matched anchors, TOOLS and SEED differ by +45.8 points in API share, compared with 4.4 points of total variation in the operation distribution, which does not exceed its permutation null. Rewriting past reads between shell and API forms shifts API share by +40.8 and −36.2 points, with smaller operation shifts of 8.6 and 2.5 points, while replacing search hits with no matches shifts the operation by 29.0 points and API share by −6.5. The frozen operation decoder responds most strongly to this result rewrite, but pushing the state along the decoder’s direction changes the decoder readout without establishing targeted control of the next operation. These findings separate changes in operation choice from history-sensitive changes in invocation interface.

### 39. From Experience to Knowledge: Algorithm Design for Black-Box Optimization with Large Language Models

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：FETK 用 LLM 搜索 EA 架构，把修改与性能结果蒸馏为自然语言知识，并在验证问题上选择知识更新；训练/持久对象是算法代码与文本知识，不是模型参数。
- 模型参数/组件边界：EA 架构、设计经验与自然语言指导；LLM 参数未训练。
- 训练算法：三阶段经验收集、知识学习、复用。
- 反向传播：摘要未训练 LLM 参数。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=QDfuYx1Rp8
- 官方摘要证据：Large language models (LLMs) have shown promise in automated evolutionary algorithm (EA) design through their ability to generate algorithmic code and iteratively refine it based on performance feedback.
However, many existing methods rely on iterative search to design algorithms for target problems, requiring repeated LLM calls and candidate evaluations. Moreover, design experience obtained on a target problem may not provide guidance for algorithm design on subsequent problems. To address these limitations, we propose FETK, a three-stage framework that distills problem algorithm design experience into knowledge, enabling an EA architecture to be generated for each subsequent problem with a single LLM call. First, the Experience Collection module collects problem design experience by searching EA architectures on training problems and recording landscape representations, architectural modifications, and performance outcomes. Second, the Knowledge Learning module learns design knowledge by distilling experience across training problems into natural-language guidance and evaluating candidate knowledge updates on validation problems before retaining them. Finally, the Knowledge Reuse module combines the learned knowledge with the landscape representation of each test problem to generate an EA architecture with a single LLM call.
Experiments on BBOB and MA-BBOB problems demonstrate competitive performance compared with manually designed EA methods, learning-based design EA methods, and  LLM-based design EA methods.
\href{https://anonymous.4open.science/r/fetk-DE22}

### 40. FedPOB: Sample-efficient Federated Prompt Optimization via Bandits

- 决定：`defer_prompt_core`
- 原分类：`related_prompt_agent`
- 论文特定依据：FedPOB 的明确目标是联邦黑盒 prompt optimization。
- 模型参数/组件边界：提示词配置以及 bandit 统计参数。
- 训练算法：Linear UCB / federated dueling bandits。
- 反向传播：不更新被调用 LLM 权重；“sharing model parameters”指 bandit 模型参数。
- 待核实：需避免将 bandit 参数误记为语言模型参数。
- 原始来源：https://openreview.net/forum?id=psls0Sg5LI
- 官方摘要证据：The performance of large language models (LLMs) is highly sensitive to the input prompt, making prompt optimization a critical task. However, real-world application is hindered by three major challenges: (1) the black-box nature of powerful proprietary LLMs, (2) the need for high sample efficiency due to query costs, and (3) the desire for privacy-preserving collaboration among multiple users. To address these challenges simultaneously, we introduce a novel framework for sample-efficient federated prompt optimization based on multi-armed bandits (MABs). The MAB framework is uniquely suited for this problem as it is (1) inherently a black-box optimization method, (2) practically sample-efficient, and (3) enables collaborative learning with theoretically guaranteed benefit from more participating agents. We first propose the Federated Prompt Optimization via Bandits (FedPOB) algorithm, a federated variant of the Linear UCB algorithm, where agents collaborate by sharing model parameters instead of raw data. We then extend our approach to the practical setting of comparative user feedback by introducing FedPOB with Preference Feedback (FedPOB-Pref), an efficient algorithm based on federated dueling bandits. Extensive experiments demonstrate that both FedPOB and FedPOB-Pref significantly outperform existing baselines and that their performance consistently improves as more agents participate in the collaboration, validating the effectiveness of our federated approach.

### 41. Evolutionary Adversarial Attacks Meet LLMs: Semantic-aware Adaptive Optimization Against Vision-Language Pre-trained Models

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：LEA 让 LLM 读取演化搜索状态并自适应选择语义区域、算子和搜索参数；更新的是对抗扰动与外部搜索控制状态，未训练 LLM/VLM 参数。
- 模型参数/组件边界：图像扰动、语义区域先验、算子选择与搜索参数；控制 LLM 和受害 VLM 均无参数训练证据。
- 训练算法：异构 evolutionary operator pool。
- 反向传播：受害模型黑盒且无梯度；未训练 LLM 控制器。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=u82Fkl3jwy
- 官方摘要证据：Targeted attacks against black-box vision-language models remain challenging because transfer-based optimization must simultaneously achieve precise semantic steering, cross-model transferability, and bounded image perturbations without access to victim gradients or internal representations. Although evolutionary algorithms provide a natural gradient-free solution, their search is typically semantically blind and relies on fixed optimization strategies. We introduce LEA, an LLM-driven evolutionary adversarial framework that turns conventional evolutionary search into a semantic-aware adaptive optimization process. LEA first constructs original and target semantic anchors to explicitly characterize the desired semantic transition. More importantly, rather than directly generating adversarial perturbations, LEA employs the LLM as a high-level controller that interprets the evolving search state and adaptively coordinates semantic region priors, operator selection, and search parameters. A heterogeneous evolutionary operator pool then performs the low-level gradient-free perturbation search, enabling complementary global exploration and local refinement. Experiments on SMALLCAP, ViECap, and LLaVA-13B demonstrate consistent improvements over representative black-box and transfer-based baselines. On SMALLCAP, LEA improves Target ASR from 39.7% to 53.2% over the strongest targeted baseline while increasing the average CLIP score from 63.78 to 68.76. These results show that high-level LLM reasoning can effectively control evolutionary adversarial search and expose the vulnerability of vision-language systems to targeted semantic manipulation under transfer-based black-box settings.

### 42. EvoMem: Memory-Augmented Evolution for Code Optimization

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：LLM 驱动程序搜索把成功 mutation 提炼为带出处的文本建议，并跨 run 检索以继续改写代码；持久更新的是程序和外部记忆，不是模型参数。
- 模型参数/组件边界：候选程序、mutation advice、provenance 与检索记忆；LLM 参数未训练。
- 训练算法：memory-augmented evolutionary program search。
- 反向传播：未训练 LLM 参数。
- 待核实：若未来把该系统界定为 agent memory，需再按范围复核。
- 原始来源：https://openreview.net/forum?id=nrx0FyO4my
- 官方摘要证据：Successful mutation strategies in evolutionary code search may contain reusable knowledge that is useful beyond a single run, and in some cases may transfer across related tasks and domains. However, existing LLM-driven evolutionary frameworks largely discard such knowledge, repeatedly rediscovering similar ideas and limiting opportunities for cross-run and cross-task learning. We introduce EvoMem, a mechanism for transferring mutation knowledge across LLM-based evolutionary program-search runs. EvoMem converts successful mutation events into structured, task-aware advice for future runs. It operates in two phases: after each run, it extracts and stores promising ideas with provenance, and during subsequent evolution, it retrieves a small set of relevant instructions based on the current task and program context to guide mutation. Across geometric optimization, multi-hop question answering, GPU kernel optimization, and related benchmarks, our experiments show positive average improvements in target metrics or search speed for most evaluated settings, while also revealing variability across tasks. Overall, EvoMem provides evidence that persistent memory can reduce some redundant exploration and improve the reuse and adaptation of successful strategies in LLM-driven evolutionary search.

### 43. EvoG: A Modular Framework for Evolutionary Optimization of Agentic Workflows

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：EvoG 明确优化 agentic workflow 图；四组件和共享历史更新候选工作流，无模型参数训练证据。
- 模型参数/组件边界：agent workflow、候选 lineage 和执行历史。
- 训练算法：模块化 evolutionary optimization。
- 反向传播：摘要没有 LLM 参数更新。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=0MiTxo4j9d
- 官方摘要证据：Designing effective agentic workflows for large language model (LLM) applications requires repeated, costly revision and evaluation. Evolutionary optimization can automate this process and existing methods have instantiated specific combinations of candidate selection, revision, example sampling, and evaluation strategies. Making these choices explicit and composable would help users construct and compare configurations suited to their task objectives and budget. Therefore, we introduce EvoG (Evolve on Graph), a modular framework for composing evolution strategies within a shared optimization loop. EvoG separates evolution into four components: a Selector that chooses parent candidates; a Generator that produces revisions; a Sampler that selects evaluation examples; and an Evaluator that assesses candidates. A shared history links candidate lineage, per-example outcomes, and execution traces to inform subsequent iterations. We evaluate EvoG on HotpotQA, MuSiQue-Ans, BigCodeBench-Hard, ScienceWorld, and WebShop. It achieves the highest mean test scores among the evaluated methods on four of five benchmarks, improving over the strongest baseline by 1.10 points on HotpotQA, 3.76 points on MuSiQue-Ans, 7.00 points on ScienceWorld, and 4.89 points on WebShop. On BigCodeBench-Hard, the best EvoG configuration achieves 35.33 points versus AgentSquare's 37.00 points, at approximately one-eighth its search cost and half its inference cost. For reproducibility, we release our code at https://anonymous.4open.science/r/EvoG-D6C2/

### 44. EvoDisco: Strategy Discovery for Self-Evolving Agent Memory

- 决定：`defer_agent_training_unverified`
- 原分类：`related_prompt_agent`
- 论文特定依据：EvoDisco 声称 learnable policy 按双层 fitness 更新，但摘要未说明该 policy 是参数化模型还是外部规则/状态，不能认定训练语言/策略模型参数。
- 模型参数/组件边界：记忆操作选择/实例化 policy 与 memory state。
- 训练算法：双层 fitness 的在线 policy update。
- 反向传播：是否使用反向传播、ES 或规则更新均未说明。
- 待核实：需核实 policy 表示、可训练参数、更新算法及其是否属于 agent policy model。
- 原始来源：https://openreview.net/forum?id=FmXVyNi3hK
- 官方摘要证据：Large language model agents accumulate experience in memory, and how that memory evolves during interaction is as important as what it stores. Recent methods update memory online, yet both the operators that transform memory and the rules that select them remain fixed by design. We propose EvoDisco, which formulates agent memory evolution as evolutionary strategy discovery: the agent must discover which operator to apply, when to apply it, and how to instantiate it, rather than rewriting memory under a static operator schedule. A learnable policy conditions on the current memory state and recent task history, then selects and instantiates one of four semantic operators---Abstract, Refine, Bridge, and Reframe---which respectively compress related memories, decompose overloaded entries, connect weakly linked experiences, and reorganize retrieved reasoning chains. The policy is updated with a bi-level fitness. An inner signal scores each transformation using a retrieval-quality improvement regularized by memory complexity. An outer signal scores strategic efficacy over a window of past decisions, combining historical operator-utility regret, utility-prediction error, and selection diversity. Under a one-pass online plus frozen-transfer protocol on ALFWorld, WebShop, and LifelongAgentBench (OS and DB), EvoDisco improves over strong memory baselines including MemP and MemRL. The largest gains are on ALFWorld ($+8.8$ online / $+12.9$ frozen-transfer points over MemP; $+16.4$ / $+17.9$ over MemRL). Ablations attribute these gains to both fitness levels and the operator library.

### 45. Escaping Alignment: A Physical Trap Model of Best-of-N Jailbreaking

- 决定：`defer_prompt_core`
- 原分类：`related_prompt_agent`
- 论文特定依据：BoN jailbreak 的核心对象是 unsafe prompt 的随机 augmentation 与 completion 采样。
- 模型参数/组件边界：攻击提示词变体。
- 训练算法：Best-of-N 随机增强采样及物理 barrier 建模。
- 反向传播：不更新目标模型参数。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=x7eAMFALle
- 官方摘要证据：Best-of-$N$ jailbreaking (BoN) bypasses safeguards of aligned models by drawing $N$ independent augmentations of an unsafe prompt and sampling $M$ completions of each. Previous works have shown that the attack success rate (ASR) seems to follow a power-law in $N$, which we challenge. The exponent drifts with $N$, with an exponential crossover which is a finite-size artifact of the adversarial dataset. Little work has been done to explore the entire two-budget ($N, M$) attack surface as well as its dependence on the generation temperature $T$. We introduce a simple barrier model where each prompt has a baseline safety level and each augmentation a random thermally activated barrier. Then four numbers, each backed by an interpretable safety mechanism, determine the entire ($N, M$) attack surface. They extrapolate predictions from $N \leq 100$ to $N = 10^4$, collapse five distinct models on the same scaling function and predict ASR at different temperatures from the one they were fitted at.

### 46. Elicitation or Expansion? Demystifying Gains from Agent Harness Optimization

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：论文明确研究不更新模型权重的 harness optimization，并分析其 elicitation/expansion 效应。
- 模型参数/组件边界：context、tool use 与 execution workflow。
- 训练算法：harness 前后对照和 pass@k 分析。
- 反向传播：明确不更新模型权重。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=bSBejKazyx
- 官方摘要证据：Recent studies in harness optimization have shown substantial performance gains in language model agents without updating model weights. A well-designed harness more effectively leverages the underlying model's capabilities by shaping context, tool use, and execution workflows. However, naïve success rates alone do not fully characterize whether optimized harness yields more reliable success on tasks already within reach (*elicitation*) or a broader range of solvable tasks (*expansion*). This distinction is crucial for recursive self-improvement and evolutionary search, as expansion may provide a broader range of successful experiences to push the capability boundaries. Despite the growing significance, this distinction remains underexplored in harness optimization. We conduct a systematic analysis to study the effect of gains from harness optimization. Building on pass@k analyses in the reinforcement learning (RL) literature that compare models before and after RL training, we compare optimized harnesses with their pre-optimization counterparts. Specifically, we assess changes in reachable task coverage, compare harness optimization with model scaling and increased inference-time compute, and examine how gains vary with task difficulty. Across static prediction and dynamic tasks, we find that pass@1 advantages of harness over stronger interventions can reverse at larger attempt budgets and aggregate gains conceal shortfalls on hard tasks, underscoring the need for a fine-grained diagnosis.

### 47. EVOUNDO: RECOVERABILITY-CONSTRAINED SELF-EVOLUTION FOR LLM AGENT HARNESSES

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：EvoUndo 的对象是 prompts、tools、middleware、resources 和 harness 自修改及其可恢复性，不是模型参数。
- 模型参数/组件边界：agent harness 自修改与 recovery calculus。
- 训练算法：反事实状态下的合成、诊断和验证。
- 反向传播：摘要未报告语言模型参数训练。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=IFmd4fBKfS
- 官方摘要证据：LLM agents increasingly modify their own prompts, tools, middleware, resources, and
execution harnesses at runtime. Such self-evolution can improve capability, but a successful mutation may leave persistent effects that cannot be safely reversed in states
different from the one in which it was created. We introduce EvoUndo, a framework for representing, synthesizing, diagnosing, and independently verifying recoverability of model-generated self-modifications across counterfactual states. Across
600 unseen one-shot self-evolution tasks, we identify 197 capability-improving mutations that fail recoverability verification. Under the original recovery representation,
conventional repair strategies recover 0/197 of these natural failures. Deterministic
oracle analysis recovers 48/197 under the original recovery language L0, while the extended recovery calculus increases empirical oracle recovery to 191/197. A protocollocked 2×2 grounding-by-expressivity intervention then separates two bottlenecks: exact state-address grounding increases successful recovery from 0/48 to 38/48 (79.2%)
when the original language is sufficient, while extending the recovery language enables
recovery on 142/143 (99.3%) failures in the oracle-defined S1 stratum. On the primary gpt-oss-120b backbone, adding exact-address diagnostics to the richer language
reduces recovery to 133/143 (93.0%); a Qwen3.8-27B replication preserves the grounding and expressivity effects but not this negative interaction, indicating that the latter
is model-dependent. These results indicate that reliable agent self-evolution requires
co-designing verification, state grounding, witness semantics, and recovery-language
expressivity rather than relying on iterative prompting alone.

### 48. EEVEE: Post-Deployment Prompt Learning across Heterogeneous Tasks

- 决定：`defer_prompt_core`
- 原分类：`related_prompt_agent`
- 论文特定依据：EEVEE 明确联合演化 router 与 prompt configurations，核心仍是 post-deployment prompt learning。
- 模型参数/组件边界：提示词配置与外部 router。
- 训练算法：router-prompt co-evolution。
- 反向传播：摘要未证明更新 LLM 权重；router 是否为参数模型及训练方式未说明，但不改变 prompt 核心暂缓决定。
- 待核实：需核实 router 的表示与持久参数。
- 原始来源：https://openreview.net/forum?id=tHX0Ublg85
- 官方摘要证据：Prompt learning has become an important approach to adapting large language models to downstream tasks. However, some existing methods require access to model internals, while others are largely designed for single-dataset settings, limiting their practical applicability. In real-world deployments, models are often accessible only as black boxes, while incoming queries form heterogeneous streams drawn from multiple datasets, domains, and task distributions. We therefore propose EEVEE, a multi-dataset post-deployment prompt learning framework for LLM agents, enabling prompt learning under heterogeneous task streams. To mitigate cross-dataset interference, EEVEE introduces a router that partitions incoming inputs into task clusters and assigns them to suitable prompt configurations. This design is optimized via a router-prompt co-evolution strategy, which employs interleaved router and prompt learning phases to address their mutual dependency. Experiments across multiple datasets demonstrate that the framework improves robustness under heterogeneous data streams while maintaining single-benchmark learning capability and efficiency. Specifically, EEVEE improves average multi-benchmark scores by 10.38 and 24.32 points over Qwen3-4B-Instruct and DeepSeek-V3.2, surpassing SOTA methods GEPA and ACE by up to 37.2% and 48.2%.

### 49. E$^{2}$MEND: Evidence-guided Evolution for Memory Enhancement via Bottleneck Diagnosis

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：E2MEND 变异和回滚的是 versioned memory-strategy artifacts，runtime 锁定；未训练语言智能体模型。
- 模型参数/组件边界：记忆提取、检索、typed state 等策略工件。
- 训练算法：诊断驱动的 bounded evolution。
- 反向传播：摘要没有模型参数训练。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=EcMoDY6gpg
- 官方摘要证据：Long-term memory failures are heterogeneous: evidence may be lost, unretrieved, insufficiently structured, or available while the answer model still fails; a uniform update can target the wrong bottleneck and introduce regressions. We present E$^{2}$MEND, a diagnosis-guided framework for bounded memory-strategy evolution: it estimates the bottleneck, mutates versioned strategy artifacts through a bounded LLM evolver under a locked runtime, and adopts candidates via paired evaluation, negative evidence, and rollback. It matches failure modes to bounded edits---extraction or provenance for ingestion gaps, support selection for retrieval gaps, typed state for state construction, and no memory mutation for answer-model limitations. On a fixed 1,540-question LoCoMo slice, a staged trajectory raises accuracy from 0.756 to 0.947 (final paired checkpoint: 16 repairs, 0 regressions); on MemBench, matched strategies yield a descriptive $0.770\to0.863$. We frame these as diagnostic and strategy claims on fixed slices, not public-task superiority.

### 50. Does Prompt Sensitivity Improve Cross-Family Degradation Prediction?

- 决定：`defer_prompt_core`
- 原分类：`related_prompt_agent`
- 论文特定依据：论文以十种 instruction wording 的 prompt sensitivity 为核心变量，研究其跨模型家族预测价值；虽然不优化提示词，仍属于提示词核心研究。
- 模型参数/组件边界：无持久更新；只计算不同提示措辞下的统计特征。
- 训练算法：交叉验证和 permutation reference。
- 反向传播：无模型训练。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=uVn7IU6iPN
- 官方摘要证据：Models whose answers barely change when instructions are reworded might also hold their accuracy when the data change. Does prompt sensitivity predict how much accuracy a new model family will lose, beyond source accuracy? We test two source-side features, accuracy dispersion and label-free disagreement across ten wordings, on fifteen open-weight models, three classification tasks and seven natural shifts. Both lower held-out error under cross-validation over five development families. Under one frozen fit, disagreement raises error by 6% in a first held-out cohort and lowers it by 35% and 30% in a second and a third, of three and two families; dispersion has the same signs. No cohort reaches the registered level, and no test pools them. Disagreement's falls in the second and third cohorts exceed a within-source permutation reference, but in development the invalid-response rate alone predicts degradation nearly as well, and the first cohort's rise reverses when one training family is dropped. The evidence does not establish that the gain transfers to a new family, nor that sensitivity carries no information about shift.

### 51. Do Vision-Language Models Use the Regions They Cite? A Step-Specific Intervention Test

- 决定：`keep_unaffected`
- 原分类：`related_prompt_agent`
- 论文特定依据：复核保留：在固定推理步骤上做区域扰动和似然测量，属于 VLM 内部证据使用分析，不优化提示或外部代理状态。
- 模型参数/组件边界：无；固定 reasoning steps 上进行区域扰动。
- 训练算法：似然变化与成对顺序统计检验。
- 反向传播：无模型参数训练。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=JwUvLVBgt7
- 官方摘要证据：Vision-language models increasingly attach a bounding box to each reasoning step as the visual evidence for that step. Localization metrics measure whether such boxes match reference regions; they do not test whether the step is selectively sensitive to the region it cites. We introduce a step-specific intervention test that requires no region annotations: perturb each cited region in turn, record the change in every fixed step's mean per-token log-likelihood, and compare a step's sensitivity to its own region with its sensitivity to distinct regions cited by other steps of the same chain. Because every pair of distinct regions is compared in both directions, the expected own-region ordering probability is at most 50% under an additive step-and-region sensitivity model with row-exchangeable residuals, so a confidence interval entirely above 50% is evidence against that joint null. For Qwen3-VL-4B the own-region ordering probability is about 61% in each of three image-disjoint GQA cohorts and 72% on A-OKVQA. On the largest GQA cohort, every preregistered change of scoring context and intervention operator (removing the preceding steps, replacing blur with within-box patch permutation, or both) keeps the interval above 50% (lowest point estimate 58%). On a held-out cohort, under a protocol specified in advance, we regenerate each current step with the preceding steps held fixed. The fixed-text margin predicts the relative content change caused by blurring the step's own rather than a sibling step's region (Spearman's ρ = 0.504, 95% CI [0.402, 0.600]). The advantage is strong for GLM-4.6V-Flash on two image-disjoint cohorts, weak and cohort-variable for InternVL3.5-4B, and partial throughout: about 40% of Qwen3-VL-4B's comparisons in the three fixed-text GQA cohorts favor another step's region. A cited region is a testable claim about evidence use, not proof of it.

### 52. Direction-Indexed Evolutionary Red-Teaming of Large Language Models

- 决定：`defer_prompt_core`
- 原分类：`related_prompt_agent`
- 论文特定依据：DIER 演化 roles、pretexts、personas 等 jailbreak framings，本质是攻击提示工件搜索。
- 模型参数/组件边界：攻击 framing/library。
- 训练算法：response-direction indexed evolutionary ranking。
- 反向传播：方向不进入模型激活且不更新目标模型参数。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=TWCBAEspBn
- 官方摘要证据：We introduce Direction-Indexed Evolutionary Red-Teaming (DIER), a black-box jailbreak method that learns its search coordinate from a target language model's own responses rather than from the text of the attack. A search that accumulates reusable framings, such as roles, pretexts and personas, has to decide which are close enough to recombine, and text does not carry that decision: across 21 target models, how a framing is worded says little about what it does, and a whole response is dominated by what was asked rather than by how it was asked. After each attempt DIER takes the displacement of the response from the request in a fixed sentence-embedding space and projects out the direction every response to that request shares; what survives is a signature of the tactic alone. That signature is cheap to measure and not predictable from a framing's text, so it can be read only after an attempt and used only to rank the library the search has already built. That ranking is the coordinate's only causal path into an attack: the direction never enters a prompt, is never decoded into words, and never touches the target's activations. On the 400-behavior HarmBench text benchmark at 32 target queries per behavior, DIER attacks at the state of the art: a mean attack success rate of 86.4 across the 16 targets with published baselines against 55.2 for the strongest attack in the HarmBench suite, level on the mean with the strongest prior strategy-library agent and ahead of it on all five targets where that agent stays below 90 percent. Replacing the ranking with a uniform random draw from the same library, with the attacker model, the library and the budget untouched, costs 13.5 to 39.0 points, placing the effect in the measured coordinate rather than in the language model that writes the attacks.

### 53. Designing and Evolving Multi-Agent Systems via a Typed Intermediate Representation

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：meta-agent 生成 typed IR 来设计 MAS；经验演化 refine design policy，但摘要明确不更新任何模型参数。
- 模型参数/组件边界：MAS typed IR、角色/目标/instructions 与外部经验。
- 训练算法：experience-guided evolutionary design。
- 反向传播：摘要明确 updating no model parameters。
- 待核实：“design policy”是外部生成策略，不能据词面当作参数化 policy model。
- 原始来源：https://openreview.net/forum?id=6YccHf9cEN
- 官方摘要证据：Automatic design of LLM-based multi-agent systems (MAS) has largely taken one of two forms: a meta-agent writes each system as free-form code, which is expressive but hard to validate and entangles design quality with coding ability; or a search over prebuilt operators, which is reliable but usually settles for one design per task family. We take a middle route in which the meta-agent designs and an engine implements. For each query the meta-agent emits a typed intermediate representation (IR) that composes agents from interaction primitives and specifies each agent by role, objective, and instructions. A rule-based compiler deterministically lowers each valid IR into an executable MAS, making every design statically checkable, executor-independent, and fully traceable from architecture to outcome. An experience-guided evolutionary loop then mines successful strategies and failure lessons from development traces to refine the meta-agent's design policy, updating no model parameters and adding no test-time cost. With a lightweight open-source executor, our system attains the best average accuracy across four benchmarks spanning math and coding, exceeding the strongest of eight baselines by 9.3 points, and evolution improves every benchmark. Because execution is fully traced, gains and losses are attributable: evolution repairs coordination while residual errors localize to executor capability, making failures of automatically designed MAS inspectable.

### 54. DebtMerge: Long-Horizon Expert Evolution for Continual Model Merging

- 决定：`keep_unaffected`
- 原分类：`related_prompt_agent`
- 论文特定依据：复核保留：进化搜索优化专家结构与 merge recipe，持久结果是合并模型/专家库，属于非智能体模型合并。
- 模型参数/组件边界：专家选择、merge recipe、结构和集成几何。
- 训练算法：Lyapunov debt control 加 evolutionary transfer optimization。
- 反向传播：不联合重训；候选专家既有训练不属于本文更新。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=h2B3uQpSxt
- 官方摘要证据：Continual model merging (CMM) sequentially integrates task-specific experts without joint retraining. Existing methods mainly make local merge decisions based on the incoming task and current expert state, without accounting for the cumulative effects of past merges. Over long task streams, this can lead to persistent historical perturbation, insufficient integration of incoming knowledge, and growing expert-capacity pressure. Jointly optimizing expert selection and update parameters is also constrained by costly candidate evaluations. To address these, we introduce \textbf{DebtMerge}, a long-horizon optimization framework for expert-managed CMM that jointly addresses long-horizon control and finite-budget merge optimization. DebtMerge formulates CMM as an online problem with time-average targets and uses Lyapunov virtual queues to represent accumulated \emph{stability}, \emph{plasticity}, and \emph{resource debts}. These debts induce a per-arrival objective, while stability and plasticity debts guide geometry initialization without future task information. To optimize this objective under a fixed evaluation budget, DebtMerge uses evolutionary transfer optimization over merge recipes specifying expert structure, knowledge composition, and integration geometry. Compatible historical recipe blocks are adapted to the current expert bank and debt state, with objective feedback guiding their reuse toward promising combinations. We characterize debt-guided directional control, incorporate finite-budget solver error into the long-horizon control bound, and derive sufficient conditions for preserving historical predictions under stated assumptions. Experiments across vision and language models show improved average performance over the compared merging baselines.

### 55. DarwinX: Evolving Agent Harnesses through Natural Selection

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：DarwinX 明确在 model fixed 条件下演化 instructions、tools、memory 和 control-flow harness。
- 模型参数/组件边界：agent harness 与 archive/shared memory。
- 训练算法：population-based natural selection。
- 反向传播：模型明确固定。
- 待核实：无。
- 原始来源：https://openreview.net/forum?id=XVvUgp3Bu8
- 官方摘要证据：An LLM agent’s capabilities depend on the harness that supplies its instructions, tools, memory, and control flow. Improving that harness is a selection problem: an edit that fixes one task can regress another, a discarded variant may contain a complementary capability, and a noisy local gain may not repeat. We introduce DarwinX, a population-based method for evolving harnesses with the model fixed. Its preserve-and-extend contract screens task-level regressions, while independent confirmation determines which variants may steer later search. The archive retains other specialists for recombination, and execution traces and shared memory guide subsequent proposals. Search uses verifier-backed synthetic tasks that reuse benchmark environments; original benchmark tasks remain outside the search loop. On complete official evaluations, the selected harnesses improve five-attempt average success by 7.19 percentage points on Terminal-Bench 2.1 and 9.38 points on DeepSWE. On WebArena-Infinity, the frozen winner achieves 91.19% single-attempt success across 1,260 tasks, versus 75.48% for the composite report baseline, with no static-invalid evolved trajectory flagged by the action audit. These results show that the complete selection procedure can improve a frozen-model agent beyond the synthetic tasks used for search.

### 56. Customize Your Memory: Scenario-Adaptive and Evolvable Memory Modeling for LLM Agents

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：ScenarioModelMem 演化的是动态 memory policy 和外部记忆建模结构；摘要没有训练语言/策略模型参数。
- 模型参数/组件边界：静态记忆结构与动态记忆策略。
- 训练算法：验证驱动的 mutation、crossover、pruning。
- 反向传播：无语言模型参数训练证据。
- 待核实：“policy”表现为可演化的记忆配置；是否参数化未说明，但摘要机制支持外部工件解释。
- 原始来源：https://openreview.net/forum?id=qm5Z3S6e4g
- 官方摘要证据：Memory enables large language model (LLM) agents to learn continually across sessions and scenarios. Memory systems have attracted great attention as LLM agents are widely used in coding, office work, and other scenarios. However, memory modeling, i.e. how to represent flat text and what features to extract, is either ignored or hand-crafted and frozen at design time. We argue that memory is a process of identification, extraction, and synthesis, i.e. an offline cognitive capability whose core is memory modeling instead of a flat archive. We formulate the memory system as a modeling-guided optimization problem and present ScenarioModelMem, a scenario-adaptive memory-modeling system. We split memory modeling into a static memory structure and a dynamic memory policy to achieve efficient representation, flexible configuration, and optimizability. A validation-driven evolutionary algorithm refines the dynamic memory policy through error-informed mutation, crossover, and pruning. Under the same experimental configuration as the strongest published systems, ScenarioModelMem achieves state-of-the-art performance on LOCOMO (94.03) and PersonaMem (70.63) with a pre-defined memory policy. Furthermore, we evaluate automatic policy design on PersonaMem. Starting from a basic initial policy, the evolved policy outperforms a carefully crafted human-designed one. Memory modeling thus becomes scenario-adaptive and optimizable, rather than a fixed design choice.
