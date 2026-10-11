# 2026-10-12 提示词与智能体范围收紧：第 6 批审查

本报告逐条审查第 6 批 109 条核心 ES/ZO、系统及理论记录。判断只用于落实 2026-10-12 的目录范围：提示词核心研究暂缓；智能体研究仅在原始来源明确训练或持久更新语言模型、策略模型或适配器参数时保留。未据 `prompt`、`agent` 等词面自动删除。

## 结果

- 总计：109
- 不受本次范围影响并保留：105
- 明确训练智能体模型参数并保留：3
- 提示词核心而暂缓：1
- 智能体明确不训练模型参数而暂缓：0
- 智能体参数训练证据待核实而暂缓：0

## 逐条决定

### 1. EA4LLM: A Gradient-Free Approach to Large Language Model Optimization via Evolutionary Algorithms

- 决定：`keep_unaffected`
- 原分类：`es_pretraining`
- 原始来源：https://arxiv.org/abs/2510.10603
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《EA4LLM: A Gradient-Free Approach to Large Language Model Optimization via Evolutionary Algorithms》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“以真实下一 token 的平均对数概率作为适应度，使用全参数 ES 进行预训练；实验覆盖 0.5B 至 32B 参数规模的 Qwen3 风格模型。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：以真实下一 token 的平均对数概率作为适应度，使用全参数 ES 进行预训练；实验覆盖 0.5B 至 32B 参数规模的 Qwen3 风格模型。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 2. DART-ES: Difficulty-Aware Reweighting and Targeted Replay for Fine-Tuning LLMs with Evolution Strategies

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 原始来源：https://openreview.net/forum?id=dtVcF6LLYr
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《DART-ES: Difficulty-Aware Reweighting and Targeted Replay for Fine-Tuning LLMs with Evolution Strategies》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“在纯前向全参数 ES 微调中，根据种群通过率和历史难度估计重加权奖励并重放罕见可解样本；评测覆盖数学推理、指令微调、代码生成和 Countdown。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：在纯前向全参数 ES 微调中，根据种群通过率和历史难度估计重加权奖励并重放罕见可解样本；评测覆盖数学推理、指令微调、代码生成和 Countdown。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 3. Can Bayesian Optimization Efficiently Find a Strong Single Expert in Neural Thickets?

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 原始来源：https://arxiv.org/abs/2608.10867
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Can Bayesian Optimization Efficiently Find a Strong Single Expert in Neural Thickets?》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“在随机线性权重子空间中使用高斯过程引导的贝叶斯优化，无需 LLM 反传即可搜索单个可部署专家；初步推理实验使用 Qwen2.5-Instruct 0.5B–3B，方法属于贝叶斯搜索。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：在随机线性权重子空间中使用高斯过程引导的贝叶斯优化，无需 LLM 反传即可搜索单个可部署专家；初步推理实验使用 Qwen2.5-Instruct 0.5B–3B，方法属于贝叶斯搜索。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 4. Consolidating Rewarded Perturbations for LLM Post-Training

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 原始来源：https://arxiv.org/abs/2605.31494
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Consolidating Rewarded Perturbations for LLM Post-Training》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“CoRP 通过奖励与兼容性重加权、留出验证及步长校准，将高奖励参数扰动合并为单个可部署模型，全程无需 LLM 反传。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：CoRP 通过奖励与兼容性重加权、留出验证及步长校准，将高奖励参数扰动合并为单个可部署模型，全程无需 LLM 反传。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 5. Quantized Evolution Strategies: High-precision Fine-tuning of Quantized LLMs at Low-precision Cost

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 原始来源：https://openreview.net/forum?id=LR8wVOqE28
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Quantized Evolution Strategies: High-precision Fine-tuning of Quantized LLMs at Low-precision Cost》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“在离散量化权重上进行直接奖励优化，并结合误差反馈和随机种子重放；在 Countdown 上进行评测。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：在离散量化权重上进行直接奖励优化，并结合误差反馈和随机种子重放；在 Countdown 上进行评测。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 6. Fine-Tuning Language Models to Know What They Know

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 原始来源：https://arxiv.org/abs/2602.02605
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Fine-Tuning Language Models to Know What They Know》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“ESMA 直接优化元认知校准和对齐奖励。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：ESMA 直接优化元认知校准和对齐奖励。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 7. ESSAM: A Novel Competitive Evolution Strategies Approach to Reinforcement Learning for Memory Efficient LLMs Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 原始来源：https://arxiv.org/abs/2602.01003
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《ESSAM: A Novel Competitive Evolution Strategies Approach to Reinforcement Learning for Memory Efficient LLMs Fine-Tuning》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“面向内存高效推理微调的竞争式奖励 ES，主要在 GSM8K 上训练，并评估数学与代码任务的迁移能力。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：面向内存高效推理微调的竞争式奖励 ES，主要在 GSM8K 上训练，并评估数学与代码任务的迁移能力。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 8. Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 原始来源：https://openreview.net/forum?id=92oF5bU4cU
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“RandOpt 对参数扰动进行采样，筛选最佳专家并集成预测。Iterative RandOpt 博客扩展加入梯度蒸馏并重复搜索，报告在等计算量设置下使用 OLMo-3-7B 在 GSM8K 上达到 92.9%；适用性博客通过正弦波 MLP 玩具实验探索序列长度的影响。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：RandOpt 对参数扰动进行采样，筛选最佳专家并集成预测。Iterative RandOpt 博客扩展加入梯度蒸馏并重复搜索，报告在等计算量设置下使用 OLMo-3-7B 在 GSM8K 上达到 92.9%；适用性博客通过正弦波 MLP 玩具实验探索序列长度的影响。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 9. GA-LoRA: A Gradient-Free Path to Robust Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 原始来源：https://openreview.net/forum?id=yryzq0PrWy
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《GA-LoRA: A Gradient-Free Path to Robust Fine-Tuning》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“GA-LoRA 以任务准确率为 fitness、用 genetic algorithm 无反传演化 LoRA 参数，并分析其宽盆地偏好。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：GA-LoRA 以任务准确率为 fitness、用 genetic algorithm 无反传演化 LoRA 参数，并分析其宽盆地偏好。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 10. Evolution Strategies at the Hyperscale

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 原始来源：https://openreview.net/forum?id=bfVJ4GsHrO
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Evolution Strategies at the Hyperscale》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“EGGROLL 使用低秩扰动降低开销，同时通过种群聚合保留高秩更新，以支持可扩展的推理后训练。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：EGGROLL 使用低秩扰动降低开销，同时通过种群聚合保留高秩更新，以支持可扩展的推理后训练。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 11. Evolution Strategies at Scale: LLM Fine-Tuning Beyond Reinforcement Learning

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 原始来源：https://openreview.net/forum?id=i0P4ew9GpS
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Evolution Strategies at Scale: LLM Fine-Tuning Beyond Reinforcement Learning》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“采用全参数、种群并行的 ES，直接优化 Countdown、数学推理、数独、简洁性和 ARC-AGI 等任务的奖励。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：采用全参数、种群并行的 ES，直接优化 Countdown、数学推理、数独、简洁性和 ARC-AGI 等任务的奖励。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 12. Evaluation and Restoration of Safety in Reasoning-Tuned LLMs

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 原始来源：https://openreview.net/forum?id=P9tPg5GAyt
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Evaluation and Restoration of Safety in Reasoning-Tuned LLMs》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“将 evolution strategies 与后训练 guardrail 结合，以推理级显存开销恢复 reasoning-tuned LLM 的安全性。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：将 evolution strategies 与后训练 guardrail 结合，以推理级显存开销恢复 reasoning-tuned LLM 的安全性。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 13. ESSA: Evolutionary Strategies for Scalable Alignment

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 原始来源：https://arxiv.org/abs/2507.04453
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《ESSA: Evolutionary Strategies for Scalable Alignment》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“对 LoRA 适配器的奇异值坐标进行演化，并支持低精度推理；在 GSM8K、PRM800K 和 IFEval 上进行评测。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：对 LoRA 适配器的奇异值坐标进行演化，并支持低精度推理；在 GSM8K、PRM800K 和 IFEval 上进行评测。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 14. Evolutionary System 2 Reasoning: An Empirical Proof

