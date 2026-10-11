# 2026-10-12 提示词与智能体范围审查：批次 6（语义修正版）

本批次逐篇审查 109 条。语义修正版按真实机制判定，不以是否自称 agent/harness、原类别名或关键词规避范围。

## 统计

- `defer_prompt_core`：1 条
- `keep_agent_model_training`：3 条
- `keep_unaffected`：105 条

## 逐篇决定

### 1. EA4LLM: A Gradient-Free Approach to Large Language Model Optimization via Evolutionary Algorithms

- 决定：`keep_unaffected`
- 原分类：`es_pretraining`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《EA4LLM: A Gradient-Free Approach to Large Language Model Optimization via Evolutionary Algorithms》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“以真实下一 token 的平均对数概率作为适应度，使用全参数 ES 进行预训练；实验覆盖 0.5B 至 32B 参数规模的 Qwen3 风格模型。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：以真实下一 token 的平均对数概率作为适应度，使用全参数 ES 进行预训练；实验覆盖 0.5B 至 32B 参数规模的 Qwen3 风格模型。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://arxiv.org/abs/2510.10603
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 2. DART-ES: Difficulty-Aware Reweighting and Targeted Replay for Fine-Tuning LLMs with Evolution Strategies

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《DART-ES: Difficulty-Aware Reweighting and Targeted Replay for Fine-Tuning LLMs with Evolution Strategies》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“在纯前向全参数 ES 微调中，根据种群通过率和历史难度估计重加权奖励并重放罕见可解样本；评测覆盖数学推理、指令微调、代码生成和 Countdown。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：在纯前向全参数 ES 微调中，根据种群通过率和历史难度估计重加权奖励并重放罕见可解样本；评测覆盖数学推理、指令微调、代码生成和 Countdown。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=dtVcF6LLYr
- 官方摘要证据：Evolution Strategies (ES) enable memory efficient full parameter fine-tuning of large language models (LLMs) using only forward computation. However, standard ES uniformly averages rewards across problems and compresses problem level population feedback into a single scalar, making it difficult to capture how the learning value of each problem changes with model capability. To address this limitation, we propose Difficulty-Aware Reweighting and Targeted Replay for Evolution Strategies (DART-ES). DART-ES estimates the local solvability of each problem from its pass rate across the perturbation population and aggregates historical observations to construct a dynamic difficulty state. This shared state jointly guides continuous difficulty reweighting and rare solvable sample replay, thereby improving perturbation direction evaluation and training data allocation without introducing an additional difficulty model or backpropagation. Extensive experiments show that DART-ES achieves good fine-tuning performance. DART-ES outperforms ES on all five base models and improves the average accuracy from 72.07\% to 73.53\%, exceeding the 73.26\% achieved by GRPO on GSM8K. Across five challenging mathematical reasoning benchmarks, DART-ES achieves an average accuracy of 49.20\%, compared with 48.34\% for ES and remains competitive with strong 7B models trained with RL. Further experiments show consistent gains in instruction tuning, code generation and the Countdown task with a 14B model, demonstrating strong generalization across tasks and scalability to larger models. Beyond performance gains, DART-ES also shows clear advantages in system efficiency. It reduces runtime per step by 15.2\%--50.2\% and peak memory usage per GPU by 21.1\%--51.1\% compared with GRPO. Despite performing full parameter fine-tuning, DART-ES also requires less runtime and GPU memory than GRPO+LoRA. Overall, DART-ES achieves strong performance while maintaining generalization, scalability and system efficiency. Code: https://anonymous.4open.science/r/DART-ES/

### 3. Can Bayesian Optimization Efficiently Find a Strong Single Expert in Neural Thickets?

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Can Bayesian Optimization Efficiently Find a Strong Single Expert in Neural Thickets?》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“在随机线性权重子空间中使用高斯过程引导的贝叶斯优化，无需 LLM 反传即可搜索单个可部署专家；初步推理实验使用 Qwen2.5-Instruct 0.5B–3B，方法属于贝叶斯搜索。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：在随机线性权重子空间中使用高斯过程引导的贝叶斯优化，无需 LLM 反传即可搜索单个可部署专家；初步推理实验使用 Qwen2.5-Instruct 0.5B–3B，方法属于贝叶斯搜索。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://arxiv.org/abs/2608.10867
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 4. Consolidating Rewarded Perturbations for LLM Post-Training

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Consolidating Rewarded Perturbations for LLM Post-Training》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“CoRP 通过奖励与兼容性重加权、留出验证及步长校准，将高奖励参数扰动合并为单个可部署模型，全程无需 LLM 反传。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：CoRP 通过奖励与兼容性重加权、留出验证及步长校准，将高奖励参数扰动合并为单个可部署模型，全程无需 LLM 反传。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://arxiv.org/abs/2605.31494
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 5. Quantized Evolution Strategies: High-precision Fine-tuning of Quantized LLMs at Low-precision Cost

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Quantized Evolution Strategies: High-precision Fine-tuning of Quantized LLMs at Low-precision Cost》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“在离散量化权重上进行直接奖励优化，并结合误差反馈和随机种子重放；在 Countdown 上进行评测。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：在离散量化权重上进行直接奖励优化，并结合误差反馈和随机种子重放；在 Countdown 上进行评测。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=LR8wVOqE28
- 官方摘要证据：Post-Training Quantization (PTQ) is essential for deploying Large Language Models (LLMs) on memory-constrained devices, yet it renders models static and difficult to fine-tune. Standard fine-tuning paradigms, including Reinforcement Learning (RL), fundamentally rely on backpropagation and high-precision weights to compute gradients. Thus they cannot be used on quantized models, where the parameter space is discrete and non-differentiable. While Evolution Strategies (ES) offer a backpropagation-free alternative, optimization of the quantized parameters can still fail due to vanishing or inaccurate gradient estimation. This paper introduces Quantized Evolution Strategies (QES), an optimization paradigm that performs full-parameter fine-tuning directly in the quantized space. QES is based on two innovations: (1) it integrates accumulated error feedback to preserve high-precision weight updating signals, and (2) it utilizes a stateless seed replay to reduce memory usage to low-precision inference levels. QES significantly outperforms the state-of-the-art zeroth-order fine-tuning method on a variety of tasks, making direct fine-tuning for quantized models possible. It therefore opens up the possibility for scaling up LLMs entirely in the quantized space.

### 6. Fine-Tuning Language Models to Know What They Know

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Fine-Tuning Language Models to Know What They Know》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“ESMA 直接优化元认知校准和对齐奖励。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：ESMA 直接优化元认知校准和对齐奖励。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://arxiv.org/abs/2602.02605
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 7. ESSAM: A Novel Competitive Evolution Strategies Approach to Reinforcement Learning for Memory Efficient LLMs Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《ESSAM: A Novel Competitive Evolution Strategies Approach to Reinforcement Learning for Memory Efficient LLMs Fine-Tuning》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“面向内存高效推理微调的竞争式奖励 ES，主要在 GSM8K 上训练，并评估数学与代码任务的迁移能力。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：面向内存高效推理微调的竞争式奖励 ES，主要在 GSM8K 上训练，并评估数学与代码任务的迁移能力。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://arxiv.org/abs/2602.01003
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 8. Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“RandOpt 对参数扰动进行采样，筛选最佳专家并集成预测。Iterative RandOpt 博客扩展加入梯度蒸馏并重复搜索，报告在等计算量设置下使用 OLMo-3-7B 在 GSM8K 上达到 92.9%；适用性博客通过正弦波 MLP 玩具实验探索序列长度的影响。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：RandOpt 对参数扰动进行采样，筛选最佳专家并集成预测。Iterative RandOpt 博客扩展加入梯度蒸馏并重复搜索，报告在等计算量设置下使用 OLMo-3-7B 在 GSM8K 上达到 92.9%；适用性博客通过正弦波 MLP 玩具实验探索序列长度的影响。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=92oF5bU4cU
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 9. GA-LoRA: A Gradient-Free Path to Robust Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《GA-LoRA: A Gradient-Free Path to Robust Fine-Tuning》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“GA-LoRA 以任务准确率为 fitness、用 genetic algorithm 无反传演化 LoRA 参数，并分析其宽盆地偏好。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：GA-LoRA 以任务准确率为 fitness、用 genetic algorithm 无反传演化 LoRA 参数，并分析其宽盆地偏好。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=yryzq0PrWy
- 官方摘要证据：Fine-tuning a pre-trained model on a target distribution can improve in-distribution accuracy at the cost of the out-of-distribution robustness acquired during pre-training. Parameter-efficient fine-tuning methods such as Low-Rank Adaptation (LoRA) mitigate this tension by restricting updates to a compact subspace, yet the choice of optimizer still governs the geometry of the resulting solution. We introduce GA-LoRA, a gradient-free fine-tuning framework that evolves LoRA parameters with a Genetic Algorithm (GA), directly maximizing task accuracy as its fitness objective without backpropagation. We show analytically that the mutation--selection dynamics of GA-LoRA preferentially retain solutions in broader basins characterized by lower average-case sharpness. Empirically, across multiple model architectures and distribution-shift benchmarks, GA-LoRA preserves competitive in-distribution accuracy while consistently improving out-of-distribution generalization relative to gradient-based optimizers. These results establish evolutionary optimization as a principled and effective pathway toward robust fine-tuning of large-scale pre-trained models.

### 10. Evolution Strategies at the Hyperscale

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Evolution Strategies at the Hyperscale》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“EGGROLL 使用低秩扰动降低开销，同时通过种群聚合保留高秩更新，以支持可扩展的推理后训练。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：EGGROLL 使用低秩扰动降低开销，同时通过种群聚合保留高秩更新，以支持可扩展的推理后训练。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=bfVJ4GsHrO
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 11. Evolution Strategies at Scale: LLM Fine-Tuning Beyond Reinforcement Learning

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Evolution Strategies at Scale: LLM Fine-Tuning Beyond Reinforcement Learning》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“采用全参数、种群并行的 ES，直接优化 Countdown、数学推理、数独、简洁性和 ARC-AGI 等任务的奖励。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：采用全参数、种群并行的 ES，直接优化 Countdown、数学推理、数独、简洁性和 ARC-AGI 等任务的奖励。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=i0P4ew9GpS
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 12. Evaluation and Restoration of Safety in Reasoning-Tuned LLMs

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Evaluation and Restoration of Safety in Reasoning-Tuned LLMs》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“将 evolution strategies 与后训练 guardrail 结合，以推理级显存开销恢复 reasoning-tuned LLM 的安全性。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：将 evolution strategies 与后训练 guardrail 结合，以推理级显存开销恢复 reasoning-tuned LLM 的安全性。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=P9tPg5GAyt
- 官方摘要证据：Open-source LLMs that are optimized for reasoning, such as VibeThinker, aim to democratize AI by bringing high-capability models to users with limited resources.
They are broadly available but lack regulation and external guardrails; therefore, in order to integrate them safely into human society, it is critical that they perform in a safe manner.
There are popular and intuitive arguments for why improved reasoning should improve safety, but recent evidence suggests that, in fact, the opposite may be true. This paper aims to characterize and mitigate this issue.
First, it develops a metric for evaluating LLMs optimized for reasoning, and shows that increasing reasoning across multiple model families increases the unsafe rate in all cases.
Second, it proposes a method for restoring safety by combining evolution strategies with a post-training guardrail (ESPG). Compared to alternative methods for safety post-training such as GRPO, ESPG is simple to implement, requires no GPU memory beyond that of inference, and works with remarkably few training samples (e.g. 30), yet makes the model significantly safer. The study thus establishes a path towards safe post-training of open-source AI models.

### 13. ESSA: Evolutionary Strategies for Scalable Alignment

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《ESSA: Evolutionary Strategies for Scalable Alignment》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“对 LoRA 适配器的奇异值坐标进行演化，并支持低精度推理；在 GSM8K、PRM800K 和 IFEval 上进行评测。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：对 LoRA 适配器的奇异值坐标进行演化，并支持低精度推理；在 GSM8K、PRM800K 和 IFEval 上进行评测。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://arxiv.org/abs/2507.04453
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 14. Evolutionary System 2 Reasoning: An Empirical Proof

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Evolutionary System 2 Reasoning: An Empirical Proof》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“ERO 通过演化模型参数，增强模型的 System 2 reasoning 能力。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：ERO 通过演化模型参数，增强模型的 System 2 reasoning 能力。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://doi.org/10.66361/jiss.38
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 15. Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Memory Requirements

- 决定：`keep_agent_model_training`
- 原分类：`es_multi_turn`
- 论文特定依据：保留：这是智能体研究，但官方摘要明确提出 forward-only full-parameter ES，并支持训练期微调和测试时适配；其持久更新对象包含智能体底层语言模型的全参数。摘要同时提到可与 prompt-space optimization 结合，但提示词搜索不是唯一或核心参数更新，不能据此排除。
- 模型参数/组件边界：官方摘要原文明确写明“forward-only full-parameter optimization”以及“a full-parameter ES framework supporting both train-time fine-tuning and on-the-fly adaptation”。
- 训练算法：以完整长程智能体轨迹的环境总奖励评价参数扰动，用 Evolution Strategies 更新全量语言模型参数；按摘要，该 ES 分支无需 backpropagation。摘要中的 Agentic RL/GRPO 是比较对象，不据此归入所提 ES 方法。
- 反向传播：原始来源未进一步说明。
- 待核实：测试时适配是否保存为长期检查点、prompt-space 分支的具体启用方式与各实验使用的参数范围仍需逐实验核实。
- 原始来源：https://openreview.net/forum?id=LfIpbuIKLb
- 官方摘要证据：Adapting long-horizon LLM agents to specific tasks requires efficient and flexible optimization under limited GPU resources. Although Reinforcement Learning (RL) has shown promise in single-turn LLM fine-tuning, this setting exposes two challenges: backpropagation makes full-parameter adaptation increasingly expensive for larger LLMs and longer contexts, while sparse rewards and branching interactions complicate long-horizon credit assignment. We argue that evolution strategies (ES) can often be a better choice for such \textbf{task-specific adaptation, offering 1) Model Scalability through forward-only full-parameter optimization, 2) Flexibility to integrate parameter updates with prompt-space optimization, and 3) Long-Horizon Scalability by avoiding explicit turn-level credit decomposition. Based on these insights, we propose Agentic ESOpt, a full-parameter ES framework supporting both train-time fine-tuning and on-the-fly adaptation during agentic test-time compute, together with a cosine perturbation schedule for balancing exploration and adaptation. Agentic ESOpt outperforms the strongest Agentic RL baseline by 13.19 percentage points in our longest-horizon Sudoku experiment, improves over Agentic GRPO on multi-turn tool-usage Math and DocVQA, enables full-parameter fine-tuning on a MoE LLM Qwen3-30B-A3B with 4$\times$80GB GPUs, and improves existing automatic heuristic design pipelines in 28 of 36 comparisons. Code is available at https://anonymous.4open.science/status/Agentic-ESOpt-anonymous-197C.

