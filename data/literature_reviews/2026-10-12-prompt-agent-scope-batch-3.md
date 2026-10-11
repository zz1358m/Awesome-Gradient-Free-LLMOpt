# 2026-10-12 提示词与智能体范围审查：批次 3（语义修正版）

本批次逐篇审查 55 条。语义修正版按真实机制判定，不以是否自称 agent/harness、原类别名或关键词规避范围。

## 统计

- `defer_agent_no_model_training`：32 条
- `defer_agent_training_unverified`：6 条
- `defer_prompt_core`：6 条
- `keep_agent_model_training`：3 条
- `keep_unaffected`：8 条

## 逐篇决定

### 1. Context-Space Adaptation of Frozen Multimodal Large Language Models for Medical Image Diagnosis

- 决定：`defer_prompt_core`
- 原分类：`related_prompt_agent`
- 论文特定依据：论文明确把冻结 MLLM 的数据集适配放在 context space：持续选择视觉 exemplars、优化检索键并自精炼诊断经验，作为推理输入上下文；预训练参数不更新。
- 模型参数/组件边界：视觉示例、检索键与诊断经验上下文状态；MLLM 参数明确冻结。
- 训练算法：DECS 样例选择与 SRES 经验汇总。
- 反向传播：摘要明确预训练 MLLM 冻结且不更新。
- 待核实：DECS/SRES 是否包含另训辅助组件仍待核实。
- 原始来源：https://openreview.net/forum?id=6JkxoF616C
- 官方摘要证据：Multimodal large language models (MLLMs) offer a promising paradigm for medical image diagnosis, yet their performance can degrade substantially when applied to medical datasets with heterogeneous visual distributions and diagnostic tasks. Fine-tuning can improve domain adaptation, but requires repeated model updates for each target dataset. In this work, we investigate gradient-free adaptation of frozen MLLMs through the construction of dataset-specific context states. We propose Clinician Mimetic Workflow, a context-space adaptation framework that adapts frozen MLLMs by jointly constructing complementary visual and experiential context states. The framework comprises two coordinated context construction processes. Discriminative Exemplar Coreset Selection (DECS) organizes representative diagnostic cases in a frozen DINOv2 feature space and refines their adaptive retrieval keys to construct the visual context state. Self-Refined Experience Summarization (SRES) distills reusable diagnostic experience from diverse reasoning trajectories and maintains it through adaptive experience-state updates to construct the experiential context state. During inference, the visual exemplars provided by DECS and the diagnostic experience accumulated by SRES are jointly incorporated into the multimodal context, enabling the frozen MLLM to perform dataset-specific diagnostic reasoning without updating pretrained model parameters. We systematically evaluate the proposed framework on a subset of the public MedMNIST 2D datasets and a private nasopharyngeal carcinoma MRI dataset. Experimental results show that our method consistently improves over representative gradient-free in-context learning methods and achieves competitive diagnostic performance on real-world clinical data.

### 2. Constructive Prediction: The Role of Lexical Code Organization in Language Modeling

- 决定：`keep_unaffected`
- 原分类：`related_prompt_agent`
- 论文特定依据：复核保留：论文训练 ILM 语言模型参数并研究词汇路径编码，属于真实模型训练。
- 模型参数/组件边界：ILM 语言模型参数。
- 训练算法：常规下游语言模型训练；摘要未说明优化器。
- 反向传播：摘要说明进行 language-model training，但未说明反传细节。
- 待核实：具体训练目标、优化器和参数范围待原文核实。
- 原始来源：https://openreview.net/forum?id=DXrf6mhnGR
- 官方摘要证据：Character, byte, and subword language models build text from categorical events that are individually valid but may combine into strings with no corresponding entry in a given lexicon. Thus, the prediction interface does not explicitly distinguish such constructions from those that complete a lexical entry. We introduce *constructive prediction*, which instead represents each lexical entry by a short path over a shared, low-cardinality alphabet. In this case, partial paths are intermediate shared states with many possible continuations, and only a completed path can either resolve to a lexical identity or remain unassigned. We instantiate this representation as **Intuitionistic Language Models** (ILM). We first test Flat ILM, which applies a causal Transformer to the coordinate stream. We then extend this design with Full ILM, which adds coordinate-role interfaces and prefix-aware supervision.
To assess the effect of constructive prediction, our central experiment asks whether a lexical-to-path assignment constructed from external pretrained embeddings and frozen before downstream language-model training carries predictive structure. To do so, we reassign entries among the same set of paths under the Flat model. Using three assignment seeds, each evaluated with three training seeds, unrestricted reassignment worsens test BPB by $0.1442\pm0.0014$ on Tiny Shakespeare and $0.1817\pm0.0093$ on enwik8. All nine paired comparisons favor the original assignment on each corpus. To control for permutation-induced frequency shifts, we use a stricter control that shuffles only entries with equal training frequency, thereby preserving training-weighted coordinate frequencies at each path position. Reassignment still worsens BPB by $0.1063\pm0.0079$ and $0.0957\pm0.0015$, respectively.
Beyond assignment, we ask whether the Transformer can exploit path structure. We find that Full ILM has lower mean BPB than Flat ILM at 6.5M and 15.5M on both corpora, and at 100M on enwik8. Full's advantage remains substantial on enwik8 but narrows to $0.0055$ BPB at 15.5M on Tiny Shakespeare. Overall, these results show that the organization of lexical identities over shared sequential codes is a modeling variable that can improve prediction under a compact representation.

### 3. Confidence-Adaptive Permutation-Tree Self Speculative Decoding for Diffusion Large Language Models

- 决定：`keep_unaffected`
- 原分类：`related_prompt_agent`
- 论文特定依据：复核保留：training-free permutation-tree speculative decoding 是推理系统机制，不调用 LLM 代理依据反馈改写外部工件。
- 模型参数/组件边界：不更新模型参数；运行时更新 permutation tree、置信分区和接受路径。
- 训练算法：置信自适应树剪枝及单次批量前向验证。
- 反向传播：摘要明确 training-free。
- 待核实：实现中的缓存和验证细节待核实。
- 原始来源：https://openreview.net/forum?id=heTK8MXaWg
- 官方摘要证据：Diffusion-based Large Language Models (dLLMs) offer a promising alternative
to autoregressive models by enabling parallel decoding and bidirectional context
modeling. However, existing speculative decoding methods for dLLMs rely on
linear or heuristic verification structures that fail to capture the full space of valid
generation orders within a block, leading to premature rejection of correct tokens
and suboptimal acceptance rates. In this work, we propose CAPSpec (Confidence-
Adaptive Perm-tree Speculative Decoding), a training-free framework targeting
block-based diffusion models. CAPSpec exploits the key insight that, within a
fixed-length block, the n remaining masked positions admit n! possible decoding
orders, forming a full permutation tree whose size grows factorially. By first
constructing this complete permutation tree over a block’s decoding trajectories
and then applying Adaptive Confidence Partitioning (ACP)—which clusters
candidate positions by their draft-stage confidence and prunes low-value branches
before verification—CAPSpec compresses the factorial-sized search space into a
compact tree that retains all high-probability trajectories. A single batched forward
pass over the pruned tree evaluates the retained trajectories and identifies a unique
accepted path. Extensive experiments on LLaDA-8B-Instruct across mathematics,
code, and dialogue benchmarks demonstrate that CAPSpec achieves up to 3.08×
wall-clock speedup over step-by-step baselines, establishing a new state of the art
for training-free speculative decoding in block-based diffusion language models.

### 4. Component-Aware Feedback for Self-Evolving Programs

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：LLM 充当 mutator，核心更新对象是多组件程序及其归因记忆；摘要没有训练或持久更新语言模型参数。
- 模型参数/组件边界：候选程序、组件改动归因记忆和 fitness 历史。
- 训练算法：LLM-guided evolutionary program search。
- 反向传播：摘要未描述模型反传或参数训练。
- 待核实：mutator LLM 与评估器是否完全固定待原文核实，但所提更新机制仅落在程序和记忆。
- 原始来源：https://openreview.net/forum?id=PtpPmfGxts
- 官方摘要证据：LLM-guided evolutionary search can discover complex programs, but existing methods mostly only save candidate programs and fitness scores while discarding which component edits produced which fitness metric changes. Existing methods force the mutator LLM to infer the effect of prior edits from cluttered histories, making program search slow and unstable. This is especially true for locally servable LLMs to evolve multi-component systems. We introduce component-aware feedback, which compares each evaluated program with its parent, identifies the components that changed, and logs them with the associated metric differences into an attribution memory that later mutations read. The memory keeps each change in two reference frames, local against the parent it came from and global against the seed program, which shows both the immediate effect of a change and the cumulative progress made since the seed. We study this on LLM reranking, a multi-objective optimization problem where a multi-stage pipeline must balance quality against serving cost. Across twelve \textsc{Bright} datasets, our method reaches the strongest baseline's final quality after a median of one third of the search budget and ends 7.2\% higher in held-out nDCG@10, and under a cost-aware objective it finds pipelines that are on average more accurate while using 11\% fewer tokens per query, showing component-aware feedback to be a promising direction for more efficient self-evolving systems.

### 5. Competition Discovers, Cooperation Consolidates: Social Rewards Shape Self-Evolving LLM Agents

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：自演化来自交互轨迹筛选并写入持久外部记忆；摘要没有模型参数训练。
- 模型参数/组件边界：多智能体轨迹、社会信用和持久外部记忆。
- 训练算法：竞争/合作社会奖励驱动的经验筛选。
- 反向传播：未说明反传；摘要把改进载体明确为 persistent external memory。
- 待核实：所用代理底座和记忆 updater 实现待核实。
- 原始来源：https://openreview.net/forum?id=plmHDI1b7d
- 官方摘要证据：Self-evolving LLM agents improve by converting interaction traces into persistent external memory. Yet while substantial effort has been devoted to refining downstream memory updaters, the upstream social environment that generates and filters these trajectories remains largely unexamined. In multi-agent self-evolution, social reward structures govern the evolutionary loop at two foundational stages: during interaction, process rewards dictate how agents search, communicate, and commit; after interaction, social credit assigns marginal value to outcomes, selecting which experiences are retained in persistent memory. To systematically explore this mechanism, we investigate two canonical social regimes: competition driven by relative individual credit, and cooperation driven by shared team outcomes. Our results reveal a fundamental division of labor: competitive pressure penalizes hesitation and incentivizes divergent exploration, accelerating environment-verified discovery under finite budgets and yielding decisive heuristics that elevate downstream speed-sensitive task completion. Cooperation instead aligns agents toward shared objectives and favors partner-legible proceduralization, producing structured routines that prove essential when downstream deployment requires inheriting complex collaborative conventions. Rather than revealing a universally superior paradigm, these findings show that competitive environments drive expansive frontier discovery, whereas cooperative environments synthesize inheritable order. Overall, social reward structures thus act not as incidental scaffolds, but as primary evolutionary drivers that determine both what multi-agent systems can discover and what persistent capabilities they ultimately inherit.

### 6. CompEvolve: Competitive Evolution of LLM Agent Harness Regularized by Behavioral Diversity and Generalization Judging

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：CompEvolve 明确进化 prompt、控制流和多智能体 harness，而非模型权重。
- 模型参数/组件边界：prompt、控制流、多智能体结构和候选 harness。
- 训练算法：竞争式进化、行为多样性选择和重组。
- 反向传播：摘要明确 modifies the harness rather than model weights。
- 待核实：LLM architect/judge 是否另训未说明。
- 原始来源：https://openreview.net/forum?id=4IVbz5H9ER
- 官方摘要证据：Evolutionary search is a well-established paradigm for automatic design, and has recently been applied to evolve the \emph{harness} around a large language model (LLM): its prompt, control flow, and multi-agent structure. Because it modifies the harness rather than the model weights, this paradigm extends even to closed-source models, at lower cost and with greater interpretability than fine-tuning. Within it, competition, keeping only the fittest of competing harnesses, is a natural mechanism for directed improvement. We find, however, that naive competition among LLM agents does not reliably surpass independent, non-competitive evolution: the population rapidly converges to a few near-identical architectures, and selection by training accuracy alone rewards designs that overfit the training problems. We present CompEvolve, which turns competitive evolution into a reliable optimizer through three components: information isolation prevents a capable LLM architect from exploiting the training signal, compelling it to improve genuinely transferable ability; selection regularized by behavioral diversity retains agents that are initially weak but complementary to the rest of the population, which are more likely to be recombined into stronger agents in later generations; and an LLM generalization judge evaluates the transferability of an agent's design at the architecture level, complementing training accuracy. CompEvolve consistently improves out-of-distribution generalization over independent evolution across multiple reasoning benchmarks and LLMs of varying capability.