- 决定：`keep_unaffected`
- 原分类：`es_single_turn`
- 原始来源：https://doi.org/10.66361/jiss.38
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Evolutionary System 2 Reasoning: An Empirical Proof》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“ERO 通过演化模型参数，增强模型的 System 2 reasoning 能力。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：ERO 通过演化模型参数，增强模型的 System 2 reasoning 能力。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 15. Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Memory Requirements

- 决定：`keep_agent_model_training`
- 原分类：`es_multi_turn`
- 原始来源：https://openreview.net/forum?id=LfIpbuIKLb
- 范围证据：保留：这是智能体研究，但官方摘要明确提出 forward-only full-parameter ES，并支持训练期微调和测试时适配；其持久更新对象包含智能体底层语言模型的全参数。摘要同时提到可与 prompt-space optimization 结合，但提示词搜索不是唯一或核心参数更新，不能据此排除。
- 参数证据：官方摘要原文明确写明“forward-only full-parameter optimization”以及“a full-parameter ES framework supporting both train-time fine-tuning and on-the-fly adaptation”。
- 方法/更新对象：以完整长程智能体轨迹的环境总奖励评价参数扰动，用 Evolution Strategies 更新全量语言模型参数；按摘要，该 ES 分支无需 backpropagation。摘要中的 Agentic RL/GRPO 是比较对象，不据此归入所提 ES 方法。
- 待核实：测试时适配是否保存为长期检查点、prompt-space 分支的具体启用方式与各实验使用的参数范围仍需逐实验核实。

### 16. Beyond the Best Guess: Improving LLM Solution Coverage with Evolution Strategies

- 决定：`keep_unaffected`
- 原分类：`es_understanding`
- 原始来源：https://arxiv.org/abs/2608.12679
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Beyond the Best Guess: Improving LLM Solution Coverage with Evolution Strategies》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“说明 ES 不仅影响 pass@1，还会改变推理解法的多样性和 pass@k。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：说明 ES 不仅影响 pass@1，还会改变推理解法的多样性和 pass@k。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 17. Overcoming Forgetting in LLM Fine-Tuning with Evolution Strategies

- 决定：`keep_unaffected`
- 原分类：`es_understanding`
- 原始来源：https://openreview.net/forum?id=OBMw8FwmyZ
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Overcoming Forgetting in LLM Fine-Tuning with Evolution Strategies》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“将遗忘重新表述为性能漂移，并提出锚定权重衰减方法。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：将遗忘重新表述为性能漂移，并提出锚定权重衰减方法。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 18. Matching Accuracy, Different Geometry: Evolution Strategies vs GRPO in LLM Post-Training

- 决定：`keep_unaffected`
- 原分类：`es_understanding`
- 原始来源：https://arxiv.org/abs/2604.01499
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Matching Accuracy, Different Geometry: Evolution Strategies vs GRPO in LLM Post-Training》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“比较 ES 与 GRPO 在推理准确率相近时仍然存在差异的更新几何。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：比较 ES 与 GRPO 在推理准确率相近时仍然存在差异的更新几何。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 19. The Blessing of Dimensionality in LLM Fine-tuning: A Variance-Curvature Perspective

- 决定：`keep_unaffected`
- 原分类：`es_understanding`
- 原始来源：https://openreview.net/forum?id=Pz7PpCK6Py
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《The Blessing of Dimensionality in LLM Fine-tuning: A Variance-Curvature Perspective》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“从较低的有效曲率和先升后降的训练动态解释小规模 ES 种群为何能在极高维空间中工作；实验覆盖 Qwen2.5 的多个规模以及 GSM8K、ARC-C 和 WinoGrande。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：从较低的有效曲率和先升后降的训练动态解释小规模 ES 种群为何能在极高维空间中工作；实验覆盖 Qwen2.5 的多个规模以及 GSM8K、ARC-C 和 WinoGrande。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 20. Evolutionary Strategies Lead to Catastrophic Forgetting in LLMs

- 决定：`keep_unaffected`
- 原分类：`es_understanding`
- 原始来源：https://arxiv.org/abs/2601.20861
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Evolutionary Strategies Lead to Catastrophic Forgetting in LLMs》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“分析 ES 后训练过程中模型既有能力退化的问题。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：分析 ES 后训练过程中模型既有能力退化的问题。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 21. The Exact Exchange Rate of Gradient-Free Credit

- 决定：`keep_unaffected`
- 原分类：`es_understanding`
- 原始来源：https://openreview.net/forum?id=QPRPX7pOHD
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《The Exact Exchange Rate of Gradient-Free Credit》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“推导并测量矩阵层中标量广播 ES 信用信号所需前向评估的精确交换率。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：推导并测量矩阵层中标量广播 ES 信用信号所需前向评估的精确交换率。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 22. The Evolution Strategies Paradox: Better Models from Worse Perturbations

- 决定：`keep_unaffected`
- 原分类：`es_understanding`
- 原始来源：https://openreview.net/forum?id=whvp3RjkiO
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《The Evolution Strategies Paradox: Better Models from Worse Perturbations》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“解释即使所有采样扰动均弱于当前模型，ES 仍能持续改进大语言模型的现象。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：解释即使所有采样扰动均弱于当前模型，ES 仍能持续改进大语言模型的现象。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 23. EGGROLL, Unrolled: Understanding and Improving Low-Rank Evolution Strategies at Scale

- 决定：`keep_unaffected`
- 原分类：`es_understanding`
- 原始来源：https://openreview.net/forum?id=kbNjFLXanS
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《EGGROLL, Unrolled: Understanding and Improving Low-Rank Evolution Strategies at Scale》的核心对象记为模型参数的 Evolution Strategies/遗传搜索，或该类模型训练的理论与实证分析。具体记录为“分析并改进 EGGROLL 在大语言模型规模采用的低秩进化策略机制。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：分析并改进 EGGROLL 在大语言模型规模采用的低秩进化策略机制。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 24. Dimension Is Free, Horizon Is Not: When Evolution Strategies Rival Policy Gradients for LLM Fine-Tuning

- 决定：`keep_agent_model_training`
- 原分类：`es_understanding`
- 原始来源：https://openreview.net/forum?id=59ufz75SkM
- 范围证据：保留：论文核心是比较 ES 与 policy gradient 对语言模型参数的训练，并将长程智能体任务作为关键适用场景之一；官方摘要明确 ES 评价 perturbed model 的总回报，而非只优化智能体文本、轨迹或外部 workflow。
- 参数证据：官方摘要将 ES 定义为扰动参数的估计器，并报告使用 Qwen2.5-7B-Instruct 在 27 个 NLP、数学推理和智能体任务上进行 ES–PG 对比。
- 方法/更新对象：ES 通过参数扰动和整条轨迹总回报估计语言模型更新；PG/GRPO 通过动作采样与 token 级信用训练模型。论文分析两类梯度估计器的有效参数维数与有效信用分配时域，不应把比较用 PG 的反传属性归给 ES。
- 待核实：官方摘要未逐项列出 27 个任务各自训练的参数子集、检查点持久化方式和 PG 实现细节。