### 16. Beyond the Best Guess: Improving LLM Solution Coverage with Evolution Strategies

- 决定：`keep_unaffected`
- 原分类：`es_understanding`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Beyond the Best Guess: Improving LLM Solution Coverage with Evolution Strategies》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“说明 ES 不仅影响 pass@1，还会改变推理解法的多样性和 pass@k。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：说明 ES 不仅影响 pass@1，还会改变推理解法的多样性和 pass@k。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://arxiv.org/abs/2608.12679
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 17. Overcoming Forgetting in LLM Fine-Tuning with Evolution Strategies

- 决定：`keep_unaffected`
- 原分类：`es_understanding`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Overcoming Forgetting in LLM Fine-Tuning with Evolution Strategies》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“将遗忘重新表述为性能漂移，并提出锚定权重衰减方法。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：将遗忘重新表述为性能漂移，并提出锚定权重衰减方法。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=OBMw8FwmyZ
- 官方摘要证据：Evolution Strategies (ES) has recently emerged as a competitive alternative to reinforcement learning (RL) for large language model (LLM) fine-tuning, offering advantages through simplicity, scalability, and inference-only training. However, recent work suggests that ES fine-tuning on new tasks may induce forgetting of prior tasks. First, this paper shows that prior task forgetting (1) is better characterized as performance drift rather than irreversible forgetting, with prior-task performance often recovering during ES training; and (2) is not a specific failure mode of ES, but can also arise for fine-tuning with RL methods. Second, it analyzes when and why such drift arises, highlighting its dependence on ES training dynamics, particularly random walk behavior in weakly constrained directions of the weight space. Third, based on these insights, it introduces Anchored Weight Decay (AWD) as a parameter-space regularization technique that constrains optimization toward the initial model parameters. AWD effectively stabilizes prior-task performance while preserving target-task performance, achieving benefits comparable to large ES population sizes at much lower computational cost. Thus, contrary to previous beliefs, the paper shows that prior-task forgetting under ES is largely avoidable, positioning ES as a promising approach for continual learning in LLMs.

### 18. Matching Accuracy, Different Geometry: Evolution Strategies vs GRPO in LLM Post-Training

- 决定：`keep_unaffected`
- 原分类：`es_understanding`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Matching Accuracy, Different Geometry: Evolution Strategies vs GRPO in LLM Post-Training》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“比较 ES 与 GRPO 在推理准确率相近时仍然存在差异的更新几何。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：比较 ES 与 GRPO 在推理准确率相近时仍然存在差异的更新几何。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://arxiv.org/abs/2604.01499
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 19. The Blessing of Dimensionality in LLM Fine-tuning: A Variance-Curvature Perspective

- 决定：`keep_unaffected`
- 原分类：`es_understanding`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《The Blessing of Dimensionality in LLM Fine-tuning: A Variance-Curvature Perspective》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“从较低的有效曲率和先升后降的训练动态解释小规模 ES 种群为何能在极高维空间中工作；实验覆盖 Qwen2.5 的多个规模以及 GSM8K、ARC-C 和 WinoGrande。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：从较低的有效曲率和先升后降的训练动态解释小规模 ES 种群为何能在极高维空间中工作；实验覆盖 Qwen2.5 的多个规模以及 GSM8K、ARC-C 和 WinoGrande。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=Pz7PpCK6Py
- 官方摘要证据：Weight-perturbation evolution strategies (ES) can fine-tune billion-parameter language models with surprisingly small populations (e.g., $N\approx 30$), contradicting classical zeroth-order curse-of-dimensionality intuition. A second, seemingly separate phenomenon also appears under fixed hyperparameters, when the fine-tuning reward often rises, peaks, and then degrades, not just with ES but also with GRPO. Both effects admit a common geometric account: fine-tuning landscapes are *low-dimensional in curvature*, with a few stiff directions embedded in a large, nearly flat bulk. The separation of curvature scales produces (i) heterogeneous time scales that yield rise-then-decay under fixed stochasticity, as captured by a minimal quadratic stochastic-ascent model, while the concentration of curvature produces (ii) degenerate improving updates, where many random perturbations share similar components along the stiff directions. For isotropic perturbations, directions without curvature add nothing to the cost of a random perturbation, so the probability of sampling an improving one does not depend on the ambient dimension $D$, and the scaling question reduces to how the curvature-active dimension $k$ grows with $D$. Probing the fine-tuning reward landscapes of GSM8K, ARC-C, and WinoGrande with ES across Qwen2.5-Instruct models (0.5B-7B) reveals that reward-improving perturbations remain accessible with small populations at every scale, and direct Hessian-spectrum measurements on the same models yield effective curvature dimensions on the order of tens, growing sub-linearly with $D$ over the tested scales and occupying a vanishing fraction of parameter space. These results reconcile ES scalability with non-monotonic training dynamics under a single geometric account, and they open the door to a broad class of fine-tuning algorithms, beyond policy-gradient RL, that worst-case zeroth-order theory had ruled out as infeasible at scale.

### 20. Evolutionary Strategies Lead to Catastrophic Forgetting in LLMs

- 决定：`keep_unaffected`
- 原分类：`es_understanding`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Evolutionary Strategies Lead to Catastrophic Forgetting in LLMs》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“分析 ES 后训练过程中模型既有能力退化的问题。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：分析 ES 后训练过程中模型既有能力退化的问题。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://arxiv.org/abs/2601.20861
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 21. The Exact Exchange Rate of Gradient-Free Credit

- 决定：`keep_unaffected`
- 原分类：`es_understanding`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《The Exact Exchange Rate of Gradient-Free Credit》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“推导并测量矩阵层中标量广播 ES 信用信号所需前向评估的精确交换率。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：推导并测量矩阵层中标量广播 ES 信用信号所需前向评估的精确交换率。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=QPRPX7pOHD
- 官方摘要证据：Gradient-free training is back at LLM scale, and its cost is now the
central question. Folklore holds that on a layer of $d$ parameters,
scalar-broadcast evolution strategies
need ${\sim}d$ times more samples than backpropagation --- directionally
right, but the constant has never been measured. We derive it exactly: for
antithetic rank-1 perturbations of an $m \times n$ layer, the estimate
$\hat{g}_N$ from $N$ forward evaluations against the true gradient $G$
obeys $\cos^2 = N/(N + N_0)$ with $N_0 = 2(m{+}2)(n{+}2)$,
parameter-free, exact in the linear regime at frozen weights;
dynamic training adds landscape-dependent excess variance atop this floor.
We verify it on every layer of the reference MLP (ratios
0.93--1.12) and of a frozen extreme-aspect-ratio chain (0.976--1.006),
killing all four alternatives in that pre-registered experiment
(maximum deviation 0.006 across a $340\times$ span of $N_0$). The law then prices, by extrapolation, the
largest gradient-free training system to date: it operates at per-step
$\cos \approx 0.02$ and finances that signal with ${\sim}10^5$ coherently
integrated steps at ${\sim}180\times$ the GPU-hours of backpropagation.
Channel by channel, our measurements yield a design-space map (two
primitives, four laws, six measured rows) and three impossibility
statements, among them: no scalar-broadcast channel escapes the exchange
rate, and approximate backpropagation is the wrong objective. This is a
measurement study, not a new method.

### 22. The Evolution Strategies Paradox: Better Models from Worse Perturbations

- 决定：`keep_unaffected`
- 原分类：`es_understanding`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《The Evolution Strategies Paradox: Better Models from Worse Perturbations》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“解释即使所有采样扰动均弱于当前模型，ES 仍能持续改进大语言模型的现象。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：解释即使所有采样扰动均弱于当前模型，ES 仍能持续改进大语言模型的现象。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=whvp3RjkiO
- 官方摘要证据：How is it possible for perturbation-based methods like Evolution Strategies (ES) to optimize billion-parameter large language models with population sizes of thirty? Classical evolutionary methods are highly dependent on finding good candidates within generated populations. However, when performing ES in various fine tuning tasks for large language models, a phenomenon can occur where all population members consistently perform worse than the current model, yet with each iteration the model consistently improves. This paradox occurs across models, tasks, and even domains. This paper first reports this ES paradox, then examines how the local reward landscape as well as the ES estimator properties contribute to this paradox: in high-dimensional spaces, exploration leads to worse performance, but still highlights good directions; aggregating those directions then allows making local improvements.  These findings provide guidance for taking advantage of perturbation-based methods in LLM fine-tuning and in high-dimensional optimization in general.

### 23. EGGROLL, Unrolled: Understanding and Improving Low-Rank Evolution Strategies at Scale

- 决定：`keep_unaffected`
- 原分类：`es_understanding`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《EGGROLL, Unrolled: Understanding and Improving Low-Rank Evolution Strategies at Scale》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“分析并改进 EGGROLL 在大语言模型规模采用的低秩进化策略机制。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：分析并改进 EGGROLL 在大语言模型规模采用的低秩进化策略机制。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=kbNjFLXanS
- 官方摘要证据：EGGROLL (Sarkar et al., 2026) makes evolution strategies (ES) practical for LLMs by replacing dense Gaussian weight perturbations with low-rank Gaussian products, often of rank one. This choice is computationally attractive but geometrically severe: Each rank-one perturbation lies in a zero-volume subset of the ambient matrix space, despite having identity covariance. We characterize the EGGROLL update mean field at finite rank and nonzero perturbation radius as a resolvent applied to the gradient of the perturbation-smoothed objective. This transformation can make the mean field nonconservative and reverse the local stability of an optimum. EGGROLL nevertheless recovers the gradient exactly on quadratic objectives at every rank and radius. In finite populations, the additional sampling variance of rank-one perturbations relative to dense Gaussian ES decays inversely with matrix width under a local affine model, and is only $0.098\%$ at width $4096$. Finally, we introduce LOO-ROLL, a leave-one-out estimator that replaces EGGROLL's two antithetic evaluations per direction by one. At equal evaluation cost, LOO-ROLL halves estimator MSE in transformer blocks. Across fourteen post-training settings up to 14B parameters, matched-time comparisons with EGGROLL yield eleven improvements in individual paired tests and no significant loss. At 1.7B, 8B, and 14B parameters, matched-time gains are $2.9$, $14.1$, and $7.9$ percentage points on GSM8K and $12.2$, $8.4$, and $8.1$ points on MATH-500.

### 24. Dimension Is Free, Horizon Is Not: When Evolution Strategies Rival Policy Gradients for LLM Fine-Tuning

- 决定：`keep_agent_model_training`
- 原分类：`es_understanding`
- 论文特定依据：保留：论文核心是比较 ES 与 policy gradient 对语言模型参数的训练，并将长程智能体任务作为关键适用场景之一；官方摘要明确 ES 评价 perturbed model 的总回报，而非只优化智能体文本、轨迹或外部 workflow。
- 模型参数/组件边界：官方摘要将 ES 定义为扰动参数的估计器，并报告使用 Qwen2.5-7B-Instruct 在 27 个 NLP、数学推理和智能体任务上进行 ES–PG 对比。
- 训练算法：ES 通过参数扰动和整条轨迹总回报估计语言模型更新；PG/GRPO 通过动作采样与 token 级信用训练模型。论文分析两类梯度估计器的有效参数维数与有效信用分配时域，不应把比较用 PG 的反传属性归给 ES。
- 反向传播：原始来源未进一步说明。
- 待核实：官方摘要未逐项列出 27 个任务各自训练的参数子集、检查点持久化方式和 PG 实现细节。
- 原始来源：https://openreview.net/forum?id=59ufz75SkM
- 官方摘要证据：Policy gradient (PG) methods such as GRPO are the dominant approach to LLM fine-tuning, but they suffer from imprecise credit assignment, a limitation that becomes especially pronounced in long-horizon agentic tasks. Recent work has established Evolution Strategies (ES) as a scalable alternative to PG. Because ES evaluates each perturbed model by its total return, it avoids per-token credit assignment, which makes it a natural candidate for long-horizon settings. We analyze ES and PG within a single framework, as two estimators of the same gradient that explore in different currencies. ES perturbs parameters and therefore pays a dimension tax, whereas PG samples actions and therefore pays a horizon tax. We show that the taxes actually incurred are effective quantities. For ES, the tax is $D_{\mathrm{eff}}$, the number of reward-relevant parameter directions. For PG, it is $T_{\mathrm{eff}}$, the number of token positions that contribute reward-relevant variance, which increases only when reward-irrelevant tokens share both credit and weights with reward-carrying ones. To disentangle the two, we construct a synthetic task in which $D_{\mathrm{eff}}$ and $T_{\mathrm{eff}}$ can be controlled independently. On this task, PG outperforms ES at high $D_{\mathrm{eff}}$ and short $T_{\mathrm{eff}}$, whereas ES outperforms PG when $T_{\mathrm{eff}}$ is long relative to $D_{\mathrm{eff}}$, and this region expands with the training budget of ES. We then estimate proxies for $D_{\mathrm{eff}}$ and $T_{\mathrm{eff}}$ on 27 NLP, mathematical reasoning, and agentic tasks with Qwen2.5-7B-Instruct and relate the resulting atlas to head-to-head ES–PG comparisons. Our results support ES as a scalable alternative for LLM fine-tuning, particularly for long-horizon tasks with sparse credit.

### 25. Dust: Pretraining Transformers Without Backpropagation

- 决定：`keep_unaffected`
- 原分类：`zo_pretraining`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Dust: Pretraining Transformers Without Backpropagation》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“通过逐词元激活扰动和损失反馈分配学习信号，训练语言模型权重，并对残差混合标量使用权重空间 ES；大种群比较需要更多计算，相对 EGGROLL 的效率优势包含外推估计。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：通过逐词元激活扰动和损失反馈分配学习信号，训练语言模型权重，并对残差混合标量使用权重空间 ES；大种群比较需要更多计算，相对 EGGROLL 的效率优势包含外推估计。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：None
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 26. Scaling Zero-Order Pretraining Through Model Sharding