### 7. Collective Alignment in LLM Multi-Agent Systems: Disentangling Bias from Cooperation via Statistical Physics

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：该多智能体研究只查询固定 LLM 更新晶格二元状态并测量群体现象，没有训练智能体模型参数。
- 模型参数/组件边界：晶格代理的运行时二元状态及统计量。
- 训练算法：温度扫描、有限尺寸标度和有效耦合/场估计。
- 反向传播：摘要未描述模型训练或反传。
- 待核实：采样与模型部署细节待核实。
- 原始来源：https://openreview.net/forum?id=Qj9Mbp6dCi
- 官方摘要证据：We investigate the emergent collective dynamics of LLM-based multi-agent systems on a 2D square lattice and present a model-agnostic statistical-physics method to disentangle social conformity from intrinsic bias, compute critical exponents, and probe the collective behavior and possible phase transitions of multi-agent systems.
In our framework, each node of an $L\times L$ lattice hosts an identical LLM agent holding a binary state ($+1$/$-1$, mapped to yes/no) and updating it by querying the model conditioned on the four nearest-neighbor states.
The sampler temperature~$T$ serves as the sole control parameter.
Across three open-weight models (llama3.1:8b, phi4-mini:3.8b, mistral:7b), we measure magnetization and susceptibility under a global-flip protocol designed to probe $\mathbb{Z}_2$ symmetry.
All models display temperature-driven order-disorder crossovers and susceptibility peaks; finite-size scaling on even-$L$ lattices yields effective exponents $\gamma/\nu$ whose values are model-dependent, close to but incompatible with the 2D Ising universality class ($\gamma/\nu=7/4$). Our method enables the extraction of effective $\beta$-weighted couplings $\tilde{J}(T)$ and fields $\tilde{h}(T)$, which serve as a measure of social conformity and intrinsic bias. In the models we analyzed, we found that collective alignment is dominated by an intrinsic bias ($\tilde{h}\gg\tilde{J}$) rather than by cooperative neighbor coupling, producing field-driven crossovers instead of genuine phase transitions.
These effective parameters vary qualitatively across models, providing compact collective-behavior fingerprints for LLM agents and a quantitative diagnostic for the reliability of multi-agent consensus and collective alignment.

### 8. Code to Control: Synthesizing Parameterized Reactive Controllers

- 决定：`defer_agent_training_unverified`
- 原分类：`related_prompt_agent`
- 论文特定依据：已确认 LLM 生成 Python controller 结构，导数无关搜索拟合该程序的连续参数；摘要没有证明这些参数属于语言模型、神经策略、adapter 或 neural controller，因此不能计为已确认模型参数训练。
- 模型参数/组件边界：已确认：Python 控制器程序的连续数值参数；待核实：控制器是否含可训练神经模型参数。
- 训练算法：环境反馈驱动的 derivative-free parameter search。
- 反向传播：控制器参数搜索不依赖反传；LLM 本身是否训练未说明。
- 待核实：控制器参数化形式、搜索算法和持久保存方式待原文核实。
- 原始来源：https://openreview.net/forum?id=z62vbEOWDO
- 官方摘要证据：Recent LLM-based approaches to control either invoke a language model to select actions or synthesize world models that require planning at every decision, introducing latency that can limit real-time use. We introduce Code to Control, an approach that synthesizes Python controllers which execute directly as policies. Code to Control separates program structure from parameters. An LLM synthesizes
the controller structure, while derivative-free search fits its parameters for continuous control using feedback from the environment. Once learned, the resulting controllers require neither LLM inference nor planning at decision time, enabling real-time gameplay and, under our timing protocol, faster action selection than a PPO policy. Across a suite of Atari games, Flappy Bird, and MuJoCo tasks, Code to Control outperforms planning-based program synthesis methods, remains competitive with deep reinforcement learning while using fewer environment interactions, transfers across substantial changes in environment dynamics, and scales to complex locomotion tasks.

### 9. Co-Evolving LLM Agents and Bayesian Optimizers for Automated Feature Engineering

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：CoEvolve 更新特征变换、双记忆、FE-MDP/DSGO 代理状态；摘要没有训练 LLM agent 的模型参数，辅助 surrogate 更新不等同代理政策训练。
- 模型参数/组件边界：特征集、变换、CAM/UAM、FE-MDP 与 DSGO surrogate 状态。
- 训练算法：局部 beam expansion 与 BO expected improvement。
- 反向传播：摘要未说明 LLM 参数反传；辅助 surrogate 的训练细节未给出。
- 待核实：FE-MDP/Set Transformer 的训练方式待核实。
- 原始来源：https://openreview.net/forum?id=Oal3lWxqBY
- 官方摘要证据：Automated feature engineering (AutoFE) involves searching a combinatorial space of compositional transformations under expensive downstream evaluations, making efficient exploration and effective reuse of search experience essential. We introduce CoEvolve, a collaborative evolution framework that couples an LLM agent for local exploration with a global optimizer for selecting promising feature set anchors. Starting from an anchor, the agent invokes FE-MDP, a surrogate network that predicts one-step performance gains conditioned on the current feature set and candidate action, to guide exploratory beam expansion and collect local search experience. A dual-memory mechanism distills this experience into Conditional Agent Memory (CAM), which captures context-specific evidence about effective and ineffective transformations, and Unconditional Agent Memory (UAM), which accumulates reusable knowledge across feature sets. Together, these memories guide the agent in proposing candidate transformations for downstream evaluation. To coordinate global exploration, we introduce the Deep Set Global Optimizer (DSGO), which combines a permutation-invariant Set Transformer encoder with a Bayesian linear regression posterior to estimate downstream performance and predictive uncertainty. DSGO selects promising anchors through expected improvement, directing local exploration toward promising regions of the search space. As newly evaluated candidates expand the search pool, the surrogate models and agent memories are iteratively updated, allowing global optimization and local exploration to inform one another. Experiments on public tabular benchmarks demonstrate that CoEvolve outperforms existing feature selection and generation methods, achieving average relative performance improvements of 21.68\% over the raw-feature baseline and 3.59\% over the strongest competing baseline on each dataset.

### 10. Characterizing and Improving Bijection Attacks through Prompt-Level Perturbation

- 决定：`defer_prompt_core`
- 原分类：`related_prompt_agent`
- 论文特定依据：核心对象是双射编码 prompt 及 prompt-level perturbation，SLS 直接搜索可成功越狱的提示编码。
- 模型参数/组件边界：双射编码提示及其 perturbation。
- 训练算法：gradient-free Signed Langevin Search。
- 反向传播：搜索以模型反馈进行，摘要未声明训练目标模型参数。
- 待核实：白盒设置使用哪些信号待原文核实。
- 原始来源：https://openreview.net/forum?id=Jq6I5yUXXR
- 官方摘要证据：Among Large Language Model (LLM) jailbreaking methods, *bijection attacks*, that communicate using an invertible bijection language, have drawn interest due to their efficiency, black box applicability, and large attack space. These attacks are commonly characterized via a dispersion parameter, which specifies the number of characters in the alphabet that are encoded by the bijection. However, attacks with the same dispersion value can vary significantly across trials and prompts, making dispersion alone a coarse measure for characterizing attack success or identifying effective bijections in the large attack space. In this work, we characterize bijection attacks through *prompt-level perturbation*, a measure of the bijection's interaction with the prompt. We first show that the attack outcomes are structured along this measure, both within and across dispersion values. Next, we demonstrate that optimal prompt-level perturbation can vary across prompts, motivating adaptive strategies to localize successful attacks. Finally, we introduce Signed Langevin Search (SLS), a *gradient-free* stochastic search method inspired by Langevin dynamics for efficiently identifying successful bijection attacks in *both white and black-box settings*. SLS uses prompt-level perturbation to organize the search space and model feedback to guide exploration towards promising regions, demonstrating consistent improvements in query efficiency across multiple models and datasets. Together, these findings allow us to better understand vulnerabilities LLMs have to encoded prompts, providing a deeper understanding of LLM safety behavior.

### 11. CUDA-Harness: Harnessing Agentic CUDA Kernel Generation and Optimization from Natural Language

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：CUDA-Harness 的智能体生成、验证和演化 CUDA kernel 程序；摘要没有模型参数更新。
- 模型参数/组件边界：CUDA kernel 源码、中间结构和候选程序。
- 训练算法：Feedback-Adaptive Evolution。
- 反向传播：未描述语言模型训练或反传。
- 待核实：生成 LLM 与验证器是否固定待核实。
- 原始来源：https://openreview.net/forum?id=PdZhD2bbqe
- 官方摘要证据：Developing high-performance CUDA kernels demands specialized knowledge in algorithm implementation, correctness validation, and hardware-aware parallel optimization, creating a substantial expertise barrier and making generating CUDA kernels directly from natural language (Text2CUDA) essential.
Meanwhile, the general-purpose code generation capability of Large Language Models (LLMs) prompts a series of works exploring LLM-based CUDA kernel generation.
They mainly focus on transpilation from high-level frameworks such as PyTorch to CUDA (Torch2CUDA) rather than Text2CUDA, where models must understand the high-level input semantics and handle low-level kernel implementation and validation.
Additionally, these methods are vulnerable to reward hacking due to reliance on predefined test inputs.
In this paper, we propose CUDA-Harness, a framework for harnessing agentic CUDA kernel generation and optimization from natural language.
Specifically, we introduce Intermediate-Structured Generation to connect high-level semantic understanding with low-level kernel generation.
To dilute reward hacking in Text2CUDA, we construct Synthesis-Based Verification to provide isolated test data and progressive validation.
Furthermore, we propose Feedback-Adaptive Evolution, a kernel evolution strategy that prioritizes correctness while optimizing performance.
Finally, through extensive experiments, we demonstrate the effectiveness of CUDA-Harness, with further evaluations illustrating generalization across LLMs, hardware platforms, and to C-to-CUDA transpilation.

### 12. COMIC: Agentic Sketch Comedy Generation

- 决定：`defer_agent_training_unverified`
- 原分类：`related_prompt_agent`
- 论文特定依据：COMIC 明确演化剧本和渲染候选，但“与观众偏好对齐的 LLM critics”是否通过模型参数训练获得，摘要没有说明。
- 模型参数/组件边界：已明确更新剧本和视频候选；critic 参数是否更新未知。
- 训练算法：多岛相对演化与渲染锦标赛。
- 反向传播：剧本搜索无需推断反传；critic 的训练/反传证据不足。
- 待核实：需核实 LLM critics 的对齐究竟是提示/检索还是参数训练。
- 原始来源：https://openreview.net/forum?id=Rfj9wv4EDR
- 官方摘要证据：We propose a fully automated AI system that produces short comedic videos similar to sketch shows such as Saturday Night Live. Starting from character references, the system employs a population of agents loosely modeled on roles in real production studios and structured to optimize the quality and diversity of ideas and outputs through iterative competition, evaluation, and refinement. A key contribution is the introduction of LLM-based critics aligned with real viewer preferences through the analysis of a corpus of comedy videos on YouTube, enabling automatic evaluation of humor. We further propose multi-island relativistic evolution for script improvement, along with script-conditioned rendering critics that perform shot- and video-level tournaments. In both human and automated evaluations, COMIC receives higher scores than agentic and video generation baselines.

### 13. CB-Orchestrator: Adaptive Workflow Optimization for LLM Agents via Contextual Bandits

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：两阶段方法只进化工作流池并用 contextual bandit 选择工作流，未训练 agent 模型参数。
- 模型参数/组件边界：工作流池及 bandit 选择状态。
- 训练算法：evolutionary search + contextual bandit。
- 反向传播：摘要未描述语言模型反传。
- 待核实：bandit 参数化和持久化实现待核实。
- 原始来源：https://openreview.net/forum?id=YEDtlblPEM
- 官方摘要证据：Large Language Model (LLM) agents have demonstrated remarkable capabilities in tackling complex tasks through agentic workflows. However, manually designing these workflows is labor-intensive and lacks flexibility to adapt to diverse queries. While automated workflow optimization is a promising direction, existing methods often incur expensive API costs during training-phase feedback collection. Furthermore, they fail to adaptively reuse high-quality workflows, which creates a bottleneck for both performance and cost-effectiveness. To address these limitations, we propose CB-Orchestrator, an adaptive framework that decouples workflow generation from selection. In the first stage, we construct a diverse pool of candidate workflows via evolutionary search. In the second stage, we formulate workflow selection as a Contextual Bandit problem, which enables sample-efficient learning by balancing exploration and exploitation, thereby significantly reducing the feedback required for training. During inference, the model adaptively selects the optimal workflow tailored to each query. Evaluations across five diverse benchmarks demonstrate that CB-Orchestrator consistently outperforms all baselines. Notably, on the MATH dataset, CB-Orchestrator achieves better performance than strong recent baselines while reducing training-phase API token overhead by no less than 40.55% and total end-to-end training (including workflow pool generation) token overhead by no less than 29.73%.

### 14. BoLT: A Benchmark to Democratize Black-box Optimization Research for Expensive LLM Tasks