### 25. Dust: Pretraining Transformers Without Backpropagation

- 决定：`keep_unaffected`
- 原分类：`zo_pretraining`
- 原始来源：现有记录未提供可抽取链接
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Dust: Pretraining Transformers Without Backpropagation》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“通过逐词元激活扰动和损失反馈分配学习信号，训练语言模型权重，并对残差混合标量使用权重空间 ES；大种群比较需要更多计算，相对 EGGROLL 的效率优势包含外推估计。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：通过逐词元激活扰动和损失反馈分配学习信号，训练语言模型权重，并对残差混合标量使用权重空间 ES；大种群比较需要更多计算，相对 EGGROLL 的效率优势包含外推估计。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 26. Scaling Zero-Order Pretraining Through Model Sharding

- 决定：`keep_unaffected`
- 原分类：`zo_pretraining`
- 原始来源：https://openreview.net/forum?id=YRoVIXOAky
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Scaling Zero-Order Pretraining Through Model Sharding》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“通过模型分片扩展零阶语言模型预训练。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：通过模型分片扩展零阶语言模型预训练。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 27. Perturbation Propagation: Scalable Local Learning without Weight Transport

- 决定：`keep_unaffected`
- 原分类：`zo_pretraining`
- 原始来源：https://openreview.net/forum?id=5T4cPwU3Nh
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Perturbation Propagation: Scalable Local Learning without Weight Transport》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“PerProp 以局部扰动斜率和随机探针反馈替代导数及权重传输，并包含 GPT 与 Mamba 预训练实验。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：PerProp 以局部扰动斜率和随机探针反馈替代导数及权重传输，并包含 GPT 与 Mamba 预训练实验。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 28. MpSub: A Momentum p-Dimensional Subspace Trust-Region Method for Derivative-Free Fine-Tuning of Large Language Models

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 原始来源：https://arxiv.org/abs/2609.07666
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《MpSub: A Momentum p-Dimensional Subspace Trust-Region Method for Derivative-Free Fine-Tuning of Large Language Models》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“在低维子空间中结合动量与随机方向，以中心有限差分估计梯度并自适应调整信赖域半径；实验使用 OPT-125M/350M 与 CommitmentBank。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：在低维子空间中结合动量与随机方向，以中心有限差分估计梯度并自适应调整信赖域半径；实验使用 OPT-125M/350M 与 CommitmentBank。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 29. AIM-ZO: Activation-Informed Subspace Maintenance for Zeroth-Order LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 原始来源：https://openreview.net/forum?id=LsJ9H83guc
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《AIM-ZO: Activation-Informed Subspace Maintenance for Zeroth-Order LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“利用前向激活持续维护参数子空间，并从中采样较窄的活跃方向集合进行纯前向零阶更新；在相同前向评估预算下评测五种大语言模型和十一个下游任务。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：利用前向激活持续维护参数子空间，并从中采样较窄的活跃方向集合进行纯前向零阶更新；在相同前向评估预算下评测五种大语言模型和十一个下游任务。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 30. SubZero+: Memory-Efficient Adaptive Zeroth-Order LLM Fine-Tuning in Random Subspaces

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 原始来源：https://openreview.net/forum?id=pZjhFo9XgF
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《SubZero+: Memory-Efficient Adaptive Zeroth-Order LLM Fine-Tuning in Random Subspaces》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“在周期刷新随机子空间中进行多查询前向差分，结合低维 Adam 和周期性动量重启，无需反向传播即可进行全权重或 LoRA 微调；在 SuperGLUE 上评测 1.3B 至 32B 模型。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：在周期刷新随机子空间中进行多查询前向差分，结合低维 Adam 和周期性动量重启，无需反向传播即可进行全权重或 LoRA 微调；在 SuperGLUE 上评测 1.3B 至 32B 模型。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 31. ZO-Act: Efficient Zeroth-Order Fine-Tuning via One-Shot Activation-Informed Low-Rank Subspaces

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 原始来源：https://openreview.net/forum?id=qy0AJWUh1L
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《ZO-Act: Efficient Zeroth-Order Fine-Tuning via One-Shot Activation-Informed Low-Rank Subspaces》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“一次性构建由激活信息引导的子空间，随后在该空间中执行 ZO 监督微调；使用 Llama-3-8B 和 OPT-13B 在语言理解、问答和常识推理任务上评测。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：一次性构建由激活信息引导的子空间，随后在该空间中执行 ZO 监督微调；使用 Llama-3-8B 和 OPT-13B 在语言理解、问答和常识推理任务上评测。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 32. RoZO: Geometry-Aware Zeroth-Order Fine-Tuning on Low-Rank Adapters for Black-Box Large Language Models

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 原始来源：https://aclanthology.org/2026.eacl-long.80/
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《RoZO: Geometry-Aware Zeroth-Order Fine-Tuning on Low-Rank Adapters for Black-Box Large Language Models》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“在 LoRA 流形的切空间中使用扰动、回缩和向量传输。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：在 LoRA 流形的切空间中使用扰动、回缩和向量传输。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 33. LOZO+: Provably Efficient Zeroth-Order Fine-Tuning via Greedy Low-Rank Subspace Selection

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 原始来源：https://proceedings.mlr.press/v306/fang26k.html
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《LOZO+: Provably Efficient Zeroth-Order Fine-Tuning via Greedy Low-Rank Subspace Selection》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“利用损失反馈与自适应阈值贪心保留有效低秩子空间方向，实现仅前向的 LLM 微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：利用损失反馈与自适应阈值贪心保留有效低秩子空间方向，实现仅前向的 LLM 微调。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 34. Enabling Downstream Adaptation of Spiking LLMs: From Zeroth-Order Learning to Cross-Resolution Transfer

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 原始来源：https://openreview.net/forum?id=bmxM07322c
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Enabling Downstream Adaptation of Spiking LLMs: From Zeroth-Order Learning to Cross-Resolution Transfer》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“使用零阶学习对脉冲大语言模型进行下游适配。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：使用零阶学习对脉冲大语言模型进行下游适配。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 35. MaZO: Masked Zeroth-Order Optimization for Multi-Task Fine-Tuning of Large Language Models

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 原始来源：https://aclanthology.org/2025.emnlp-main.935/
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《MaZO: Masked Zeroth-Order Optimization for Multi-Task Fine-Tuning of Large Language Models》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“利用参数重要性与多任务更新掩码缩小零阶微调的搜索空间并减少任务冲突。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：利用参数重要性与多任务更新掩码缩小零阶微调的搜索空间并减少任务冲突。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 36. Zeroth-Order Fine-Tuning of LLMs in Random Subspaces

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 原始来源：https://openaccess.thecvf.com/content/ICCV2025/html/Yu_Zeroth-Order_Fine-Tuning_of_LLMs_in_Random_Subspaces_ICCV_2025_paper.html
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Zeroth-Order Fine-Tuning of LLMs in Random Subspaces》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“SubZero 构造逐层低秩随机子空间，在其中进行纯前向适配。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：SubZero 构造逐层低秩随机子空间，在其中进行纯前向适配。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 37. TeZO: Empowering the Low-Rankness on the Temporal Dimension in the Zeroth-Order Optimization for Fine-tuning LLMs

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 原始来源：https://arxiv.org/abs/2501.19057
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《TeZO: Empowering the Low-Rankness on the Temporal Dimension in the Zeroth-Order Optimization for Fine-tuning LLMs》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“利用连续多个 ZO 估计之间共享的时间低秩结构。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：利用连续多个 ZO 估计之间共享的时间低秩结构。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 38. Sparse MeZO: Less Parameters for Better Performance in Zeroth-Order LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 原始来源：https://proceedings.neurips.cc/paper_files/paper/2025/hash/1e5c2efbddc02c1d971e2f19ccdb07d0-Abstract-Conference.html
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Sparse MeZO: Less Parameters for Better Performance in Zeroth-Order LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“仅扰动经过选择的一部分参数坐标，以提高监督适配效率。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：仅扰动经过选择的一部分参数坐标，以提高监督适配效率。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 39. Enhancing Zeroth-order Fine-tuning for Language Models with Low-rank Structures

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 原始来源：https://proceedings.iclr.cc/paper_files/paper/2025/hash/9ccc9d814d3dee4750debaf23061e733-Abstract-Conference.html
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Enhancing Zeroth-order Fine-tuning for Language Models with Low-rank Structures》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“LOZO 用结构化低秩扰动替代稠密随机方向。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：LOZO 用结构化低秩扰动替代稠密随机方向。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 40. Zeroth-Order Fine-Tuning of LLMs with Extreme Sparsity

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 原始来源：https://icml.cc/virtual/2024/39663
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Zeroth-Order Fine-Tuning of LLMs with Extreme Sparsity》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“选择 Fisher 敏感参数进行更新，并以低精度保存冻结权重。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：选择 Fisher 敏感参数进行更新，并以低精度保存冻结权重。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 41. Fine-Tuning Language Models with Just Forward Passes

