# ICLR 2027 方法定向检索覆盖与审查结果

## 结论

本轮按用户指定范围完成 18 个梯度无关方法短语的 OpenReview 会议限定精确检索。查询统一使用 `group=ICLR.cc/2027/Conference`、`source=forum`、`type=exact`、`content=all`；每项官方计数均小于 1000，单页返回的独立 note 数与官方 `count` 一致。18 页合并为 387 个独立 note，其中 206 个已在主审查记录，余下 181 个逐篇阅读官方摘要后，补收录 7 个、具体排除 174 个、待处理 0 个。

这证明指定的 18 个方法定向查询在 2026-10-11 的返回已完整处理，不证明覆盖全部 ICLR 2027 投稿。此前保存的 14,990 条广泛语言语料、409 条词面命中和 14,581 条未命中二筛不用于本轮候选发现、科学排除或收录。

## 查询证据

| 精确短语 | 官方计数 | 独立 note | 页数 |
|---|---:|---:|---:|
| zeroth-order | 94 | 94 | 1 |
| zero-order | 13 | 13 | 1 |
| gradient-free | 85 | 85 | 1 |
| derivative-free | 20 | 20 | 1 |
| backpropagation-free | 19 | 19 | 1 |
| forward-only | 51 | 51 | 1 |
| without backpropagation | 22 | 22 | 1 |
| without gradients | 13 | 13 | 1 |
| MeZO | 7 | 7 | 1 |
| SPSA | 3 | 3 | 1 |
| CMA-ES | 19 | 19 | 1 |
| evolution strategies | 30 | 30 | 1 |
| evolutionary optimization | 19 | 19 | 1 |
| neuroevolution | 7 | 7 | 1 |
| parameter perturbation | 7 | 7 | 1 |
| weight perturbation | 8 | 8 | 1 |
| finite difference | 48 | 48 | 1 |
| forward gradient | 4 | 4 | 1 |

- 实际检索开始：`2026-10-11T19:02:01.928575+08:00`
- 实际检索结束：`2026-10-11T19:02:38.896542+08:00`
- 机器可读查询 URL、逐页时间、响应哈希和 181 条决定：[`2026-10-11-iclr2027-method-directed-search.json`](2026-10-11-iclr2027-method-directed-search.json)
- 官方原始响应缓存：`/tmp/iclr2027-catalog-20261011-attempt10/method-exact-all/`

## 新收录

| OpenReview | 论文 | 分类 | 关联边界 |
|---|---|---|---|
| [mDDEcTyT5B](https://openreview.net/forum?id=mDDEcTyT5B) | GS-MoE | `related_closed_form` | training-free MoE 压缩与 gradient-free 层重要性评分；不是 ZO 梯度估计。 |
| [a04cCyok2x](https://openreview.net/forum?id=a04cCyok2x) | SURGE | `related_closed_form` | 谱分解融合既有 RL checkpoint；融合阶段不继续训练，原 RL 训练方式待核实。 |
| [iVQu1sp529](https://openreview.net/forum?id=iVQu1sp529) | HO-FL | `related_hybrid` | 模型底段用 ZO，顶段明确用 FO/backpropagation。 |
| [G8GNLtlyAV](https://openreview.net/forum?id=G8GNLtlyAV) | OFTA | `zo_directions` | 在一次 LLM 生成前向中记录随机参数方向导数，反馈后更新参数。 |
| [CiCNIXROuS](https://openreview.net/forum?id=CiCNIXROuS) | Shrinkage in Zeroth-Order Optimization | `zo_understanding` | 分析 shrinkage 的估计风险与期望下降，并在 OPT-125M 邻域审计。 |
| [lXiUD5V7wG](https://openreview.net/forum?id=lXiUD5V7wG) | Neural Thickets | `related_closed_form` | 随机权重扰动专家的有限差分分解与谱选择；候选专家训练方式待核实。 |
| [XhdOPTxLyT](https://openreview.net/forum?id=XhdOPTxLyT) | ZO-COSMO | `zo_systems` | 两查询 ZO 与 masked consensus，用于 Qwen2-7B QNLI LoRA worker。 |

七条均为匿名 ICLR 2027 Conference Submission，未添加录用标记。其 OpenReview `odate` 均为 2026-10-03；这只表示平台公开日期，因此属于 2026-10-04 至 2026-10-11 窗口外的周期补收录，跨平台首次公开日期仍待核实。

## 逐篇审查文件

- [批次 1](2026-10-11-iclr2027-method-exact-batch-1.md)：31 条，收录 1、排除 30。
- [批次 2](2026-10-11-iclr2027-method-exact-batch-2.md)：30 条，收录 0、排除 30。
- [批次 3](2026-10-11-iclr2027-method-exact-batch-3.md)：30 条，收录 1、排除 29。
- [批次 4](2026-10-11-iclr2027-method-exact-batch-4.md)：30 条，收录 1、排除 29。
- [批次 5](2026-10-11-iclr2027-method-exact-batch-5.md)：30 条，收录 4、排除 26。
- [批次 6](2026-10-11-iclr2027-method-exact-batch-6.md)：30 条，收录 0、排除 30。

每条排除都保留题名、官方链接、命中查询和论文特定理由；有限差分作为时间导数、数值验证或理论工具，以及纯视觉、时序、物理、控制和通用优化研究，均未因词面命中被误收录。