- 决定：`keep_unaffected`
- 原分类：`related_prompt_agent`
- 论文特定依据：复核保留：贡献是昂贵 LLM 任务的黑箱优化基准与评测协议，不是反馈式冻结 LLM 工件优化方法。
- 模型参数/组件边界：随 benchmark task 而异，包括超参数、数据混合、并行策略等。
- 训练算法：BO/BBO benchmark。
- 反向传播：随被评估问题和方法而异。
- 待核实：各底层实验与优化器训练方式需按任务核实。
- 原始来源：https://openreview.net/forum?id=jRLlZdU76s
- 官方摘要证据：Optimization of LLM training and inference configurations, such as hyperparameters, data mixtures, prompts, and parallelism strategies, is critical to performance. However, it is often done heuristically, which can lead to suboptimal outcomes. These tasks are noisy, expensive, and derivative-free, making them a natural fit for sample-efficient Bayesian optimization (BO) and other black-box optimization (BBO) methods.  This direction remains underexplored, largely because LLM training and inference are prohibitively expensive for most BBO researchers, and new methods are often evaluated only on synthetic test functions and small-scale datasets that fail to capture the challenges of LLM optimization. This impedes the development of BBO methods and makes their effectiveness on modern LLM tasks difficult to assess. We introduce BoLT, the first LLM-centric benchmark that democratizes LLM research for the BBO community. BoLT covers a broad set of well-motivated LLM optimization problems, involving multi-fidelity, multi-objective, heteroscedastic noise, high-dimensional search spaces, and black-box constraints. Each problem is grounded in thousands of real LLM experiments, and is fully reproducible and accessible through lightweight emulators or tabular datasets. We benchmark a wide range of BO and BBO methods on BoLT. BO methods generally outperform other baselines, but no single method wins across tasks, and methods remain far from optimal on some problems. These gaps underscore the need for benchmarks grounded in modern LLM tasks. An anonymized version of BoLT is available at https://github.com/anonom799/bolt.

### 15. Beyond Successful Experience Reuse: Inducing Revision Knowledge from Evolving Experience for LLM Agents

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：CEA 从演变经验恢复程序适用条件与状态到程序映射，摘要没有模型参数训练。
- 模型参数/组件边界：修订因素、程序知识和状态—程序映射。
- 训练算法：结构化对比归因。
- 反向传播：未描述模型反传或参数更新。
- 待核实：知识表示和诱导组件实现待核实。
- 原始来源：https://openreview.net/forum?id=oFY9G0m3ts
- 官方摘要证据：Experience-based learning enables LLM agents to accumulate and reuse knowledge from prior interactions, but previously successful procedures may become inapplicable as contexts evolve. We study revision knowledge induction: recovering structured knowledge about when acquired procedures remain valid or require revision. We introduce Contrastive Evolution Attribution (CEA), which factorizes evolutionary experience through structured contrasts to identify revision-relevant contextual factors and recover the corresponding state-to-procedure mapping. To evaluate this capability, we develop ApplyBoundary, a controlled diagnostic benchmark for revision knowledge recovery and downstream procedure selection under unseen contexts with correlated contextual changes. Experiments show that CEA improves both revision-factor identification and state-to-procedure mapping recovery over experience-based approaches that use the same evolutionary evidence without contrastive factorization. A small-scale validation on documented real-world system changes provides preliminary evidence that similar revision patterns can also appear in practical settings. Further analysis shows that controlled-success evidence helps identify revision-relevant changes, while effectively utilizing recovered knowledge for future decisions remains a separate challenge.

### 16. BehEvolve: Behavior-Guided Evolution of Multi-Agent Program Policies under Sparse Task Feedback

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：BehEvolve 的持久改进对象是多智能体程序政策、代码修改和调度分支，不是语言模型参数。
- 模型参数/组件边界：程序政策、父子代码、执行轨迹和 idea 调度状态。
- 训练算法：行为反馈引导的 program evolution。
- 反向传播：摘要没有模型参数训练证据。
- 待核实：feedback model 是否另训未说明，但不是摘要所述优化对象。
- 原始来源：https://openreview.net/forum?id=GhCb2ZuoHN
- 官方摘要证据：Large language models (LLMs) can synthesize executable multi-agent policies, but improving these policies through program evolution requires informative feedback that distinguishes promising candidates. Under sparse task-completion feedback, unsuccessful programs receive identical fitness scores, creating zero-fitness plateaus where fitness alone cannot determine which programs to expand or how they should be revised. We present BehEvolve, an idea–program evolution framework that leverages execution behavior to guide program evolution without requiring hand-designed process rewards. The framework retains parent–child code changes and paired execution traces, from which a feedback model produces behavioral diagnoses for program mutation and relative preferences for parent selection. Behavioral progress further guides idea-level scheduling when a strategy branch stalls. Across eight VMAS tasks and five Overcooked layouts, BehEvolve achieves the strongest average performance, reaching an average success rate of 81.5% on VMAS and 12.6 soups on Overcooked. It outperforms the strongest general evolution baseline, AdaEvolve, and the strongest Overcooked-specific baseline, KnowPC, by 29.0% and 18.9%, respectively. Further analyses show that the three behavioral feedback pathways—program mutation, parent selection, and idea-level scheduling—work together to improve search efficiency and final performance.

### 17. Bandit Limited Discrepancy Search for Agent Harness Configuration

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：BLDS-AF 搜索 agent-DAG 的 agent type、模型选择、推理预算等 harness 配置，不更新所选模型参数。
- 模型参数/组件边界：DAG 节点/边配置及 ridge posterior。
- 训练算法：limited-discrepancy search + factored bandit surrogate。
- 反向传播：未描述被配置 LLM 的反传训练。
- 待核实：ridge posterior 的在线更新细节待核实。
- 原始来源：https://openreview.net/forum?id=u4uHWlP1gE
- 官方摘要证据：Coding-agent harnesses decompose work into a task DAG and dispatch each node to a sub-agent, but they fix the per-node configuration---agent type, model, reasoning effort, turn budget---from a plan the language model emits once, and never revisit it. We formalise the resulting problem as agent-DAG configuration selection and introduce BLDS-AF, a discrepancy-limited search over the Hamming ball around that plan that replaces the usual independent-arm bandit with a factored surrogate: a ridge posterior over node-arm and edge-pair indicators, weighted by compute allocation, with a group-wise prior that lets the model collapse onto an additive basis while data is scarce and switch interactions on as evidence accumulates. Every evaluation is pooled across configurations rather than treated as evidence about one configuration alone, and a composed candidate from the surrogate's own argmax is evaluated like any other. BLDS-AF beats the deployed greedy cascade and all fourteen baselines we tried, including Hyperband, TPE, evolutionary search, and UCT; it also beats plan-local coordinate descent by a significant margin, an advantage that grows monotonically with the size of the configuration space and holds at every interaction strength. It beats every plan-blind method on NAS-Bench-Macro with every interval excluding zero, and reaches zero normalised regret at a modest budget on a DAG of live multi-turn coding agents. The gains come from pooling statistical strength across configurations: a pre-flight diagnostic derived from the bias--variance condition of the factored surrogate predicts in advance on which substrates this works and on which it does not.

### 18. BRAID: Evolving Evaluators for Reliable and Effective Self-Evolving Agents

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：BRAID 明确是 training-free，演化评估器候选与任务代理分支等外部实现。
- 模型参数/组件边界：Evaluator challengers、lineage 和 Task-Agent branches。
- 训练算法：可靠性门控的双重演化。
- 反向传播：摘要明确 training-free。
- 待核实：Evaluator/Task-Agent 的具体表示是 prompt 还是代码待核实。
- 原始来源：https://openreview.net/forum?id=N0mDtvLk4W
- 官方摘要证据：Self-evolving LLM agents iteratively modify themselves from task experience, making reliable and actionable evaluation signals critical to efficient improvement. Existing systems, however, largely evolve the Task Agent while leaving the
Evaluator that diagnoses failures and provides feedback fixed. To address this issue, we introduce Branch-Realized Adaptive Interventional Dual-Evolution (BRAID), a training-free framework that is agnostic to the underlying Task-Agent search topology and treats the Evaluator as an explicitly evolvable agent with an independent evolutionary lineage. BRAID periodically generates Evaluator challengers from accumulated task trajectories, modification histories, and ground-truth outcomes. A challenger replaces the incumbent only when it passes an Interventional Reliability Gate and, through Challenger Branch Realization, produces a Task Agent branch whose realized branch utility exceeds the incumbent utility baseline. This selection goes beyond stand-alone evaluation accuracy by measuring the downstream utility of the Task Agent modification induced by each challenger's feedback. We evaluate BRAID across multiple self-evolution topologies and tasks spanning executable code, repository-level software engineering, and mathematical grading. Compared with the corresponding underlying-system baselines, BRAID consistently improves held-out performance under matched search-action budgets, while Frozen-Evaluator controls isolate the additional gains from Evaluator evolution. These gains persist on Token--Performance curves after accounting for Evaluator-side computation, and ablations confirm the complementary roles of Evaluator evolution, the Interventional Reliability Gate, and Challenger Branch Realization.

### 19. Automated Discovery Has No Universally Superior Harness

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：该研究比较并自适应分配自动发现 harness 的档案、父代选择和预算组件，未训练语言智能体参数。
- 模型参数/组件边界：harness 配置和并行运行预算。
- 训练算法：进化 harness 比较、剪枝与预算重分配。
- 反向传播：摘要未描述模型反传。
- 待核实：底层 OpenEvolve/TTT-Discover 具体工件表示待核实。
- 原始来源：https://openreview.net/forum?id=2ONrI9JEqu
- 官方摘要证据：Autonomous discovery systems such as OpenEvolve and TTT-Discover are often used as general-purpose harnesses. However, in practice, these are composite systems combining several design choices about archives, parent selection, exploration, and budget allocation into a single recipe. Because discovery runs are expensive and inherently stochastic, existing harnesses are often compared using too few independent trials to distinguish key methodological improvements from run-to-run variance. We systematically decompose OpenEvolve-style evolutionary search and the TTT-Discover search harness into their constituent components and systematically evaluate 30 budget-matched harnesses across 12 model–problem pairs using more than 3.1 million LLM rollouts and repeated-trial statistical analysis. Our results show that discovery harnesses have a generalization problem: No fixed harness is reliably superior across the model–problem pairs, and variants of OpenEvolve generally underperform simpler alternatives. Thus, harness choice is better viewed as a hyperparameter rather than as a universal recipe, and should be tailored to the problem and underlying model. We also find that early discovery progress predicts final performance, and use this property to present a budget-matched adaptive-allocation experiment that starts multiple harnesses, prunes weak partial runs, and reallocates compute to stronger survivors, outperforming both commitment to sampled fixed harnesses and non-adaptive harness ensembles. Together, these results motivate shifting from fixed harness selection to online adaptation guided by early performance. We will release all run pools, including baseline null distributions for every model–problem pair, as statistical infrastructure for evaluating future harness proposals.

### 20. AttriOpt: Attribution-Based Credit Assignment for Evolutionary API-Calling Optimization

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：AttriOpt 进化 LLM 生成的 API workflow，并更新统计归因分数；没有训练 agent 模型参数。
- 模型参数/组件边界：API workflow、调用参数及归因状态。
- 训练算法：归因引导的 evolutionary workflow optimization。
- 反向传播：摘要未描述 LLM 参数反传。
- 待核实：归因估计器是否含可训练模型待核实。
- 原始来源：https://openreview.net/forum?id=NFtZmpfvFx
- 官方摘要证据：Large language models (LLMs) are increasingly used to solve complex tasks by composing sequences of calls to external APIs, forming executable API workflows. However, optimizing such API workflows remains challenging because existing methods typically rely on a single evaluation signal of each workflow, providing little information about which API calls actually contribute to performance. This coarse feedback limits the effectiveness of subsequent search, especially when workflow evaluation is expensive. To address this problem, we propose AttriOpt, a statistical attribution framework for evolutionary optimization of LLM-generated API workflows. AttriOpt exploits accumulated evaluations across workflows to estimate fine-grained attribution scores for API identities, parameter configurations, and interaction patterns. These attribution signals are then incorporated into evolutionary search to effectively guide the API calling process. Experiments on mixed-integer linear programming, traveling salesman problem, and logic synthesis show that AttriOpt consistently outperforms existing API-calling methods and LLM-driven evolutionary approaches. Further ablation and attribution analyses demonstrate that these attribution signals provide more informative guidance than relying solely on a single evaluation signal for each workflow.

### 21. AscendAgent: Evolving Context to Fit the Harness in CANN Kernel Optimization

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：AscendAgent 明确模型权重、workflow 和 evaluator 固定，只演化 kernel 程序图和外部可复用知识。
- 模型参数/组件边界：kernel program graph 与条件化变换知识。
- 训练算法：LLM-guided mutation、evolutionary search 和 workflow replay。
- 反向传播：摘要明确 model weights remain fixed。
- 待核实：知识确认和冲突消解细节待核实。
- 原始来源：https://openreview.net/forum?id=gtuspdBfQo
- 官方摘要证据：High-performance accelerator kernels are fundamental to efficient large
language model (LLM) inference, yet optimizing them still requires substantial
systems expertise. Existing approaches often optimize workloads independently,
making it difficult to reuse experience across input patterns and hardware.
We present \ascendagent, a kernel optimization framework that evolves reusable
knowledge across workloads while keeping the optimization harness fixed.
It organizes API documentation, community implementations, and technical
discussions into conditional, composable transformations with expected effects
and supporting evidence. \ascendagent operates through two mechanisms.
\textbf{(1)} Within each workload, a frozen knowledge snapshot guides
evolutionary search over a program graph. The harness proposes changes,
checks correctness, and measures latency. Compatible programs share evaluation
evidence and explored continuations, while LLM-guided mutations explore changes
beyond existing knowledge.
\textbf{(2)} After each source search, workflow replay uses recorded proposals
and execution outcomes to revise transformation preferences, application
conditions, and reusable combinations. Independent confirmation determines
which updates guide later workloads. Model weights, the workflow, and the
evaluator remain fixed, and each new workload starts with fresh local search
state. We evaluate \ascendagent with five language models on four kernel
benchmarks spanning Ascend NPUs and NVIDIA GPUs under a budget of
\SearchBudget{} candidate compilations per task. With \MainModel,
\ascendagent achieves mean best speedups of \textbf{1.40$\times$} on CANN-Bench
and \textbf{1.75$\times$} on TritonBench-G, compared with
\textbf{1.21$\times$} and \textbf{1.36$\times$} for the same harness with frozen
initial knowledge.