- 决定：`keep_unaffected`
- 原分类：`zo_baselines`
- 原始来源：https://proceedings.neurips.cc/paper_files/paper/2023/hash/a627810151be4d13f907ac898ff7e948-Abstract-Conference.html
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Fine-Tuning Language Models with Just Forward Passes》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“MeZO 引入原位参数扰动和随机种子重放，使纯前向监督微调达到与推理相当的内存占用。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：MeZO 引入原位参数扰动和随机种子重放，使纯前向监督微调达到与推理相当的内存占用。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 42. ZoAQ: Adaptive Zeroth-Order Querying via Query-Reuse Coupling

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://openreview.net/forum?id=wwgUVpgO9P
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《ZoAQ: Adaptive Zeroth-Order Querying via Query-Reuse Coupling》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“复用带种子的历史双边函数评估，并通过动量一致性门控自适应分配查询预算，无需额外验证查询；纯前向 OPT 微调更新 LoRA 参数并减少评估次数，历史反馈过时偏差仍需关注。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：复用带种子的历史双边函数评估，并通过动量一致性门控自适应分配查询预算，无需额外验证查询；纯前向 OPT 微调更新 LoRA 参数并减少评估次数，历史反馈过时偏差仍需关注。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 43. Universally Empowering Zeroth-Order Optimization via Adaptive Layer-wise Sampling

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://aclanthology.org/2026.findings-acl.1999/
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Universally Empowering Zeroth-Order Optimization via Adaptive Layer-wise Sampling》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“AdaLeZO 通过非平稳多臂老虎机选层与有放回逆概率加权采样改善零阶估计及运行效率；实验覆盖 6.7B 至 30B 的 LLaMA/OPT 模型。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：AdaLeZO 通过非平稳多臂老虎机选层与有放回逆概率加权采样改善零阶估计及运行效率；实验覆盖 6.7B 至 30B 的 LLaMA/OPT 模型。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 44. Zeroth-Order Riemannian Optimization on Fixed-Rank Manifolds for LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://openreview.net/forum?id=W5wPEmfLn0
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Zeroth-Order Riemannian Optimization on Fixed-Rank Manifolds for LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“在固定秩流形上进行零阶黎曼优化，用于大语言模型微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：在固定秩流形上进行零阶黎曼优化，用于大语言模型微调。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 45. Zero-order Parameter-free Optimization for LMO-based Methods: Novel Approach for Efficient Fine-tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://openreview.net/forum?id=ZyafEp0RQn
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Zero-order Parameter-free Optimization for LMO-based Methods: Novel Approach for Efficient Fine-tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“将 parameter-free 调参、zeroth-order 函数值优化与 LMO 非欧几里得更新统一，并用于 OPT-1.3B 微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：将 parameter-free 调参、zeroth-order 函数值优化与 LMO 非欧几里得更新统一，并用于 OPT-1.3B 微调。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 46. ZOLD: A Zeroth-Order Langevin Dynamics Framework for LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://openreview.net/forum?id=IgzZOlnr2t
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《ZOLD: A Zeroth-Order Langevin Dynamics Framework for LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“ZOLD 将零阶损失评估与朗之万动力学结合，用于持久化大语言模型微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：ZOLD 将零阶损失评估与朗之万动力学结合，用于持久化大语言模型微调。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 47. Wanda-Guided Sparse Perturbations for Efficient Zeroth-Order Optimization

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://openreview.net/forum?id=gbmohVa04D
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Wanda-Guided Sparse Perturbations for Efficient Zeroth-Order Optimization》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“利用 Wanda 引导的稀疏参数扰动提高零阶优化效率。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：利用 Wanda 引导的稀疏参数扰动提高零阶优化效率。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 48. Stabilizing Zeroth-Order Fine-Tuning of Mixture-of-Experts via One-Sided Estimation and Expert Replay

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://openreview.net/forum?id=kw1764GtFE
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Stabilizing Zeroth-Order Fine-Tuning of Mixture-of-Experts via One-Sided Estimation and Expert Replay》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“结合单边估计与专家重放，稳定混合专家模型的零阶微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：结合单边估计与专家重放，稳定混合专家模型的零阶微调。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 49. Sample-Adaptive Zeroth-Order Post-Training

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://openreview.net/forum?id=1A2seNVDZG
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Sample-Adaptive Zeroth-Order Post-Training》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“SAZO 从已有方向差分估计动态样本重要性，在不增加模型评估的情况下自适应分配零阶查询。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：SAZO 从已有方向差分估计动态样本重要性，在不增加模型评估的情况下自适应分配零阶查询。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 50. Robust and Efficient Zeroth-Order LLM Fine-Tuning via Adaptive Bayesian Subspace Optimizer

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://arxiv.org/abs/2601.01452
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Robust and Efficient Zeroth-Order LLM Fine-Tuning via Adaptive Bayesian Subspace Optimizer》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“ABSO 使用贝叶斯优化器聚合带噪声的子空间观测。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：ABSO 使用贝叶斯优化器聚合带噪声的子空间观测。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 51. Prior-Informed Zeroth-Order Optimization with Adaptive Direction Alignment for Memory-Efficient LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://arxiv.org/abs/2601.04710
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Prior-Informed Zeroth-Order Optimization with Adaptive Direction Alignment for Memory-Efficient LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“PIZOO 使采样方向偏向一个能够自适应更新的先验方向。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：PIZOO 使采样方向偏向一个能够自适应更新的先验方向。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 52. Powering Up Zeroth-Order Training via Subspace Gradient Orthogonalization

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://arxiv.org/abs/2602.17155
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Powering Up Zeroth-Order Training via Subspace Gradient Orthogonalization》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“ZO-Muon 对子空间估计应用谱正交化。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：ZO-Muon 对子空间估计应用谱正交化。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 53. On Adaptivity in Zeroth-Order Optimization

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://openreview.net/forum?id=uggzfUoAgS
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《On Adaptivity in Zeroth-Order Optimization》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“MEAZO 研究大语言模型零阶微调的自适应性，以单个步长标量替代完整 Adam 矩状态。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：MEAZO 研究大语言模型零阶微调的自适应性，以单个步长标量替代完整 Adam 矩状态。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 54. MSZO: Scheduled Multi-Scale Zeroth-Order Fine-Tuning of Large Language Models

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://openreview.net/forum?id=LX2ejcw9e7
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《MSZO: Scheduled Multi-Scale Zeroth-Order Fine-Tuning of Large Language Models》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“MSZO 在多个尺度上调度扰动，用于大语言模型零阶微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：MSZO 在多个尺度上调度扰动，用于大语言模型零阶微调。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 55. MAPS: Momentum-Aware Perturbation Sampling for Zeroth-Order Optimization

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://openreview.net/forum?id=PEDv0gnlhd
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《MAPS: Momentum-Aware Perturbation Sampling for Zeroth-Order Optimization》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“MAPS 采用动量感知扰动采样改进零阶更新。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：MAPS 采用动量感知扰动采样改进零阶更新。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 56. Low-Rank Curvature for Zeroth-Order Optimization in LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://ojs.aaai.org/index.php/AAAI/article/view/39715
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Low-Rank Curvature for Zeroth-Order Optimization in LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“LOREN 将低秩分块对角曲率建模与留一估计相结合。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：LOREN 将低秩分块对角曲率建模与留一估计相结合。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 57. Learning a Zeroth-Order Optimizer for Fine-Tuning LLMs

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://openreview.net/forum?id=bRS5iwbqlC
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Learning a Zeroth-Order Optimizer for Fine-Tuning LLMs》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“学习可以在同一模型上重复使用的扰动策略。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：学习可以在同一模型上重复使用的扰动策略。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 58. LIZO: Enhancing Zeroth-Order LLM Fine-Tuning via Lateral Inhibition-Inspired Parameter Perturbation

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://openreview.net/forum?id=9PoJmVxDG5
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《LIZO: Enhancing Zeroth-Order LLM Fine-Tuning via Lateral Inhibition-Inspired Parameter Perturbation》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“LIZO 使用受侧抑制启发的结构化参数扰动改进大语言模型零阶微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：LIZO 使用受侧抑制启发的结构化参数扰动改进大语言模型零阶微调。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 59. HiZO: Hebbian-informed Zeroth-order Optimization for Efficient Fine-tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://openreview.net/forum?id=JgMy03717F
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《HiZO: Hebbian-informed Zeroth-order Optimization for Efficient Fine-tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“HiZO 利用 Hebbian 信息构造零阶方向，以提升微调效率。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：HiZO 利用 Hebbian 信息构造零阶方向，以提升微调效率。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 60. GaNsZO: Gauss-Newton Step-sized Zeroth-Order Optimization for Memory-Efficient LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://openreview.net/forum?id=iNHpKDFZRy
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《GaNsZO: Gauss-Newton Step-sized Zeroth-Order Optimization for Memory-Efficient LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“GaNsZO 以受高斯—牛顿启发的规则选择零阶步长，用于内存高效的大语言模型微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：GaNsZO 以受高斯—牛顿启发的规则选择零阶步长，用于内存高效的大语言模型微调。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 61. Displacement-Aware Subspace Adaptation for Muon-Style Zeroth-Order Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://openreview.net/forum?id=5GdFuqdQwr
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Displacement-Aware Subspace Adaptation for Muon-Style Zeroth-Order Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“DAZM 在刷新低秩 ZO-Muon 搜索子空间时保留由历史位移提取的奇异方向，用于大语言模型微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：DAZM 在刷新低秩 ZO-Muon 搜索子空间时保留由历史位移提取的奇异方向，用于大语言模型微调。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 62. Difficulty Aware Reweighting for Zeroth Order Fine-Tuning of LLMs

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://openreview.net/forum?id=KISxCpKBIf
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Difficulty Aware Reweighting for Zeroth Order Fine-Tuning of LLMs》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“在大语言模型零阶微调中按样本难度重加权，以提高查询效率。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：在大语言模型零阶微调中按样本难度重加权，以提高查询效率。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 63. CurvZO: Adaptive Curvature-Guided Sparse Zeroth-Order Optimization for Efficient LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://openreview.net/forum?id=L35b2JZ8gS
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《CurvZO: Adaptive Curvature-Guided Sparse Zeroth-Order Optimization for Efficient LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“将曲率感知的稀疏采样与概率校正结合起来。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：将曲率感知的稀疏采样与概率校正结合起来。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 64. ConMeZO: Adaptive Descent-Direction Sampling for Gradient-Free Finetuning of Large Language Models

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://proceedings.mlr.press/v300/behric26a.html
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《ConMeZO: Adaptive Descent-Direction Sampling for Gradient-Free Finetuning of Large Language Models》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“从以动量估计为中心的锥形区域中采样搜索方向。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：从以动量估计为中心的锥形区域中采样搜索方向。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 65. Adaptive Zeroth-Order Optimization via Sample-Wise Second Moments

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://openreview.net/forum?id=J5QiZLm5qs
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Adaptive Zeroth-Order Optimization via Sample-Wise Second Moments》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“利用逐样本二阶矩自适应零阶采样，实现内存高效的大语言模型微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：利用逐样本二阶矩自适应零阶采样，实现内存高效的大语言模型微调。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 66. AGZO: Activation-Guided Zeroth-Order Optimization for LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://openreview.net/forum?id=zfVxpXEZti
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《AGZO: Activation-Guided Zeroth-Order Optimization for LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“使用前向激活信息塑造扰动方向。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：使用前向激活信息塑造扰动方向。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 67. AGOZO: Activation-Guided Orthogonalized Zeroth-Order Optimization for LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://openreview.net/forum?id=rX09aLiLs7
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《AGOZO: Activation-Guided Orthogonalized Zeroth-Order Optimization for LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“AGOZO 对激活引导扰动进行正交化，用于大语言模型零阶微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：AGOZO 对激活引导扰动进行正交化，用于大语言模型零阶微调。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 68. Private Zeroth-Order Optimization with Public Data

