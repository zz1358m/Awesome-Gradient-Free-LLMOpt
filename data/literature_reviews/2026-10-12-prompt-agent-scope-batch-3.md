# 2026-10-12 提示词与智能体范围收紧：第 3 批逐篇审查

本报告逐篇依据仓库已保存的 OpenReview 官方投稿摘要审查 55 条记录；未发起新检索。决定只反映 2026-10-12 用户范围例外，不评价论文有效性或学术质量。

## 汇总

- 保留：非本次提示词/智能体范围：10 条
- 保留：明确训练或持久更新模型/策略参数：4 条
- 暂缓：提示词为核心对象：5 条
- 暂缓：智能体但不训练模型参数：31 条
- 暂缓：智能体参数训练证据待核实：5 条

## 逐篇决定

### 1. Context-Space Adaptation of Frozen Multimodal Large Language Models for Medical Image Diagnosis

- 决定：`keep_unaffected`（保留：非本次提示词/智能体范围）
- 依据：研究对象是冻结医学 MLLM 的视觉样例、检索键和诊断经验上下文适配，不是提示词优化，也不是智能体模型训练研究。
- 模型/状态更新对象：无模型参数更新；持久对象为视觉样例、检索键和经验状态。
- 训练或搜索算法：DECS 样例选择与 SRES 经验汇总。
- 反向传播：摘要明确预训练 MLLM 冻结且不更新。
- 待核实：DECS/SRES 是否包含另训辅助组件仍待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=6JkxoF616C)

### 2. Constructive Prediction: The Role of Lexical Code Organization in Language Modeling

- 决定：`keep_unaffected`（保留：非本次提示词/智能体范围）
- 依据：研究词汇条目到共享路径编码的语言模型表示及训练，不以提示词或智能体为核心。
- 模型/状态更新对象：ILM 语言模型参数。
- 训练或搜索算法：常规下游语言模型训练；摘要未说明优化器。
- 反向传播：摘要说明进行 language-model training，但未说明反传细节。
- 待核实：具体训练目标、优化器和参数范围待原文核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=DXrf6mhnGR)

### 3. Confidence-Adaptive Permutation-Tree Self Speculative Decoding for Diffusion Large Language Models

- 决定：`keep_unaffected`（保留：非本次提示词/智能体范围）
- 依据：CAPSpec 是 diffusion LLM 的训练-free 推测解码，不属于提示词优化或智能体模型训练范围。
- 模型/状态更新对象：不更新模型参数；运行时更新 permutation tree、置信分区和接受路径。
- 训练或搜索算法：置信自适应树剪枝及单次批量前向验证。
- 反向传播：摘要明确 training-free。
- 待核实：实现中的缓存和验证细节待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=heTK8MXaWg)

### 4. Component-Aware Feedback for Self-Evolving Programs

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：LLM 充当 mutator，核心更新对象是多组件程序及其归因记忆；摘要没有训练或持久更新语言模型参数。
- 模型/状态更新对象：候选程序、组件改动归因记忆和 fitness 历史。
- 训练或搜索算法：LLM-guided evolutionary program search。
- 反向传播：摘要未描述模型反传或参数训练。
- 待核实：mutator LLM 与评估器是否完全固定待原文核实，但所提更新机制仅落在程序和记忆。
- 原始来源：[OpenReview](https://openreview.net/forum?id=PtpPmfGxts)

### 5. Competition Discovers, Cooperation Consolidates: Social Rewards Shape Self-Evolving LLM Agents

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：自演化来自交互轨迹筛选并写入持久外部记忆；摘要没有模型参数训练。
- 模型/状态更新对象：多智能体轨迹、社会信用和持久外部记忆。
- 训练或搜索算法：竞争/合作社会奖励驱动的经验筛选。
- 反向传播：未说明反传；摘要把改进载体明确为 persistent external memory。
- 待核实：所用代理底座和记忆 updater 实现待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=plmHDI1b7d)