### 22. Agentic Bayesian Optimization through Surrogate-Augmented Autoresearch

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：Sara 调整 BO 评估选择、边界和问题表述，概率 surrogate 存于外部 backend；摘要未训练 LLM agent 参数。
- 模型参数/组件边界：BO 搜索策略、边界、评估候选和 surrogate 状态。
- 训练算法：agentic Bayesian optimization。
- 反向传播：未描述 LLM 参数反传。
- 待核实：lenz backend 的拟合实现待核实。
- 原始来源：https://openreview.net/forum?id=ZIF61XReMF
- 官方摘要证据：Bayesian optimization (BO) is the standard tool for sample-efficient gradient-free optimization through uncertainty-aware search driven by generic statistical priors. Richer domain priors can improve BO, but encoding them through, e.g., tailored kernels is difficult. LLMs can help bring these priors into the optimization, drawing them directly from natural language, code, and documentation. However, existing LLM-based BO methods either insert the LLM into a fixed role, surrogate, acquisition proxy, or configuration interface, or hand it broad control, sacrificing the systematic exploration that makes BO reliable. We introduce agentic Bayesian optimization: a paradigm in which an LLM agent controls the BO loop while a Bayesian backend holds the probabilistic surrogate. The agent selects evaluations and can revise the strategy during the run by tightening bounds, proposing targeted evaluations, or reframing the problem as evidence or instructions change. We instantiate this idea in Sara, a surrogate-augmented autoresearch agent, and lenz, a modular BO backend that the agent can inspect and modify through a structured interface. Across synthetic and real-world benchmarks, Sara preserves the reliability of standard BO without prior knowledge, outperforms LLM-based baselines, and uses natural-language priors to improve beyond standard BO. Furthermore, in dynamic settings, Sara can reconfigure the full optimization problem on the fly as requirements change; a capability not available in standard BO.

### 23. Adaptive Transfer for Cost-Aware Bayesian Optimization of LLM Agent Configurations

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：ALT 搜索 reasoning effort、工具权限和资源等 agent 配置，执行固定配置获得轨迹；不训练 agent 模型。
- 模型参数/组件边界：agent 配置、行为转移模型和 utility surface。
- 训练算法：cost-aware transfer Bayesian optimization。
- 反向传播：摘要未描述被测代理参数训练。
- 待核实：GP/transfer 模型的拟合细节待核实。
- 原始来源：https://openreview.net/forum?id=UjDZ0KzZ4X
- 官方摘要证据：LLM agents can now autonomously perform long-horizon development tasks. An agent’s configuration, including its reasoning effort, tool access, and resource allocation, affects its performance, runtime, and monetary cost. An optimal configuration needs to balance these outcomes, as greater resource use does not necessarily yield higher utility. A full grid search on each new task is not practical because every configuration requires a costly, time-consuming run. Bayesian optimization can improve sample efficiency in search, and transferring knowledge from earlier tasks can further reduce search cost. The challenge is to identify what transfers when outcomes change across tasks and few target evaluations are affordable. In this work, we propose adaptive-level transfer (ALT), a cost-aware Bayesian optimization method that uses target evidence to adapt what is transferred from earlier tasks. Through systematic evaluation of every configuration of one agent across several tasks, recording agent action trajectories and outcomes, we obtain complete landscapes for exact replay of configuration search. Our analysis shows that configuration effects on several agent behavior features are relatively stable across tasks, while their effects on utility shift. ALT transfers configuration-to-behavior patterns from source trajectories and learns their utility contributions from target runs. It combines this behavior-level hypothesis with an objective-level hypothesis that transfers source utility surfaces. The target evidence decides how much each contributes to the prediction. Its acquisition weighs expected improvement against predicted cost, with the cost discount learned from target evidence on whether resource-intensive behavior raises utility. In cross-task search under monetary budgets, ALT reduces mean regret area by 4--12\% relative to our main transfer baseline, ScaML-GP with expected improvement across all four evaluated utilities, with the largest reductions on the performance- and time-focused utilities. When sources include other repetitions of the target task, ALT outperforms its behavior-only ablation.

### 24. Adaptive Scenario Selection for Screening Overeager Behavior in Coding Agents

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：ASSBF 只改变筛查场景和 Thompson-sampling 预算，执行固定 framework–model pairs，没有智能体模型训练。
- 模型参数/组件边界：场景、archetype-consent 预算和 bandit state。
- 训练算法：受控场景 mutation + Thompson sampling。
- 反向传播：摘要未描述模型反传。
- 待核实：场景生成过程是否使用固定模型待核实。
- 原始来源：https://openreview.net/forum?id=E6IQGL7SaC
- 官方摘要证据：A coding agent executes a developer task as a sequence of shell, file, and network actions, any of which can exceed the authorized scope even when the requested artifact is produced. We study overeager behavior: actions that exceed the authorization of a benign developer task, such as exposing credentials or deleting protected files. Existing benchmarks miss this behavior: task-completion suites do not score authorization scope, adversarial suites study a different input regime, and the closest overeager benchmark uses one fixed prompt distribution for every framework–model pair. We present ASSBF (Adaptive Scenario Selection with Bandit Feedback), which builds a structurally screened pool of benign-task scenarios, applies controlled scope-pressure mutations, scores observable effects with a judge-free two-signal rule, and reallocates each pair's run budget across archetype–consent cells using Thompson sampling. Instantiating the method over 24 behavioral archetypes yields OverEager, evaluated on a 4 × 5 matrix of coding-agent frameworks and base models. Across 10,000 runs, the broad screening rule returns 1,951 positives (19.51%), including 493 runs matched by scenario-specific trap predicates; pair-conditioned screening yields span 11.9×. All 24 scenario archetypes are represented for every pair, a framework-first sequential decomposition assigns 56.1% of the observed deviance reduction to framework identity and 23.1% to the framework–model interaction, and adaptive-500 recovers full-pool screening rates within one percentage point on the evaluated ablation column while halving executions. Code and data are available at https://anonymous.4open.science/r/overeager-E385/.

### 25. Adaptive Exploratory Landscape Analysis for LLM-based Meta-Black-Box Optimization