- 决定：`defer_prompt_core`
- 原分类：`zo_directions`
- 原始来源：https://proceedings.neurips.cc/paper_files/paper/2025/hash/54de3c17e1a2457658a22ad801c721db-Abstract-Conference.html
- 范围证据：暂缓：目录记录和原始论文页面所述文本实验以 RoBERTa-base 的 prompt-tuning 为模型适配对象，优化的是提示参数；这属于用户明确要求移出现行目录的软提示核心研究。论文的差分隐私 ZO 方法本身有效，本决定仅是当前目录范围调整。
- 参数证据：现有目录的一手来源摘要记录明确将文本实验描述为 RoBERTa-base prompt-tuning on MNLI；更新对象是 prompt 参数，而非基础模型权重。
- 方法/更新对象：PAZO 使用公开数据的一阶梯度引导私有数据上的零阶估计，执行差分隐私提示参数训练；它是 FO 引导的混合 ZO prompt-tuning，而非纯函数值全模型训练。
- 待核实：论文是否还有不依赖 prompt-tuning 的语言模型全参数实验不影响本次判断；若用户解除提示词排除规则，可从归档恢复。

### 69. MUZO: Leveraging Multiple Queries and Momentum for Zeroth-Order Fine-Tuning of Large Language Models

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://aclanthology.org/2025.emnlp-main.432/
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《MUZO: Leveraging Multiple Queries and Momentum for Zeroth-Order Fine-Tuning of Large Language Models》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“对多次有限差分估计取平均并结合 Adam，实现更低方差的仅前向微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：对多次有限差分估计取平均并结合 Adam，实现更低方差的仅前向微调。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 70. Towards Fast LLM Fine-tuning through Zeroth-Order Optimization with Projected Gradient-Aligned Perturbations

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://arxiv.org/abs/2510.18228
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Towards Fast LLM Fine-tuning through Zeroth-Order Optimization with Projected Gradient-Aligned Perturbations》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“P-GAP 使低秩扰动与投影后的梯度估计方向对齐。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：P-GAP 使低秩扰动与投影后的梯度估计方向对齐。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 71. KerZOO: Kernel Function Informed Zeroth-Order Optimization for Accurate and Accelerated LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://arxiv.org/abs/2505.18886
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《KerZOO: Kernel Function Informed Zeroth-Order Optimization for Accurate and Accelerated LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“使用核函数加权扰动修正估计器。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：使用核函数加权扰动修正估计器。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 72. Harmony in Divergence: Towards Fast, Accurate, and Memory-efficient Zeroth-order LLM Fine-tuning

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://proceedings.neurips.cc/paper_files/paper/2025/hash/ffd4f5a2ea6b93e9bf5af9264d568cf2-Abstract-Conference.html
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Harmony in Divergence: Towards Fast, Accurate, and Memory-efficient Zeroth-order LLM Fine-tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“DiZO 在分析一阶与零阶优化的逐层差异后，对 ZO 更新进行逐层投影和重缩放。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：DiZO 在分析一阶与零阶优化的逐层差异后，对 ZO 更新进行逐层投影和重缩放。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 73. Variance-reduced Zeroth-Order Methods for Fine-Tuning Language Models