- 决定：`keep_unaffected`
- 原分类：`zo_pretraining`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Scaling Zero-Order Pretraining Through Model Sharding》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“通过模型分片扩展零阶语言模型预训练。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：通过模型分片扩展零阶语言模型预训练。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=YRoVIXOAky
- 官方摘要证据：Zero-order optimization (ZO) enables training without backpropagation, or retention of activations, making it relevant to forward-only hardware and non-differentiable loss, but its gradient error grows with perturbed dimension. This inhibits large model training. Sharded Optimization Mixture of Assemblies (SOMA) is an architecture designed with ZO in mind. SOMA is an ensemble of LSTM experts that train independently on $N$ clusters of data using simultaneous perturbation stochastic approximation (SPSA). Its separable loss function removes cross-expert perturbation noise at the cost of jointly learned representations across domains. Experts train independently, without exchanging gradients, activations or optimizer state. We use 80,000 estimated RTX~5090 GPU-hours to study SOMA compared to baseline methods. Modest sharding improves training compute efficiency over all tested monolithic ZO controls. We study a 8.44M model at 150 aggregate GPU-hour budget and show SOMA $N=2$ with 64 perturbations reaches 1.76 test nats/byte, versus 2.00--2.11 for monolithic SPSA at 64, 256 or 1,024 perturbations and 2.21 for EGGROLL. On WikiText-103, these frozen checkpoints reach 2.07, 2.25--2.36 and 2.49, respectively. We isolate the mechanism and prove that independent losses reduce relative gradient error to approximately $1/N$ of a shared-loss estimator's. Holding starting weights, data, perturbations and compute fixed, local rather than summed losses lower SOMA $N=4$ test loss by 0.035 nats/byte after 1,000 updates across three seeds. Finally, we show larger ensembles offer a separate inference benefit. At similar model size with top-$k$ routing ($k=4$), SOMA $N=256$ achieves 2.36M tokens/s versus 257k for SOMA $N=8$ ($9.19\times$, including routing), at lower test loss (1.68 versus 1.71), albeit with SOMA $N=256$ using $59.9\times$ as much aggregate training compute. We release all training and evaluation code and checkpoints for reproduction.

### 27. Perturbation Propagation: Scalable Local Learning without Weight Transport

- 决定：`keep_unaffected`
- 原分类：`zo_pretraining`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Perturbation Propagation: Scalable Local Learning without Weight Transport》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“PerProp 以局部扰动斜率和随机探针反馈替代导数及权重传输，并包含 GPT 与 Mamba 预训练实验。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：PerProp 以局部扰动斜率和随机探针反馈替代导数及权重传输，并包含 GPT 与 Mamba 预训练实验。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=5T4cPwU3Nh
- 官方摘要证据：The growing energy demands of artificial neural networks on digital hardware increasingly limit the level of intelligence they can reach, motivating the search for potentially far more energy-efficient analog implementations.
The brain offers an existence proof that a physical system can learn complex tasks at very low energy cost, but a biologically plausible learning algorithm that trains at scale remains elusive.
Backpropagation is not biologically plausible: it relies on exact derivatives from mathematical models of neuron responses and on weight transport, which copies forward weights into the backward pathway.
More biologically plausible alternatives struggle to match backpropagation's scalability and algorithmic simplicity.
We propose Perturbation Propagation (PerProp), which keeps the forward-backward structure of backpropagation but replaces both operations with local measurements: neuron derivatives with slopes measured by small forward perturbations, and weight transposes with feedback matrices learned from random probes.
Because each neuron acts on its own input, one pair of perturbed evaluations measures a whole layer's slopes; because weights are shared across examples, feedback matrices are learned once per update.
In Transformer pretraining, PerProp scales at a rate comparable to backpropagation with model size and compute, and at a faster rate with data, batch size, and depth.
On GPT and Mamba-2 language models, it outperforms the feedback-alignment and perturbation-based alternatives we evaluate, both in and out of distribution.
On spiking, comparator, and probabilistic-bit networks, it rivals or exceeds surrogate-gradient training without hand-designed surrogate derivatives.
On analog hardware, PerProp trains physical neural networks directly, learning entirely on the BrainScaleS-2 neuromorphic chip and substantially outperforming reward-modulated STDP.
Component-level estimates for analog crossbars further project orders-of-magnitude lower training energy than GPU backpropagation, an advantage that grows with network size.
PerProp thus offers a unified approach to scalable, local learning in digital and physical neural networks.