### 6. CompEvolve: Competitive Evolution of LLM Agent Harness Regularized by Behavioral Diversity and Generalization Judging

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：CompEvolve 明确进化 prompt、控制流和多智能体 harness，而非模型权重。
- 模型/状态更新对象：prompt、控制流、多智能体结构和候选 harness。
- 训练或搜索算法：竞争式进化、行为多样性选择和重组。
- 反向传播：摘要明确 modifies the harness rather than model weights。
- 待核实：LLM architect/judge 是否另训未说明。
- 原始来源：[OpenReview](https://openreview.net/forum?id=4IVbz5H9ER)

### 7. Collective Alignment in LLM Multi-Agent Systems: Disentangling Bias from Cooperation via Statistical Physics

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：该多智能体研究只查询固定 LLM 更新晶格二元状态并测量群体现象，没有训练智能体模型参数。
- 模型/状态更新对象：晶格代理的运行时二元状态及统计量。
- 训练或搜索算法：温度扫描、有限尺寸标度和有效耦合/场估计。
- 反向传播：摘要未描述模型训练或反传。
- 待核实：采样与模型部署细节待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=Qj9Mbp6dCi)

### 8. Code to Control: Synthesizing Parameterized Reactive Controllers

- 决定：`keep_agent_model_training`（保留：明确训练或持久更新模型/策略参数）
- 依据：LLM 生成控制器结构后，derivative-free search 持久拟合可执行策略的连续控制参数；这属于明确的策略参数训练。
- 模型/状态更新对象：参数化 Python controller 的连续策略参数。
- 训练或搜索算法：环境反馈驱动的 derivative-free parameter search。
- 反向传播：控制器参数搜索不依赖反传；LLM 本身是否训练未说明。
- 待核实：控制器参数化形式、搜索算法和持久保存方式待原文核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=z62vbEOWDO)

### 9. Co-Evolving LLM Agents and Bayesian Optimizers for Automated Feature Engineering

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：CoEvolve 更新特征变换、双记忆、FE-MDP/DSGO 代理状态；摘要没有训练 LLM agent 的模型参数，辅助 surrogate 更新不等同代理政策训练。
- 模型/状态更新对象：特征集、变换、CAM/UAM、FE-MDP 与 DSGO surrogate 状态。
- 训练或搜索算法：局部 beam expansion 与 BO expected improvement。
- 反向传播：摘要未说明 LLM 参数反传；辅助 surrogate 的训练细节未给出。
- 待核实：FE-MDP/Set Transformer 的训练方式待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=Oal3lWxqBY)

### 10. Characterizing and Improving Bijection Attacks through Prompt-Level Perturbation

- 决定：`defer_prompt_core`（暂缓：提示词为核心对象）
- 依据：核心对象是双射编码 prompt 及 prompt-level perturbation，SLS 直接搜索可成功越狱的提示编码。
- 模型/状态更新对象：双射编码提示及其 perturbation。
- 训练或搜索算法：gradient-free Signed Langevin Search。
- 反向传播：搜索以模型反馈进行，摘要未声明训练目标模型参数。
- 待核实：白盒设置使用哪些信号待原文核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=Jq6I5yUXXR)

### 11. CUDA-Harness: Harnessing Agentic CUDA Kernel Generation and Optimization from Natural Language

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：CUDA-Harness 的智能体生成、验证和演化 CUDA kernel 程序；摘要没有模型参数更新。
- 模型/状态更新对象：CUDA kernel 源码、中间结构和候选程序。
- 训练或搜索算法：Feedback-Adaptive Evolution。
- 反向传播：未描述语言模型训练或反传。
- 待核实：生成 LLM 与验证器是否固定待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=PdZhD2bbqe)

### 12. COMIC: Agentic Sketch Comedy Generation

- 决定：`defer_agent_training_unverified`（暂缓：智能体参数训练证据待核实）
- 依据：COMIC 明确演化剧本和渲染候选，但“与观众偏好对齐的 LLM critics”是否通过模型参数训练获得，摘要没有说明。
- 模型/状态更新对象：已明确更新剧本和视频候选；critic 参数是否更新未知。
- 训练或搜索算法：多岛相对演化与渲染锦标赛。
- 反向传播：剧本搜索无需推断反传；critic 的训练/反传证据不足。
- 待核实：需核实 LLM critics 的对齐究竟是提示/检索还是参数训练。
- 原始来源：[OpenReview](https://openreview.net/forum?id=Rfj9wv4EDR)

### 13. CB-Orchestrator: Adaptive Workflow Optimization for LLM Agents via Contextual Bandits

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：两阶段方法只进化工作流池并用 contextual bandit 选择工作流，未训练 agent 模型参数。
- 模型/状态更新对象：工作流池及 bandit 选择状态。
- 训练或搜索算法：evolutionary search + contextual bandit。
- 反向传播：摘要未描述语言模型反传。
- 待核实：bandit 参数化和持久化实现待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=YEDtlblPEM)