- 决定：`keep_unaffected`
- 原分类：`zo_directions`
- 原始来源：https://proceedings.mlr.press/v235/gautam24a.html
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Variance-reduced Zeroth-Order Methods for Fine-Tuning Language Models》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“MeZO-SVRG 在监督 ZO 微调中加入基于锚点的控制变量。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：MeZO-SVRG 在监督 ZO 微调中加入基于锚点的控制变量。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 74. VLA-ZO: Fast Zeroth-Order Adaptation for Vision-Language-Action Models

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://openreview.net/forum?id=5Azm1dweoz
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《VLA-ZO: Fast Zeroth-Order Adaptation for Vision-Language-Action Models》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“通过零阶有限差分、冻结视觉语言状态复用和调度感知预取，适配视觉语言动作模型的持久动作侧参数；在 LIBERO 分布偏移上评测，语言骨干保持冻结。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：通过零阶有限差分、冻结视觉语言状态复用和调度感知预取，适配视觉语言动作模型的持久动作侧参数；在 LIBERO 分布偏移上评测，语言骨干保持冻结。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 75. ZOCheck: CPU-Shadow Checkpointing for Zeroth-Order LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://arxiv.org/abs/2609.27189
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《ZOCheck: CPU-Shadow Checkpointing for Zeroth-Order LLM Fine-Tuning》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“通过 CPU 影子进程重放随机种子与标量更新日志，构建一致恢复镜像并在 GPU 关键路径之外持久化检查点，为零阶 LLM 微调提供容错。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：通过 CPU 影子进程重放随机种子与标量更新日志，构建一致恢复镜像并在 GPU 关键路径之外持久化检查点，为零阶 LLM 微调提供容错。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 76. Global Adaptive Momentum Meets Local Personalized Perturbation: Efficient Federated LLM Fine-Tuning with Zeroth-Order Gradients

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://aclanthology.org/2026.acl-long.1851/
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Global Adaptive Momentum Meets Local Personalized Perturbation: Efficient Federated LLM Fine-Tuning with Zeroth-Order Gradients》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“结合本地个性化扰动、零阶梯度传输与全局重构，以及自适应动量聚合，改善客户端数据异质条件下的联邦 LLM 微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：结合本地个性化扰动、零阶梯度传输与全局重构，以及自适应动量聚合，改善客户端数据异质条件下的联邦 LLM 微调。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 77. TerMeZO: Ternary Sparse Zeroth-Order Optimization for Fine-tuning BitNet Models at the Edge

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://openreview.net/forum?id=bstvvfFV4y
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《TerMeZO: Ternary Sparse Zeroth-Order Optimization for Fine-tuning BitNet Models at the Edge》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“TerMeZO 对 BitNet 边缘微调采用三值稀疏零阶更新。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：TerMeZO 对 BitNet 边缘微调采用三值稀疏零阶更新。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 78. SeedFlood: A Step Toward Scalable Decentralized Fine-Tuning of LLMs

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://openreview.net/forum?id=Psl8GgO2we
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《SeedFlood: A Step Toward Scalable Decentralized Fine-Tuning of LLMs》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“向所有客户端传播可重建零阶更新的随机种子，使去中心化微调通信量近乎不随模型规模增长。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：向所有客户端传播可重建零阶更新的随机种子，使去中心化微调通信量近乎不随模型规模增长。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 79. Rethinking Quantized LLM Fine-Tuning: An Adaptive-Grouping Alternating Zeroth-Order  Algorithm in Continuous Mapping Space

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://openreview.net/forum?id=kaA2itb1S8
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Rethinking Quantized LLM Fine-Tuning: An Adaptive-Grouping Alternating Zeroth-Order  Algorithm in Continuous Mapping Space》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“在连续映射空间中交替执行分组零阶更新，用于量化大语言模型微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：在连续映射空间中交替执行分组零阶更新，用于量化大语言模型微调。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 80. Quantize Once, Adapt in Place: Zeroth-Order Optimization with Detectable Signals

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://openreview.net/forum?id=DnAsidFUmk
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Quantize Once, Adapt in Place: Zeroth-Order Optimization with Detectable Signals》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“为量化模型设计可检测扰动信号，通过零阶评估进行原位适配。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：为量化模型设计可检测扰动信号，通过零阶评估进行原位适配。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 81. Piggybacking Training on Inference Systems

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://openreview.net/forum?id=PCZw5EG9Ft
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Piggybacking Training on Inference Systems》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“NoisyGEMM 将低秩扰动融合进推理矩阵乘，使 CMA-ES 能在服务运行时内训练 Qwen 模型。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：NoisyGEMM 将低秩扰动融合进推理矩阵乘，使 CMA-ES 能在服务运行时内训练 Qwen 模型。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 82. Inference-Native Zeroth-Order Optimization for LLMs

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://openreview.net/forum?id=EnBpzU8b3z
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Inference-Native Zeroth-Order Optimization for LLMs》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“围绕推理原生执行与前向评估重组大语言模型零阶优化。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：围绕推理原生执行与前向评估重组大语言模型零阶优化。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 83. High-Throughput and Memory-Efficient Zeroth-Order Fine-tuning LLMs with Distributed Parallel Computing

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://aclanthology.org/2026.findings-acl.2128/
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《High-Throughput and Memory-Efficient Zeroth-Order Fine-tuning LLMs with Distributed Parallel Computing》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“DistZO2 分布式执行扰动评估，并且只聚合标量结果。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：DistZO2 分布式执行扰动评估，并且只聚合标量结果。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 84. Hi-ZFO: Hierarchical Zeroth- and First-Order LLM Fine-Tuning via Importance-Guided Tensor Selection

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://aclanthology.org/2026.findings-acl.239/
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Hi-ZFO: Hierarchical Zeroth- and First-Order LLM Fine-Tuning via Importance-Guided Tensor Selection》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“根据张量重要性为其分配一阶或零阶更新。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：根据张量重要性为其分配一阶或零阶更新。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 85. HO-SFL: Hybrid-Order Split Federated Learning with Backprop-Free Clients and Dimension-Free Aggregation

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://proceedings.mlr.press/v306/chen26fd.html
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《HO-SFL: Hybrid-Order Split Federated Learning with Backprop-Free Clients and Dimension-Free Aggregation》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“在切分联邦 LoRA 微调中结合客户端零阶更新与服务端一阶反传，降低客户端内存及模型聚合通信；切分激活仍需传输。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：在切分联邦 LoRA 微调中结合客户端零阶更新与服务端一阶反传，降低客户端内存及模型聚合通信；切分激活仍需传输。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 86. Converge Faster, Talk Less: Hessian-Informed Federated Zeroth-Order Optimization

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://proceedings.iclr.cc/paper_files/paper/2026/hash/3e8b1835833ef809059efa74b9df6805-Abstract-Conference.html
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Converge Faster, Talk Less: Hessian-Informed Federated Zeroth-Order Optimization》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“HiSo 从零阶更新重建全局对角曲率预条件器，加速联邦 LLM 微调，并仅传输标量与随机种子。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：HiSo 从零阶更新重建全局对角曲率预条件器，加速联邦 LLM 微调，并仅传输标量与随机种子。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 87. AdaMeZO: Adam-style Zeroth-Order Optimizer for LLM Fine-tuning Without Maintaining the Moments

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://openreview.net/forum?id=XLc102wbnT
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《AdaMeZO: Adam-style Zeroth-Order Optimizer for LLM Fine-tuning Without Maintaining the Moments》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“无需保存完整的优化器状态即可近似自适应矩估计。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：无需保存完整的优化器状态即可近似自适应矩估计。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 88. MobiZO: Enabling Efficient LLM Fine-Tuning at the Edge via Inference Engines

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://aclanthology.org/2025.emnlp-main.1022/
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《MobiZO: Enabling Efficient LLM Fine-Tuning at the Edge via Inference Engines》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“通过 Multi-Perturbed LoRA 并行执行多查询零阶估计，并接入 ExecuTorch 实现端侧微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：通过 Multi-Perturbed LoRA 并行执行多查询零阶估计，并接入 ExecuTorch 实现端侧微调。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 89. Improving the Straight-Through Estimator with Zeroth-Order Information

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://proceedings.neurips.cc/paper_files/paper/2025/hash/f49d76cf84df83a611883c621c96d2d9-Abstract-Conference.html
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Improving the Straight-Through Estimator with Zeroth-Order Information》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“FOGZO 在量化感知预训练中结合一阶 STE 梯度与零阶更新，降低估计偏差及零阶计算成本；语言实验覆盖至 0.3B 参数的 LLaMA 模型。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：FOGZO 在量化感知预训练中结合一阶 STE 梯度与零阶更新，降低估计偏差及零阶计算成本；语言实验覆盖至 0.3B 参数的 LLaMA 模型。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 90. Second-Order Fine-Tuning without Pain for LLMs: A Hessian Informed Zeroth-Order Optimizer

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://proceedings.iclr.cc/paper_files/paper/2025/hash/6bf82cc56a5fa0287c438baa8be65a70-Abstract-Conference.html
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Second-Order Fine-Tuning without Pain for LLMs: A Hessian Informed Zeroth-Order Optimizer》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“HiZOO 使用纯前向计算估计对角曲率。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：HiZOO 使用纯前向计算估计对角曲率。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 91. Scalable Zeroth-Order Fine-Tuning for Extremely Large Language Models with Limited GPU Memory

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://openreview.net/forum?id=s0p9xpORgP
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Scalable Zeroth-Order Fine-Tuning for Extremely Large Language Models with Limited GPU Memory》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“ZO2 通过参数卸载和执行重叠支持大模型 ZO 监督微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：ZO2 通过参数卸载和执行重叠支持大模型 ZO 监督微调。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 92. QuZO: Quantized Zeroth-Order Fine-Tuning for Large Language Models

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://aclanthology.org/2025.emnlp-main.271/
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《QuZO: Quantized Zeroth-Order Fine-Tuning for Large Language Models》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“将量化整合到纯前向监督微调中。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：将量化整合到纯前向监督微调中。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 93. PaZO: Preconditioned Accelerated Zeroth-Order Optimization for Fine-Tuning LLMs

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://proceedings.neurips.cc/paper_files/paper/2025/hash/a14193e9d9fb0b03af0b717de1cac8ac-Abstract-Conference.html
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《PaZO: Preconditioned Accelerated Zeroth-Order Optimization for Fine-Tuning LLMs》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“采用预条件 SPSA、对角 Hessian 估计与移动平均，稳定并加速零阶微调。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：采用预条件 SPSA、对角 Hessian 估计与移动平均，稳定并加速零阶微调。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 94. HELENE: Hessian Layer-wise Clipping and Gradient Annealing for Accelerating Fine-tuning LLM with Zeroth-order Optimization

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://aclanthology.org/2025.emnlp-main.1323/
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《HELENE: Hessian Layer-wise Clipping and Gradient Annealing for Accelerating Fine-tuning LLM with Zeroth-order Optimization》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“引入逐层裁剪和退火机制。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：引入逐层裁剪和退火机制。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 95. Bilevel ZOFO: Efficient LLM Fine-Tuning and Meta-Training

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://proceedings.neurips.cc/paper_files/paper/2025/hash/5f999632c48f87cffb214e575581e4a9-Abstract-Conference.html
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Bilevel ZOFO: Efficient LLM Fine-Tuning and Meta-Training》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“以双层优化结合全骨干的零阶更新与适配器的一阶更新，用于微调和元训练；属于混合 FO/ZO 方法。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：以双层优化结合全骨干的零阶更新与适配器的一阶更新，用于微调和元训练；属于混合 FO/ZO 方法。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 96. ComPO: Preference Alignment via Comparison Oracles