### 28. MpSub: A Momentum p-Dimensional Subspace Trust-Region Method for Derivative-Free Fine-Tuning of Large Language Models

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《MpSub: A Momentum p-Dimensional Subspace Trust-Region Method for Derivative-Free Fine-Tuning of Large Language Models》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“在低维子空间中结合动量与随机方向，以中心有限差分估计梯度并自适应调整信赖域半径；实验使用 OPT-125M/350M 与 CommitmentBank。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：在低维子空间中结合动量与随机方向，以中心有限差分估计梯度并自适应调整信赖域半径；实验使用 OPT-125M/350M 与 CommitmentBank。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://arxiv.org/abs/2609.07666
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 29. AIM-ZO: Activation-Informed Subspace Maintenance for Zeroth-Order LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《AIM-ZO: Activation-Informed Subspace Maintenance for Zeroth-Order LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“利用前向激活持续维护参数子空间，并从中采样较窄的活跃方向集合进行纯前向零阶更新；在相同前向评估预算下评测五种大语言模型和十一个下游任务。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：利用前向激活持续维护参数子空间，并从中采样较窄的活跃方向集合进行纯前向零阶更新；在相同前向评估预算下评测五种大语言模型和十一个下游任务。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=LsJ9H83guc
- 官方摘要证据：Zeroth-order (ZO) optimization offers a memory-efficient alternative for LLM fine-tuning by estimating updates only from forward evaluations of perturbed parameters, without backpropagation or activation storage. However, in billion-parameter LLMs, isotropic perturbations often waste many forward evaluations on weakly informative directions. To make these evaluations more informative, existing ZO methods restrict perturbations to low-dimensional subspaces. Yet the quality of these subspaces is critical: overly compressed or poorly maintained spaces can miss useful update directions.
To obtain a high-quality subspace for ZO updates, this paper proposes AIM-ZO, a ZO fine-tuning method based on Activation-Informed Subspace Maintenance. AIM-ZO uses forward activations as local directional information and continuously integrates them into a broad, evolving subspace over training. To access broader gradient-relevant structure while keeping individual perturbations low-dimensional, AIM-ZO activates only a smaller set of shared and sampled directions, decoupling the maintained width from the active width. We evaluate AIM-ZO across 5 LLMs and 11 downstream tasks under matched forward-evaluation budgets; its six-task average exceeds the strongest fully evaluated ZO baseline by 1.26 percentage points on OPT-2.7B and MeZO by 2.85 percentage points on OPT-30B. Our code is available at \url{https://anonymous.4open.science/r/AIM-ZO-0155/}

### 30. SubZero+: Memory-Efficient Adaptive Zeroth-Order LLM Fine-Tuning in Random Subspaces

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《SubZero+: Memory-Efficient Adaptive Zeroth-Order LLM Fine-Tuning in Random Subspaces》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“在周期刷新随机子空间中进行多查询前向差分，结合低维 Adam 和周期性动量重启，无需反向传播即可进行全权重或 LoRA 微调；在 SuperGLUE 上评测 1.3B 至 32B 模型。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：在周期刷新随机子空间中进行多查询前向差分，结合低维 Adam 和周期性动量重启，无需反向传播即可进行全权重或 LoRA 微调；在 SuperGLUE 上评测 1.3B 至 32B 模型。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=pZjhFo9XgF
- 官方摘要证据：Zeroth-order (ZO) optimization with SGD in random subspaces enables memory-efficient fine-tuning of large language models without backpropagation. However, high gradient estimation noise fundamentally undermines adaptive optimizers like Adam. We propose SubZero+, which achieves practical adaptive ZO optimization through a carefully designed dual low-dimensionality strategy: (i) multi-query forward-difference gradient estimation in periodically refreshed random subspaces to mitigate noise amplification in moment buffers, and (ii) Adam updates with periodic restarts performed directly in low-dimensional space rather than full-parameter space. In experiments, this dual design retains memory overhead comparable to momentum-free ZO methods while achieving stronger optimization performance than the evaluated ZO baselines. Theoretically, in the exact-directional limit, $K$-query averaging preserves conditional unbiasedness, while the coefficient estimator's covariance and mean-squared error, as well as query-induced second-moment inflation, scale exactly as $1/K$. Extensive experiments across SuperGLUE with models from 1.3B to 32B parameters under both full fine-tuning and LoRA schemes demonstrate consistent improvements over competing ZO methods. SubZero+ significantly narrows the performance gap with first-order optimization while preserving ZO's inference-time memory efficiency. Code is available at [https://anonymous.4open.science/r/SubZero-Plus-E8A6](https://anonymous.4open.science/r/SubZero-Plus-E8A6).

### 31. ZO-Act: Efficient Zeroth-Order Fine-Tuning via One-Shot Activation-Informed Low-Rank Subspaces

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《ZO-Act: Efficient Zeroth-Order Fine-Tuning via One-Shot Activation-Informed Low-Rank Subspaces》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“一次性构建由激活信息引导的子空间，随后在该空间中执行 ZO 监督微调；使用 Llama-3-8B 和 OPT-13B 在语言理解、问答和常识推理任务上评测。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：一次性构建由激活信息引导的子空间，随后在该空间中执行 ZO 监督微调；使用 Llama-3-8B 和 OPT-13B 在语言理解、问答和常识推理任务上评测。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=qy0AJWUh1L
- 官方摘要证据：Zeroth-order (ZO) optimization enables fine-tuning large language models when backpropagation is unavailable or memory-prohibitive, but existing methods typically perturb the full parameter space or rely on structured low-dimensional perturbations, still leading to noisy gradient estimates and limited optimization flexibility. We propose ZO-Act, an activation-informed ZO fine-tuning method that uses input activations to define a fixed low-rank parameterization. For each linear layer, ZO-Act computes a small activation basis once at initialization and optimizes only lightweight coefficient matrices using forward-only loss evaluations. This explicit coefficient-space parameterization reduces the effective perturbation dimension, enables direct use of standard momentum-based optimizers such as Adam, and naturally supports quantized LLM fine-tuning by keeping low-bit weights frozen. Our analysis characterizes a dimension-alignment trade-off: reducing the perturbation dimension improves ZO gradient estimation, while effective subspace optimization requires preserving sufficient gradient energy. We further show empirically that activation-informed subspaces capture substantially more gradient energy than random and weight-based alternatives. Across Llama-3-8B, OPT-13B, Qwen2.5-7B, Qwen2.5-32B, and INT4 Llama-3-8B, ZO-Act consistently achieves competitive performance against strong ZO baselines across language understanding, question answering, commonsense reasoning, and mathematical reasoning.

### 32. RoZO: Geometry-Aware Zeroth-Order Fine-Tuning on Low-Rank Adapters for Black-Box Large Language Models

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《RoZO: Geometry-Aware Zeroth-Order Fine-Tuning on Low-Rank Adapters for Black-Box Large Language Models》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“在 LoRA 流形的切空间中使用扰动、回缩和向量传输。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：在 LoRA 流形的切空间中使用扰动、回缩和向量传输。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://aclanthology.org/2026.eacl-long.80/
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 33. LOZO+: Provably Efficient Zeroth-Order Fine-Tuning via Greedy Low-Rank Subspace Selection

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《LOZO+: Provably Efficient Zeroth-Order Fine-Tuning via Greedy Low-Rank Subspace Selection》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“利用损失反馈与自适应阈值贪心保留有效低秩子空间方向，实现仅前向的 LLM 微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：利用损失反馈与自适应阈值贪心保留有效低秩子空间方向，实现仅前向的 LLM 微调。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://proceedings.mlr.press/v306/fang26k.html
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 34. Enabling Downstream Adaptation of Spiking LLMs: From Zeroth-Order Learning to Cross-Resolution Transfer

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Enabling Downstream Adaptation of Spiking LLMs: From Zeroth-Order Learning to Cross-Resolution Transfer》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“使用零阶学习对脉冲大语言模型进行下游适配。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：使用零阶学习对脉冲大语言模型进行下游适配。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=bmxM07322c
- 官方摘要证据：Spiking large language models (LLMs) communicate through spike trains and support event-driven computation, offering the potential for energy-efficient language processing on neuromorphic hardware.
However, adapting these models to downstream tasks remains challenging.
Backpropagation through time incurs memory costs that grow with time steps and compound the substantial memory demands of LLMs, making forward-only ZO-SGD an attractive alternative.
To examine its effectiveness, we derive a convergence bound for spiking LLMs that accounts for conversion error, suggesting that its accumulation may limit fine-tuning gains under limited-resolution neuron settings.
Our empirical results are consistent with this analysis, showing that ZO-SGD fine-tuning remains effective at higher neuron resolutions but yields substantially smaller gains under limited-resolution settings.
Motivated by these findings, we propose a two-stage framework that combines task learning with knowledge transfer across neuron resolutions to obtain task-adapted spiking LLMs with limited-resolution neurons.
The task learning stage applies ZO-SGD at a high-resolution neuron setting to acquire task-specific knowledge.
The knowledge transfer stage uses the adapted high-resolution model as a frozen teacher for progressive block-wise representation alignment, matching the limited-resolution model's intermediate representations to the corresponding teacher outputs.
This teacher-guided alignment is designed to compensate for representation mismatch across neuron resolutions while preserving the task knowledge acquired during high-resolution fine-tuning.
Experimental results show that the proposed framework improves downstream task performance over direct ZO-SGD fine-tuning under limited-resolution neuron settings.

### 35. MaZO: Masked Zeroth-Order Optimization for Multi-Task Fine-Tuning of Large Language Models

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《MaZO: Masked Zeroth-Order Optimization for Multi-Task Fine-Tuning of Large Language Models》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“利用参数重要性与多任务更新掩码缩小零阶微调的搜索空间并减少任务冲突。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：利用参数重要性与多任务更新掩码缩小零阶微调的搜索空间并减少任务冲突。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://aclanthology.org/2025.emnlp-main.935/
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 36. Zeroth-Order Fine-Tuning of LLMs in Random Subspaces

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Zeroth-Order Fine-Tuning of LLMs in Random Subspaces》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“SubZero 构造逐层低秩随机子空间，在其中进行纯前向适配。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：SubZero 构造逐层低秩随机子空间，在其中进行纯前向适配。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openaccess.thecvf.com/content/ICCV2025/html/Yu_Zeroth-Order_Fine-Tuning_of_LLMs_in_Random_Subspaces_ICCV_2025_paper.html
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 37. TeZO: Empowering the Low-Rankness on the Temporal Dimension in the Zeroth-Order Optimization for Fine-tuning LLMs

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《TeZO: Empowering the Low-Rankness on the Temporal Dimension in the Zeroth-Order Optimization for Fine-tuning LLMs》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“利用连续多个 ZO 估计之间共享的时间低秩结构。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：利用连续多个 ZO 估计之间共享的时间低秩结构。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://arxiv.org/abs/2501.19057
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 38. Sparse MeZO: Less Parameters for Better Performance in Zeroth-Order LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Sparse MeZO: Less Parameters for Better Performance in Zeroth-Order LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“仅扰动经过选择的一部分参数坐标，以提高监督适配效率。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：仅扰动经过选择的一部分参数坐标，以提高监督适配效率。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://proceedings.neurips.cc/paper_files/paper/2025/hash/1e5c2efbddc02c1d971e2f19ccdb07d0-Abstract-Conference.html
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 39. Enhancing Zeroth-order Fine-tuning for Language Models with Low-rank Structures

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Enhancing Zeroth-order Fine-tuning for Language Models with Low-rank Structures》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“LOZO 用结构化低秩扰动替代稠密随机方向。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：LOZO 用结构化低秩扰动替代稠密随机方向。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://proceedings.iclr.cc/paper_files/paper/2025/hash/9ccc9d814d3dee4750debaf23061e733-Abstract-Conference.html
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 40. Zeroth-Order Fine-Tuning of LLMs with Extreme Sparsity

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Zeroth-Order Fine-Tuning of LLMs with Extreme Sparsity》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“选择 Fisher 敏感参数进行更新，并以低精度保存冻结权重。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：选择 Fisher 敏感参数进行更新，并以低精度保存冻结权重。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://icml.cc/virtual/2024/39663
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 41. Fine-Tuning Language Models with Just Forward Passes

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Fine-Tuning Language Models with Just Forward Passes》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“MeZO 引入原位参数扰动和随机种子重放，使纯前向监督微调达到与推理相当的内存占用。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：MeZO 引入原位参数扰动和随机种子重放，使纯前向监督微调达到与推理相当的内存占用。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://proceedings.neurips.cc/paper_files/paper/2023/hash/a627810151be4d13f907ac898ff7e948-Abstract-Conference.html
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 42. ZoAQ: Adaptive Zeroth-Order Querying via Query-Reuse Coupling

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《ZoAQ: Adaptive Zeroth-Order Querying via Query-Reuse Coupling》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“复用带种子的历史双边函数评估，并通过动量一致性门控自适应分配查询预算，无需额外验证查询；纯前向 OPT 微调更新 LoRA 参数并减少评估次数，历史反馈过时偏差仍需关注。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：复用带种子的历史双边函数评估，并通过动量一致性门控自适应分配查询预算，无需额外验证查询；纯前向 OPT 微调更新 LoRA 参数并减少评估次数，历史反馈过时偏差仍需关注。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=wwgUVpgO9P
- 官方摘要证据：Zeroth-order optimization (ZOO) estimates updates from function evaluations, making perturbation queries a primary cost. Fixed budgets spend the same number of queries at every step, while adaptive controllers may offset their savings by using additional oracle calls to test estimator reliability. We introduce ZoAQ, an adaptive ZOO method built around query reuse. Rather than discarding past evaluations after each step, ZoAQ makes them useful for both the next update and the decision to query further. This enables adaptive query allocation without extra validation queries. Our analysis characterizes when this agreement identifies an update that supports descent and guides the controller to a sufficient query budget. On synthetic objectives, ZoAQ reduces queries by 43–48% relative to fixed baselines using 1.2M queries. In black-box attacks, it reaches 100% success with 320 and 625 average queries on MNIST and CIFAR-10, respectively. Across four OPT fine-tuning settings, ZoAQ saves 43–46% forward evaluations relative to fixed K = 4, with accuracy changes within tasks ranging from −0.018 to +0.010.

### 43. Universally Empowering Zeroth-Order Optimization via Adaptive Layer-wise Sampling

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Universally Empowering Zeroth-Order Optimization via Adaptive Layer-wise Sampling》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“AdaLeZO 通过非平稳多臂老虎机选层与有放回逆概率加权采样改善零阶估计及运行效率；实验覆盖 6.7B 至 30B 的 LLaMA/OPT 模型。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：AdaLeZO 通过非平稳多臂老虎机选层与有放回逆概率加权采样改善零阶估计及运行效率；实验覆盖 6.7B 至 30B 的 LLaMA/OPT 模型。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://aclanthology.org/2026.findings-acl.1999/
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 44. Zeroth-Order Riemannian Optimization on Fixed-Rank Manifolds for LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Zeroth-Order Riemannian Optimization on Fixed-Rank Manifolds for LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“在固定秩流形上进行零阶黎曼优化，用于大语言模型微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：在固定秩流形上进行零阶黎曼优化，用于大语言模型微调。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=W5wPEmfLn0
- 官方摘要证据：Zeroth-order (ZO) optimization estimates descent directions from function values alone, which removes the activation storage required by backpropagation and makes it attractive for memory-efficient fine-tuning of large language models (LLMs). Existing low-rank ZO methods either parameterize the additive update through Euclidean factors with a non-unique representation, or restrict each finite-difference direction to be low-rank. In this work, we propose to constrain each additive update block to a fixed-rank matrix manifold while keeping the pretrained weights frozen, so the learned update remains rank-constrained throughout fine-tuning. On this geometry, we build a Riemannian ZO gradient estimator that projects a random matrix onto the tangent space, normalizes it to correct the scale mismatch induced by projection, and further propose Zeroth-order Riemannian Gradient Descent (ZO-RGD) and its smoothed variant, ZO-RGD-S. We show that the ambient finite difference matches its retracted counterpart, the normalized estimator recovers the Riemannian gradient in expectation, and ZO-RGD converges under trajectory-regularity conditions. Experiments on LLM fine-tuning tasks show that the proposed algorithms are competitive with strong forward-only baselines across model families and tasks, with gains in several settings.

### 45. Zero-order Parameter-free Optimization for LMO-based Methods: Novel Approach for Efficient Fine-tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Zero-order Parameter-free Optimization for LMO-based Methods: Novel Approach for Efficient Fine-tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“将 parameter-free 调参、zeroth-order 函数值优化与 LMO 非欧几里得更新统一，并用于 OPT-1.3B 微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：将 parameter-free 调参、zeroth-order 函数值优化与 LMO 非欧几里得更新统一，并用于 OPT-1.3B 微调。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=ZyafEp0RQn
- 官方摘要证据：Fine-tuning large language models (LLMs) has become a central application of modern optimization, enabling pretrained models to adapt to diverse downstream tasks and domain-specific data. A major obstacle in large-scale fine-tuning is the memory overhead of backpropagation, which requires storing activations, gradients, and optimizer states. Zeroth-order (ZO) optimization offers a memory-efficient alternative, but its performance is highly sensitive to the stepsize and smoothing parameter, often requiring costly task-specific tuning. Parameter-free (PF) optimization addresses this issue by adapting algorithmic parameters without prior knowledge of problem-dependent constants. Moreover, large-scale fine-tuning can benefit from geometry-aware updates that account for the heterogeneous structure of parameter blocks, which can be modeled through methods that exploit linear minimization oracle (LMO). In this work, we study PF adaptation for LMO-based ZO optimization and introduce $\texttt{AdaNAGED}$, a method that unifies gradient-free training, adaptive tuning, and non-Euclidean update geometry. We establish convergence guarantees and validate the method on large-scale LLM fine-tuning task with $\texttt{OPT}-1.3\mathrm{B}$ model.

### 46. ZOLD: A Zeroth-Order Langevin Dynamics Framework for LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《ZOLD: A Zeroth-Order Langevin Dynamics Framework for LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“ZOLD 将零阶损失评估与朗之万动力学结合，用于持久化大语言模型微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：ZOLD 将零阶损失评估与朗之万动力学结合，用于持久化大语言模型微调。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=IgzZOlnr2t
- 官方摘要证据：Zeroth-order (ZO) optimization has emerged as a memory-efficient paradigm for fine-tuning LLMs, estimating gradients from forward evaluations alone. However, existing approaches refine the ZO gradient estimator within an SGD-style update and thereby inherit a structural limitation of SGD: the absence of a mechanism for global exploration of the loss landscape. In this paper, we propose a novel framework, Zeroth-Order Langevin Dynamics (ZOLD), which can be viewed as a zeroth-order analogue of stochastic gradient Langevin dynamics. A precise coupling between the smoothing radius and the inverse temperature ties the ZOLD dynamics to a Gibbs measure concentrating on the global flat minima of the loss, i.e., the global minimizers of a Hessian-trace regularized objective. Within this framework, we further introduce layerwise normalized ZOLD (LN-ZOLD) that addresses the layerwise scale heterogeneity of pretrained LLMs at no additional memory or forward evaluation. On the theoretical side, we establish non-asymptotic Wasserstein-1 error bounds for ZOLD with respect to the flatness-biased Gibbs measure. Empirically, ZOLD and LN-ZOLD improve over MeZO in accuracy across OPT-13B/30B/66B, LLaMA3, and Phi-2, while remaining substantially faster than HiZOO and FZOO at comparable accuracy.

### 47. Wanda-Guided Sparse Perturbations for Efficient Zeroth-Order Optimization

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Wanda-Guided Sparse Perturbations for Efficient Zeroth-Order Optimization》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“利用 Wanda 引导的稀疏参数扰动提高零阶优化效率。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：利用 Wanda 引导的稀疏参数扰动提高零阶优化效率。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=gbmohVa04D
- 官方摘要证据：Zeroth-order (ZO) optimization provides a memory-efficient alternative to backpropagation for fine-tuning large language models (LLMs), but its estimator variance grows with the ambient parameter dimension, often causing slow and unstable optimization. We propose Wanda-Importance Sparsity-MeZO (WIS-MeZO), a saliency-guided ZO method that concentrates sparse perturbations on task-relevant coordinates. WIS-MeZO uses weight magnitudes and downstream input-feature statistics to allocate the perturbation budget while keeping the pretrained model dense and requiring neither gradients nor pre-training data. We characterize support quality through the gradient energy capture ratio and show that, under stated conditions, WIS-guided supports preserve more gradient energy than random sparse supports. We further establish an $L$-smooth convergence guarantee governed by the effective search dimension and captured gradient energy. Experiments across two model families, scales from 3B to 32B, and 16 benchmarks show improved aggregate performance over MeZO and random sparse perturbations, competitive or stronger results than magnitude-based Sparse-MeZO, and fewer optimization steps to reach comparable validation losses.

### 48. Stabilizing Zeroth-Order Fine-Tuning of Mixture-of-Experts via One-Sided Estimation and Expert Replay

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Stabilizing Zeroth-Order Fine-Tuning of Mixture-of-Experts via One-Sided Estimation and Expert Replay》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“结合单边估计与专家重放，稳定混合专家模型的零阶微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：结合单边估计与专家重放，稳定混合专家模型的零阶微调。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=kw1764GtFE
- 官方摘要证据：Zeroth-order (ZO) optimization enables memory-efficient fine-tuning through forward loss queries. In sparse mixture-of-experts (MoE) models, however, parameter perturbations can change the experts selected for a token. This path inconsistency mixes continuous parameter effects with discrete routing changes in finite-difference estimates. We propose ZOMoE, a ZO fine-tuning algorithm that combines expert replay with one-sided estimation. At each update, an unperturbed forward pass records the selected expert indices. Perturbed queries reuse these indices while recomputing routing weights and other continuous computations. Expert selections are refreshed at the next update, allowing routing to adapt throughout training. The recording pass also supplies a shared loss baseline, so replay adds no forward queries to the one-sided estimator. Mathematically, we isolate the term introduced by expert switching in the finite-difference estimate and show that expert replay removes this term. Across two sparse MoE backbones and six downstream tasks,
ZOMoE achieves the highest average accuracy among the evaluated ZO methods, accelerates loss descent, and adds negligible memory or runtime overhead.

### 49. Sample-Adaptive Zeroth-Order Post-Training

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Sample-Adaptive Zeroth-Order Post-Training》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“SAZO 从已有方向差分估计动态样本重要性，在不增加模型评估的情况下自适应分配零阶查询。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：SAZO 从已有方向差分估计动态样本重要性，在不增加模型评估的情况下自适应分配零阶查询。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=1A2seNVDZG
- 官方摘要证据：Zeroth-order (ZO) optimization offers a memory-efficient alternative to backpropagation for fine-tuning large language models. However, existing ZO methods typically sample training examples uniformly, overlooking their evolving importance and leaving avoidable estimation variance. To address this limitation, we propose Sample-Adaptive Zeroth-Order Optimization (SAZO), which learns sample importance online and adaptively allocates queries to accelerate convergence. SAZO extracts gradient-norm information from existing directional differences to estimate sample importance without access to true gradients. Furthermore, to track evolving importance from sparse minibatch feedback, SAZO maintains per-example exponential moving averages that aggregate observations across updates. The method requires no additional model evaluations and only $O(N)$ additional scalar state compared with MeZO. We prove that SAZO asymptotically matches the leading convergence term of the *minimum-variance* sampling oracle,  and achieves a strictly faster convergence rate than standard methods. Extensive experiments across four model families demonstrate improved average downstream performance and up to $6\times$ faster convergence to the same training loss in terms of query count.

### 50. Robust and Efficient Zeroth-Order LLM Fine-Tuning via Adaptive Bayesian Subspace Optimizer

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Robust and Efficient Zeroth-Order LLM Fine-Tuning via Adaptive Bayesian Subspace Optimizer》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“ABSO 使用贝叶斯优化器聚合带噪声的子空间观测。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：ABSO 使用贝叶斯优化器聚合带噪声的子空间观测。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://arxiv.org/abs/2601.01452
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 51. Prior-Informed Zeroth-Order Optimization with Adaptive Direction Alignment for Memory-Efficient LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Prior-Informed Zeroth-Order Optimization with Adaptive Direction Alignment for Memory-Efficient LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“PIZOO 使采样方向偏向一个能够自适应更新的先验方向。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：PIZOO 使采样方向偏向一个能够自适应更新的先验方向。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://arxiv.org/abs/2601.04710
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 52. Powering Up Zeroth-Order Training via Subspace Gradient Orthogonalization

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Powering Up Zeroth-Order Training via Subspace Gradient Orthogonalization》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“ZO-Muon 对子空间估计应用谱正交化。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：ZO-Muon 对子空间估计应用谱正交化。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://arxiv.org/abs/2602.17155
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 53. On Adaptivity in Zeroth-Order Optimization

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《On Adaptivity in Zeroth-Order Optimization》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“MEAZO 研究大语言模型零阶微调的自适应性，以单个步长标量替代完整 Adam 矩状态。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：MEAZO 研究大语言模型零阶微调的自适应性，以单个步长标量替代完整 Adam 矩状态。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=uggzfUoAgS
- 官方摘要证据：We investigate the effectiveness of adaptive zeroth-order (ZO) optimization for memory-constrained fine-tuning of large language models (LLMs). Contrary to prior claims, we show that adaptive ZO methods such as ZO-Adam provide no performance or convergence advantage over well-tuned ZO-SGD, while incurring significant memory overhead due to optimizer state. We provide theoretical justification for why Adam-like adaptivity is less effective in large-scale ZO settings, and confirm this through both synthetic and LLM fine-tuning experiments. Importantly, we show empirically that adaptivity can still provide a practical benefit in ZO optimization by improving robustness to step-size selection. To retain this robustness without incurring the memory cost of optimizer state, we propose MEAZO, a Memory-Efficient Adaptive ZO optimizer that tracks only a single scalar to adapt the global step size.  We support our method with theoretical convergence guarantees under standard smoothness assumptions. Experiments on synthetic quadratic problems, multiple LLM families, and diverse fine-tuning tasks demonstrate that MEAZO performs comparably to competing methods while matching the robustness gains of ZO-Adam over ZO-SGD, without additional memory or latency overhead.

### 54. MSZO: Scheduled Multi-Scale Zeroth-Order Fine-Tuning of Large Language Models

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《MSZO: Scheduled Multi-Scale Zeroth-Order Fine-Tuning of Large Language Models》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“MSZO 在多个尺度上调度扰动，用于大语言模型零阶微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：MSZO 在多个尺度上调度扰动，用于大语言模型零阶微调。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=LX2ejcw9e7
- 官方摘要证据：Compared with first-order (FO) backpropagation, zeroth-order (ZO) optimization is much more memory-efficient in fine-tuning large language models (LLMs) by estimating gradients using only forward passes. Existing ZO methods typically use a fixed perturbation scale for finite-difference gradient estimation throughout training, which implicitly assumes a stationary bias-variance trade-off across optimization stages. In this work, we show that this trade-off changes substantially during LLM fine-tuning. By probing checkpoints along LLM fine-tuning trajectories, we find a pronounced stage-dependent perturbation-scale effect: a small perturbation scale yields lower variance and lower FO-gradient referenced mean-squared error (MSE) early in training, but both can exceed those of a larger scale by the middle stage. In contrast, the larger scale provides more stable estimates at later stages at the cost of higher bias. Motivated by this finding, we propose MSZO, a scheduled multi-scale ZO optimizer that uses a small perturbation scale in the early stage and subsequently combines small- and large-scale estimates along the same random direction. This design dynamically balances bias and variance over the course of training. Experiments on RoBERTa-Large, OPT-1.3B, Llama3-8B, and Qwen3-4B demonstrate consistent improvement of MSZO over single-scale ZO fine-tuning. Unlike the common practice of using a fixed perturbation radius throughout fine-tuning, our results reveal that the appropriate scale in ZO optimization is inherently stage-dependent.

### 55. MAPS: Momentum-Aware Perturbation Sampling for Zeroth-Order Optimization

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《MAPS: Momentum-Aware Perturbation Sampling for Zeroth-Order Optimization》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“MAPS 采用动量感知扰动采样改进零阶更新。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：MAPS 采用动量感知扰动采样改进零阶更新。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=PEDv0gnlhd
- 官方摘要证据：Zeroth-order (ZO) optimization enables memory-efficient LLM fine-tuning through gradient estimation by forward-only function queries, but most existing methods sample queries based on random isotropic perturbations on parameters that ignore informative optimization states accumulated during training.
We introduce **Momentum-Aware Perturbation Sampling (MAPS)**, a plug-and-play framework that uses momentum state to guide subsequent ZO queries.
MAPS first calibrates the momentum state to the scale of isotropic perturbations and then mixes momentum-guided directions with stochastic exploration.
It further balances the momentum-driven exploitation with random exploration through block-wise gating and temporal scheduling, controlling when and where the momentum-guided queries are applied.
Our theoretical analysis establishes the convergence guarantee for MAPS.
Since MAPS only modifies perturbation sampling without changing subsequent operations or introducing any additional function evaluation budget, it is generally applicable and extensively evaluated on various base ZO methods, foundation models and tasks.
Our extensive experiments show that MAPS improves downstream performance and achieves lower training loss, demonstrating the effectiveness of reusing optimizer states in perturbation sampling.

### 56. Low-Rank Curvature for Zeroth-Order Optimization in LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Low-Rank Curvature for Zeroth-Order Optimization in LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“LOREN 将低秩分块对角曲率建模与留一估计相结合。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：LOREN 将低秩分块对角曲率建模与留一估计相结合。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://ojs.aaai.org/index.php/AAAI/article/view/39715
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 57. Learning a Zeroth-Order Optimizer for Fine-Tuning LLMs

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Learning a Zeroth-Order Optimizer for Fine-Tuning LLMs》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“学习可以在同一模型上重复使用的扰动策略。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：学习可以在同一模型上重复使用的扰动策略。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=bRS5iwbqlC
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 58. LIZO: Enhancing Zeroth-Order LLM Fine-Tuning via Lateral Inhibition-Inspired Parameter Perturbation

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《LIZO: Enhancing Zeroth-Order LLM Fine-Tuning via Lateral Inhibition-Inspired Parameter Perturbation》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“LIZO 使用受侧抑制启发的结构化参数扰动改进大语言模型零阶微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：LIZO 使用受侧抑制启发的结构化参数扰动改进大语言模型零阶微调。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=9PoJmVxDG5
- 官方摘要证据：Fine-tuning is widely used to adapt large language models (LLMs) to downstream tasks, while zeroth-order (ZO) optimization provides a memory-efficient alternative through forward-only gradient estimation. However, existing ZO methods lack a principled characterization of parameter importance for guiding where perturbations should be introduced. In biological neural systems, lateral inhibition (LI) emphasizes the contrast between individual neuronal activity and its surrounding population. Inspired by this principle, we formulate an energy function to characterize the relative importance of individual parameters within their population and derive an LI score for parameter selection. Based on perturbation analysis, we show that parameters with higher LI scores are more sensitive to perturbations. We therefore propose Lateral-Inhibition-inspired Zeroth-Order Optimization (LIZO), which preserves parameters with higher LI scores and restricts perturbations and updates to parameters with lower scores. Extensive experiments on multiple LLMs and downstream tasks show that LIZO consistently improves over existing ZO methods across a range of settings.

### 59. HiZO: Hebbian-informed Zeroth-order Optimization for Efficient Fine-tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《HiZO: Hebbian-informed Zeroth-order Optimization for Efficient Fine-tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“HiZO 利用 Hebbian 信息构造零阶方向，以提升微调效率。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：HiZO 利用 Hebbian 信息构造零阶方向，以提升微调效率。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=JgMy03717F
- 官方摘要证据：Zeroth-order optimization enables language model fine-tuning without backpropagation, but isotropic perturbations do not exploit the task-dependent information contained in forward activations. We introduce Hebbian-informed Zeroth-order Optimization (HiZO), which uses this information to guide the perturbation distribution and improve convergence. HiZO uses the magnitude of centered input--output covariance to allocate perturbation variance across weight coordinates while preserving the total variance budget. The resulting guidance reflects both learned weights and downstream input statistics. These statistics are collected during existing loss evaluations and require no additional model forward passes. We also develop subsampled and separable variants to reduce the computation and storage needed for guidance. For smooth nonconvex objectives, we establish convergence bounds in the directional-derivative limit that characterize the roles of covariance--gradient alignment and estimator variability. A complementary one-layer analysis identifies conditions under which Hebbian covariance provides information about task-gradient magnitudes. Language-model experiments and controlled ablations show faster optimization with Hebbian guidance while retaining comparable or better predictive performance. These findings suggest that forward activations offer a practical source of task-dependent information for improving zeroth-order convergence.

### 60. GaNsZO: Gauss-Newton Step-sized Zeroth-Order Optimization for Memory-Efficient LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《GaNsZO: Gauss-Newton Step-sized Zeroth-Order Optimization for Memory-Efficient LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“GaNsZO 以受高斯—牛顿启发的规则选择零阶步长，用于内存高效的大语言模型微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：GaNsZO 以受高斯—牛顿启发的规则选择零阶步长，用于内存高效的大语言模型微调。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=iNHpKDFZRy
- 官方摘要证据：Fine-tuning large language models at scale is increasingly constrained by the memory cost of backpropagation. Zeroth-order (ZO) optimizers (e.g., MeZO) alleviate this bottleneck by relying solely on forward passes, but they often suffer from slow convergence. Recent works such as HiZOO utilize diagonal Hessian estimators as preconditioner for acceleration, yet this incurs additional memory costs comparable to training parameters. Moreover, the noisy diagonal Hessian estimates often lead to training instabilities. In this work, we introduce the $\textbf{Ga}$uss-$\textbf{N}$ewton $\textbf{s}$tepsized $\textbf{Z}$eroth-$\textbf{O}$rder (GaNsZO) algorithm, a $\textit{memory- and computation-efficient}$ ZO optimizer. GaNsZO estimates the directional second derivative along the descent direction and uses it as a stepsize scaling factor, reducing memory overhead while improving robustness. To estimate efficiently, GaNsZO exploits the model's composite structure and computes Gauss-Newton quadratic form along that direction, saving one forward pass compared to standard central-difference schemes. Empirically, on OPT and Llama models, GaNsZO consistently outperforms HiZOO in terms of accuracy and training stability. In certain tasks (e.g., SST-2), GaNsZO approaches the performance of first-order fine-tuning. In terms of efficiency, GaNsZO reduces memory consumption by up to 43% compared to HiZOO, while requiring significantly fewer forward passes to reach comparable loss, leading to up to $6\times$ end-to-end speedup in selected settings. Finally, we show that GaNsZO combines naturally with PEFT and recent ZO techniques (e.g., LOZO) and produces further improvements.

### 61. Displacement-Aware Subspace Adaptation for Muon-Style Zeroth-Order Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Displacement-Aware Subspace Adaptation for Muon-Style Zeroth-Order Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“DAZM 在刷新低秩 ZO-Muon 搜索子空间时保留由历史位移提取的奇异方向，用于大语言模型微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：DAZM 在刷新低秩 ZO-Muon 搜索子空间时保留由历史位移提取的奇异方向，用于大语言模型微调。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=5GdFuqdQwr
- 官方摘要证据：First-order fine-tuning of large language models (LLMs) is often constrained by the substantial memory overhead of backpropagation, whereas zeroth-order (ZO) fine-tuning offers a memory-efficient alternative based solely on forward evaluations.
However, high-dimensional ZO estimates can be noisy, making it difficult to reliably exploit matrix structure through Muon-style spectral updates. Recent ZO-Muon methods alleviate this issue by restricting ZO estimation to low-rank search subspaces, but repeatedly refreshing these subspaces at random may discard directions that have consistently driven recent parameter updates. Consequently, subsequent Muon steps may operate in less informative search spaces, as polar normalization can only exploit directions already captured by the selected bases.
To address this issue, we propose Displacement-Aware Subspace ZO-Muon (DAZM), which uses accumulated parameter displacements produced by recent Muon updates to adapt the low-rank search subspace. Specifically, we accumulate the realized Muon updates over each interval, allowing directions that are repeatedly reinforced along the optimization trajectory to become prominent in the resulting displacement. We then retain the leading left and right singular directions as trajectory-informed exploitation bases, while filling the remaining dimensions with random directions orthogonal to the retained subspaces to preserve exploration.
Theoretically, we show that under the temporal persistence of the local optimization geometry, displacement-aware subspace adaptation retain more informative gradient structure for subsequent Muon updates than purely random refreshes.
Extensive experiments on multiple LLMs and downstream tasks demonstrate that our method achieves consistently superior performance over existing ZO-Muon and non-Muon ZO baselines.

### 62. Difficulty Aware Reweighting for Zeroth Order Fine-Tuning of LLMs

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Difficulty Aware Reweighting for Zeroth Order Fine-Tuning of LLMs》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“在大语言模型零阶微调中按样本难度重加权，以提高查询效率。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：在大语言模型零阶微调中按样本难度重加权，以提高查询效率。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=KISxCpKBIf
- 官方摘要证据：Fine-tuning large language models (LLMs) is essential for downstream tasks, but backpropagation incurs prohibitive activation memory. Zeroth-order (ZO) optimization uses only forward passes, which provides a memory-efficient route to LLM adaptation on resource-constrained devices. Despite substantial progress on ZO optimizers and query schemes, the data-dependent characteristics of ZO gradient estimation remain under-explored. This work reveals that ZO gradient estimation exhibits \textit{sample-wise alignment heterogeneity w.r.t. the global descent direction, and hard samples yield more informative ZO updates for minimizing the global objective than easy ones}. Based on this finding, we propose a difficulty-aware ZO (DaZO) algorithm that exploits sample-wise heterogeneity through sample reweighting. It down-weights easy samples while preserving informative hard samples. Further, we show that difficulty-aware reweighting reduces the global-gradient referenced estimation error and benefits faster convergence. Extensive experiments on RoBERTa-Large, Llama3-8B, and OPT models (1.3B/13B/30B) demonstrate significant improvement of DaZO over strong ZO baselines. Our work provides the first sample-centric view of ZO optimization, and shows that the quality of ZO gradient estimation depends systematically on the training samples. It is shown that difficulty-aware reweighting significantly improves ZO methods but has limited impact on FO methods, which highlights its particular relevance to the noisy gradient-estimation regime of ZO optimization.

### 63. CurvZO: Adaptive Curvature-Guided Sparse Zeroth-Order Optimization for Efficient LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《CurvZO: Adaptive Curvature-Guided Sparse Zeroth-Order Optimization for Efficient LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“将曲率感知的稀疏采样与概率校正结合起来。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：将曲率感知的稀疏采样与概率校正结合起来。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=L35b2JZ8gS
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 64. ConMeZO: Adaptive Descent-Direction Sampling for Gradient-Free Finetuning of Large Language Models

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《ConMeZO: Adaptive Descent-Direction Sampling for Gradient-Free Finetuning of Large Language Models》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“从以动量估计为中心的锥形区域中采样搜索方向。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：从以动量估计为中心的锥形区域中采样搜索方向。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://proceedings.mlr.press/v300/behric26a.html
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 65. Adaptive Zeroth-Order Optimization via Sample-Wise Second Moments

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Adaptive Zeroth-Order Optimization via Sample-Wise Second Moments》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“利用逐样本二阶矩自适应零阶采样，实现内存高效的大语言模型微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：利用逐样本二阶矩自适应零阶采样，实现内存高效的大语言模型微调。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=J5QiZLm5qs
- 官方摘要证据：Zeroth-order optimization (ZO) estimates gradients using function evaluations without requiring access to first-order derivatives. Existing ZO methods either rely on isotropic perturbations or require additional function evaluations to obtain adaptive curvature information, introducing extra computation overhead and slowing the convergence. We propose two adaptive ZO optimizers that share an efficient diagonal second-moment estimator built from per-sample gradient surrogates. This state shapes both perturbations and updates, with distinct update scalings and shared adaptive damping for stability and perturbation-scale control. We provide convergence proofs for both variants and demonstrate the first variant’s superior performance on test functions with heterogeneous curvature. Experiments on both full-model and parameter-efficient language-model fine-tuning show that standard and adaptive ZO baselines require up to $3.3\times$ as many forward passes as our methods, while our methods achieve competitive final performance.

### 66. AGZO: Activation-Guided Zeroth-Order Optimization for LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《AGZO: Activation-Guided Zeroth-Order Optimization for LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“使用前向激活信息塑造扰动方向。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：使用前向激活信息塑造扰动方向。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=zfVxpXEZti
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 67. AGOZO: Activation-Guided Orthogonalized Zeroth-Order Optimization for LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《AGOZO: Activation-Guided Orthogonalized Zeroth-Order Optimization for LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“AGOZO 对激活引导扰动进行正交化，用于大语言模型零阶微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：AGOZO 对激活引导扰动进行正交化，用于大语言模型零阶微调。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=rX09aLiLs7
- 官方摘要证据：Zeroth-order (ZO) fine-tuning reduces memory use by replacing backpropagation with forward evaluations, but limited queries produce noisy gradient estimates. We propose Activation-Guided Orthogonalized ZO (AGOZO), which combines activation-guided queries with gradient orthogonalization. AGOZO uses input activations to select a low-rank query subspace, estimates the gradient within that subspace, and replaces the estimate's nonzero singular values by one before mapping it back to the full weight matrix. Our theory quantifies how much gradient information this operation preserves. Assuming exact directional derivatives along Gaussian perturbations, we derive upper and lower bounds on the update's average alignment with the true gradient. These bounds agree up to constant factors when the subspace rank and query budget are small relative to the layer's output dimension. We also characterize when orthogonalization provides a stronger one-step loss-reduction guarantee than raw activation-guided ZO under a common smoothness assumption. This comparison considers growing matrix dimensions while keeping the number of queries fixed. We further quantify how sharing queries across layers weakens each layer's alignment. Across three language-model backbones and nine tasks, experiments with three seeds and a matched budget of 40,000 forward evaluations show that AGOZO achieves the highest reported mean validation score or a rounded tie on 16 of 27 model--task pairs.

### 68. Private Zeroth-Order Optimization with Public Data

- 决定：`defer_prompt_core`
- 原分类：`zo_directions`
- 论文特定依据：暂缓：目录记录和原始论文页面所述文本实验以 RoBERTa-base 的 prompt-tuning 为模型适配对象，优化的是提示参数；这属于用户明确要求移出现行目录的软提示核心研究。论文的差分隐私 ZO 方法本身有效，本决定仅是当前目录范围调整。
- 模型参数/组件边界：现有目录的一手来源摘要记录明确将文本实验描述为 RoBERTa-base prompt-tuning on MNLI；更新对象是 prompt 参数，而非基础模型权重。
- 训练算法：PAZO 使用公开数据的一阶梯度引导私有数据上的零阶估计，执行差分隐私提示参数训练；它是 FO 引导的混合 ZO prompt-tuning，而非纯函数值全模型训练。
- 反向传播：原始来源未进一步说明。
- 待核实：论文是否还有不依赖 prompt-tuning 的语言模型全参数实验不影响本次判断；若用户解除提示词排除规则，可从归档恢复。
- 原始来源：https://proceedings.neurips.cc/paper_files/paper/2025/hash/54de3c17e1a2457658a22ad801c721db-Abstract-Conference.html
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 69. MUZO: Leveraging Multiple Queries and Momentum for Zeroth-Order Fine-Tuning of Large Language Models

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《MUZO: Leveraging Multiple Queries and Momentum for Zeroth-Order Fine-Tuning of Large Language Models》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“对多次有限差分估计取平均并结合 Adam，实现更低方差的仅前向微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：对多次有限差分估计取平均并结合 Adam，实现更低方差的仅前向微调。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://aclanthology.org/2025.emnlp-main.432/
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 70. Towards Fast LLM Fine-tuning through Zeroth-Order Optimization with Projected Gradient-Aligned Perturbations

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Towards Fast LLM Fine-tuning through Zeroth-Order Optimization with Projected Gradient-Aligned Perturbations》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“P-GAP 使低秩扰动与投影后的梯度估计方向对齐。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：P-GAP 使低秩扰动与投影后的梯度估计方向对齐。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://arxiv.org/abs/2510.18228
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 71. KerZOO: Kernel Function Informed Zeroth-Order Optimization for Accurate and Accelerated LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《KerZOO: Kernel Function Informed Zeroth-Order Optimization for Accurate and Accelerated LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“使用核函数加权扰动修正估计器。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：使用核函数加权扰动修正估计器。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://arxiv.org/abs/2505.18886
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 72. Harmony in Divergence: Towards Fast, Accurate, and Memory-efficient Zeroth-order LLM Fine-tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Harmony in Divergence: Towards Fast, Accurate, and Memory-efficient Zeroth-order LLM Fine-tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“DiZO 在分析一阶与零阶优化的逐层差异后，对 ZO 更新进行逐层投影和重缩放。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：DiZO 在分析一阶与零阶优化的逐层差异后，对 ZO 更新进行逐层投影和重缩放。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://proceedings.neurips.cc/paper_files/paper/2025/hash/ffd4f5a2ea6b93e9bf5af9264d568cf2-Abstract-Conference.html
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 73. Variance-reduced Zeroth-Order Methods for Fine-Tuning Language Models

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Variance-reduced Zeroth-Order Methods for Fine-Tuning Language Models》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“MeZO-SVRG 在监督 ZO 微调中加入基于锚点的控制变量。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：MeZO-SVRG 在监督 ZO 微调中加入基于锚点的控制变量。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://proceedings.mlr.press/v235/gautam24a.html
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 74. VLA-ZO: Fast Zeroth-Order Adaptation for Vision-Language-Action Models

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《VLA-ZO: Fast Zeroth-Order Adaptation for Vision-Language-Action Models》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“通过零阶有限差分、冻结视觉语言状态复用和调度感知预取，适配视觉语言动作模型的持久动作侧参数；在 LIBERO 分布偏移上评测，语言骨干保持冻结。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：通过零阶有限差分、冻结视觉语言状态复用和调度感知预取，适配视觉语言动作模型的持久动作侧参数；在 LIBERO 分布偏移上评测，语言骨干保持冻结。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=5Azm1dweoz
- 官方摘要证据：Adapting vision-language-action (VLA) models to deployment-time distribution shifts is important for reliable robotic operation, but conventional first-order adaptation can exceed the memory budget of inference-oriented deployment platforms. Zeroth-order (ZO) optimization offers a forward-only alternative with inference-level memory, but accurate gradient estimation requires many perturbation queries, making naive ZO prohibitively slow for large VLA models. We present VLA-ZO, a framework for fast ZO adaptation that exploits the structure of VLA computation. By confining adaptation to the action side, VLA-ZO keeps the expensive vision-language prefix frozen and reuses its conditioning states across perturbation queries and optimizer steps, while schedule-aware prefetching hides state-transfer overhead. On LIBERO camera-viewpoint shifts, VLA-ZO reduces end-to-end adaptation time by 25.59$\times$ at $q=16$ and 32.54$\times$ at $q=64$ relative to baseline ZO, while improving average task success from 48.27\% without adaptation to 58.17\% and 63.58\%, respectively. These results show that making ZO faster can make larger query budgets practical, providing a promising path toward resource-efficient VLA adaptation on deployment platforms.

### 75. ZOCheck: CPU-Shadow Checkpointing for Zeroth-Order LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《ZOCheck: CPU-Shadow Checkpointing for Zeroth-Order LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“通过 CPU 影子进程重放随机种子与标量更新日志，构建一致恢复镜像并在 GPU 关键路径之外持久化检查点，为零阶 LLM 微调提供容错。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：通过 CPU 影子进程重放随机种子与标量更新日志，构建一致恢复镜像并在 GPU 关键路径之外持久化检查点，为零阶 LLM 微调提供容错。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://arxiv.org/abs/2609.27189
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 76. Global Adaptive Momentum Meets Local Personalized Perturbation: Efficient Federated LLM Fine-Tuning with Zeroth-Order Gradients

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Global Adaptive Momentum Meets Local Personalized Perturbation: Efficient Federated LLM Fine-Tuning with Zeroth-Order Gradients》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“结合本地个性化扰动、零阶梯度传输与全局重构，以及自适应动量聚合，改善客户端数据异质条件下的联邦 LLM 微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：结合本地个性化扰动、零阶梯度传输与全局重构，以及自适应动量聚合，改善客户端数据异质条件下的联邦 LLM 微调。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://aclanthology.org/2026.acl-long.1851/
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 77. TerMeZO: Ternary Sparse Zeroth-Order Optimization for Fine-tuning BitNet Models at the Edge

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《TerMeZO: Ternary Sparse Zeroth-Order Optimization for Fine-tuning BitNet Models at the Edge》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“TerMeZO 对 BitNet 边缘微调采用三值稀疏零阶更新。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：TerMeZO 对 BitNet 边缘微调采用三值稀疏零阶更新。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=bstvvfFV4y
- 官方摘要证据：Fine-tuning large language models (LLMs) with first-order optimizers requires a memory several times larger than that required for inference. Memory-efficient zeroth-order optimization (MeZO) sidesteps this cost by estimating gradients from forward passes only. However, for BitNet architectures, a family of LLMs with ternary {-1,0,1} weights and 8-bit activations, fine-tuning requires updating full-precision latent weights, and thus the memory footprint of MeZO no longer matches that of inference. A promising solution is to fine-tune only a subset of the latent weights, but existing sparse zeroth-order (ZO) methods either ignore the ternary structure or require first-order gradient information to build a sparse mask, which is at odds with the purpose of ZO fine-tuning. We propose TerMeZO, a sparse MeZO scheme that exploits the geometry of the ternary quantizer itself to identify the latent weights that are more likely to change values during fine-tuning, at no additional data or memory cost. Our convergence analysis shows that TerMeZO can converge faster than full-parameter MeZO, owing to its optimized reduction of the fine-tuning effective dimension. We run extensive experiments on BitNet models ranging from 1B to 3B parameters, spanning classification, instruction-following, and mathematical reasoning tasks. TerMeZO matches or exceeds the performance of full-parameter MeZO while substantially reducing the fine-tuning memory footprint.

### 78. SeedFlood: A Step Toward Scalable Decentralized Fine-Tuning of LLMs

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《SeedFlood: A Step Toward Scalable Decentralized Fine-Tuning of LLMs》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“向所有客户端传播可重建零阶更新的随机种子，使去中心化微调通信量近乎不随模型规模增长。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：向所有客户端传播可重建零阶更新的随机种子，使去中心化微调通信量近乎不随模型规模增长。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=Psl8GgO2we
- 官方摘要证据：This work presents SeedFlood, a new approach to decentralized LLM fine-tuning designed to scale across large models, large collaborations, and complex network topologies while achieving global consensus with negligible communication overhead.
Traditional methods suffer from high communication costs that grow with model size, while information decay over network hops renders global consensus inefficient.
SeedFlood takes a significant departure from these practices by exploiting the seed-reconstructible structure of zeroth-order gradients and effectively making the messages to transmit near-zero in size, allowing them to be flooded to every client in the network, and thereby enhancing scalability of decentralized training.
Consequently, SeedFlood enables training in regimes previously considered impractical, such as billion-parameter scale models or distributed across hundred of clients.
Despite the intrinsic optimization inefficiency of zeroth-order estimation, SeedFlood can match or surpass first-order gossip baselines at larger collaboration scales by avoiding consensus errors, while requiring orders-of-magnitude less communication.
We also provide theoretical analysis to formalize that SeedFlood avoids topology-dependent consensus terms in the convergence bound while retaining the acceleration enabled by increased client participation.

### 79. Rethinking Quantized LLM Fine-Tuning: An Adaptive-Grouping Alternating Zeroth-Order  Algorithm in Continuous Mapping Space

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Rethinking Quantized LLM Fine-Tuning: An Adaptive-Grouping Alternating Zeroth-Order  Algorithm in Continuous Mapping Space》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“在连续映射空间中交替执行分组零阶更新，用于量化大语言模型微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：在连续映射空间中交替执行分组零阶更新，用于量化大语言模型微调。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=kaA2itb1S8
- 官方摘要证据：Fine-tuning quantized Large Language Models (LLMs) is crucial for model adaptation on resource-constrained edge devices, where zeroth-order (ZO) optimization has emerged as a memory-friendly alternative to first-order methods. Existing ZO fine-tuning methods typically focus on either perturbing discrete quantized weights or coarse-grained (per-tensor/channel) continuous scales. In this paper, we rethink this fundamental choice and recognize that while fine-tuning should ideally target the dequantized weights, the discrete nature of weights restricts optimization to a finite search space, and tuning coarse-grained scales is limited to a constrained continuous subspace that lacks the expressive capacity of the full parameter space. To mitigate these issues, we propose to break down scales and zero-points to a fine-grained  level and fine-tune them in a continuous mapping space. Motivated by this, we propose CoZO, an adaptive-grouping alternating zeroth-order algorithm that optimizes these fine-grained parameters while adaptively balancing search-space expressiveness and estimation stability. Crucially, we provide a theoretical convergence guarantee for CoZO. Extensive experiments demonstrate that CoZO achieves superior stability and effectiveness, consistently outperforming discrete-perturbation and scale-tuning baselines under stringent memory constraints.

### 80. Quantize Once, Adapt in Place: Zeroth-Order Optimization with Detectable Signals

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Quantize Once, Adapt in Place: Zeroth-Order Optimization with Detectable Signals》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“为量化模型设计可检测扰动信号，通过零阶评估进行原位适配。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：为量化模型设计可检测扰动信号，通过零阶评估进行原位适配。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=DnAsidFUmk
- 官方摘要证据：Quantization reduces the memory required to store and deploy large language
    models, while zeroth-order (ZO) optimization avoids storing activations for
    backpropagation. Combining these two advantages still leaves a key question:
    which parameters should be optimized? We
    therefore study a simple constraint: keep the packed weights and quantization
    metadata fixed, and fine-tune only the floating-point model tensors retained
    in the checkpoint. We collect these tensors into the Quantization-Preserved Subspace (QPS)
    and propose Quantization-Preserved Zeroth-order Optimization (QPZO), which applies
    two-point ZO updates only in QPS. This enables adaptation without adding
    trainable modules or dequantizing the low-bit backbone for optimization.
    We support QPZO with theoretical analysis and empirical evidence. Specifically,
    (1) we show that an updateable output head retained in QPS yields a nonzero projected
    gradient whenever its aggregate gradient is nonzero, establishing the presence of
    task-relevant signal; and (2) because ZO accesses this signal only through finite forward-loss
    differences, we introduce Signal-to-Error Ratio (SER) to compare directional task-signal energy with
    measurement-error energy. Under the stated error bound, we prove that SER above one
    is the sharp threshold for guaranteeing positive expected alignment,
    characterizing when finite forward queries robustly preserve a useful task direction.
    Our theoretical analysis and extensive experiments demonstrate that QPZO offers a simple
    approach that substantially reduces GPU memory usage while maintaining highly competitive
    performance and stability.

### 81. Piggybacking Training on Inference Systems

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Piggybacking Training on Inference Systems》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“NoisyGEMM 将低秩扰动融合进推理矩阵乘，使 CMA-ES 能在服务运行时内训练 Qwen 模型。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：NoisyGEMM 将低秩扰动融合进推理矩阵乘，使 CMA-ES 能在服务运行时内训练 Qwen 模型。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=PCZw5EG9Ft
- 官方摘要证据：Training a model on the inference system that serves it would enable private on-device fine-tuning and turn idle inference fleet capacity into training capacity without separate training infrastructure. Inference hardware, however, often lacks the memory and interconnect needed for backpropagation. Zeroth-order optimization, such as evolution strategies (ES), uses only forward passes, but evaluating candidate-specific perturbations adds weight-update traffic or separate correction costs to batched inference. We address this problem with NoisyGEMM, a matrix-multiplication kernel that evaluates perturbed models without materializing their weight perturbations. Candidates use compact coefficient vectors over shared Hadamard bases, whose corrections are fused into the base GEMM. We integrate NoisyGEMM into vLLM's linear layers and run training through its existing scheduler, KV-cache manager, and sampler. On an A100, perturbed linear layers run at 1.1×–1.3× the latency of unperturbed cuBLAS GEMM. Using a separable CMA-ES variant, reinforcement learning of Qwen3 models from 1.7B to 30B-A3B improves on the base model on all six reasoning benchmarks and outperforms GRPO on 17 of 18 model–benchmark pairs with the same maximum completion length of 16k tokens. Compared to the state-of-the-art ES framework EGGROLL, NoisyGEMM hosting CMA-ES achieves higher accuracy on AIME 2025 and lower latency when scaling the population size and adapter rank. Finally, we demonstrate piggybacking CMA-ES training on a serving engine that replays one day of BurstGPT live traffic. We will open-source our code upon publication.

### 82. Inference-Native Zeroth-Order Optimization for LLMs

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Inference-Native Zeroth-Order Optimization for LLMs》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“围绕推理原生执行与前向评估重组大语言模型零阶优化。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：围绕推理原生执行与前向评估重组大语言模型零阶优化。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=EnBpzU8b3z
- 官方摘要证据：Zeroth-order (ZO) methods train large language models using only forward passes, yet common ZO execution paths perform substantial work beyond what the algorithm itself requires. To remove this extra execution overhead, we present Infer-ZO, which separates the evaluations required by the algorithm from how they are executed, allowing them to reuse existing inference-engine optimizations. After removing inherited execution work, a complete Infer-ZO step on Qwen3-14B adds only 1.16% wall-clock time over matched inference, bringing ZO execution close to its fundamental inference workload. With Infer-ZO, ZO evaluations run at near-inference cost with frozen base weights and can share GPU batches with ordinary inference requests. In co-serving experiments, foreground and background throughput remain within 1–3% of the corresponding background-request baseline. Across 15 Qwen3, Llama, and OPT models, Infer-ZO achieves 2.10×–9.94× end-to-end step speedups over released LoZO.

### 83. High-Throughput and Memory-Efficient Zeroth-Order Fine-tuning LLMs with Distributed Parallel Computing

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《High-Throughput and Memory-Efficient Zeroth-Order Fine-tuning LLMs with Distributed Parallel Computing》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“DistZO2 分布式执行扰动评估，并且只聚合标量结果。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：DistZO2 分布式执行扰动评估，并且只聚合标量结果。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://aclanthology.org/2026.findings-acl.2128/
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 84. Hi-ZFO: Hierarchical Zeroth- and First-Order LLM Fine-Tuning via Importance-Guided Tensor Selection

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Hi-ZFO: Hierarchical Zeroth- and First-Order LLM Fine-Tuning via Importance-Guided Tensor Selection》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“根据张量重要性为其分配一阶或零阶更新。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：根据张量重要性为其分配一阶或零阶更新。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://aclanthology.org/2026.findings-acl.239/
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 85. HO-SFL: Hybrid-Order Split Federated Learning with Backprop-Free Clients and Dimension-Free Aggregation

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《HO-SFL: Hybrid-Order Split Federated Learning with Backprop-Free Clients and Dimension-Free Aggregation》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“在切分联邦 LoRA 微调中结合客户端零阶更新与服务端一阶反传，降低客户端内存及模型聚合通信；切分激活仍需传输。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：在切分联邦 LoRA 微调中结合客户端零阶更新与服务端一阶反传，降低客户端内存及模型聚合通信；切分激活仍需传输。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://proceedings.mlr.press/v306/chen26fd.html
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 86. Converge Faster, Talk Less: Hessian-Informed Federated Zeroth-Order Optimization

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Converge Faster, Talk Less: Hessian-Informed Federated Zeroth-Order Optimization》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“HiSo 从零阶更新重建全局对角曲率预条件器，加速联邦 LLM 微调，并仅传输标量与随机种子。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：HiSo 从零阶更新重建全局对角曲率预条件器，加速联邦 LLM 微调，并仅传输标量与随机种子。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://proceedings.iclr.cc/paper_files/paper/2026/hash/3e8b1835833ef809059efa74b9df6805-Abstract-Conference.html
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 87. AdaMeZO: Adam-style Zeroth-Order Optimizer for LLM Fine-tuning Without Maintaining the Moments

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《AdaMeZO: Adam-style Zeroth-Order Optimizer for LLM Fine-tuning Without Maintaining the Moments》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“无需保存完整的优化器状态即可近似自适应矩估计。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：无需保存完整的优化器状态即可近似自适应矩估计。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=XLc102wbnT
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 88. MobiZO: Enabling Efficient LLM Fine-Tuning at the Edge via Inference Engines

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《MobiZO: Enabling Efficient LLM Fine-Tuning at the Edge via Inference Engines》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“通过 Multi-Perturbed LoRA 并行执行多查询零阶估计，并接入 ExecuTorch 实现端侧微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：通过 Multi-Perturbed LoRA 并行执行多查询零阶估计，并接入 ExecuTorch 实现端侧微调。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://aclanthology.org/2025.emnlp-main.1022/
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 89. Improving the Straight-Through Estimator with Zeroth-Order Information

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Improving the Straight-Through Estimator with Zeroth-Order Information》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“FOGZO 在量化感知预训练中结合一阶 STE 梯度与零阶更新，降低估计偏差及零阶计算成本；语言实验覆盖至 0.3B 参数的 LLaMA 模型。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：FOGZO 在量化感知预训练中结合一阶 STE 梯度与零阶更新，降低估计偏差及零阶计算成本；语言实验覆盖至 0.3B 参数的 LLaMA 模型。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://proceedings.neurips.cc/paper_files/paper/2025/hash/f49d76cf84df83a611883c621c96d2d9-Abstract-Conference.html
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 90. Second-Order Fine-Tuning without Pain for LLMs: A Hessian Informed Zeroth-Order Optimizer

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Second-Order Fine-Tuning without Pain for LLMs: A Hessian Informed Zeroth-Order Optimizer》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“HiZOO 使用纯前向计算估计对角曲率。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：HiZOO 使用纯前向计算估计对角曲率。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://proceedings.iclr.cc/paper_files/paper/2025/hash/6bf82cc56a5fa0287c438baa8be65a70-Abstract-Conference.html
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 91. Scalable Zeroth-Order Fine-Tuning for Extremely Large Language Models with Limited GPU Memory

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Scalable Zeroth-Order Fine-Tuning for Extremely Large Language Models with Limited GPU Memory》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“ZO2 通过参数卸载和执行重叠支持大模型 ZO 监督微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：ZO2 通过参数卸载和执行重叠支持大模型 ZO 监督微调。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=s0p9xpORgP
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 92. QuZO: Quantized Zeroth-Order Fine-Tuning for Large Language Models

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《QuZO: Quantized Zeroth-Order Fine-Tuning for Large Language Models》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“将量化整合到纯前向监督微调中。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：将量化整合到纯前向监督微调中。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://aclanthology.org/2025.emnlp-main.271/
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 93. PaZO: Preconditioned Accelerated Zeroth-Order Optimization for Fine-Tuning LLMs

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《PaZO: Preconditioned Accelerated Zeroth-Order Optimization for Fine-Tuning LLMs》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“采用预条件 SPSA、对角 Hessian 估计与移动平均，稳定并加速零阶微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：采用预条件 SPSA、对角 Hessian 估计与移动平均，稳定并加速零阶微调。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://proceedings.neurips.cc/paper_files/paper/2025/hash/a14193e9d9fb0b03af0b717de1cac8ac-Abstract-Conference.html
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 94. HELENE: Hessian Layer-wise Clipping and Gradient Annealing for Accelerating Fine-tuning LLM with Zeroth-order Optimization

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《HELENE: Hessian Layer-wise Clipping and Gradient Annealing for Accelerating Fine-tuning LLM with Zeroth-order Optimization》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“引入逐层裁剪和退火机制。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：引入逐层裁剪和退火机制。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://aclanthology.org/2025.emnlp-main.1323/
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 95. Bilevel ZOFO: Efficient LLM Fine-Tuning and Meta-Training

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Bilevel ZOFO: Efficient LLM Fine-Tuning and Meta-Training》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“以双层优化结合全骨干的零阶更新与适配器的一阶更新，用于微调和元训练；属于混合 FO/ZO 方法。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：以双层优化结合全骨干的零阶更新与适配器的一阶更新，用于微调和元训练；属于混合 FO/ZO 方法。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://proceedings.neurips.cc/paper_files/paper/2025/hash/5f999632c48f87cffb214e575581e4a9-Abstract-Conference.html
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 96. ComPO: Preference Alignment via Comparison Oracles

- 决定：`keep_unaffected`
- 原分类：`zo_alignment`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《ComPO: Preference Alignment via Comparison Oracles》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“利用一比特偏好比较聚合参数扰动进行零阶对齐，实践结合 DPO/SimPO 梯度训练；在 UltraFeedback 上训练并以 AlpacaEval 2、Arena-Hard 和 MT-Bench 评估，2026 扩展加入在线 KL 控制。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：利用一比特偏好比较聚合参数扰动进行零阶对齐，实践结合 DPO/SimPO 梯度训练；在 UltraFeedback 上训练并以 AlpacaEval 2、Arena-Hard 和 MT-Bench 评估，2026 扩展加入在线 KL 控制。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://arxiv.org/abs/2505.05465
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 97. Beyond the Capability Boundary: Zeroth-Order Optimization for Self-Evolving LLM Agents

- 决定：`keep_agent_model_training`
- 原分类：`zo_multi_turn`
- 论文特定依据：保留：这是自演化智能体研究，官方摘要明确扰动并更新 LLM 的 LoRA 参数，随后还以成功的深度研究轨迹执行监督微调；不是只更新轨迹、文本、记忆或 workflow。
- 模型参数/组件边界：官方摘要明确写明“perturb LoRA parameters of LLMs”、以损失差估计梯度并“update the LoRA parameters”，以及用更新后的 LLM 采样轨迹用于 supervised fine-tuning。
- 训练算法：第一阶段以 answer perplexity 为损失，通过参数扰动和损失差进行零阶 LoRA 更新；第二阶段以成功轨迹执行 SFT。ZO 阶段不需要反传，但 SFT 通常是一阶训练，摘要未明确其具体反传实现，故不把整个闭环称为无反向传播。
- 反向传播：原始来源未进一步说明。
- 待核实：SFT 的优化器、底座冻结范围、LoRA 持久化与最终发布检查点形式待原文实现进一步核实。
- 原始来源：https://openreview.net/forum?id=qqOjD3pcxL
- 官方摘要证据：Self-evolving methods improve the capabilities of LLM agents by sampling trajectories from the underlying LLMs and learning from these trajectories. However, these methods struggle to learn beyond the inherent capability boundary of the agents, since successful trajectories can be rare on difficult examples for further improvements.In this paper, we propose a zeroth-order self-evolution framework that enables agents to learn beyond their capability boundary by perturbing LLM parameters to adapt to difficult examples without any trajectory annotations.Specifically, we perturb LoRA parameters of LLMs, run the agent, compute the losses under the perturbed and original parameters, and use the loss difference to estimate gradients and further update the LoRA parameters.
We sample trajectories using the updated LLMs for supervised fine-tuning to break through the capability boundary of the agents, forming a closed self-evolution loop.We introduce a parallel perturbation inference mechanism and an adaptive lookup mechanism to reduce time consumption in zeroth-order optimization, with an answer perplexity loss that provides smooth and stable zeroth-order loss values.
Experiments on multiple deep research benchmarks show that our method obtains substantially more successful trajectories and consistently outperforms strong baselines, especially on difficult examples.

### 98. Zeroth-Order Optimization at the Edge of Stability

- 决定：`keep_unaffected`
- 原分类：`zo_understanding`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Zeroth-Order Optimization at the Edge of Stability》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“通过 Hessian 谱刻画两点零阶方法的均方线性稳定性，并以最大特征值和迹给出稳定性界；稳定性边缘的实验证据来自全批量视觉训练。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：通过 Hessian 谱刻画两点零阶方法的均方线性稳定性，并以最大特征值和迹给出稳定性界；稳定性边缘的实验证据来自全批量视觉训练。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://proceedings.mlr.press/v306/song26ac.html
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 99. When Does Symmetry Reduce Effective Rank in Zeroth-Order Optimization?

- 决定：`keep_unaffected`
- 原分类：`zo_understanding`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《When Does Symmetry Reduce Effective Rank in Zeroth-Order Optimization?》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“用对称轨道余维界定 Hessian 有效秩，并推导 ZO-SGD 的有限样本维度无关查询界。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：用对称轨道余维界定 Hessian 有效秩，并推导 ZO-SGD 的有限样本维度无关查询界。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=EplKUVCy5D
- 官方摘要证据：Fine-tuning large neural networks is often limited by the substantial memory overhead of backpropagation. To address this bottleneck, memory-efficient zeroth-order optimization (MeZO) enables fine-tuning using only function evaluations, but classical zeroth-order optimization (ZO) query-complexity bounds typically scale with the ambient parameter dimension. Recent theory suggests that ZO efficiency can instead depend on the effective rank, a spectral measure of how curvature is distributed across parameter directions. In this work, we show that, for smooth objectives with appropriate symmetries, the effective rank of the Hessian is bounded by the codimension of the symmetry orbit together with an explicit correction term that quantifies nonstationarity. Our bound is tight, with equality achieved by an explicit family of smooth invariant objectives. At stationary points, it recovers the exact Hessian null directions induced by symmetry.  Lastly, we establish finite-sample convergence of ZO-SGD under mild conditions and obtain dimension-independent function-query bounds without assuming a dominate low-effective-rank Hessian matrix. In experiments, empirical evidences are provided to illustrate the theoretical mechanism and the connection between  effective rank and ZO optimization.

### 100. Understanding Clipping in Zeroth-order Optimization

- 决定：`keep_unaffected`
- 原分类：`zo_understanding`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Understanding Clipping in Zeroth-order Optimization》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“研究裁剪在零阶优化中的行为及影响，并包含语言模型场景。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：研究裁剪在零阶优化中的行为及影响，并包含语言模型场景。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=nZByC53zgL
- 官方摘要证据：Zeroth-order optimization has emerged as a resource-efficient alternative to Stochastic Gradient Descent (SGD) when fine-tuning LLMs, thanks to the inherent low dimensionality of the loss landscape. It relies on a two-point estimate of the gradient that only accesses the function value and not the gradient, bypassing the resource-heavy backpropagation. Recently, it was accidentally discovered that per-sample clipping can improve the performance of the trained model, while running a differentially private version of zeroth-order optimization \cite{zhang2024dpzero} with a very large privacy parameter $\epsilon$ (corresponding to very little privacy). In this paper, we systematically investigate this phenomenon and demonstrate that ($i$) the optimal choice of learning rate $\eta$ is inversely proportional to the clipping threshold $c$, satisfying $\eta c =$ constant; ($ii$) clipping drives the zeroth-order optimization to a different solution with higher test accuracy; and ($iii$) this phenomenon is only observed with per-sample clipped zeroth-order optimization and not other zeroth-order alternatives that also provide robust estimates of the gradient. Further analyses with artificially injected label noise reveals that clipping leads to more robust predictions, which stems from the implicit down weighting of hard-to-fit training examples.

### 101. Query Complexity of Forward-Only Hebbian Learning: Theory and a Native Fit for Diffusion Models

- 决定：`keep_unaffected`
- 原分类：`zo_understanding`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Query Complexity of Forward-Only Hebbian Learning: Theory and a Native Fit for Diffusion Models》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“为反向成对的纯前向 Hebbian 参数扰动估计器推导精确梯度对齐式和闭式查询预算。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：为反向成对的纯前向 Hebbian 参数扰动估计器推导精确梯度对齐式和闭式查询预算。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=NR8lYUNnka
- 官方摘要证据：We study the query complexity of forward-only, gradient-free learning rules for training neural networks, motivated by settings where backpropagation is structurally unavailable: activation-tape memory that grows with depth and context, and objectives (quantized weights, non-differentiable rewards) whose exact gradient is zero almost everywhere. We analyze a three-factor Hebbian rule, an antithetic zeroth-order gradient estimator that perturbs parameters along a random probe and broadcasts a single scalar score to every synapse, and derive an exact, non-asymptotic identity for its gradient alignment as a function of probe count and problem dimension, yielding a closed-form query budget $M^* \approx (P+1)/3$. We relate this upper bound to known minimax lower bounds for zeroth-order stochastic convex optimization, characterizing how close the rule's query complexity comes to the best possible rate for any gradient-free method. We further identify an architecture-dependent separability criterion, a measurable coupling scope $S$ and feedback bandwidth $K$, that predicts when this query cost stays small, and confirm it empirically on a diffusion denoiser, where the per-noise-level residual gives $S=1$: the rule closes most of the gap to backpropagation from scratch while eliminating its activation-memory overhead entirely, and continues to descend the loss through a quantized codebook argmin where the exact gradient is identically zero.

### 102. Position: Zeroth-Order Optimization in Deep Learning Is Underexplored, Not Underpowered

- 决定：`keep_unaffected`
- 原分类：`zo_understanding`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Position: Zeroth-Order Optimization in Deep Learning Is Underexplored, Not Underpowered》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“立场论文，主张加强零阶深度学习的算法、系统与评估研究，讨论子空间结构及查询与方差权衡；范围超出 LLM，并非新优化器。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：立场论文，主张加强零阶深度学习的算法、系统与评估研究，讨论子空间结构及查询与方差权衡；范围超出 LLM，并非新优化器。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://proceedings.mlr.press/v306/liu26gv.html
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 103. Learning Dynamics of Zeroth-Order Optimization: A Kernel Perspective

- 决定：`keep_unaffected`
- 原分类：`zo_understanding`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Learning Dynamics of Zeroth-Order Optimization: A Kernel Perspective》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“通过随机投影的经验神经切线核分析 ZO-SGD 的单步学习动力学，在分析假设下将核近似精度与扰动数量及输出维数联系起来。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：通过随机投影的经验神经切线核分析 ZO-SGD 的单步学习动力学，在分析假设下将核近似精度与扰动数量及输出维数联系起来。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://proceedings.mlr.press/v306/li26in.html
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 104. LLM Zeroth-Order Fine-Tuning is an Inference Workload

- 决定：`keep_unaffected`
- 原分类：`zo_understanding`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《LLM Zeroth-Order Fine-Tuning is an Inference Workload》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“说明重复的 ZO 评分过程可以围绕推理服务运行时重新组织。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：说明重复的 ZO 评分过程可以围绕推理服务运行时重新组织。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://arxiv.org/abs/2605.28760
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 105. Zeroth-Order Optimization Finds Flat Minima

- 决定：`keep_unaffected`
- 原分类：`zo_understanding`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Zeroth-Order Optimization Finds Flat Minima》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“将随机 ZO 动力学与偏向平坦极小值的隐式偏置联系起来，并包含语言模型微调实验。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：将随机 ZO 动力学与偏向平坦极小值的隐式偏置联系起来，并包含语言模型微调实验。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://proceedings.neurips.cc/paper_files/paper/2025/hash/ebc62a3af9342eb4ebc728e5c5bc4cca-Abstract-Conference.html
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 106. Revisiting Zeroth-Order Optimization for Memory-Efficient LLM Fine-Tuning: A Benchmark

- 决定：`keep_unaffected`
- 原分类：`zo_understanding`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Revisiting Zeroth-Order Optimization for Memory-Efficient LLM Fine-Tuning: A Benchmark》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“ZO-Bench 在代表性的语言理解和生成任务上比较不同目标函数、可训练接口和模型系列。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 训练算法：ZO-Bench 在代表性的语言理解和生成任务上比较不同目标函数、可训练接口和模型系列。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://proceedings.mlr.press/v235/zhang24ad.html
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 107. ZORA: Zeroth-Order Reliability-Calibrated Adaptation with Shift-Sensitive Updates for Multimodal Test-Time Shifts

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《ZORA: Zeroth-Order Reliability-Calibrated Adaptation with Shift-Sensitive Updates for Multimodal Test-Time Shifts》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“ZORA 将前向零阶适配限制到漂移敏感的归一化层，并以偏差、置信度及源统计校准更新信号。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：ZORA 将前向零阶适配限制到漂移敏感的归一化层，并以偏差、置信度及源统计校准更新信号。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=4rQFijPAgb
- 官方摘要证据：Audio-visual continual test-time adaptation (AV-CTTA) enables pretrained multimodal models to adapt online to non-stationary target streams. However, most existing AV-CTTA methods rely on backpropagation-based updates, limiting their deployment on edge platforms with quantized backbones, inference-only engines, or strict memory and latency constraints. Zeroth-order optimization (ZOO) provides a forward-only alternative, but its direct application to AV-CTTA faces two challenges: zeroth-order queries must explore a high-dimensional multimodal parameter space without shift awareness, and entropy minimization may reinforce incorrect predictions that exhibit high confidence and low entropy under online multimodal shifts. To address these limitations, we introduce Zeroth-Order Reliability-Calibrated Adaptation (ZORA), a forward-only AV-CTTA framework that determines both where ZOO should update and which learning signals it should trust. ZORA incorporates Shift-Sensitive Layer Selection (SSLS) to restrict zeroth-order updates to shift-sensitive normalization layers in the audio and visual branches. It further employs Bias-Aware Reliability Calibration (BARC) to assign signed entropy weights based on prediction bias and confidence, while aligning target-window feature statistics with cached source-reference statistics. Experiments on Kinetics50-C and VGGSound-C demonstrate that ZORA consistently outperforms representative CTTA, multimodal adaptation, and forward-only baselines across multiple continual audio-visual shift protocols. Experiments with quantized CAV-MAE models and efficiency analyses further support resource-constrained forward-only deployment.

### 108. Shrinkage in Zeroth-Order Optimization: Estimation Risk and Expected Descent

- 决定：`keep_unaffected`
- 原分类：`zo_understanding`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《Shrinkage in Zeroth-Order Optimization: Estimation Risk and Expected Descent》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“研究有限随机方向批次下 anchored ridge shrinkage 对零阶更新的估计风险与选步后期望下降的不同影响，并在冻结 OPT-125M 检查点上用拟合损失步长搜索检验理论预测。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：研究有限随机方向批次下 anchored ridge shrinkage 对零阶更新的估计风险与选步后期望下降的不同影响，并在冻结 OPT-125M 检查点上用拟合损失步长搜索检验理论预测。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=CiCNIXROuS
- 官方摘要证据：Reducing the estimation error of a zeroth-order (ZO) update need not improve optimization after its step size is chosen. We study this distinction for anchored ridge shrinkage under exact finite batches of random directions. Optimally rescaled Euclidean risk and optimized isotropic quadratic descent rank updates identically. For iid sphere updates, an explicit Stein kernel gives risk bounds at a specified nonzero shrinkage strength. With the direction count fixed at $m\ge3$ and dimension sufficiently large, the same zero-anchor rule has certified risk reduction and strictly worse optimized descent. We quantify this relative loss and give explicit finite-dimensional enclosures. The nonlinear coefficient remains random in the limit, making effective steps vary across updates. In a specified curvature family with bounded anchors, the rule can beat Raw while remaining asymptotically inferior to the fixed mixture $(X+a)/2$. Independent simulations test these predictions. At frozen OPT-125M checkpoints, expanded step searches yield interior fitting-loss minima in all forty selections, yet the nonlinear rule has no consistent advantage. Independent profiling predicts some coefficient effects at small steps, with reduced predictive agreement at the full selected step. A local audit obtains informative risk and optimization bounds but no final endpoint confirmation in six budget--curvature comparisons. The results separate estimation risk, expected descent after choosing a step size, and statistical confirmation.

### 109. ZO-COSMO: Index-Free One-Hop Mixing for Decentralized Zeroth-Order Optimization

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 论文特定依据：保留且不受本次收紧影响：现有摘要/目录将《ZO-COSMO: Index-Free One-Hop Mixing for Decentralized Zeroth-Order Optimization》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“提出 ZO-COSMO，把两查询零阶估计与保持平均值的 masked consensus 结合，在无需显式坐标索引的一跳通信中完成稀疏去中心化更新，并在八个逻辑 Qwen LoRA worker 上验证。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 模型参数/组件边界：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 训练算法：提出 ZO-COSMO，把两查询零阶估计与保持平均值的 masked consensus 结合，在无需显式坐标索引的一跳通信中完成稀疏去中心化更新，并在八个逻辑 Qwen LoRA worker 上验证。
- 反向传播：原始来源未进一步说明。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
- 原始来源：https://openreview.net/forum?id=XhdOPTxLyT
- 官方摘要证据：Sparse communication in decentralized zeroth-order learning requires compatible peer-state coordinates. We characterize this one-hop condition and develop ZO-COSMO, coupling two-query estimation with average-preserving masked consensus using $q$ values per active link. Global supports serve all-neighbor mixing; matching updates require agreement only within each pair. We derive a sharp contraction-per-scalar bound within the matching class and convergence guarantees for the core and sparse-momentum updates. At fixed matching, exact moment identities characterize how shared directions preserve gradient-heterogeneity cancellation and redistribute estimation error and disagreement. Mechanism experiments cover unequal curvatures, noise, and sparse momentum. Further tests span $64$ synthetic agents and eight logical Qwen LoRA workers. At matched payload budgets, Qwen2-7B QNLI gains $3.65$ accuracy points over explicit-index Rand-$k$; edge-local updates gain $3.42$ and $2.53$ points over all-neighbor mixing on eight-worker complete and ring graphs. A matched-first-step ablation gives a $3.92$-point momentum benefit. Seed-aware and same-matching controls distinguish encoding, scheduling, and query correlation.