- 决定：`keep_agent_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：AdaELA 明确把 population-aware attention 选择器参数作为多任务问题并用 neuroevolution 训练，属于持久模型参数更新。
- 模型参数/组件边界：AdaELA self-/cross-attention 选择模型参数。
- 训练算法：neuroevolution strategy；摘要另称可进一步 fine-tuning。
- 反向传播：neuroevolution 本身无需反传；后续 fine-tuning 是否反传未说明。
- 待核实：LLM meta-policy 是否冻结及 fine-tuning 对象待核实。
- 原始来源：https://openreview.net/forum?id=Ke3tLwqK3L
- 官方摘要证据：Large Language Models (LLMs) have recently advanced Meta-Black-Box Optimization (MetaBBO) by enabling optimizer design with reduced expert intervention, while existing approaches typically rely on fixed optimization-state representations, such as predefined Exploratory Landscape Analysis (ELA) indicators. We argue that adaptive optimization-state perception is more effective than fixed optimization-state representations for improving MetaBBO performance. Motivated by this idea, we propose AdaELA, a plug-and-play adaptive ELA selection framework for LLM-based MetaBBO. AdaELA dynamically selects informative ELA indicators through a population-aware self-attention encoder and a cross-attention-based selection mechanism, and provides the selected landscape information to LLM-based meta-policies for optimizer control. We formulate the training of AdaELA as a multi-task optimization problem and optimize its parameters using a neuroevolution strategy. Extensive experiments demonstrate that AdaELA consistently improves different LLM-based MetaBBO methods, generalizes to unseen optimization tasks, and enables further performance improvements through fine-tuning. This work highlights adaptive optimization-state perception as a promising direction toward more generalizable and effective MetaBBO.

### 26. AdaGEPA: Adaptive Feedback Allocation for Reflective Prompt Optimization

- 决定：`defer_prompt_core`
- 原分类：`related_prompt_agent`
- 论文特定依据：AdaGEPA 的目标就是通过反馈分配反复优化 prompt。
- 模型参数/组件边界：反馈 minibatch 与迭代 prompt。
- 训练算法：弱点感知的 reflective prompt optimization。
- 反向传播：摘要无模型参数训练证据。
- 待核实：reflection 使用的模型及其固定状态待核实。
- 原始来源：https://openreview.net/forum?id=GxTIfjjhA4
- 官方摘要证据：Prompt optimization improves the performance of language-model systems on downstream tasks by refining their prompts. Classical methods evaluate prompts on task examples and use the resulting feedback to guide prompt updates through reflection. However, when feedback selection does not account for the prompt's weaknesses, these updates may improve performance on selected examples without yielding broader task improvements. To address this issue, we propose AdaGEPA, an adaptive feedback-allocation method that uses the prompt's performance and task structure to select examples for the next prompt update. Our method replaces at most one example in each feedback minibatch to target an identified weakness while preserving the remaining feedback context. Across our main experiments on six downstream benchmarks, AdaGEPA achieves higher mean validation scores than non-adaptive feedback selection under matched rollout budgets. AdaGEPA also finds high-performing prompts earlier across several tasks. In the initial Schema-Guided Dialogue (SGD) study, its half-budget prompts outperform the non-adaptive baseline's full-budget prompts in joint goal accuracy on new dialogues from services seen and unseen during search. Overall, our findings highlight the potential of adaptive feedback allocation to improve both the effectiveness and rollout efficiency of reflective prompt optimization.

### 27. Active Learning for Communication Structure Optimization in LLM-Based Multi-Agent Systems

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：方法更新多智能体通信图参数分布和任务选择状态，不是语言/策略模型参数。
- 模型参数/组件边界：通信图参数、候选任务池及 surrogate/bandit state。
- 训练算法：ensemble Kalman inversion + batch Thompson sampling。
- 反向传播：摘要未描述 LLM 参数训练。
- 待核实：“graph parameters”是拓扑/通信结构而非模型权重；具体参数化待核实。
- 原始来源：https://openreview.net/forum?id=esnxNWIVMO
- 官方摘要证据：Optimizing the communication structure of large language model based multi-agent systems (LLM-MAS) has been shown to improve downstream performance and reduce token usage. Existing methods typically rely on randomly sampled training tasks. However, tasks may differ substantially in difficulty and domain, and thus they are not equally informative for updating communication structure, making optimization often unstable and highly sensitive to the particular training set. To actively identify the most valuable tasks for communication-structure optimization, we propose an ensemble-based information-theoretic task selection framework. The proposed method estimates task informativeness by how much a candidate task changes the distribution over graph parameters, using ensemble Kalman inversion as an efficient and derivative-free approximation of the corresponding Bayesian update. The resulting estimator is especially suitable for black-box and noisy multi-agent systems. To enhance scalability, we construct a compact candidate pool through embedding-based representative selection and combine the informative selection with surrogate modeling and batch Thompson sampling. We validate the proposed framework across both benign and adversarial settings and multiple task formats. It consistently outperforms random training, demonstrating more effective task selection and greater overall cost efficiency.

### 28. APEX-Data: Automated Prompt Engineering eXpert with Dynamic Data Selection

- 决定：`defer_prompt_core`
- 原分类：`related_prompt_agent`
- 论文特定依据：APEX-Data 明确与数据分层联合执行 prompt search，核心产物仍是优化后的 prompt。
- 模型参数/组件边界：候选 prompt、搜索谱系和数据层级。
- 训练算法：evolutionary prompt mutation 与动态数据选择。
- 反向传播：摘要未描述模型参数更新。
- 待核实：mutation 模型是否固定待核实。
- 原始来源：https://openreview.net/forum?id=urjXCbKVzH
- 官方摘要证据：Large Language Models are highly sensitive to prompt formulation, necessitating automatic prompt optimization to unlock their full potential. While evolutionary algorithms have emerged as the dominant paradigm, they suffer from a critical bottleneck: data efficiency. Current methods treat the development dataset as a static benchmark, wasting significant compute budget on uninformative data. In this work, we introduce APEX-Data (Automatic Prompt Engineering eXpert with Dynamic Data Selection), a novel framework that optimizes the data usage alongside the prompt search. APEX dynamically stratifies the dataset into Easy, Hard, and Mixed tiers based on the optimization lineage. By prioritizing the Mixed tier, which identifies the data where the LLM has mixed performance, we identify two high-leverage subsets: the addressable frontier for generating informative mutations and the rank-sensitive frontier for distinguishing candidate quality. We evaluate APEX across three diverse benchmarks: IFBench, SimpleQA Verified, and FACTS Grounding. Under a fixed budget of 5,000 evaluation calls, due to its data efficiency, APEX outperforms the initial prompt by an average of 11.2% on Gemini 2.5 Flash and 6.8% on Gemma 3 27B, demonstrating that a data-centric approach is key to efficient and effective prompt optimization.

### 29. AGAR: A REINFORCEMENT LEARNING SUBSTRATE FOR LLM PROGRAM EVOLUTION

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：AGAR 进化候选程序和 modular-prefix controller，且明确 backend model 不做梯度训练。
- 模型参数/组件边界：程序候选、prefix controller、选择和经验记忆。
- 训练算法：程序进化的 MDP/RL estimator substrate。
- 反向传播：摘要明确 no gradient training of backend model。
- 待核实：各 estimator 是否含小型可训练组件待核实。
- 原始来源：https://openreview.net/forum?id=npY9pJqb57
- 官方摘要证据：Given a task and an evaluator, a language model can rewrite a candidate program while a search loop decides which rewrites survive — a practical route to algorithm discovery. But that loop is governed by five constants set by hand — which parent to select, how hard to mutate, how to keep diversity, what to remember,and a scalar score that never says which part of the program earned it — and reinforcement learning already has an estimator for each. The obstacle is that program evolution is not usually written down as a decision process. We formalize it as a Markov decision process whose action is the modular prefix the model is conditioned on, not the program it emits, so that credit assignment, value estimation,adaptive exploration and experience memory each attach to a distinct component.AGAR (Algorithm Generation As RL) provides the substrate this licenses: any estimator can be replaced or switched off without touching the controller, making the transfer auditable one mechanism at a time, with no gradient training of the backend model. Across 19 tasks, two backends and three seeds under one harness,AGAR improves on the stronger of two published baselines on most tasks, with the gains concentrated on the competitive-programming family. The formalization also yields a checkable reading of prior work: these systems are implicitly zero-discount, not by choice but because fitness is exogenous to an individual rather than a return over successors, leaving a discount factor nothing to act on.

### 30. A Narrow Residual Bottleneck from Evidence to Answer in Language Models

- 决定：`keep_unaffected`
- 原分类：`related_prompt_agent`
- 论文特定依据：复核保留：通过隐藏态干预测量语言模型内部 evidence-to-answer bottleneck，属于模型内部分析而非适配。
- 模型参数/组件边界：不做持久参数更新；干预运行时 hidden states。
- 训练算法：充分性/必要性双向干预与置换零假设。
- 反向传播：摘要未提出训练过程。
- 待核实：模型选取和干预实现细节待核实。
- 原始来源：https://openreview.net/forum?id=Q5iYGwAe9W
- 官方摘要证据：When a language model answers a question about a passage, the answer hinges on a small span of the input. We ask where inside the model that information is forced to pass, and find a narrow residual bottleneck: a small set of evidence-token positions at a single residual-stream layer that carries the evidence-to-answer computation on its own. We locate it with two hidden-state interventions on a single candidate set. One copies the original evidence into a corrupted run and asks whether the correct answer returns (sufficiency); the other injects the corrupted state into a clean run and asks whether the answer breaks (necessity). Requiring the same set to pass both is strictly stronger than either direction alone. Against a size-matched permutation null, the existence of a bottleneck becomes falsifiable: a bottleneck must pass the two-sided test far more often than random sets of its own size, and it does. On the controlled benchmark, in our best-powered models the cut passes about 0.98 of the time against about 0.01 for the matched control, and is narrow (typically two to three positions, one to two on real text) throughout. It reappears across three normalization schemes on real single-hop, multi-hop, arithmetic, and long-context question answering, and at a fixed budget steers the answer far more reliably than editing a random set. Most tellingly, the bottleneck is not simply the top of an importance ranking: fixing the set size, the test, and the model, and changing only how the set is chosen, the same-size set of highest-importance attention heads fails the very test the located cut passes, a gap that holds across four model families.

### 31. A Closer Look at Agentic BBO: Benchmarking LLM Agents for Black-Box Optimization

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：AgenticBBO-Bench 执行固定 LLM agents 做黑盒候选搜索并评估工具/先验，不训练其模型参数。
- 模型参数/组件边界：黑盒候选、工具配置和评测轨迹。
- 训练算法：统一有限预算的 Agentic BBO benchmark。
- 反向传播：摘要未描述被测模型训练。
- 待核实：个别被测 agent 的内部实现待核实。
- 原始来源：https://openreview.net/forum?id=aAcE9xwrev
- 官方摘要证据：Black-box optimization (BBO) arises in many scientific and engineering problems where objective evaluations are expensive and limited. Recent large language model (LLM) agents offer a new way to approach BBO by combining task semantics, computation, optimization tools, and feedback-driven decision making.
However, existing Agentic BBO studies use different task domains and system configurations, making their results difficult to compare and the effects of individual design choices hard to isolate.
We introduce AgenticBBO-Bench, a cross-domain benchmark for Agentic BBO spanning synthetic optimization, hyperparameter optimization, database tuning, chip design, and molecular design under a unified finite-budget evaluation protocol.
Agentic BBO achieves higher family-averaged scores than direct candidate generation by the same LLM in all five domains and outperforms the best evaluated numerical optimizers in four. We further study three factors shaping agent performance: optimization tools, task information and prior knowledge, and the role of the LLM during search.
Our results show that additional numerical tools do not consistently improve performance, task semantics are broadly useful while more specific priors are less reliable, and numerical optimizers can sometimes continue effectively from search trajectories established by the agent.
Finally, we introduce a five-task frontier challenge within AgenticBBO-Bench and evaluate seven LLMs under the same Codex agent harness. GPT-6 Astra and DeepSeek-V4.1-Flash lie on the Pareto frontier of performance and cost among the evaluated models. AgenticBBO-Bench provides a common standardized leaderboard for comparing future general-purpose models and agent systems.

### 32. SeaEvo: Strategy as State for LLM-Driven Evolution

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：SeaEvo 持久化程序候选的文本策略描述和群体状态，未更新 LLM 参数。
- 模型参数/组件边界：程序、策略描述及 population state。
- 训练算法：LLM-driven evolutionary program search。
- 反向传播：摘要未描述模型反传。
- 待核实：mutation models 是否固定待核实。
- 原始来源：https://openreview.net/forum?id=39Hpdbjdtz
- 官方摘要证据：Large language model (LLM)-driven evolutionary search is increasingly used for automated algorithm discovery and program optimization. However, most existing methods represent search progress primarily through executable programs and scalar fitness, while language-level strategies remain transient mutation context or unstructured memory. This makes it difficult to organize search progress across related algorithmic directions or reason about which directions are promising, saturated, or underexplored.

We introduce \model, which treats \textit{strategy as persistent population-level evolutionary state}. Each candidate is associated with an explicit strategy description, and these candidate-aligned strategies form a semantic space that supports complementary experience retrieval and population-level search guidance. \model operates as a lightweight layer over existing evolutionary backbones without modifying their selection or evaluation logic. Across mathematical and systems optimization benchmarks, \model improves the mean performance of its matched evolutionary backbone in 23 of 24 comparisons across two mutation models. By retrieving compact strategy descriptions rather than full source programs, \model reduces average LLM token usage by 48.8\%. These results suggest that persistent strategy representations provide a practical mechanism for improving the effectiveness and cost-efficiency of LLM-guided evolutionary search, pointing toward compound AI systems whose search capabilities benefit from the structured accumulation and reuse of algorithmic strategies.

### 33. BayesianAgent: Guiding Agentic Evolution with Bayesian Optimization

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：BayesianAgent 用 GP/Thompson sampling 分配候选扩展实验，改进的是可执行方案而非 LLM 参数。
- 模型参数/组件边界：候选方案、实验选择及 GP posterior。
- 训练算法：Bayesian optimization + joint Thompson sampling。
- 反向传播：摘要未描述语言模型参数训练。
- 待核实：候选扩展器的固定状态待核实。
- 原始来源：https://openreview.net/forum?id=CzDLiwNxO8
- 官方摘要证据：Agents that iteratively improve executable solutions must allocate a limited experimental budget across a growing set of candidates.
Most existing systems use rule-based selection informed by observed performance and experimental history.
However, these rules do not explicitly learn to predict the gain from the next expansion and quantify uncertainty in that prediction.
We introduce **BayesianAgent**, a Bayesian optimization approach that learns where to invest further experiments from completed outcomes.
Its central intuition is that an experiment can inform the improvement potential of related candidates, including those with little direct evidence.
A Gaussian process learns expansion gains and their uncertainty, sharing evidence across candidates.
Joint Thompson sampling then selects the next candidate to expand, balancing promising refinements with opportunities whose value remains uncertain.
We compare all methods using Muse Spark 1.3 under matched experimental budgets.
Across 15 AlphaEvolve mathematical optimization tasks and 22 MLE-bench Lite tasks, BayesianAgent outperforms the MLEvolve baseline.
It achieves the best AlphaEvolve average rank (1.83), the highest MLE-bench Lite gold rate (**45.45%**), and a joint-highest medal rate (**72.73%**) among evaluated methods.
Further analysis shows that its predictions rank observed expansion gains more accurately than MLEvolve's historical rewards.
These results support learning from experimental outcomes to guide subsequent allocation in agentic evolution. Our code is available at https://anonymous.4open.science/r/BayesianAgent-anonymous-6EBB.

### 34. Stateful Search with Stateless Agents: Scaling Long-Horizon Automated Research

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：AES 由 harness 保存候选和测量结果并重建上下文，持久状态明确位于代理对话之外。
- 模型参数/组件边界：候选方案、测量结果、任务分派和 harness state。
- 训练算法：Agentic Evolutionary Search。
- 反向传播：摘要未描述模型反传或参数更新。
- 待核实：Advisor/Worker 的底座是否固定待核实。
- 原始来源：https://openreview.net/forum?id=DK9rlpEHBf
- 官方摘要证据：Automated research systems increasingly run LLM agents over long horizons, but more inference does not by itself produce more progress: agents replay ever-growing histories, duplicate one another's work, or stop experimenting while token consumption continues. Yet most evaluations use short budgets or benchmarks that saturate early, leaving these failure modes untested. We introduce Agentic Evolutionary Search (AES), built on the principle of stateful search with stateless agents: the harness owns candidate solutions and measured outcomes, and reconstructs a fresh, role-specific context for every Advisor epoch and Worker trial. The Advisor turns accumulated evidence into concrete assignments for parallel Workers. We evaluate AES against three recent frameworks on software engineering, kernel optimization, and algorithm design at budgets of up to one billion cumulative tokens. AES achieves the best final result on every evaluated task and reaches the strongest kernel baseline's final performance with over 84\% fewer tokens. Ablations from shared checkpoints show that focused contexts and explicit assignments each contribute, with effects that compound over full runs, while the Advisor consumes less than 0.6\% of total tokens. These results argue for keeping durable research state out of agent conversations, and show that short evaluation horizons can misjudge both research systems and their components.

### 35. Beyond Scripted Search: Sample-Efficient Reward Discovery via Agentic Black-box Optimization

- 决定：`keep_agent_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：ARBO 每次候选 reward evaluation 都运行完整 RL policy training，因而明确训练并持久更新策略模型参数；LLM 搜索代理本身是否训练不影响该事实。
- 模型参数/组件边界：下游 RL policy 参数；外部还更新 reward function 和搜索 workspace。
- 训练算法：LLM agent 黑盒奖励搜索；候选评估采用 full RL training run。
- 反向传播：RL policy training 通常依赖反传，但摘要未明确优化器，故具体反传实现待核实。
- 待核实：LLM agent 是否固定、RL 算法与参数保存方式待核实。
- 原始来源：https://openreview.net/forum?id=JZSS6Stlhv
- 官方摘要证据：Designing dense reward functions for low-level reinforcement learning (RL) control remains difficult. Recent work uses large language models (LLMs) to iteratively generate and refine reward functions using policy-training feedback within scripted search algorithms. However, evaluating each candidate requires a full RL training run, making sample efficiency a central challenge for reward search on complex control tasks. To address this limitation, we propose an Agentic Reward Black-box Optimization (ARBO) framework, in which an LLM agent builds the search strategy at run time from an evaluation history maintained as its persistent workspace. The evaluation history comprises two components: observations maintained by the evaluation oracle, including candidate scores, per-term training curves, and error tracebacks; and an agent-maintained belief that records diagnoses and intended next steps. The agent queries both with tools and generates the next batch of reward candidates, rather than generating them in a single pass from a fixed prompt. Across four control domains, ARBO achieves gains of 29.9% in manipulation success rate and 192.8% in power-grid score over baseline means under a shared evaluation budget. Ablations examine each component’s contribution and sensitivity to backbone choice.