- 决定：`keep_unaffected`
- 原分类：`zo_alignment`
- 原始来源：https://arxiv.org/abs/2505.05465
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《ComPO: Preference Alignment via Comparison Oracles》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“利用一比特偏好比较聚合参数扰动进行零阶对齐，实践结合 DPO/SimPO 梯度训练；在 UltraFeedback 上训练并以 AlpacaEval 2、Arena-Hard 和 MT-Bench 评估，2026 扩展加入在线 KL 控制。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：利用一比特偏好比较聚合参数扰动进行零阶对齐，实践结合 DPO/SimPO 梯度训练；在 UltraFeedback 上训练并以 AlpacaEval 2、Arena-Hard 和 MT-Bench 评估，2026 扩展加入在线 KL 控制。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 97. Beyond the Capability Boundary: Zeroth-Order Optimization for Self-Evolving LLM Agents

- 决定：`keep_agent_model_training`
- 原分类：`zo_multi_turn`
- 原始来源：https://openreview.net/forum?id=qqOjD3pcxL
- 范围证据：保留：这是自演化智能体研究，官方摘要明确扰动并更新 LLM 的 LoRA 参数，随后还以成功的深度研究轨迹执行监督微调；不是只更新轨迹、文本、记忆或 workflow。
- 参数证据：官方摘要明确写明“perturb LoRA parameters of LLMs”、以损失差估计梯度并“update the LoRA parameters”，以及用更新后的 LLM 采样轨迹用于 supervised fine-tuning。
- 方法/更新对象：第一阶段以 answer perplexity 为损失，通过参数扰动和损失差进行零阶 LoRA 更新；第二阶段以成功轨迹执行 SFT。ZO 阶段不需要反传，但 SFT 通常是一阶训练，摘要未明确其具体反传实现，故不把整个闭环称为无反向传播。
- 待核实：SFT 的优化器、底座冻结范围、LoRA 持久化与最终发布检查点形式待原文实现进一步核实。

### 98. Zeroth-Order Optimization at the Edge of Stability

- 决定：`keep_unaffected`
- 原分类：`zo_understanding`
- 原始来源：https://proceedings.mlr.press/v306/song26ac.html
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Zeroth-Order Optimization at the Edge of Stability》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“通过 Hessian 谱刻画两点零阶方法的均方线性稳定性，并以最大特征值和迹给出稳定性界；稳定性边缘的实验证据来自全批量视觉训练。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：通过 Hessian 谱刻画两点零阶方法的均方线性稳定性，并以最大特征值和迹给出稳定性界；稳定性边缘的实验证据来自全批量视觉训练。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 99. When Does Symmetry Reduce Effective Rank in Zeroth-Order Optimization?