### 14. BoLT: A Benchmark to Democratize Black-box Optimization Research for Expensive LLM Tasks

- 决定：`keep_unaffected`（保留：非本次提示词/智能体范围）
- 依据：BoLT 是覆盖多类 LLM 训练/推理配置的 BBO benchmark，prompt 仅是众多问题之一，也不是智能体研究。
- 模型/状态更新对象：随 benchmark task 而异，包括超参数、数据混合、并行策略等。
- 训练或搜索算法：BO/BBO benchmark。
- 反向传播：随被评估问题和方法而异。
- 待核实：各底层实验与优化器训练方式需按任务核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=jRLlZdU76s)

### 15. Beyond Successful Experience Reuse: Inducing Revision Knowledge from Evolving Experience for LLM Agents

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：CEA 从演变经验恢复程序适用条件与状态到程序映射，摘要没有模型参数训练。
- 模型/状态更新对象：修订因素、程序知识和状态—程序映射。
- 训练或搜索算法：结构化对比归因。
- 反向传播：未描述模型反传或参数更新。
- 待核实：知识表示和诱导组件实现待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=oFY9G0m3ts)

### 16. BehEvolve: Behavior-Guided Evolution of Multi-Agent Program Policies under Sparse Task Feedback

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：BehEvolve 的持久改进对象是多智能体程序政策、代码修改和调度分支，不是语言模型参数。
- 模型/状态更新对象：程序政策、父子代码、执行轨迹和 idea 调度状态。
- 训练或搜索算法：行为反馈引导的 program evolution。
- 反向传播：摘要没有模型参数训练证据。
- 待核实：feedback model 是否另训未说明，但不是摘要所述优化对象。
- 原始来源：[OpenReview](https://openreview.net/forum?id=GhCb2ZuoHN)

### 17. Bandit Limited Discrepancy Search for Agent Harness Configuration

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：BLDS-AF 搜索 agent-DAG 的 agent type、模型选择、推理预算等 harness 配置，不更新所选模型参数。
- 模型/状态更新对象：DAG 节点/边配置及 ridge posterior。
- 训练或搜索算法：limited-discrepancy search + factored bandit surrogate。
- 反向传播：未描述被配置 LLM 的反传训练。
- 待核实：ridge posterior 的在线更新细节待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=u4uHWlP1gE)

### 18. BRAID: Evolving Evaluators for Reliable and Effective Self-Evolving Agents

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：BRAID 明确是 training-free，演化评估器候选与任务代理分支等外部实现。
- 模型/状态更新对象：Evaluator challengers、lineage 和 Task-Agent branches。
- 训练或搜索算法：可靠性门控的双重演化。
- 反向传播：摘要明确 training-free。
- 待核实：Evaluator/Task-Agent 的具体表示是 prompt 还是代码待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=N0mDtvLk4W)

### 19. Automated Discovery Has No Universally Superior Harness

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：该研究比较并自适应分配自动发现 harness 的档案、父代选择和预算组件，未训练语言智能体参数。
- 模型/状态更新对象：harness 配置和并行运行预算。
- 训练或搜索算法：进化 harness 比较、剪枝与预算重分配。
- 反向传播：摘要未描述模型反传。
- 待核实：底层 OpenEvolve/TTT-Discover 具体工件表示待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=2ONrI9JEqu)

### 20. AttriOpt: Attribution-Based Credit Assignment for Evolutionary API-Calling Optimization

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：AttriOpt 进化 LLM 生成的 API workflow，并更新统计归因分数；没有训练 agent 模型参数。
- 模型/状态更新对象：API workflow、调用参数及归因状态。
- 训练或搜索算法：归因引导的 evolutionary workflow optimization。
- 反向传播：摘要未描述 LLM 参数反传。
- 待核实：归因估计器是否含可训练模型待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=NFtZmpfvFx)