### 36. EvoForge: Agentic Online Hyperparameter Tuning for Pretraining

- 决定：`keep_agent_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：EvoForge 将代理置于正在运行的分布式 pretraining 环路，超参数动作直接控制同一 GPT-2 模型权重的持续训练。
- 模型参数/组件边界：GPT-2 124M 预训练模型参数及训练超参数。
- 训练算法：单轨迹 agentic online hyperparameter tuning + distributed pretraining。
- 反向传播：预训练明确发生，通常反传；摘要未列优化器细节。
- 待核实：三类控制代理自身是否训练、经验库规则形式待核实。
- 原始来源：https://openreview.net/forum?id=LAmTBYPHye
- 官方摘要证据：Pretraining hyperparameters are typically fixed before training begins, while the optimal configuration drifts as training proceeds. Existing automated methods, such as random search, Bayesian optimization, multi-fidelity scheduling, and population-based training, presuppose multiple trials or concurrent replicas; a single large-scale pretraining run yields one trajectory, precluding a second trial. We present EvoForge, to the best of our knowledge, the first system that places LLM agents in the control loop of a running distributed pretraining job. We cast online tuning as a single-trajectory, partially observable sequential decision problem, where observations are induced by past actions, and organize the system around three cooperating agents, namely, one for tuning, one for safety, and one for cross-task reflection. EvoForge distills rules into a two-layer experience store only after sufficient evidence has accumulated. In GPT-2 124M trained on 10B FineWeb-Edu tokens, EvoForge reduces the final validation loss by 4.15% relative to a tuned cosine schedule.

### 37. Gödel Ecology: Productivity-Guided Continuous Co-Evolution of Agents and Evaluators for Collective Recursive Self-Improvement

- 决定：`defer_agent_training_unverified`
- 原分类：`related_prompt_agent`
- 论文特定依据：摘要只说进化 agent/evaluator implementations，没有说明这些 implementation 是模型权重、adapter，还是 prompt/代码等外部工件。
- 模型参数/组件边界：agent/evaluator implementation 与 population state；是否含模型参数未知。
- 训练算法：生产力引导的连续共同演化。
- 反向传播：没有可确认的模型参数训练/反传证据。
- 待核实：必须核实 implementation 表示及 mutation/update operator 后才能判断。
- 原始来源：https://openreview.net/forum?id=N4GJVmrzsF
- 官方摘要证据：Self-improving coding agents rely on evolutionary search over their own implementations, with evaluators determining which variants survive. Recent work has begun to co-evolve agents and evaluators, but evaluator updates remain periodic and anchored to fixed criteria. We introduce Gödel Ecology, a framework of collective recursive self-improvement via productivity-guided continuous co-evolution of self-improving agents and evaluators. Evaluators are scored jointly with Co-Clade Metaproductivity of the agent lineages they induce, and a continuously updated soft mixture of evaluator candidates forms an adaptive evaluation landscape. Delayed credit assignment and adversarial interventions are additionally adopted to counter self-reinforcing evaluator drift with reliable external evidence. Together, these interacting populations form an evolving ecology in which agents and evaluation criteria actively interplay and shape one another. Across experiments on coding, math, and writing domains, Gödel Ecology produces stronger evaluator signals, better downstream search decisions, and improvements that transfer across benchmarks and model backbones. These results suggest that continuously adapting the evaluation criteria that determine which directions of improvement are worth pursuing helps make better recursive self-improvement.

### 38. Adaptive Evolutionary Pareto Search with Online Transferability Estimation for Resource-Aware LLM Adaptation

- 决定：`keep_unaffected`
- 原分类：`related_prompt_agent`
- 论文特定依据：复核保留：搜索 PEFT 层、rank 与 dropout 配置，并实际评估模型适配参数；核心包含模型参数训练而非仅外部工件更新。
- 模型参数/组件边界：PEFT 适配器/所选层参数及 Pareto archive。
- 训练算法：GA/DE/PSO/EDA 配置提议与 PEFT 评估。
- 反向传播：PEFT 候选训练是否反传及训练预算未由摘要说明。
- 待核实：每个候选实际适配的层、rank、dropout 和训练细节待核实。
- 原始来源：https://openreview.net/forum?id=N7vHnqiAZo
- 官方摘要证据：Adapting large language models to changing tasks and deployment requirements
requires balancing accuracy, latency, and memory under limited evaluation
resources.  Although parameter-efficient fine-tuning (PEFT) reduces adaptation cost, selecting which layers to adapt together with rank and dropout creates a combinatorial multi-objective search problem.
Under a fixed evaluation budget, reusing configurations from previous tasks can further waste evaluations when their usefulness on the new target is unknown. We present Adaptive Evolutionary Pareto Search with Online
Transferability Estimation (AEPS-OT), a framework
that allocates a fixed evaluation budget across multiple proposal mechanisms and
historical configurations. A controller uses the current search state and objective weights to select among
genetic algorithm (GA), differential evolution (DE), particle swarm optimization
(PSO), and estimation of distribution algorithm (EDA) proposals, while a
Pareto archive preserves search quality. To reuse experience from prior
tasks, AEPS-OT first probes historical configurations on the target task and
estimates transferability separately for accuracy, latency, and memory from rank agreement, stability, and
performance gains measured on the target task. The resulting scores, combined
using the current deployment preference, determine bounded source quotas, with all probes and transfers charged to the same 1,000-slot
target budget. On Qwen2-0.5B and the Internet Movie Database (IMDb) dataset,
five-seed independent audits give a mean
hypervolume of 0.193424, higher than all fourteen external
controls, including Bayesian optimization, fixed evolutionary operators, policy-learning baselines, classical multi-objective evolutionary algorithms and randomized search. In terms of mean audited hypervolume, AEPS-OT outperforms the base Adaptive Evolutionary Pareto Search (AEPS) by 4.4\%. Search using
target probes without subsequently adding historical configurations reaches 0.192410, indicating
that evaluating historical configurations on the target task accounts for most of the observed transfer gain.
These results support evaluating historical configurations on the current task before reusing them in resource-aware PEFT search under the evaluated single-model setting with one target task and four historical source tasks.

### 39. BOTAS: Bayesian Optimization for Zero-Shot Source Task Selection in Merging of LLMs

- 决定：`keep_unaffected`
- 原分类：`related_prompt_agent`
- 论文特定依据：复核保留：BO 选择已微调 checkpoint 子集并形成合并模型，属于非智能体模型合并。
- 模型参数/组件边界：合并后的 LLM 权重及源任务子集。
- 训练算法：离散 Bayesian optimization + model merging。
- 反向传播：合并阶段 training-free；源 checkpoint 的 fine-tuning 依赖训练但细节未述。
- 待核实：合并算法和 scaling coefficient 选择细节待核实。
- 原始来源：https://openreview.net/forum?id=TGI79TQF5v
- 官方摘要证据：Model merging combines independently fine-tuned checkpoints into a single model without joint training. However, existing evaluations assess the merged model only on the same in-domain source tasks, leaving zero-shot transfer to an unseen target task underresearched. To this end, we conduct an exhaustive study of source task subset selection for model merging, evaluating all $4{,}083$ subsets of 12 source tasks against 12 disjoint held-out target tasks, each at 40 scaling coefficients. Our results show that transfer is strongly aligned with the task family and that optimal mixtures typically involve fewer than 5 source tasks. We also show that a naive training-free solution based on training-free geometric selection, i.e., a task similarity measured by alignment between task vectors, does not identify the best mixture. To address this, we introduce BOTAS (Bayesian Optimization for TAsk Selection), which models the discrete space of source subsets with a Gaussian process surrogate. Without access to any target training data, BOTAS recovers the true optimal subset in 83\% of runs while exploring only 1.5\% of the search space. In addition, we show that in four out of twelve target tasks, the best merged subset outperforms full fine-tuning on the target itself. Finally, we release the full evaluation as a reusable benchmark for future source-selection methods.

### 40. From Knobs to Actions: Agentic Bayesian Optimization for Self-Improving System Tuning

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：EvoTune 用 agentic BO 调节数据库、Spark/LLM inference engine 的系统配置，未训练语言智能体模型。
- 模型参数/组件边界：系统配置、语义 Actions、图和 BO state。
- 训练算法：agentic Bayesian optimization。
- 反向传播：摘要未描述 LLM 参数训练。
- 待核实：LLM diagnosis 模块是否固定待核实。
- 原始来源：https://openreview.net/forum?id=am1vQQwJJ1
- 官方摘要证据：Modern systems such as Large Language Model (LLM) inference engines and databases expose large configuration spaces with strongly interacting parameters. Their workloads can change, making automated tuning essential. Bayesian optimization (BO) is sample-efficient for expensive black-box functions, but BO-based autotuners often underuse runtime metrics and parameter relationships, require many evaluations in high-dimensional spaces, and adapt slowly to workload shifts. We observe that transitions from suboptimal to better configurations follow recurring directions in parameter space. These directions remain partly stable across similar workloads, and LLMs can infer candidate directions from system knowledge. Building on this observation, we propose EvoTune, an agentic BO framework that searches over semantic Actions and refines them using trial evidence. EvoTune maintains an Action–Metric–Objective Graph to combine LLM-based diagnosis with model-based Action selection, while BO optimizes execution magnitudes and evidence and feasibility checks govern Action and graph updates. Across eight static workloads, EvoTune achieves the best observed endpoint, with average and maximum gains over a common initial reference of 33.47% and 55.19%, respectively. Under workload shifts, its post-switch throughput exceeds the strongest compared baseline by 11.42% on databases and 25.79% on Spark.

### 41. SPOON: Strategy-based Prompt Optimization for Multi-Agent LLM Games

- 决定：`defer_prompt_core`
- 原分类：`related_prompt_agent`
- 论文特定依据：SPOON 把多智能体策略直接表示为文本规则并做 strategy-based prompt optimization，且明确不更新模型权重。
- 模型参数/组件边界：多方 textual strategy rules/prompts。
- 训练算法：结构化 best-response prompt search。
- 反向传播：摘要明确 without updating model weights。
- 待核实：生成与评价规则的模型配置待核实。
- 原始来源：https://openreview.net/forum?id=cAhKtc1zVk
- 官方摘要证据：LLM agents can collaborate, negotiate, and compete in multi-agent settings where each player’s success depends on the actions of others. While multi-agent games provide a useful formalization of these settings, improving LLM agents’ performance in these games often relies on reinforcement learning, requiring access to model parameters and costly training across many optimization iterations. To address this, we propose SPOON, a strategy-based prompt optimizer that represents each player’s strategy as explicit rules written in text and refines them without updating model weights. Our strategic abstractions compress many game histories into shared states, allowing one rule update to improve behavior across multiple situations. Explicit strategies enable our method to examine how both players’ rules interact and guide structured best-response search, directly improving each player’s strategy in response to another as they co-evolve across optimization iterations. Across 19 existing benchmarks spanning classical multi-agent games, practical multi-agent applications, and an extension to prompt optimization for single-agent tasks, our method improves optimization efficiency and held-out performance compared with training-based and prompt optimization baselines.

### 42. A Risk-Bounded Gate for Self-Improving Agents: Selecting Modifications as a Mean–Variance Knapsack

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：方法选择 memory、reflection、judge、cache、restart 和 prompt add-ons 等外部修改，测试使用 frozen LLM packer。
- 模型参数/组件边界：agent modification subset 与 knapsack statistics。
- 训练算法：mean–variance knapsack、精确求解/局部搜索。
- 反向传播：摘要明确 frozen LLM packer。
- 待核实：live packer run 尚未完成；当前结果含合成测试。
- 原始来源：https://openreview.net/forum?id=fPPQnFGSYd
- 官方摘要证据：Self-improving agent systems accumulate modifications—memory modules, reflection steps, judges, caches, extra restarts—each promising a gain on a benchmark. Recent re-evaluations show that stacking them often increases run-to-run variance and that reported gains can reverse under a shuffled task order. We treat modification selection as a mean–variance knapsack: given measured mean effects, pairwise interactions, a covariance of effects across runs and a phase-resolved cost vector, choose the subset that maximises expected gain subject to a cost budget and a variance ceiling. Mean-only selection is the unconstrained corner of this problem and is blind to correlated noise. We give an exact solver for pools of up to sixteen modifications, a variance-penalised greedy and a diversity-seeded local search; on synthetic instances with correlated noise the last recovers the exact optimum on 10 of 10 instances (greedy 4, genetic algorithm 6), but pays off over enumeration only from M=16. We lock a measurement protocol with held-out validation on a disjoint task stream: a two-agent knapsack testbed with a computable optimum, twelve pre-registered prompt add-ons, and a frozen LLM packer. The live packer run is pre-registered and pending; every number reported here comes from running the same fitting and selection pipeline end-to-end on a synthetic ground truth built from our own model. There, mean-only selection inflates true held-out variance 3–20×, the inflation grows with the correlation of add-on noise, and five held-out runs suffice to detect it; but the pre-registered ceiling at the base noise level keeps only a quarter of the gain, a kill we report. An exploratory, not pre-registered, sweep finds that a ceiling of 3σ̂₀ recovers median full gain at ρ=0.8 only, at about half the mean-only variance. We also show why: with K runs the estimated covariance has rank K−1, so a tight ceiling can be met along directions the data never saw, and we pre-specify the shrinkage diagnostic that exposes this. The frozen harness, pool, prompts, analysis script and protocol are released so that the live run can be performed without changing anything.

### 43. $\text{Turing}^2$: Scaling Turing-Style Evaluation to Optimize Human Simulation in Dialogue

- 决定：`defer_prompt_core`
- 原分类：`related_prompt_agent`
- 论文特定依据：Turing² 明确通过 prompt optimization 共同改进 user simulator 与 Machine-Turing judge，并明确不更新模型参数。
- 模型参数/组件边界：simulator prompt 与 judge prompt。
- 训练算法：human-grounded co-evolutionary prompt optimization。
- 反向传播：摘要明确 without updating model parameters。
- 待核实：人类评价批次与 prompt 更新细节待核实。
- 原始来源：https://openreview.net/forum?id=jdJFvMPRZK
- 官方摘要证据：Realistic user simulation is essential for developing and evaluating conversational AI agents, yet measuring and optimizing simulation fidelity remains challenging. Human Turing tests assess whether simulated behavior appears human, but are costly to use for iterative optimization, motivating scalable evaluation with Machine-Turing judges. We introduce $\text{Turing}^2$, a human-grounded co-evolutionary framework for improving user simulators and Machine-Turing judges through prompt optimization, without updating model parameters. Machine-Turing judges provide rewards and diagnostic feedback to improve simulators, while human Turing judgments and explanations guide judge refinement. The refined judge then provides feedback for further simulator improvement. In customer-service dialogue, simulator optimization improves Turing win rates under both held-out LLM judges and human annotators. Incorporating human explanations improves held-out judge accuracy, and optimizing against the refined judge further improves simulator human-perceived human-likeliness. These results demonstrate the effectiveness of \turing in jointly improving user simulators and their evaluators through human-grounded co-evolution.  The dataset would be released upon acceptance.

### 44. ECO: Energy-Oriented Configuration Optimization for Attention–FFN Disaggregated LLM Serving

- 决定：`keep_unaffected`
- 原分类：`related_prompt_agent`
- 论文特定依据：复核保留：约束 BO 搜索 GPU/serving 部署配置，没有 LLM 代理参与反馈式工件生成，属于推理系统配置优化。
- 模型参数/组件边界：部署配置、GPU 设置与 GP correction state。
- 训练算法：成本感知约束 Bayesian optimization。
- 反向传播：不涉及 LLM 参数训练；GP 拟合细节未述。
- 待核实：校准模型的参数学习方式待核实。
- 原始来源：https://openreview.net/forum?id=nABfUhZWr9
- 官方摘要证据：Efficient large language model serving requires reducing energy while preserving latency and throughput. Attention–feed-forward network disaggregation exposes separate resource and operating choices, but their interactions create a large configuration space. Existing profile-based approaches require substantial offline measurements and need additional calibration data when deployed on new hardware. Untested configurations may also fail execution or violate service targets. We present Energy-Oriented Configuration Optimization (ECO), a framework for jointly tuning deployment and GPU operating settings within a limited measurement budget. ECO combines a calibrated stage-time and energy model with Gaussian-process corrections and cost-aware constrained Bayesian optimization. It separately models execution validity and service feasibility, selecting measurements according to expected energy improvement and GPU-time cost. The lowest-energy measured feasible configuration is then frozen for serving. Experiments with Qwen and DeepSeek cover A100 and A6000 GPUs. Across eight A6000 and four four-GPU A100 scenarios, ECO reduces serving energy by 44.4% and increases output token rate by 23.8% on average relative to Default while meeting service targets. Across eight A6000 scenarios, its selected feasible energy averages 33.1% below Bayesian optimization and 25.8% below genetic search.

### 45. The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators

- 决定：`defer_agent_training_unverified`
- 原分类：`related_prompt_agent`
- 论文特定依据：RQGM 共同演化 coder/writer/reviewer/grader，但摘要未说明被改写的是模型权重、adapter、prompt 还是代码。
- 模型参数/组件边界：agent 与 evaluator 的实现/政策、评价目标和 population state；参数类型未知。
- 训练算法：非平稳效用下的 evolutionary co-evolution。
- 反向传播：模型参数训练和反传证据不足。
- 待核实：需核实 co-evolved reviewer/writer/grader 的表示与更新算子。
- 原始来源：https://openreview.net/forum?id=o3txFJw4JR
- 官方摘要证据：Self-improving agents are state-of-the-art on agentic coding benchmarks, yet their search methods assume a stationary evaluation criterion. This ignores a central feature of evolution: species adapt as their environments change with them. We introduce the Red Queen Godel Machine (RQGM), an evolutionary framework for recursive self-improvement under non-stationary utilities. This allows learned evaluators to improve alongside the agents they guide. On DeepSWE, the RQGM improves over its fixed-evaluator baseline by adding a complementary agent-as-a-judge code-review signal: a co-evolved reviewer grades coder patches to guide search. At low reasoning effort, the RQGM coder passes 82.1% of held-out tasks against the baseline's 75.0%, and nearly matches the GPT-6 Astra model at high effort. In scientific paper writing and reviewing, and Olympiad-level proof writing and grading, co-evolved evaluators provide an evaluation criterion. Anchored to human IMO grades, a co-evolved grader writes its own milestone rubric and exceeds static baselines at a 3x lower search cost, driving the prover to the best mean score. Since the RQGM can modify the search objective across epochs, it can regularize the search. For example, the RQGM reduces self-preference bias via an additional adversarial objective to discover reviewers equally stringent on AI and human work. Guided by these calibrated reviewers, co-evolved writers reach 1.78x-1.86x higher acceptance rates than the baseline under an agent-as-a-judge panel. The RQGM enables self-improving systems where agents and evaluators recursively bootstrap each other beyond the limits of static evaluation.

### 46. AIM: Agentic Idea Management for Automated Research

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：AIM 管理研究想法、解候选和实验预算，摘要没有训练语言智能体模型参数。
- 模型参数/组件边界：研究想法、surrogate/acquisition state 和分支预算。
- 训练算法：受 BO 启发的 agentic idea search。
- 反向传播：未描述模型反传。
- 待核实：Agentic Surrogate 是否仅由提示调用实现待核实。
- 原始来源：https://openreview.net/forum?id=rnK26MhdGM
- 官方摘要证据：Frontier LLMs are increasingly used to automate scientific research through iterative search. We distinguish idea-driven search from solution-driven search and identify three core challenges: organizing evolving research ideas, selecting promising directions, and maintaining alignment between ideas and their implementations. To address these challenges, we introduce the Agentic Idea Manager (AIM), a fully autonomous framework for managing and exploring research directions in idea-driven automated research. Inspired by Bayesian optimization, AIM uses an Agentic Surrogate and an Agentic Acquisition mechanism to organize discovered ideas and guide their selection. A Solution Auditor maintains idea-solution integrity, while a Resource Planner adaptively allocates the remaining experimental budget across parallel search branches. Experiments on 10 AutoLab benchmark tasks show that AIM surpasses the strongest baseline by 1.6 percentage points on System Optimization tasks and 4.9 percentage points on long-horizon Model Development & CUDA tasks. Notably, AIM reaches the best baseline performance up to 3.1x faster in wall-clock time. We further provide a theoretical analysis of when searching over ideas becomes beneficial. Our analysis shows that explicit idea-level allocation makes semantic coverage directly controllable, and that broader coverage becomes increasingly valuable when competitive research directions are sparse among many plausible alternatives.

### 47. AscendOptimizer: Episodic Agent for Ascend NPU Operator Optimization

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：AscendOptimizer 更新 tiling/data-movement 配置、kernel 程序和执行经验，而非代理模型参数。
- 模型参数/组件边界：AscendC kernel、host tiling 配置与 episodic knowledge。
- 训练算法：硬件反馈闭环 evolutionary configuration search。
- 反向传播：摘要未描述模型参数训练。
- 待核实：用于重写程序的 LLM 是否固定待核实。
- 原始来源：https://openreview.net/forum?id=wtVho001dF
- 官方摘要证据：Optimizing AscendC (Ascend C) operators for Ascend NPUs is difficult for two reasons. First, unlike CUDA, the ecosystem offers few public kernels to learn from. Second, performance depends on a coupled two-part implementation: a host-side tiling program that controls data movement and a kernel program that schedules and pipelines computation. We present AscendOptimizer, an episodic agent that builds missing optimization knowledge from execution itself. For kernel optimization, AscendOptimizer rewinds strong implementations by removing optimizations in a controlled way, then keeps the changes whose removal measurably hurts performance as reusable experience for later rewriting. For host-side optimization, it runs profiling-in-the-loop evolutionary search to find valid, fast tiling and data-movement configurations directly from hardware feedback. On a transductive benchmark of 101 real AscendC operators, AscendOptimizer achieves a 1.21× geometric-mean speedup over the open-source references, and 53.47% of operators run faster than those references. With hardware-evaluation counts matched across methods, its aggregate geometric-mean speedup exceeds Best-of-N sampling, OpenEvolve, CudaForge, and EvoKernel.

### 48. TABRSI: A RECURSIVE SELF-IMPROVING MULTI- AGENT SYSTEM FOR TABLE UNDERSTANDING AND REASONING

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：DGM/HGM-Flow 演化的是角色代码、拓扑和推理模式等可执行多智能体流水线工件，没有模型参数训练证据。
- 模型参数/组件边界：角色代码、pipeline topology 和 CoT/PoT 模式。
- 训练算法：code mutation 与多智能体 pipeline evolution。
- 反向传播：摘要未描述底座模型反传。
- 待核实：solver self-edits 的具体代码边界待核实。
- 原始来源：https://openreview.net/forum?id=ypByqdkzf3
- 官方摘要证据：Autonomous recursive self-improvement enables coding agents to iteratively refine their internal logic, yet whether these mechanisms generalize beyond software engineering to complex tabular reasoning, and whether performance lifts stem from algorithmic search depth or structural task levers, remains an open question. We investigate self-improving agents across seven structured-table benchmarks by formalizing a unified design space spanning search policies (greedy Darwin Gödel Machines vs. Clade-Metaproductivity in Huxley-Gödel Machines) and system architectures (monolithic solo solvers vs. modular role teams). To overcome the expressivity bottlenecks of monolithic scripts, we introduce DGM-Flow and HGM-Flow, which decompose the agent into an independently evolvable pipeline of specialized roles, Parser, Planner, Solver, Verifier, and Formatter}, governed by topological gating, code mutations, and per-role reasoning modalities (Chain-of-Thought vs. Program-of-Thought) backed by a finite-sample non-regression guarantee. Across all seven benchmarks on a unified DeepSeek-v4-flash backbone, empirical gains follow a regime law: performance lifts do not track evolutionary search depth, but rather the presence of an executable tool or structural lever targeting an addressable dominant bottleneck. Where addressable bottlenecks exist, role decomposition and solver self-improvement achieve held-out verified wins, including an absolute gain of $24\%$ in accuracy on HiTab via hierarchical header reconstruction, an absolute gain of $15\%$ on MultiHiertt through algorithmic parse-then-compute routines, and up to $71\%$ absolute accuracy recovery on MMTU subtasks via program-aided verification and formatting. Conversely, search-rule deltas remain within evaluation noise on interpretation-bound or saturated tasks, co-evolving solvers jointly with role teams fails to generalize over decoupled application, and semantic LLM-judge evaluations expose that unconstrained solver self-edits frequently optimize superficial formatting envelopes rather than genuine reasoning capabilities.

### 49. Generate and Select: A Framework for Bayesian Optimization with LLM Proposals

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：黑盒 LLM 在自适应反馈闭环中反复依据既往观测生成结构化候选，GP-BO 从累计池选择评估对象；更新的是候选池、观测与 surrogate，不是 LLM 参数。
- 模型参数/组件边界：结构化候选池、观测和 GP surrogate；生成 LLM 参数未训练。
- 训练算法：黑盒 LLM candidate generation + GP-BO selection。
- 反向传播：摘要未训练生成 LLM；GP 拟合方式未详述。
- 待核实：四项任务的候选类型和 backend 配置待核实。
- 原始来源：https://openreview.net/forum?id=zENuM3JgRz
- 官方摘要证据：Optimizing structured objects, such as molecules and symbolic
expressions, is difficult because the candidate domain is vast, often
implicit, and contains many invalid or low-quality objects. Large
language models (LLMs) can construct promising candidates, but generation
alone does not allocate scarce black-box evaluations. We introduce
generate-and-select (GaS), a modular framework that separates candidate
generation from evaluation selection within an adaptive feedback loop.
At each iteration, a black-box LLM generates $r$ candidates from previous
observations, and Bayesian optimization (BO) with a Gaussian-process (GP)
surrogate selects $q$ candidates from a cumulative pool. Assuming generation supplies improvement opportunities, we
bound Bayesian simple regret relative to the best generator-reachable
value in terms of generator improvement and cumulative missed
improvements in selection. Expected
regret vanishes exactly when average expected missed improvement
vanishes, and a GP Thompson sampling (GP--TS) specialization depends on
information gain over the generator-reachable domain. Across four
structured and synthetic tasks, GaS matches or outperforms direct LLM
optimizers and BO--LLM methods, with statistically significant gains over
the strongest baseline on three. It achieves comparable or better
performance than the closest BO--LLM baseline while using over two orders
of magnitude fewer LLM tokens. Together, these results establish \gas{}
as a strong, modular, and efficient framework for BO with LLM-generated
candidates.

### 50. AT-AT: Automatic Tool Optimization from Agent Traces

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：AT-AT 明确保持 agents fixed，只编辑共享工具描述和实现。
- 模型参数/组件边界：tool descriptions、tool implementations 和轨迹历史。
- 训练算法：trace-driven tool editing/evaluation。
- 反向传播：摘要明确 holding the agents fixed。
- 待核实：轻量 coding agent 是否固定模型调用待核实。
- 原始来源：https://openreview.net/forum?id=pp2JaGrr0r
- 官方摘要证据：Efforts to improve LLM-based agents typically focus on modifying the agent itself, yet success also depends on the environment in which an agent acts. Tools mediate this interaction: a tool's description shapes how an agent calls it, and its implementation determines the results and errors the agent receives afterwards. Many tools, such as APIs and MCP servers, are shared by many agents and maintained by providers who cannot change those agents. We introduce AT-AT (Automatic Tool Optimization from Agent Traces), an agentic tool optimizer that improves a shared toolset offline from historical agent executions while holding the agents fixed. A lightweight coding agent reads agent trajectories and their evaluation results, and selectively edits tool descriptions and, when permitted, implementations. On $\tau^2$-bench-verified, AT-AT achieves the highest task completion rates in the Airline and Telecom domains at lower cost than strong prompt- and tool-optimizer baselines, and its Telecom gain is statistically significant under paired permutation tests. Optimizing the tools within a coding agent harness also improves held-out performance on TerminalBench-2 and TBLite. On three enterprise MCP servers in production, applying AT-AT to production logs increased held-out task passes on two servers and reduced tool errors on the third.
By turning accumulated execution traces into updates to shared tool environments, AT-AT provides a path toward continual improvement of agent systems through environment-side learning.

### 51. Self-Evolution Should Be Stable, Not Frozen: Lyapunov-Gated Recursive Self-Improvement

- 决定：`defer_agent_training_unverified`
- 原分类：`related_prompt_agent`
- 论文特定依据：EVOLYAPUNOV 接纳 agent/improver 自修改，但摘要未说明自修改究竟包含模型权重还是外部 prompt、代码或记忆。
- 模型参数/组件边界：agent self-modifications、improver/meta-operation 与风险状态；参数类型未知。
- 训练算法：matched perturbation branches + Lyapunov-gated selection。
- 反向传播：模型参数训练/反传证据不足。
- 待核实：需核实 candidate self-modification 的序列化形式与持久对象。
- 原始来源：https://openreview.net/forum?id=3t0j2Y05EH
- 官方摘要证据：Recursive self-improving agents increasingly modify not only their task behavior, but also the mechanisms that generate future modifications. This creates a control problem that current self-evolution objectives do not measure: a change can improve the next agent while making future evolution increasingly sensitive to evaluator noise, misleading memories, reward misspecification, or mutation randomness.
We formulate recursive self-improvement as a non-stationary stochastic dynamical system and introduce EVOLYAPUNOV, a stability-constrained framework that allows the improver itself to evolve without freezing the meta-operation. EVOLYAPUNOV estimates an interventional evolution response operator from matched perturbation branches, decomposes evolution into capability and risk subspaces, and admits candidate self-modifications only when useful directions improve while measured risk dynamics satisfy a confidence-aware Lyapunov drift condition and an empirical finite-horizon amplification bound.
We define the Recursive Amplification Factor (RAF) and evolution risk half-life, which expose failure modes invisible to one-generation benchmark scores. Under a stochastic drift condition, accepted updates keep expected risk energy bounded despite persistent perturbations; a complementary amplification bound connects the certificate to multi-generation error propagation.
Our evaluation protocol spans SWE-bench Verified, Multi-SWE-bench, τ²-Bench, BFCL V4, and ARC-AGI-2 with Qwen2.5-Coder-7B-Instruct and Qwen2.5-7B-Instruct backbones. A stress study reveals a sharp recursive stability boundary: unrestricted self-evolution can continue improving immediately after the estimated risk gain exceeds one, whereas Lyapunov-gated evolution remains on a capability–stability Pareto frontier.
The central claim is that recursive self-improvement need not choose between open-ended evolution and stability; it should expand useful directions while contracting the directions along which mistakes compound.

### 52. SCAMP: Black-Box Knowledge Poisoning Attack on Multimodal Retrieval-Augmented Generation

- 决定：`defer_agent_training_unverified`
- 原分类：`related_prompt_agent`
- 论文特定依据：SCAMP 更新图文投毒对和视觉原型；Visual/Text Attacker、Competing Agents 与 Evaluators 是否另行训练模型参数，摘要未说明。
- 模型参数/组件边界：明确更新投毒图文对和 prototype；代理/评估器参数状态未知。
- 训练算法：self-competitive black-box candidate optimization。
- 反向传播：目标检索/生成系统无需梯度访问；攻击代理是否反传训练未知。
- 待核实：需核实 attacker/evaluator 是固定模型调用还是参数化训练组件。
- 原始来源：https://openreview.net/forum?id=O26AmnGkFD
- 官方摘要证据：Large vision–language models benefit from multimodal retrieval-augmented generation, which grounds responses in external image–text evidence to mitigate hallucination. However, reliance on external knowledge bases introduces a critical vulnerability: knowledge poisoning. Existing poisoning methods are often impractical, as they rely on white-box access, target limited sample-wise scenarios, and neglect reranking components. Additionally, they underutilize the visual modality's potential and suffer from cross-modal inconsistencies. We propose SCAMP, a black-box framework that iteratively crafts aligned poisoned pairs through a self-competitive agent loop. SCAMP integrates a Visual Attacker and a Text Attacker to jointly optimize, Competing Agents to simulate benign samples and improve attack generalization, and three Evaluators to guide optimization via retrieval, generation, and consistency feedback. For class-wise attacks, we introduce agent-driven prototype synthesis to construct effective visual anchors without gradients. Extensive experiments show SCAMP consistently outperforms baselines in black-box settings and remains robust against diverse defenses.

### 53. Breaking the Refusal Barrier: Stochastic Discovery of Residual  Unsafe Behaviors in Aligned Language Models

- 决定：`keep_unaffected`
- 原分类：`related_prompt_agent`
- 论文特定依据：复核保留：SEEK 用随机输入/响应采样生成安全训练数据，明确不做语义 prompt optimization 或 attacker-LLM 闭环，并随后真实 fine-tune 模型参数。
- 模型参数/组件边界：后续 safety-tuned LLM 参数；发现阶段更新覆盖集。
- 训练算法：随机输入扰动采样 + safety fine-tuning。
- 反向传播：发现阶段无梯度；最终 fine-tuning 会训练模型，具体反传配置未说明。
- 待核实：安全微调算法和数据过滤细节待核实。
- 原始来源：https://openreview.net/forum?id=T8c8NM6FT4
- 官方摘要证据：LLM safety alignment often creates refusal modes: dominant, high-probability regions of the output space that steer generation toward refusals, while residual unsafe behaviors persist in low-probability regions. Alignment suppresses harmful responses but need not eliminate these underlying behaviors, raising a practical question for iterative safety hardening: how can residual unsafe behaviors be efficiently discovered and converted into safety-training data? We formulate this as stochastic exploration rather than adversarial prompt optimization, showing that random input perturbations redistribute the model's response distribution away from dominant refusal modes and toward low-probability unsafe modes. Building on this, we introduce SEEK (Stochastic Exploration to Elicit residual-behavior Knowledge), a simple inference-only framework that repeatedly samples perturbed inputs and responses to discover diverse residual unsafe behaviors, without gradient optimization, semantic prompt engineering, or auxiliary attacker LLMs. We cast discovery as a coverage objective and show that coverage increases monotonically with the sampling budget, asymptotically recovering all reachable unsafe behaviors. Across five safety-tuned LLMs and two benchmarks, SEEK's discovery matches or exceeds white-box optimization at larger budgets while using one to two orders of magnitude less compute, and consistently exceeds more efficient optimization-, embedding-, transfer-, and attacker-LLM-based methods. Finally, fine-tuning on SEEK-discovered failures substantially improves robustness, cutting attack success from $90-100\%$ to at most $22\%$ across optimization-, embedding-, transfer- and attacker-LLM-based attacks, while preserving general task performance. Stochastic exploration thus offers a simple, efficient alternative to adversarial prompt optimization for residual-behavior discovery and safety-data generation.

### 54. In-Context Robot Learning with VLM Agents

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：GPT-Policy 是 VLM agent，但摘要明确只做部署期上下文适配，不做梯度更新或任务参数持久修改。
- 模型参数/组件边界：示范/反馈 context、grounding 与 action chunks。
- 训练算法：in-context robot learning。
- 反向传播：摘要明确 without gradient updates or persistent task-specific parameter changes。
- 待核实：context compiler/harness 是否含另训组件待核实。
- 原始来源：https://openreview.net/forum?id=LIa6SeOhH9
- 官方摘要证据：Enabling robots to adapt to unfamiliar environments as readily as humans remains a moonshot goal of embodied AI. No finite collection of demonstrations can cover every task and situation a robot will encounter, making the ability to learn from context at deployment essential for generalization. Such in-context learning (ICL), however, remains largely beyond the reach of existing robotic policies. The broad agentic capabilities of commercial vision-language models (VLMs), such as GPT-6 Astra, raise a compelling question: can these models learn from demonstrations and interaction feedback, then translate that information into executable robot behavior without gradient updates or persistent changes to task-specific parameters? We introduce GPT-Policy, a general-agent framework for in-context robot learning. GPT-Policy equips a VLM agent with a context compiler that organizes task-relevant information and an execution harness that supports geometric grounding, action chunking, and closed-loop decision-making through execution feedback. We evaluate GPT-Policy on ten real-world tasks spanning five context types and six RoboDojo simulation tasks. Across four real-world demonstration tasks, mean success rate increases from 10% without demonstrations to 80% with human videos or robot demonstrations that include action references. Videos provide procedural guidance, while action references can clarify motion details. Targeted ablations suggest that calibrated localization and action chunking improve success and execution efficiency. On these six RoboDojo tasks, one-shot GPT-Policy achieves 83.3% mean success. These results suggest that general-purpose VLMs can use deployment-time context to adapt robot behavior, while reliable physical execution remains a challenge.

### 55. Code-Probe-Adapt: Interactive Heuristic Learning for Self-Evolving Agents

- 决定：`defer_agent_no_model_training`
- 原分类：`related_prompt_agent`
- 论文特定依据：COPA 通过 REPL 探测和修订 code-as-policy heuristic，摘要明确整体无需梯度更新。
- 模型参数/组件边界：可执行 code-as-policy、heuristic 与 REPL state。
- 训练算法：事件触发的交互式代码策略修订。
- 反向传播：摘要明确 without gradient updates。
- 待核实：使用的 LLM 底座及代码持久化边界待核实。
- 原始来源：https://openreview.net/forum?id=zeF8echOqR
- 官方摘要证据：Existing LLM-based autonomous agents generally follow two paradigms: ReAct-
style methods, which interleave dense reasoning with continuous API calls; and
code-as-policy methods, which synthesize executable code to bypass LLM infer-
ence at runtime. However, in long-horizon interactive tasks, ReAct agents incur
prohibitive inference costs and context overload, whereas offline policies lack test-
time adaptability to unforeseen environmental dynamics. To bridge this gap, we
introduce Code-Probe-Adapt (COPA), an interactive heuristic learning framework
that transitions LLM agents from post-hoc log analyzers to active, online policy
designers. Equipped with a persistent REPL (Read-Eval-Print Loop) harness,
COPA enables live, on-demand introspection. To enable adaptive code-as-policy,
COPA modulates policy execution using adaptive step budgets and event-triggered
interruptions, returning control to the agent for immediate diagnostic probing and
policy refinement. Evaluated on five games, COPA significantly outperforms re-
cent LLM-based policy synthesizers, and demonstrates superior sample efficiency
compared to extensively trained reinforcement learning (RL) algorithms. Notably,
on the hard-exploration task Montezuma’s Revenge, where offline LLM heuristic
learning fails entirely (scoring 0 even after 6.0M steps), COPA’s interactive prob-
ing achieves an average score of 4,900 in 2.4M steps. This result also compares
favorably against the RL baseline DreamerV3 (1,853.5 at 200M steps, digitized
from its learning curve), scoring 2.6× as high with fewer environment interactions.
Attained entirely without gradient updates or task-specific engineering, COPA
successfully unites the execution efficiency of code with the adaptive power of live
debugging.