- 决定：`keep_unaffected`
- 原分类：`zo_understanding`
- 原始来源：https://openreview.net/forum?id=EplKUVCy5D
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《When Does Symmetry Reduce Effective Rank in Zeroth-Order Optimization?》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“用对称轨道余维界定 Hessian 有效秩，并推导 ZO-SGD 的有限样本维度无关查询界。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：用对称轨道余维界定 Hessian 有效秩，并推导 ZO-SGD 的有限样本维度无关查询界。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 100. Understanding Clipping in Zeroth-order Optimization

- 决定：`keep_unaffected`
- 原分类：`zo_understanding`
- 原始来源：https://openreview.net/forum?id=nZByC53zgL
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Understanding Clipping in Zeroth-order Optimization》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“研究裁剪在零阶优化中的行为及影响，并包含语言模型场景。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：研究裁剪在零阶优化中的行为及影响，并包含语言模型场景。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 101. Query Complexity of Forward-Only Hebbian Learning: Theory and a Native Fit for Diffusion Models

- 决定：`keep_unaffected`
- 原分类：`zo_understanding`
- 原始来源：https://openreview.net/forum?id=NR8lYUNnka
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Query Complexity of Forward-Only Hebbian Learning: Theory and a Native Fit for Diffusion Models》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“为反向成对的纯前向 Hebbian 参数扰动估计器推导精确梯度对齐式和闭式查询预算。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：为反向成对的纯前向 Hebbian 参数扰动估计器推导精确梯度对齐式和闭式查询预算。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 102. Position: Zeroth-Order Optimization in Deep Learning Is Underexplored, Not Underpowered

- 决定：`keep_unaffected`
- 原分类：`zo_understanding`
- 原始来源：https://proceedings.mlr.press/v306/liu26gv.html
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Position: Zeroth-Order Optimization in Deep Learning Is Underexplored, Not Underpowered》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“立场论文，主张加强零阶深度学习的算法、系统与评估研究，讨论子空间结构及查询与方差权衡；范围超出 LLM，并非新优化器。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：立场论文，主张加强零阶深度学习的算法、系统与评估研究，讨论子空间结构及查询与方差权衡；范围超出 LLM，并非新优化器。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 103. Learning Dynamics of Zeroth-Order Optimization: A Kernel Perspective

- 决定：`keep_unaffected`
- 原分类：`zo_understanding`
- 原始来源：https://proceedings.mlr.press/v306/li26in.html
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Learning Dynamics of Zeroth-Order Optimization: A Kernel Perspective》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“通过随机投影的经验神经切线核分析 ZO-SGD 的单步学习动力学，在分析假设下将核近似精度与扰动数量及输出维数联系起来。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：通过随机投影的经验神经切线核分析 ZO-SGD 的单步学习动力学，在分析假设下将核近似精度与扰动数量及输出维数联系起来。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 104. LLM Zeroth-Order Fine-Tuning is an Inference Workload

- 决定：`keep_unaffected`
- 原分类：`zo_understanding`
- 原始来源：https://arxiv.org/abs/2605.28760
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《LLM Zeroth-Order Fine-Tuning is an Inference Workload》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“说明重复的 ZO 评分过程可以围绕推理服务运行时重新组织。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：说明重复的 ZO 评分过程可以围绕推理服务运行时重新组织。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 105. Zeroth-Order Optimization Finds Flat Minima

- 决定：`keep_unaffected`
- 原分类：`zo_understanding`
- 原始来源：https://proceedings.neurips.cc/paper_files/paper/2025/hash/ebc62a3af9342eb4ebc728e5c5bc4cca-Abstract-Conference.html
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Zeroth-Order Optimization Finds Flat Minima》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“将随机 ZO 动力学与偏向平坦极小值的隐式偏置联系起来，并包含语言模型微调实验。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：将随机 ZO 动力学与偏向平坦极小值的隐式偏置联系起来，并包含语言模型微调实验。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 106. Revisiting Zeroth-Order Optimization for Memory-Efficient LLM Fine-Tuning: A Benchmark

- 决定：`keep_unaffected`
- 原分类：`zo_understanding`
- 原始来源：https://proceedings.mlr.press/v235/zhang24ad.html
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Revisiting Zeroth-Order Optimization for Memory-Efficient LLM Fine-Tuning: A Benchmark》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“ZO-Bench 在代表性的语言理解和生成任务上比较不同目标函数、可训练接口和模型系列。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：本批现有记录没有嵌入官方摘要；依据目录所链接的一手论文及已有人工目录描述。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：ZO-Bench 在代表性的语言理解和生成任务上比较不同目标函数、可训练接口和模型系列。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 107. ZORA: Zeroth-Order Reliability-Calibrated Adaptation with Shift-Sensitive Updates for Multimodal Test-Time Shifts

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://openreview.net/forum?id=4rQFijPAgb
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《ZORA: Zeroth-Order Reliability-Calibrated Adaptation with Shift-Sensitive Updates for Multimodal Test-Time Shifts》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“ZORA 将前向零阶适配限制到漂移敏感的归一化层，并以偏差、置信度及源统计校准更新信号。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：ZORA 将前向零阶适配限制到漂移敏感的归一化层，并以偏差、置信度及源统计校准更新信号。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 108. Shrinkage in Zeroth-Order Optimization: Estimation Risk and Expected Descent

- 决定：`keep_unaffected`
- 原分类：`zo_understanding`
- 原始来源：https://openreview.net/forum?id=CiCNIXROuS
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《Shrinkage in Zeroth-Order Optimization: Estimation Risk and Expected Descent》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“研究有限随机方向批次下 anchored ridge shrinkage 对零阶更新的估计风险与选步后期望下降的不同影响，并在冻结 OPT-125M 检查点上用拟合损失步长搜索检验理论预测。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：研究有限随机方向批次下 anchored ridge shrinkage 对零阶更新的估计风险与选步后期望下降的不同影响，并在冻结 OPT-125M 检查点上用拟合损失步长搜索检验理论预测。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。

### 109. ZO-COSMO: Index-Free One-Hop Mixing for Decentralized Zeroth-Order Optimization

- 决定：`keep_unaffected`
- 原分类：`zo_systems`
- 原始来源：https://openreview.net/forum?id=XhdOPTxLyT
- 范围证据：保留且不受本次收紧影响：现有摘要/目录将《ZO-COSMO: Index-Free One-Hop Mixing for Decentralized Zeroth-Order Optimization》的核心对象记为语言模型权重、适配器或动作侧参数的 ZO 更新，或该类优化的系统/理论分析。具体记录为“提出 ZO-COSMO，把两查询零阶估计与保持平均值的 masked consensus 结合，在无需显式坐标索引的一跳通信中完成稀疏去中心化更新，并在八个逻辑 Qwen LoRA worker 上验证。”该对象不是提示词、软提示或提示模板；也不是仅通过固定模型更新技能、工具、程序、workflow、记忆、检索、缓存或搜索树的智能体研究。
- 参数证据：依据官方摘要记录。本条不以 prompt/agent 词面命中作判断。
- 方法/更新对象：提出 ZO-COSMO，把两查询零阶估计与保持平均值的 masked consensus 结合，在无需显式坐标索引的一跳通信中完成稀疏去中心化更新，并在八个逻辑 Qwen LoRA worker 上验证。
- 待核实：本次仅判定提示词/智能体范围，不扩展核查论文的其他方法细节。