### 21. AscendAgent: Evolving Context to Fit the Harness in CANN Kernel Optimization

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：AscendAgent 明确模型权重、workflow 和 evaluator 固定，只演化 kernel 程序图和外部可复用知识。
- 模型/状态更新对象：kernel program graph 与条件化变换知识。
- 训练或搜索算法：LLM-guided mutation、evolutionary search 和 workflow replay。
- 反向传播：摘要明确 model weights remain fixed。
- 待核实：知识确认和冲突消解细节待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=gtuspdBfQo)

### 22. Agentic Bayesian Optimization through Surrogate-Augmented Autoresearch

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：Sara 调整 BO 评估选择、边界和问题表述，概率 surrogate 存于外部 backend；摘要未训练 LLM agent 参数。
- 模型/状态更新对象：BO 搜索策略、边界、评估候选和 surrogate 状态。
- 训练或搜索算法：agentic Bayesian optimization。
- 反向传播：未描述 LLM 参数反传。
- 待核实：lenz backend 的拟合实现待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=ZIF61XReMF)

### 23. Adaptive Transfer for Cost-Aware Bayesian Optimization of LLM Agent Configurations

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：ALT 搜索 reasoning effort、工具权限和资源等 agent 配置，执行固定配置获得轨迹；不训练 agent 模型。
- 模型/状态更新对象：agent 配置、行为转移模型和 utility surface。
- 训练或搜索算法：cost-aware transfer Bayesian optimization。
- 反向传播：摘要未描述被测代理参数训练。
- 待核实：GP/transfer 模型的拟合细节待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=UjDZ0KzZ4X)

### 24. Adaptive Scenario Selection for Screening Overeager Behavior in Coding Agents

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：ASSBF 只改变筛查场景和 Thompson-sampling 预算，执行固定 framework–model pairs，没有智能体模型训练。
- 模型/状态更新对象：场景、archetype-consent 预算和 bandit state。
- 训练或搜索算法：受控场景 mutation + Thompson sampling。
- 反向传播：摘要未描述模型反传。
- 待核实：场景生成过程是否使用固定模型待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=E6IQGL7SaC)

### 25. Adaptive Exploratory Landscape Analysis for LLM-based Meta-Black-Box Optimization

- 决定：`keep_agent_model_training`（保留：明确训练或持久更新模型/策略参数）
- 依据：AdaELA 明确把 population-aware attention 选择器参数作为多任务问题并用 neuroevolution 训练，属于持久模型参数更新。
- 模型/状态更新对象：AdaELA self-/cross-attention 选择模型参数。
- 训练或搜索算法：neuroevolution strategy；摘要另称可进一步 fine-tuning。
- 反向传播：neuroevolution 本身无需反传；后续 fine-tuning 是否反传未说明。
- 待核实：LLM meta-policy 是否冻结及 fine-tuning 对象待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=Ke3tLwqK3L)

### 26. AdaGEPA: Adaptive Feedback Allocation for Reflective Prompt Optimization

- 决定：`defer_prompt_core`（暂缓：提示词为核心对象）
- 依据：AdaGEPA 的目标就是通过反馈分配反复优化 prompt。
- 模型/状态更新对象：反馈 minibatch 与迭代 prompt。
- 训练或搜索算法：弱点感知的 reflective prompt optimization。
- 反向传播：摘要无模型参数训练证据。
- 待核实：reflection 使用的模型及其固定状态待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=GxTIfjjhA4)

### 27. Active Learning for Communication Structure Optimization in LLM-Based Multi-Agent Systems

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：方法更新多智能体通信图参数分布和任务选择状态，不是语言/策略模型参数。
- 模型/状态更新对象：通信图参数、候选任务池及 surrogate/bandit state。
- 训练或搜索算法：ensemble Kalman inversion + batch Thompson sampling。
- 反向传播：摘要未描述 LLM 参数训练。
- 待核实：“graph parameters”是拓扑/通信结构而非模型权重；具体参数化待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=esnxNWIVMO)

### 28. APEX-Data: Automated Prompt Engineering eXpert with Dynamic Data Selection

- 决定：`defer_prompt_core`（暂缓：提示词为核心对象）
- 依据：APEX-Data 明确与数据分层联合执行 prompt search，核心产物仍是优化后的 prompt。
- 模型/状态更新对象：候选 prompt、搜索谱系和数据层级。
- 训练或搜索算法：evolutionary prompt mutation 与动态数据选择。
- 反向传播：摘要未描述模型参数更新。
- 待核实：mutation 模型是否固定待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=urjXCbKVzH)

