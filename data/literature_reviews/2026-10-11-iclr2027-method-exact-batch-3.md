# ICLR 2027 方法定向精确检索：第 3 批审查

本文件逐篇依据缓存的 OpenReview 官方投稿摘要审查 30 条方法定向命中。它只记录本批决定，不代表全会场覆盖。`finite difference` 若仅为数值分析、诊断、时间差分或被避免的对照，不按梯度无关优化收录。基线或输入 checkpoint 的训练不能自动算作所提方法的反传依赖。

- 收录：1
- 排除：29
- 官方状态：本批缓存均为 `ICLR.cc/2027/Conference/Submission`；未据此声称录用。
- OpenReview 在线日期：本批原始 `odate` 均为 `2026-10-03T12:42:08.286Z`；它不是跨平台最早公开日期。

## 逐条决定

### 1. A Logarithmic Regret Bound for Optimistic Hedge in General-Sum Games

- OpenReview：[rtYZbUFotI](https://openreview.net/forum?id=rtYZbUFotI)
- 查询：`finite difference`
- 决定：`exclude`
- 核心贡献：证明一般和博弈中 Optimistic Hedge 在期望损失向量反馈下的对数遗憾界，并用高阶差分界与有限差分插值完成分析。
- 方法：没有提出梯度无关语言模型优化；finite difference 是理论插值工具。
- 更新对象：博弈策略分布；非语言模型。
- 反传分模块：摘要讨论 no-regret 动力学，不涉及语言模型训练模块。
- 持久状态：时间平均策略；非语言模型状态。
- 与仓库关系：不相关：一般博弈理论，方法命中来自分析中的 finite-difference interpolation。
- 待核实：全文中的数值实现细节未核实。

### 2. AEGIS: Differentiable Mars Climate Model with Neural Closures

- OpenReview：[B4QWjbtwO0](https://openreview.net/forum?id=B4QWjbtwO0)
- 查询：`finite difference`
- 决定：`exclude`
- 核心贡献：提出可微 Mars 气候模型 AEGIS，将行星物理与神经闭包接口结合。
- 方法：finite differences 仅用于核对轨迹梯度；模型目标是暴露梯度。
- 更新对象：Mars 气候模型和神经闭包；非语言模型。
- 反传分模块：摘要明确支持物理校准与神经训练的轨迹梯度。
- 持久状态：训练后的气候/闭包参数；非语言模型。
- 与仓库关系：不相关：物理气候建模，且有限差分仅为梯度验证。
- 待核实：未核实完整训练配置。

### 3. Beyond Estimator Moments: Minimal Information for Predicting Zeroth-Order Adam's Response

- OpenReview：[4nrxgYbatB](https://openreview.net/forum?id=4nrxgYbatB)
- 查询：`zeroth-order`
- 决定：`exclude`
- 核心贡献：分析不同 ZO query law 即使均值、协方差和 MSE 相同也可令 Adam 产生不同响应，并刻画额外信息量。
- 方法：研究一般局部指数损失模型中的 ZO estimator/query-law 理论。
- 更新对象：抽象参数向量；摘要无语言模型应用。
- 反传分模块：ZO 查询用于理论分析；无语言模型组件。
- 持久状态：理论平衡点与 Adam 更新；无特定模型状态。
- 与仓库关系：不相关：真实 ZO 理论，但没有 LLM/VLM/语言代理应用。
- 待核实：未见语言模型实验。

### 4. CAT-Flow: Curvature-Adaptive sTeps for Flow Matching

- OpenReview：[QH3ykEheO3](https://openreview.net/forum?id=QH3ykEheO3)
- 查询：`finite difference`
- 决定：`exclude`
- 核心贡献：提出 CAT-OV/CAT-OT，在 flow matching 推理时依据速度历史或时间方向有限差分估计曲率并调节 ODE 步长。
- 方法：CAT-OT 的有限差分估计的是向量场时间导数，用于采样步长而非模型参数优化。
- 更新对象：图像/音频生成采样时间步。
- 反传分模块：训练免费推理算法；摘要未称更新网络参数。
- 持久状态：仅当前采样调度，摘要无持久参数更新。
- 与仓库关系：不纳入：纯生成采样器加速，未建立语言模型优化关联。
- 待核实：虽用于 text-to-image，未优化语言骨干或语言代理。

### 5. Complexity Guarantees for Heterogeneous Federated Bilevel Optimization with Lower-Level Constraints

- OpenReview：[IWiOh98M8n](https://openreview.net/forum?id=IWiOh98M8n)
- 查询：`zeroth-order`
- 决定：`exclude`
- 核心贡献：提出带下层约束的 federated bilevel ZO 框架，用 control variates 修正 client drift 并给出复杂度保证。
- 方法：通过目标函数查询近似上层更新，并求两个非精确下层解。
- 更新对象：联邦双层优化参数；摘要无语言模型。
- 反传分模块：上层为 ZO；下层解算法细节需全文确认。
- 持久状态：联邦模型/超参数可持续更新；非语言模型特定。
- 与仓库关系：不相关：一般联邦优化与个性化学习，没有 LLM/VLM 应用。
- 待核实：下层反传依赖未由摘要完整说明。

### 6. Controlling Symmetry Drift in Forward-Only Continual Learning

- OpenReview：[lgAbT33ZED](https://openreview.net/forum?id=lgAbT33ZED)
- 查询：`forward-only`
- 决定：`exclude`
- 核心贡献：提出 gauge-damped node perturbation，用局部互易缩放抑制 forward-only continual learning 中沿重缩放对称性的参数漂移。
- 方法：节点扰动以局部活动、神经元扰动和标量损失反馈更新，并周期性做保持函数不变的缩放校正。
- 更新对象：通用持续学习网络权重。
- 反传分模块：目标是不可用 backpropagation 的 edge-device 学习；无语言模型组件。
- 持久状态：网络权重持续更新。
- 与仓库关系：不相关：明确 forward-only，但摘要没有 LLM/VLM 应用。
- 待核实：架构范围和局部写入协议需全文核实。

### 7. Decision-Aware Residual Calibration: Bridging the Prediction–Decision Gap in Electromagnetic Design with Sparse Feedback

- OpenReview：[sluZT3V92I](https://openreview.net/forum?id=sluZT3V92I)
- 查询：`gradient-free`
- 决定：`exclude`
- 核心贡献：提出 DARC，用稀疏电磁响应反馈传播历史误差，并以残余误差场景调整非线性设计评分。
- 方法：框架不更新 surrogate，以稀疏函数反馈完成响应校准和候选评分。
- 更新对象：电磁设计响应与候选排序。
- 反传分模块：摘要称 gradient-free 且不更新 surrogate。
- 持久状态：保留历史误差依赖；无模型权重更新。
- 与仓库关系：不相关：电磁设计，未涉及语言模型。
- 待核实：历史校准算子的训练方式未说明。

### 8. Does Scaling Reinforcement Learning Really Require More Training?

- OpenReview：[a04cCyok2x](https://openreview.net/forum?id=a04cCyok2x)
- 查询：`gradient-free`
- 决定：`include_new`，分类 `related_closed_form`
- 核心贡献：提出 SURGE，把同一 RL 训练历史中的高准确率 anchor 与较短回答 donor 相对共同初始化的权重更新做谱分解与互补融合，构造单一部署政策。
- 方法：融合阶段不做梯度优化或候选政策测试；按预设 anchor 保留比例从权重谱结构确定 block size 并合成 checkpoint。
- 更新对象：reasoning/coding policy 的持久模型权重（两个 RL checkpoint 的组合）。
- 反传分模块：SURGE 融合阶段据摘要无需继续训练；输入 checkpoint 来自既有 RL 训练，原 RL 训练使用何种反传实现未说明。
- 持久状态：输出为可单独运行的持久融合模型；原始 RL checkpoints 亦为持久权重。
- 与仓库关系：相关闭式/结构化模型合并：语言推理与代码模型的训练后权重融合，不是 ZO 梯度估计。
- 待核实：摘要未给出融合权重是否需要额外校准的实现细节，也未说明原 RL 各模块训练方式。

### 9. Evolving Neural Solvers for Multi-objective Combinatorial Optimization

- OpenReview：[EjCA4aPW5K](https://openreview.net/forum?id=EjCA4aPW5K)
- 查询：`evolution strategies`
- 决定：`exclude`
- 核心贡献：提出 ENS，先训练少量偏好特定神经组合优化求解器，再以 evolution strategies 扩展求解器集合以覆盖 Pareto front。
- 方法：ES 演化神经求解器参数；初始求解器由训练和 parameter transfer 获得。
- 更新对象：组合优化求解器权重；非语言模型。
- 反传分模块：初始模型训练依赖未说明；后续 ES 是梯度无关演化。
- 持久状态：产生持久求解器模型集合。
- 与仓库关系：不相关：虽有 ES 参数优化，但任务是一般多目标组合优化，无语言模型关联。
- 待核实：初始训练的反传实现待全文核实。

### 10. FHEvolve: Constraint-Guided Evolution of Efficient FHE Programs

- OpenReview：[YHSlikDOqO](https://openreview.net/forum?id=YHSlikDOqO)
- 查询：`evolutionary optimization`
- 决定：`exclude`
- 核心贡献：提出 FHEvolve，用可复用 FHE 约束、策略族保持与执行错误修复指导程序演化。
- 方法：对同态加密程序进行 evolutionary optimization。
- 更新对象：FHE 程序代码及其算法策略。
- 反传分模块：程序搜索本身以执行评估为反馈；摘要无语言模型训练。
- 持久状态：持久保存搜索所得程序；非模型权重。
- 与仓库关系：不相关：一般程序演化，未说明 LLM 生成器或语言模型优化。
- 待核实：seed programs 的来源未说明。

### 11. Generalizing On-Policy Self-Distillation for Diffusion Models

- OpenReview：[NYnvponx1H](https://openreview.net/forum?id=NYnvponx1H)
- 查询：`without gradients`
- 决定：`exclude`
- 核心贡献：提出 GenOPSD，把图像 reward 分数转成 detached query-level targets，再以 clean-prediction MSE 刷新 diffusion policy。
- 方法：reward evaluator/decoder 不传梯度，但 policy 仍通过目标拟合训练；不是全程无反传。
- 更新对象：图像 diffusion policy 参数。
- 反传分模块：evaluator 与 decoder 无梯度；policy refresh 的 MSE 拟合通常需反传，摘要未显式写优化器。
- 持久状态：训练后 diffusion policy 权重持久更新。
- 与仓库关系：不纳入：纯图像生成训练，即使在 Qwen-Image-Bench 评测也无语言模型优化证据。
- 待核实：policy refresh 的确切反传实现待全文核实。

### 12. Gradient Clipping at and Beyond the Edge of Stability

- OpenReview：[vYAFQ2gP7r](https://openreview.net/forum?id=vYAFQ2gP7r)
- 查询：`zeroth-order`
- 决定：`exclude`
- 核心贡献：比较 clipping 对一阶与 ZO 训练 Edge-of-Stability 的不同影响，并刻画 ZO 非零协方差固定点。
- 方法：包含 batch/per-sample clipped ZO 的动力学分析与实验。
- 更新对象：通用深度网络参数；摘要无语言模型。
- 反传分模块：同时研究 FO 和 ZO；无语言模型模块。
- 持久状态：训练参数持续更新。
- 与仓库关系：不相关：ZO 优化研究未给出 LLM/VLM 应用。
- 待核实：实验模型与数据集摘要未列明。

### 13. HIRA: GRADIENT-FREE RESIDUAL RETRIEVAL FOR LONG-HORIZON TIME-SERIES FORECASTING

- OpenReview：[XGgv7TfxJl](https://openreview.net/forum?id=XGgv7TfxJl)
- 查询：`gradient-free`
- 决定：`exclude`
- 核心贡献：提出 HIRA，用冻结时间序列 foundation model 的隐藏表示检索历史预测残差并按 horizon 配置修正预测。
- 方法：无需额外 gradient training 的 residual-memory 检索校正。
- 更新对象：时间序列预测残差记忆与校正配置。
- 反传分模块：backbone 冻结；encoder、retriever、fusion network 均不训练。
- 持久状态：历史残差索引是外部记忆；模型权重不更新。
- 与仓库关系：不相关：时间序列 foundation model，并非语言模型。
- 待核实：记忆在部署期间是否继续写入需全文核实。

### 14. Is your uncertainty map wrong, or is its target? Exact diagnostics for the Tweedie diagonal, and a gradient-free alternative

- OpenReview：[TnAOz7rQfI](https://openreview.net/forum?id=TnAOz7rQfI)
- 查询：`gradient-free`
- 决定：`exclude`
- 核心贡献：提出 T-PT，通过重复扰动模型支持的医学影像预测并测量去噪器响应方差，作为 Tweedie 不确定性图的梯度无关诊断探针。
- 方法：梯度无关 residual probe 估计不确定性，不优化模型或语言组件。
- 更新对象：医学图像逐体素不确定性图。
- 反传分模块：探针只做前向扰动查询；diffusion checkpoint 不更新。
- 持久状态：无持久模型参数更新；输出诊断图。
- 与仓库关系：不相关：医学图像不确定性诊断，无语言模型优化。
- 待核实：探针结果是否缓存不影响范围判断。

### 15. Learn Feasibility Once, Optimize All Objectives: Derivative-Free Diffusion Models for Chance-Constrained Programming

- OpenReview：[lWpHQ7sBfm](https://openreview.net/forum?id=lWpHQ7sBfm)
- 查询：`derivative-free`
- 决定：`exclude`
- 核心贡献：提出 D3Opt，先训练并冻结 chance-feasible diffusion prior，再用粒子 Feynman–Kac 校正在推理时以函数值优化新目标。
- 方法：后验目标优化阶段仅用 function evaluations；prior 的预训练另行进行。
- 更新对象：机会约束决策变量与粒子；非语言模型。
- 反传分模块：推理优化无需目标梯度；diffusion prior 的训练方式未说明。
- 持久状态：冻结 prior；每个目标产生优化决策，不更新模型权重。
- 与仓库关系：不相关：通用 chance-constrained programming，无语言模型应用。
- 待核实：prior 训练的反传方式待全文核实。

### 16. Learning to Search Beyond Lines

- OpenReview：[61uAE11t92](https://openreview.net/forum?id=61uAE11t92)
- 查询：`derivative-free`
- 决定：`exclude`
- 核心贡献：提出以近似条件最小值构造可复用弯曲搜索路径的 derivative-free nonconvex optimization 框架。
- 方法：通过函数值采样、卷积凸化与一维 safeguarded search 搜索。
- 更新对象：一般非凸目标参数；仅含 diagonal linear network 示例。
- 反传分模块：value-only 示例不使用目标梯度；无语言模型组件。
- 持久状态：优化变量持续变化；非语言模型。
- 与仓库关系：不相关：通用 DFO 理论和 BBOB/线性网络实验，无 LLM/VLM 应用。
- 待核实：实验实现细节待全文核实。

### 17. Master-and-Stop Training for Out-of-Distribution Detection

- OpenReview：[LGeMWMPk3s](https://openreview.net/forum?id=LGeMWMPk3s)
- 查询：`zero-order`
- 决定：`exclude`
- 核心贡献：提出 MST，以样本不确定度的零阶和二阶时间差判断是否掌握该样本，并停止对其继续训练。
- 方法：zero-order 指不确定度序列的阶数差分，不是 zeroth-order parameter optimization。
- 更新对象：训练样本选择与 OOD detector。
- 反传分模块：摘要明确仍把未停止样本用于 backpropagation。
- 持久状态：模型参数通过常规训练持久更新。
- 与仓库关系：不相关：术语误命中，且无语言模型应用。
- 待核实：具体 detector 架构摘要未说明。

### 18. Not All Observations Are Equal: Guiding Derivative-Free Ensembles via Uncertainty Contraction

- OpenReview：[wso7l8n8ms](https://openreview.net/forum?id=wso7l8n8ms)
- 查询：`derivative-free`
- 决定：`exclude`
- 核心贡献：提出 UCEG，以更新活跃度估计局部不确定性收缩并选择观测，改进 ensemble Kalman guidance。
- 方法：依赖黑盒物理 forward evaluations 的 derivative-free ensemble correction。
- 更新对象：PDE inverse problem 参数/粒子。
- 反传分模块：guidance 无需 forward model 梯度；无语言模型组件。
- 持久状态：推理粒子状态更新；不涉及语言模型权重。
- 与仓库关系：不相关：物理反问题，无 LLM/VLM 应用。
- 待核实：diffusion prior 的训练方式未说明。

### 19. Parallel Decoding Distillation for Fast Image and Video Generation

- OpenReview：[mkncGn42Ir](https://openreview.net/forum?id=mkncGn42Ir)
- 查询：`finite difference`
- 决定：`exclude`
- 核心贡献：提出 PDD，训练网络一次预测多个去噪步骤以加速图像与视频 diffusion/flow 生成。
- 方法：论文强调不以 JVP 或有限差分近似回归导数；finite difference 是被避免的对照。
- 更新对象：图像/视频生成 student 模型。
- 反传分模块：student distillation 是训练过程；摘要未详述反传，但没有无梯度更新主张。
- 持久状态：student 权重持久更新。
- 与仓库关系：不纳入：纯视觉生成蒸馏，方法词来自被避免的有限差分。
- 待核实：训练优化器待全文核实。

### 20. Performance Without Evidence: A Placebo-Controlled Audit of Medical Foundation Model Adaptation

- OpenReview：[pnWcegvgL8](https://openreview.net/forum?id=pnWcegvgL8)
- 查询：`gradient-free`
- 决定：`exclude`
- 核心贡献：提出 placebo-controlled auditing 检验医学 foundation model adapter 是否真正依赖病灶，并用 CCA 训练约束强化因果一致性。
- 方法：gradient-free null 只是审计对照，不是论文提出的参数优化方法。
- 更新对象：医学视觉 encoder 的 adapter。
- 反传分模块：CCA 为训练约束；摘要未说明反传实现，不能由 adapter 自动推断。
- 持久状态：adapter 为持久参数更新。
- 与仓库关系：不相关：医学视觉适配且 gradient-free 仅描述 null baseline。
- 待核实：CCA 的优化实现待全文核实。

### 21. POMDP Interfaces in Agentic Reinforcement Learning: A Framework-Driven Review

- OpenReview：[N7iu8vT1Dp](https://openreview.net/forum?id=N7iu8vT1Dp)
- 查询：`finite difference`
- 决定：`exclude`
- 核心贡献：以 POMDP 的 Belief、Granularity、Signal、Rollout 四个接口综述 agentic RL，并用有限差分形式描述配置交互。
- 方法：finite difference 是框架中的交互刻画，不是梯度无关优化算法。
- 更新对象：综述中的 agentic RL 配置；无新外部搜索对象。
- 反传分模块：讨论 policy-gradient update；自身未提出无反传训练组件。
- 持久状态：不适用：综述框架不安装持久状态。
- 与仓库关系：不纳入：虽与语言代理相关，但方法命中只是分析公式，未提出梯度无关优化机制。
- 待核实：综述覆盖的各被引方法不逐一在此条核实。

### 22. Problem-Dual Augmentation and Training for Neural Combinatorial Optimization

- OpenReview：[HKCvQhA1y4](https://openreview.net/forum?id=HKCvQhA1y4)
- 查询：`forward-only`
- 决定：`exclude`
- 核心贡献：将经典问题对偶变换用作神经组合优化求解器的测试时增广，并研究共享模型的 dual training。
- 方法：forward-only 在摘要中指求解器推理/候选生成；PDA 不是 forward-only 参数学习。
- 更新对象：组合优化实例及求解器。
- 反传分模块：PDA 无重训；PDT 沿用原求解器的 supervised/RL/self-imitation/preference learning。
- 持久状态：PDA 不更新权重，PDT 更新共享求解器权重。
- 与仓库关系：不相关：组合优化，且 forward-only 不是梯度无关语言模型优化。
- 待核实：四种求解器的具体训练方式待全文核实。

### 23. Rethinking Learning-Based Influence Maximization: Simple Neural Surrogates and Native Discrete Search

- OpenReview：[ohKw6V7xaU](https://openreview.net/forum?id=ohKw6V7xaU)
- 查询：`without gradients`
- 决定：`exclude`
- 核心贡献：提出 SIMBA，以浅层 GNN surrogate 配合 batched multi-swap simulated annealing 搜索影响最大化的离散种子集合。
- 方法：种子集合搜索不用梯度；surrogate 另行训练。
- 更新对象：图节点种子集合及 GNN surrogate。
- 反传分模块：离散搜索无梯度；GNN 训练反传方式摘要未说明。
- 持久状态：搜索输出种子集合，GNN 权重为持久训练状态。
- 与仓库关系：不相关：图 influence maximization，无语言模型应用。
- 待核实：surrogate 训练细节待全文核实。

### 24. SCMO: Stochastic Control for Optimization over Probability Measures on Infinite-Dimensional Spaces

- OpenReview：[NTEyoXZUdw](https://openreview.net/forum?id=NTEyoXZUdw)
- 查询：`gradient-free`
- 决定：`exclude`
- 核心贡献：提出 SCMO，以熵正则随机控制导出的 Gibbs 加权粒子替换，优化无限维概率测度上的仅目标值泛函。
- 方法：以候选采样、经验测度评分和指数重加权进行 gradient-free particle optimization。
- 更新对象：概率测度粒子；实验含函数空间、轨迹律和机器人操纵。
- 反传分模块：只用目标值；无语言模型组件。
- 持久状态：粒子测度持续更新；非模型权重。
- 与仓库关系：不相关：通用测度优化与机器人任务，无 LLM/VLM 应用。
- 待核实：实验策略模型细节待全文核实。

### 25. SHARD-SAM: Signed Hessian-Amplified Radius and Direction for Sharpness-Aware Minimizatio

- OpenReview：[0LAE4kdRGl](https://openreview.net/forum?id=0LAE4kdRGl)
- 查询：`zeroth-order`
- 决定：`exclude`
- 核心贡献：提出 SHARD-SAM，以 ZO curvature probes 构造带符号 Hessian-amplified surrogate，同时调节 SAM 扰动半径和方向。
- 方法：ZO 探针只估计曲率信号；主更新把 gradient 与谱校正结合。
- 更新对象：CNN/ViT 图像分类模型权重。
- 反传分模块：摘要明确主规则包含 gradient，属于一阶与 ZO 曲率混合。
- 持久状态：模型权重持续更新。
- 与仓库关系：不相关：纯视觉 CNN/ViT，且无语言模型应用。
- 待核实：具体梯度计算次数待全文核实。

### 26. Stabilizing Multi-Step Diffusion Distillation with Student Perturbation Consistency

- OpenReview：[7x4AAlYBDM](https://openreview.net/forum?id=7x4AAlYBDM)
- 查询：`finite difference`
- 决定：`exclude`
- 核心贡献：提出 SPC，用干净/扰动输入端点预测的一致性正则为多步 diffusion distillation 补充局部敏感性监督。
- 方法：finite difference perturbation 用于构造正则，避免显式 Jacobian 与穿过 rollout 的反传，但保留 stop-gradient student training。
- 更新对象：Qwen-Image 等视觉 diffusion student 权重。
- 反传分模块：不穿过 rollout 反传；student 的 DMD/PCM 基础目标与 SPC 正则仍训练模型，具体反传路径待全文核实。
- 持久状态：student 权重持久更新。
- 与仓库关系：不纳入：纯图像生成蒸馏，未优化语言骨干。
- 待核实：各损失的梯度路径需全文核实。

### 27. Sufficiency of Zeroth-Order Reward Shaping for Policy Gradient in Stabilization Control

- OpenReview：[qOGMXFJFTz](https://openreview.net/forum?id=qOGMXFJFTz)
- 查询：`zeroth-order`
- 决定：`exclude`
- 核心贡献：研究机器人稳定控制的 reward shaping，证明奖励需在目标相关坐标上包含 zeroth-order configuration 信息。
- 方法：zeroth-order 指状态配置阶数，而非无梯度参数估计；优化仍为 policy gradient。
- 更新对象：机器人控制 policy 与奖励设计。
- 反传分模块：摘要明确使用 policy gradient。
- 持久状态：policy 权重持续更新。
- 与仓库关系：不相关：术语误命中且为机器人控制，无语言模型应用。
- 待核实：具体 policy-gradient 算法待全文核实。

### 28. TORE: Token-Wise Taylor Order Selection via Decomposed Residual Error Estimation for Diffusion Acceleration

- OpenReview：[O7sF24j7wO](https://openreview.net/forum?id=O7sF24j7wO)
- 查询：`finite difference`
- 决定：`exclude`
- 核心贡献：提出 TORE，从缓存 residual 分解 truncation error 与 finite-difference derivative error，选择 diffusion token 的 Taylor 外推阶数。
- 方法：有限差分是推理期残差预测误差项，不是模型参数优化。
- 更新对象：图像/视频 diffusion 推理的 token-wise Taylor 阶数。
- 反传分模块：推理加速不更新模型；训练方式不属于该机制。
- 持久状态：缓存 residual 为短期推理状态；模型权重不更新。
- 与仓库关系：不纳入：纯视觉 diffusion 推理加速，无语言模型优化关联。
- 待核实：缓存生命周期待实现核实。

### 29. Weil-R: Automatic Differentiation of Exact Riemannian Hessians

- OpenReview：[kFWeDYnQyB](https://openreview.net/forum?id=kFWeDYnQyB)
- 查询：`finite difference`
- 决定：`exclude`
- 核心贡献：提出 Weil-R，把有限维 Weil algebra 经 manifold retraction 提升，在单次 forward pass 提取精确 Riemannian Hessian。
- 方法：论文明确不使用 finite-difference step size；命中来自对照描述。
- 更新对象：流形约束优化变量；非语言模型。
- 反传分模块：使用 automatic differentiation/Hessian-vector products。
- 持久状态：优化变量依下游 Newton/trust-region 持续更新。
- 与仓库关系：不相关：一般流形二阶优化，无语言模型应用，且不是梯度无关方法。
- 待核实：JAX 自动微分实现细节待全文核实。

### 30. Zeroth-Order Momentum and Adaptive Methods for Nonsmooth Policy Optimization from Human Preferences

- OpenReview：[S9iWSROf54](https://openreview.net/forum?id=S9iWSROf54)
- 查询：`zeroth-order`
- 决定：`exclude`
- 核心贡献：提出 ZOPGM 与 ZOPGAM，直接利用人类成对偏好 oracle 对可能非光滑、非凸的 policy objective 做带 momentum 或 adaptive scaling 的 zeroth-order 优化，并给出收敛与偏好查询复杂度。
- 方法：通过成对人类偏好形成 reward-model-free zeroth-order policy update；不拟合显式 reward model。
- 更新对象：policy 参数；摘要未指明是否为大语言模型参数化，但明确以 RLHF 为动机。
- 反传分模块：偏好 oracle 和 ZO policy update 不需目标梯度；环境/政策网络内部是否另有反传组件未说明。
- 持久状态：policy 参数在 ZOPGM/ZOPGAM 迭代中持续更新；不训练 reward model。
- 与仓库关系：不收录：方法本身是真实的偏好驱动 ZO policy optimization，但摘要仅以 RLHF 为动机；受控偏好环境实验没有证明实际 LLM/VLM 应用。
- 待核实：若后续正文或作者来源证明有实际 LLM 参数化实验，可重新评估；本轮不以动机替代应用证据。
