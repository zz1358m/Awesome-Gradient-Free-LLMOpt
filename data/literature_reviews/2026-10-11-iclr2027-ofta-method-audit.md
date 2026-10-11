# OFTA 方法边界审计（ICLR 2027 投稿 G8GNLtlyAV）

- 审计日期：2026-10-11（Asia/Shanghai）
- 论文：*Learning While Generating in a Single Forward Pass*
- 方法：One-Pass Forward-Trace Adaptation（OFTA）
- 官方来源：[OpenReview forum](https://openreview.net/forum?id=G8GNLtlyAV)
- 官方 PDF 路径：[OpenReview PDF](https://openreview.net/pdf/78d147f491b72579f5b33be55a2c73b7e25f828d.pdf)
- 投稿状态：官方 note 的 `venueid` 为 `ICLR.cc/2027/Conference/Submission`；作者为 Anonymous，不能写成录用论文。

## 原始来源范围

本审计使用此前由 OpenReview API2 方法定向查询保存的官方 note。note 的 `content.abstract`、`content.title`、`content.pdf`、`venueid` 和时间元数据均来自该投稿记录；对应缓存为 `/tmp/iclr2027-catalog-20261011-attempt10/method-exact-all/17-00000.json`。

官方 note 给出的 PDF 哈希路径如上。2026-10-11 直接访问 forum PDF、哈希 PDF 以及 API2 PDF 入口均返回 HTTP 403，因此未绕过访问控制，也未声称读过无法取得的方法正文。以下结论以官方摘要为证据；涉及实现细节时明确保留待核实状态。

## 可由官方摘要确认的机制

1. OFTA 在生成每个 token 时，记录响应 log-probability 沿一个随机参数方向的变化；反馈到达后，再把这条记录转成参数更新。
2. 摘要把该量明确称为 directional derivative，并称它与反馈后另做一次计算得到的 directional derivative 相同，同时保留 forward-gradient 方法的无偏估计性质。
3. 作者声明 OFTA 的适配阶段不需要第二次模型运行、不使用 backpropagation，也不保存生成过程的 activations。
4. 实验对象包括 Qwen3 系列模型，因而与 LLM 参数适配有直接关系；更新发生在反馈到达之后，摘要描述的是会改变后续交互行为的模型更新，而非仅进行无状态推理校准。

上述四项是作者在官方摘要中的陈述；在无法读取 PDF 与实现的情况下，不将其提升为独立复现结论。

## 方法边界判定

| 术语 | 判定 | 依据与限制 |
|---|---|---|
| 无反向传播 / backpropagation-free | **摘要明确支持** | 作者明确声明反馈后更新不使用 backpropagation。该结论只针对 OFTA 适配路径，不延伸到底座模型的预训练。 |
| forward gradient | **摘要明确支持** | 摘要明确称其保持 forward-gradient 方法的无偏估计，并围绕随机参数方向的 directional derivative 构造更新。 |
| forward-mode AD / JVP | **待核实** | directional derivative 可以由 forward-mode automatic differentiation 的 JVP 得到，但摘要没有明确出现 `forward-mode AD`、`JVP` 或具体算子；PDF 当前不可访问，不能把这一实现途径写成已证实事实。 |
| 无需任何梯度 / gradient-free | **不成立为已证实表述** | 摘要使用 directional derivative 和 forward-gradient；这表明方法使用导数信息。`不反向传播` 不等价于 `不使用梯度/导数`。 |
| 严格零阶 / zeroth-order | **没有证据支持** | 摘要没有说明只通过函数值查询、有限差分或黑盒扰动估计梯度。随机方向本身不能证明零阶；方向导数若由自动微分直接传播，属于 forward-gradient 而非严格函数值零阶。 |
| 一阶/零阶混合 | **没有证据支持** | 当前来源没有呈现独立零阶分支，也没有呈现与一阶反向传播混合的适配算法。不能仅因其使用随机方向而标成 hybrid。 |

因此，OFTA 不应放入 `zo_directions`，也不应描述为“forward-only/ZO 参数更新方法”。更准确的位置是独立关联分类 `related_forward_gradient`：**前向梯度与无反向传播适配 / Forward gradients and backpropagation-free adaptation**。

## 建议的目录表述

- 核心贡献：OFTA 把反馈无关的方向导数记录提前到生成前向中；反馈到达后利用该记录形成参数更新，从而省去反馈后的第二次模型运行和反向传播。
- 方法：在随机参数方向上记录响应 log-probability 的 directional derivative，并据反馈形成 forward-gradient 更新。官方摘要没有说明该方向导数是通过 forward-mode AD/JVP、解析传播还是其他实现得到。
- 反向传播：据官方摘要，OFTA 适配更新不使用 backpropagation；底座模型预训练不在该声明范围内。
- 持久状态：摘要明确描述参数 update 与后续交互学习，但具体更新参数范围、优化器状态、保存粒度和检查点持久化策略待核实。
- 关联性：这是直接用于 Qwen3 系列 LLM 的无反向传播参数适配；其依据是 forward-gradient directional derivative，而非已证实的严格零阶函数值估计。

## 仍待核实事项

- 方法正文中方向导数的准确计算式，以及是否明确使用 forward-mode AD/JVP。
- 随机方向的采样分布、参数覆盖范围和更新尺度。
- 更新是否作用于全部模型权重、某个参数子集或适配模块。
- 优化器状态与模型更新在跨请求、跨会话和检查点中的持久化方式。
- 代码是否公开，以及实现是否与摘要中的无反向传播声明一致。
- 跨平台首次公开日期；OpenReview `odate=2026-10-03T12:42:08.286Z` 仅证明平台公开日期，可判定为 2026-10-04 至 2026-10-11 窗口外补收录，不能证明全球首次公开日期。

## 结论

现有官方证据支持将 OFTA 称为 **forward-gradient、backpropagation-free 的 LLM 适配方法**。现有证据不支持把它称为“无需任何梯度”或“严格 zeroth-order”，也不支持将其归为一阶/零阶混合方法。由于 PDF 受 403 访问限制，forward-mode AD/JVP 等实现细节须继续标为待核实。