### 29. AGAR: A REINFORCEMENT LEARNING SUBSTRATE FOR LLM PROGRAM EVOLUTION

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：AGAR 进化候选程序和 modular-prefix controller，且明确 backend model 不做梯度训练。
- 模型/状态更新对象：程序候选、prefix controller、选择和经验记忆。
- 训练或搜索算法：程序进化的 MDP/RL estimator substrate。
- 反向传播：摘要明确 no gradient training of backend model。
- 待核实：各 estimator 是否含小型可训练组件待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=npY9pJqb57)

### 30. A Narrow Residual Bottleneck from Evidence to Answer in Language Models

- 决定：`keep_unaffected`（保留：非本次提示词/智能体范围）
- 依据：这是语言模型内部证据瓶颈的前向隐藏状态干预研究，不是提示词或智能体优化。
- 模型/状态更新对象：不做持久参数更新；干预运行时 hidden states。
- 训练或搜索算法：充分性/必要性双向干预与置换零假设。
- 反向传播：摘要未提出训练过程。
- 待核实：模型选取和干预实现细节待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=Q5iYGwAe9W)

### 31. A Closer Look at Agentic BBO: Benchmarking LLM Agents for Black-Box Optimization

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：AgenticBBO-Bench 执行固定 LLM agents 做黑盒候选搜索并评估工具/先验，不训练其模型参数。
- 模型/状态更新对象：黑盒候选、工具配置和评测轨迹。
- 训练或搜索算法：统一有限预算的 Agentic BBO benchmark。
- 反向传播：摘要未描述被测模型训练。
- 待核实：个别被测 agent 的内部实现待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=aAcE9xwrev)

### 32. SeaEvo: Strategy as State for LLM-Driven Evolution

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：SeaEvo 持久化程序候选的文本策略描述和群体状态，未更新 LLM 参数。
- 模型/状态更新对象：程序、策略描述及 population state。
- 训练或搜索算法：LLM-driven evolutionary program search。
- 反向传播：摘要未描述模型反传。
- 待核实：mutation models 是否固定待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=39Hpdbjdtz)

### 33. BayesianAgent: Guiding Agentic Evolution with Bayesian Optimization

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：BayesianAgent 用 GP/Thompson sampling 分配候选扩展实验，改进的是可执行方案而非 LLM 参数。
- 模型/状态更新对象：候选方案、实验选择及 GP posterior。
- 训练或搜索算法：Bayesian optimization + joint Thompson sampling。
- 反向传播：摘要未描述语言模型参数训练。
- 待核实：候选扩展器的固定状态待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=CzDLiwNxO8)

### 34. Stateful Search with Stateless Agents: Scaling Long-Horizon Automated Research

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：AES 由 harness 保存候选和测量结果并重建上下文，持久状态明确位于代理对话之外。
- 模型/状态更新对象：候选方案、测量结果、任务分派和 harness state。
- 训练或搜索算法：Agentic Evolutionary Search。
- 反向传播：摘要未描述模型反传或参数更新。
- 待核实：Advisor/Worker 的底座是否固定待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=DK9rlpEHBf)

### 35. Beyond Scripted Search: Sample-Efficient Reward Discovery via Agentic Black-box Optimization

- 决定：`keep_agent_model_training`（保留：明确训练或持久更新模型/策略参数）
- 依据：ARBO 每次候选 reward evaluation 都运行完整 RL policy training，因而明确训练并持久更新策略模型参数；LLM 搜索代理本身是否训练不影响该事实。
- 模型/状态更新对象：下游 RL policy 参数；外部还更新 reward function 和搜索 workspace。
- 训练或搜索算法：LLM agent 黑盒奖励搜索；候选评估采用 full RL training run。
- 反向传播：RL policy training 通常依赖反传，但摘要未明确优化器，故具体反传实现待核实。
- 待核实：LLM agent 是否固定、RL 算法与参数保存方式待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=JZSS6Stlhv)

### 36. EvoForge: Agentic Online Hyperparameter Tuning for Pretraining

- 决定：`keep_agent_model_training`（保留：明确训练或持久更新模型/策略参数）
- 依据：EvoForge 将代理置于正在运行的分布式 pretraining 环路，超参数动作直接控制同一 GPT-2 模型权重的持续训练。
- 模型/状态更新对象：GPT-2 124M 预训练模型参数及训练超参数。
- 训练或搜索算法：单轨迹 agentic online hyperparameter tuning + distributed pretraining。
- 反向传播：预训练明确发生，通常反传；摘要未列优化器细节。
- 待核实：三类控制代理自身是否训练、经验库规则形式待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=LAmTBYPHye)

### 37. Gödel Ecology: Productivity-Guided Continuous Co-Evolution of Agents and Evaluators for Collective Recursive Self-Improvement

- 决定：`defer_agent_training_unverified`（暂缓：智能体参数训练证据待核实）
- 依据：摘要只说进化 agent/evaluator implementations，没有说明这些 implementation 是模型权重、adapter，还是 prompt/代码等外部工件。
- 模型/状态更新对象：agent/evaluator implementation 与 population state；是否含模型参数未知。
- 训练或搜索算法：生产力引导的连续共同演化。
- 反向传播：没有可确认的模型参数训练/反传证据。
- 待核实：必须核实 implementation 表示及 mutation/update operator 后才能判断。
- 原始来源：[OpenReview](https://openreview.net/forum?id=N4GJVmrzsF)

### 38. Adaptive Evolutionary Pareto Search with Online Transferability Estimation for Resource-Aware LLM Adaptation

- 决定：`keep_unaffected`（保留：非本次提示词/智能体范围）
- 依据：AEPS-OT 是面向 LLM PEFT 配置的资源感知搜索，核心包含实际适配模型参数，不是提示词或智能体范围。
- 模型/状态更新对象：PEFT 适配器/所选层参数及 Pareto archive。
- 训练或搜索算法：GA/DE/PSO/EDA 配置提议与 PEFT 评估。
- 反向传播：PEFT 候选训练是否反传及训练预算未由摘要说明。
- 待核实：每个候选实际适配的层、rank、dropout 和训练细节待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=N7vHnqiAZo)

### 39. BOTAS: Bayesian Optimization for Zero-Shot Source Task Selection in Merging of LLMs

- 决定：`keep_unaffected`（保留：非本次提示词/智能体范围）
- 依据：BOTAS 优化已有 fine-tuned checkpoints 的源任务子集和模型合并配方，非提示词、非智能体研究。
- 模型/状态更新对象：合并后的 LLM 权重及源任务子集。
- 训练或搜索算法：离散 Bayesian optimization + model merging。
- 反向传播：合并阶段 training-free；源 checkpoint 的 fine-tuning 依赖训练但细节未述。
- 待核实：合并算法和 scaling coefficient 选择细节待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=TGI79TQF5v)

### 40. From Knobs to Actions: Agentic Bayesian Optimization for Self-Improving System Tuning

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：EvoTune 用 agentic BO 调节数据库、Spark/LLM inference engine 的系统配置，未训练语言智能体模型。
- 模型/状态更新对象：系统配置、语义 Actions、图和 BO state。
- 训练或搜索算法：agentic Bayesian optimization。
- 反向传播：摘要未描述 LLM 参数训练。
- 待核实：LLM diagnosis 模块是否固定待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=am1vQQwJJ1)

### 41. SPOON: Strategy-based Prompt Optimization for Multi-Agent LLM Games

- 决定：`defer_prompt_core`（暂缓：提示词为核心对象）
- 依据：SPOON 把多智能体策略直接表示为文本规则并做 strategy-based prompt optimization，且明确不更新模型权重。
- 模型/状态更新对象：多方 textual strategy rules/prompts。
- 训练或搜索算法：结构化 best-response prompt search。
- 反向传播：摘要明确 without updating model weights。
- 待核实：生成与评价规则的模型配置待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=cAhKtc1zVk)

### 42. A Risk-Bounded Gate for Self-Improving Agents: Selecting Modifications as a Mean–Variance Knapsack

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：方法选择 memory、reflection、judge、cache、restart 和 prompt add-ons 等外部修改，测试使用 frozen LLM packer。
- 模型/状态更新对象：agent modification subset 与 knapsack statistics。
- 训练或搜索算法：mean–variance knapsack、精确求解/局部搜索。
- 反向传播：摘要明确 frozen LLM packer。
- 待核实：live packer run 尚未完成；当前结果含合成测试。
- 原始来源：[OpenReview](https://openreview.net/forum?id=fPPQnFGSYd)

### 43. $\text{Turing}^2$: Scaling Turing-Style Evaluation to Optimize Human Simulation in Dialogue

- 决定：`defer_prompt_core`（暂缓：提示词为核心对象）
- 依据：Turing² 明确通过 prompt optimization 共同改进 user simulator 与 Machine-Turing judge，并明确不更新模型参数。
- 模型/状态更新对象：simulator prompt 与 judge prompt。
- 训练或搜索算法：human-grounded co-evolutionary prompt optimization。
- 反向传播：摘要明确 without updating model parameters。
- 待核实：人类评价批次与 prompt 更新细节待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=jdJFvMPRZK)

### 44. ECO: Energy-Oriented Configuration Optimization for Attention–FFN Disaggregated LLM Serving

- 决定：`keep_unaffected`（保留：非本次提示词/智能体范围）
- 依据：ECO 调整 LLM serving 部署和 GPU 运行配置，不是提示词或智能体研究。
- 模型/状态更新对象：部署配置、GPU 设置与 GP correction state。
- 训练或搜索算法：成本感知约束 Bayesian optimization。
- 反向传播：不涉及 LLM 参数训练；GP 拟合细节未述。
- 待核实：校准模型的参数学习方式待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=nABfUhZWr9)

### 45. The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators

- 决定：`defer_agent_training_unverified`（暂缓：智能体参数训练证据待核实）
- 依据：RQGM 共同演化 coder/writer/reviewer/grader，但摘要未说明被改写的是模型权重、adapter、prompt 还是代码。
- 模型/状态更新对象：agent 与 evaluator 的实现/政策、评价目标和 population state；参数类型未知。
- 训练或搜索算法：非平稳效用下的 evolutionary co-evolution。
- 反向传播：模型参数训练和反传证据不足。
- 待核实：需核实 co-evolved reviewer/writer/grader 的表示与更新算子。
- 原始来源：[OpenReview](https://openreview.net/forum?id=o3txFJw4JR)

### 46. AIM: Agentic Idea Management for Automated Research

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：AIM 管理研究想法、解候选和实验预算，摘要没有训练语言智能体模型参数。
- 模型/状态更新对象：研究想法、surrogate/acquisition state 和分支预算。
- 训练或搜索算法：受 BO 启发的 agentic idea search。
- 反向传播：未描述模型反传。
- 待核实：Agentic Surrogate 是否仅由提示调用实现待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=rnK26MhdGM)

### 47. AscendOptimizer: Episodic Agent for Ascend NPU Operator Optimization

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：AscendOptimizer 更新 tiling/data-movement 配置、kernel 程序和执行经验，而非代理模型参数。
- 模型/状态更新对象：AscendC kernel、host tiling 配置与 episodic knowledge。
- 训练或搜索算法：硬件反馈闭环 evolutionary configuration search。
- 反向传播：摘要未描述模型参数训练。
- 待核实：用于重写程序的 LLM 是否固定待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=wtVho001dF)

### 48. TABRSI: A RECURSIVE SELF-IMPROVING MULTI- AGENT SYSTEM FOR TABLE UNDERSTANDING AND REASONING

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：DGM/HGM-Flow 演化的是角色代码、拓扑和推理模式等可执行多智能体流水线工件，没有模型参数训练证据。
- 模型/状态更新对象：角色代码、pipeline topology 和 CoT/PoT 模式。
- 训练或搜索算法：code mutation 与多智能体 pipeline evolution。
- 反向传播：摘要未描述底座模型反传。
- 待核实：solver self-edits 的具体代码边界待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=ypByqdkzf3)

### 49. Generate and Select: A Framework for Bayesian Optimization with LLM Proposals

- 决定：`keep_unaffected`（保留：非本次提示词/智能体范围）
- 依据：GaS 是 LLM generator 与 GP-BO 组合的通用结构化对象优化器，未以提示词或语言智能体自改为研究对象。
- 模型/状态更新对象：结构化候选池、观测与 GP surrogate。
- 训练或搜索算法：黑盒 LLM candidate generation + GP-BO selection。
- 反向传播：摘要未训练生成 LLM；GP 拟合方式未详述。
- 待核实：四项任务的候选类型和 backend 配置待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=zENuM3JgRz)

### 50. AT-AT: Automatic Tool Optimization from Agent Traces

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：AT-AT 明确保持 agents fixed，只编辑共享工具描述和实现。
- 模型/状态更新对象：tool descriptions、tool implementations 和轨迹历史。
- 训练或搜索算法：trace-driven tool editing/evaluation。
- 反向传播：摘要明确 holding the agents fixed。
- 待核实：轻量 coding agent 是否固定模型调用待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=pp2JaGrr0r)

### 51. Self-Evolution Should Be Stable, Not Frozen: Lyapunov-Gated Recursive Self-Improvement

- 决定：`defer_agent_training_unverified`（暂缓：智能体参数训练证据待核实）
- 依据：EVOLYAPUNOV 接纳 agent/improver 自修改，但摘要未说明自修改究竟包含模型权重还是外部 prompt、代码或记忆。
- 模型/状态更新对象：agent self-modifications、improver/meta-operation 与风险状态；参数类型未知。
- 训练或搜索算法：matched perturbation branches + Lyapunov-gated selection。
- 反向传播：模型参数训练/反传证据不足。
- 待核实：需核实 candidate self-modification 的序列化形式与持久对象。
- 原始来源：[OpenReview](https://openreview.net/forum?id=3t0j2Y05EH)

### 52. SCAMP: Black-Box Knowledge Poisoning Attack on Multimodal Retrieval-Augmented Generation

- 决定：`defer_agent_training_unverified`（暂缓：智能体参数训练证据待核实）
- 依据：SCAMP 更新图文投毒对和视觉原型；Visual/Text Attacker、Competing Agents 与 Evaluators 是否另行训练模型参数，摘要未说明。
- 模型/状态更新对象：明确更新投毒图文对和 prototype；代理/评估器参数状态未知。
- 训练或搜索算法：self-competitive black-box candidate optimization。
- 反向传播：目标检索/生成系统无需梯度访问；攻击代理是否反传训练未知。
- 待核实：需核实 attacker/evaluator 是固定模型调用还是参数化训练组件。
- 原始来源：[OpenReview](https://openreview.net/forum?id=O26AmnGkFD)

### 53. Breaking the Refusal Barrier: Stochastic Discovery of Residual  Unsafe Behaviors in Aligned Language Models

- 决定：`keep_unaffected`（保留：非本次提示词/智能体范围）
- 依据：SEEK 是非智能体的安全失败发现与数据生成方法，之后明确用发现数据 fine-tune LLM；不属于 prompt 优化。
- 模型/状态更新对象：后续 safety-tuned LLM 参数；发现阶段更新覆盖集。
- 训练或搜索算法：随机输入扰动采样 + safety fine-tuning。
- 反向传播：发现阶段无梯度；最终 fine-tuning 会训练模型，具体反传配置未说明。
- 待核实：安全微调算法和数据过滤细节待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=T8c8NM6FT4)

### 54. In-Context Robot Learning with VLM Agents

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：GPT-Policy 是 VLM agent，但摘要明确只做部署期上下文适配，不做梯度更新或任务参数持久修改。
- 模型/状态更新对象：示范/反馈 context、grounding 与 action chunks。
- 训练或搜索算法：in-context robot learning。
- 反向传播：摘要明确 without gradient updates or persistent task-specific parameter changes。
- 待核实：context compiler/harness 是否含另训组件待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=LIa6SeOhH9)

### 55. Code-Probe-Adapt: Interactive Heuristic Learning for Self-Evolving Agents

- 决定：`defer_agent_no_model_training`（暂缓：智能体但不训练模型参数）
- 依据：COPA 通过 REPL 探测和修订 code-as-policy heuristic，摘要明确整体无需梯度更新。
- 模型/状态更新对象：可执行 code-as-policy、heuristic 与 REPL state。
- 训练或搜索算法：事件触发的交互式代码策略修订。
- 反向传播：摘要明确 without gradient updates。
- 待核实：使用的 LLM 底座及代码持久化边界待核实。
- 原始来源：[OpenReview](https://openreview.net/forum?id=zeF8echOqR)
