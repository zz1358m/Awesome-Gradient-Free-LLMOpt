# ICLR 2027 方法定向检索候选审查：Batch 6

- 范围：`review-batch-6.json` 的 30 条官方 OpenReview 投稿摘要。
- 来源限定：明确方法词/精确短语查询；未使用裸 `LLM`、`language model` 或全会场枚举发现候选。
- 结论：新增收录 0，具体排除 30。排除的共同充分条件是官方摘要未同时给出语言模型/VLM 优化关联与所提方法的梯度无关机制；各条理由如下，不将基线、有限差分标签或普通语义命中当作所提方法。
- 日期：全部记录的 OpenReview `odate` 元数据为 2026-10-03T12:42:08.286Z；这只表示平台在线日期，不等于跨平台首次公开日期。

## 1. Adaptive Stepsizes Meet Momentum: An Improved Zeroth-Order Method

- OpenReview：[gK96j8p3Vx](https://openreview.net/forum?id=gK96j8p3Vx)
- 命中查询：zeroth-order, gradient-free
- 实际机制：ZO-AdaNesterov uses stochastic zeroth-order oracle estimates, adaptive step sizes, and Nesterov momentum for generic convex and nonconvex objectives.
- 优化对象：Deep-network parameters in generic numerical experiments.
- 反传/梯度依赖：The proposed optimizer is zeroth-order; no reverse-mode gradient is required by the stated oracle model.
- 持久状态：It updates persistent optimized parameters.
- 决定：排除。The abstract contains no language-model, VLM, prompting, or agent application; this is generic ZO theory.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 2. An Energy-Aware Sampling Method for Physics-Informed Neural Networks

- OpenReview：[b26gPbGN9O](https://openreview.net/forum?id=b26gPbGN9O)
- 命中查询：derivative-free
- 实际机制：PAS allocates PINN collocation points from a derivative-free double-well-potential signal, combining global exploration and local refinement.
- 优化对象：Sampling locations for phase-field PDE training.
- 反传/梯度依赖：The sampling score is derivative-free, while the downstream PINN training procedure is not characterized as backpropagation-free.
- 持久状态：It persistently changes the collocation set; model-weight persistence is not specified.
- 决定：排除。Scientific PDE/PINN work with no language-model or VLM connection.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 3. CABM: Efficient Concept Augmentation for Interpretable Deep Models

- OpenReview：[FZAUWsJD3m](https://openreview.net/forum?id=FZAUWsJD3m)
- 命中查询：parameter perturbation
- 实际机制：CABM adds concepts post hoc using influence-inspired local parameter updates, EK-FAC approximate curvature, and a trust region.
- 优化对象：An appended concept block in a concept bottleneck model.
- 反传/梯度依赖：This is an approximate second-order/influence update, not a gradient-free search; the abstract does not establish absence of backpropagation.
- 持久状态：It installs a persistent concept block/model update.
- 决定：排除。No language-model application, and “parameter perturbation” denotes the formulation rather than ZO perturbation estimation.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 4. Closing the Train-Test Gap in World Models for Gradient-Based Planning

- OpenReview：[PgUvaCo2j4](https://openreview.net/forum?id=PgUvaCo2j4)
- 命中查询：gradient-free
- 实际机制：The paper trains world models with synthesized data to improve gradient-based test-time planning.
- 优化对象：World-model training data and action sequences in robotic planning.
- 反传/梯度依赖：The proposed planner is explicitly gradient-based; gradient-free CEM appears only as a comparator.
- 持久状态：World-model weights are trained persistently; test-time actions are transient.
- 决定：排除。Robotics/navigation work with no language-model link; a baseline mention cannot qualify the proposed method.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 5. Continual Reinforcement Learning with Neuroevolution

- OpenReview：[UxsGk4on0e](https://openreview.net/forum?id=UxsGk4on0e)
- 命中查询：evolution strategies, neuroevolution
- 实际机制：The study compares ES and genetic algorithms that mutate and select policy-network weights under continual task changes.
- 优化对象：Weights of reinforcement-learning policies.
- 反传/梯度依赖：ES/GA branches are gradient-free weight-space search; compared RL methods may use gradients.
- 持久状态：The evolved policy weights persist across tasks.
- 决定：排除。No LLM, VLM, language-agent, or language-policy application is stated.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 6. Data Selection for Conditional Flow Matching via State–Velocity Geometry

- OpenReview：[NqKMGp6N98](https://openreview.net/forum?id=NqKMGp6N98)
- 命中查询：zero-order
- 实际机制：State-Jac selects flow-matching training samples using endpoint coverage and proxy local-response sketches.
- 优化对象：A coreset for conditional flow matching.
- 反传/梯度依赖：“Zero-order” describes prescribed supervision geometry, not a zeroth-order optimizer.
- 持久状态：The selected dataset persists for final training; model weights are subsequently trained by an unspecified standard procedure.
- 决定：排除。Image flow-matching experiments only; no language-model optimization.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 7. Distilling Diffusion Score Discrepancy for Efficient Training Data Attribution

- OpenReview：[ZzJWMU6dUI](https://openreview.net/forum?id=ZzJWMU6dUI)
- 命中查询：forward-only
- 实际机制：TID estimates diffusion training-data influence with curvature/preconditioned gradient similarity, then TIDE distills its rankings into a forward-only query-time student.
- 优化对象：Attribution rankings for diffusion-generated images.
- 反传/梯度依赖：TID uses gradient similarity and curvature; TIDE inference is forward-only but its student is explicitly trained.
- 持久状态：The student parameters persist after training; per-query rankings do not.
- 决定：排除。Diffusion image attribution rather than language-model optimization.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 8. Epistemic Forward Models: Learning Predictive States for Action-Conditioned Future Distinguishability

- OpenReview：[qY8l677bHH](https://openreview.net/forum?id=qY8l677bHH)
- 命中查询：finite difference
- 实际机制：EFO learns to predict action-conditioned identifiability subspaces from supervision built with finite-difference Jacobians of a fixed RGB-D encoder.
- 优化对象：A robot predictive-state model and action selection.
- 反传/梯度依赖：Finite differences construct offline labels; they are not the optimization rule. Training backpropagation is not specified.
- 持久状态：The learned EFO model persists; action choices are transient.
- 决定：排除。Pure RGB-D robotics/active sensing with no LLM or VLM language backbone.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 9. Fast-Weight Memory for Adaptive Recommendation

- OpenReview：[phwjDb6goi](https://openreview.net/forum?id=phwjDb6goi)
- 命中查询：gradient-free
- 实际机制：FWPRec updates a user-specific fast associative memory from positive and negative feedback while keeping global recommender parameters fixed at inference.
- 优化对象：Per-user fast-weight memory for recommendations.
- 反传/梯度依赖：Inference memory updates are described as gradient-free; training of the learned update/model is not specified as gradient-free.
- 持久状态：User memory persists across requests; global parameters are unchanged at inference.
- 决定：排除。A recommender-system adaptation mechanism with no language-model or VLM application.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 10. From Decoder Backward to Encoder Forward: Antisymmetric Latent Updates for Diffusion Inverse Solvers

- OpenReview：[6kwgPuiq8R](https://openreview.net/forum?id=6kwgPuiq8R)
- 命中查询：forward-only
- 实际机制：ASLU maps pixel corrections to latent diffusion updates by antisymmetric differences of two encoder forward passes.
- 优化对象：Latents during image/video inverse-problem sampling.
- 反传/梯度依赖：The ASLU conversion avoids decoder and measurement-operator gradients, but other correction-producing solver components may differ.
- 持久状态：Sampling latents are transient; the abstract does not describe model-weight updates.
- 决定：排除。Image, video, and CT inverse solving with no language-model relevance.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 11. Geometric Regularization of Learned Behavior Spaces in Unsupervised Quality-Diversity Optimization

- OpenReview：[rtIp1pxlSG](https://openreview.net/forum?id=rtIp1pxlSG)
- 命中查询：neuroevolution
- 实际机制：AURORA-VC regularizes an autoencoder’s learned robot-behavior descriptors with variance and covariance penalties inside quality-diversity search.
- 优化对象：Robot policy repertoires and their behavior-descriptor autoencoder.
- 反传/梯度依赖：Quality-diversity search is evolutionary, while the descriptor autoencoder is trained; the abstract does not claim that component is backpropagation-free.
- 持久状态：Policy repertoires and learned descriptor parameters persist.
- 决定：排除。Robot quality-diversity optimization without language-model or VLM use.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 12. Grow or Prune? Constructive Neuroevolution of Kolmogorov–Arnold Networks

- OpenReview：[pYpybkF5Yi](https://openreview.net/forum?id=pYpybkF5Yi)
- 命中查询：neuroevolution
- 实际机制：C-KAN evolves typed spline-edge graphs with Safe Mutation, behavioral speciation, and short Lamarckian adaptation for symbolic regression.
- 优化对象：KAN graph structures and edge parameters.
- 反传/梯度依赖：Evolution is gradient-free; the short Lamarckian adaptation mechanism is not specified and may be gradient-based.
- 持久状态：Evolved graph structures and fitted parameters persist.
- 决定：排除。Symbolic regression/KAN architecture search, not language-model optimization.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 13. Hq-Recycle: Efficient Bilevel Optimization through Adjoint Recycling

- OpenReview：[per4W4wDLF](https://openreview.net/forum?id=per4W4wDLF)
- 命中查询：finite difference
- 实际机制：Hq-Recycle reuses quasi-Newton lower-level and adjoint estimates, using a directional finite-difference curvature probe to initialize implicit hypergradient refinement.
- 优化对象：Adjoints and variables in generic bilevel optimization.
- 反传/梯度依赖：The method remains an implicit-hypergradient/quasi-Newton method; finite difference is a curvature probe, not a gradient-free outer optimizer.
- 持久状态：Lower/outer variables and recycled adjoint state persist across iterations.
- 决定：排除。Only linear classification and ridge regression are stated; no language-model application.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 14. LaDiM: Layered Diagnosis for Multi-Agent Code Migration

- OpenReview：[qixS3l1Wsf](https://openreview.net/forum?id=qixS3l1Wsf)
- 命中查询：forward gradient
- 实际机制：LaDiM coordinates Translator, Verifier, and Repair LLM agents to diagnose and repair cross-framework code migrations using execution-stage discrepancies and repair history.
- 优化对象：Migrated code and persistent repair history.
- 反传/梯度依赖：The phrase hit comes from the sequence “forward, gradient computation, update”; the abstract states no gradient-free search or model adaptation.
- 持久状态：Repair history and code revisions persist; LLM-weight updates are not described.
- 决定：排除。LLMs are used, but there is no qualifying gradient-free optimization mechanism.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 15. Learning Invariant Spike Representations For Robust Remote Sensing Detection

- OpenReview：[JqlxDi0k8a](https://openreview.net/forum?id=JqlxDi0k8a)
- 命中查询：without backpropagation
- 实际机制：SIP jointly trains invariant spike representations and aggregates temporal spike responses at inference without parameter updates.
- 优化对象：Spiking remote-sensing detector representations and transient inference responses.
- 反传/梯度依赖：TSCI inference has no backpropagation, but PCT is a training stage whose gradient use is not negated.
- 持久状态：PCT model parameters persist; TSCI makes no parameter updates.
- 决定：排除。Remote-sensing vision/SNN work without language models.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 16. LESS: Lightweight Evolutionary Supernet Search in Minutes

- OpenReview：[ORAHHcnXVe](https://openreview.net/forum?id=ORAHHcnXVe)
- 命中查询：CMA-ES, evolutionary optimization
- 实际机制：LESS briefly warms up a supernet, then uses CMA-ES over discrete neural architectures with candidate-conditioned supernet updates.
- 优化对象：CNN/NAS architectures and supernet weights.
- 反传/梯度依赖：CMA-ES architecture search is gradient-free, but each candidate receives learned supernet updates.
- 持久状态：The selected architecture/configuration and supernet training state persist.
- 决定：排除。NAS-Bench/CIFAR/ImageNet architecture search with no language-model application.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 17. Neighbor Averaging as Perturbation: Risk-Aware Decentralized Federated Learning via Noise-Probed Sensitivity

- OpenReview：[zl4U97GZ9L](https://openreview.net/forum?id=zl4U97GZ9L)
- 命中查询：parameter perturbation
- 实际机制：NoRA scores the risk of decentralized neighbor-model averaging from noise-probed sensitivity and model displacement, then attenuates risky interactions.
- 优化对象：Federated model-averaging weights and local client models.
- 反传/梯度依赖：Noise probes estimate sensitivity, while local model training remains part of DFL and is not claimed gradient-free.
- 持久状态：Client models and averaging state persist.
- 决定：排除。Generic/CIFAR federated learning with no LLM or VLM optimization.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 18. Observable Geometry for Derivative-Free Optimization of Dynamical Systems

- OpenReview：[C69ql69qP4](https://openreview.net/forum?id=C69ql69qP4)
- 命中查询：derivative-free
- 实际机制：OM-EKI builds response-informed coordinates and applies ensemble Kalman inversion to structured dynamical-system outputs.
- 优化对象：Parameters of Neural ODE, stiff UDE, and spiking recurrence models.
- 反传/梯度依赖：OM-EKI is derivative-free; exact and surrogate gradients are comparison settings.
- 持久状态：Optimized dynamical-system model parameters persist.
- 决定：排除。Scientific dynamical systems and spiking digits only; no language-model application.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 19. Past2Next: Past Action Conditioning Policy with Data-Augmented Tokenization

- OpenReview：[R8obaNz0uu](https://openreview.net/forum?id=R8obaNz0uu)
- 命中查询：finite difference
- 实际机制：Past2Next conditions a robot autoregressive policy on past actions and their first- and second-order temporal finite differences.
- 优化对象：Robot action tokens and a geometry-aware tokenizer/policy.
- 反传/梯度依赖：Finite differences are input motion features, not function-value gradient estimates or an optimizer.
- 持久状态：Tokenizer and policy parameters persist after standard training; inference actions are transient.
- 决定：排除。Robot imitation learning without a language model or qualifying VLM optimization.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 20. Physics-Informed Stochastic Configuration Machine: A Backpropagation-Free Neural Network with Fast Training involving Nonlinear Differential Equations

- OpenReview：[9TVnxhsWUC](https://openreview.net/forum?id=9TVnxhsWUC)
- 命中查询：backpropagation-free
- 实际机制：PI-SCM analytically linearizes nonlinear physical operators and solves successive least-squares problems for network weights.
- 优化对象：Physics-informed network weights for differential equations.
- 反传/梯度依赖：The proposed training is explicitly backpropagation-free, using analytic Jacobians and least squares rather than a ZO estimator.
- 持久状态：Solved network weights persist.
- 决定：排除。Scientific PDE learning without language-model or VLM use.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 21. Principled Backpropagation-Free Training via Layerwise Fenchel-Young Lifting

- OpenReview：[L6QLnBFEml](https://openreview.net/forum?id=L6QLnBFEml)
- 命中查询：backpropagation-free
- 实际机制：Lifty lifts activations into optimization variables and uses layerwise closed-form Fenchel–Young/proximal updates.
- 优化对象：Generic neural-network activations and layer parameters.
- 反传/梯度依赖：It is explicitly backpropagation-free but is not shown on language models in the abstract.
- 持久状态：Trained network parameters persist.
- 决定：排除。General neural-network training theory with no LLM/VLM application stated.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 22. Query Efficient Black-box Adversarial Attack via Dataset Distillation

- OpenReview：[hRc0sauHSE](https://openreview.net/forum?id=hRc0sauHSE)
- 命中查询：gradient-free
- 实际机制：DDAttack uses distilled examples to initialize and guide score-based black-box adversarial perturbation search.
- 优化对象：Input-space adversarial perturbations.
- 反传/梯度依赖：The attack search is gradient-free; dataset distillation may have its own training procedure, which is not characterized here.
- 持久状态：Attack perturbations are instance-specific; distilled examples may persist.
- 决定：排除。The abstract gives generic/adversarially trained model evaluation, with no language-model or VLM target.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 23. Rollback: Experience Backtracking in World Models for Policy Improvement

- OpenReview：[k7VrTpZ9RJ](https://openreview.net/forum?id=k7VrTpZ9RJ)
- 命中查询：forward-only
- 实际机制：Rollback rewinds a robot world model, branches alternative actions, and distills counterfactual outcomes into policy supervision.
- 优化对象：Robot policy and world-model experience.
- 反传/梯度依赖：“Forward-only” describes prior world models as passive surrogates, not the proposed method’s gradient property; training details are unspecified.
- 持久状态：World-model and policy improvements persist.
- 决定：排除。Real-robot policy improvement without language-model optimization.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 24. Second-Order Geometry of Generative Paths: Fragility and Targeted Refinement

- OpenReview：[JruDtQUl8A](https://openreview.net/forum?id=JruDtQUl8A)
- 命中查询：finite difference
- 实际机制：The work measures second-order bending/acceleration risk in generative paths and uses it to allocate a refinement budget.
- 优化对象：Evaluation/refinement locations and perturbations in visual generative paths.
- 反传/梯度依赖：Finite differences estimate material acceleration for diagnosis/allocation; no ZO parameter optimization is proposed.
- 持久状态：No persistent model-weight update is described; refinement allocation is run-specific.
- 决定：排除。Visual flow/image-editing analysis without language-model connection.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 25. Simulator-Refined Diffusion for Radio-Frequency Inverse Design

- OpenReview：[IJWhEOL1pT](https://openreview.net/forum?id=IJWhEOL1pT)
- 命中查询：zeroth-order
- 实际机制：SRD combines differentiable-surrogate gradients with searches evaluated by a non-differentiable electromagnetic simulator during diffusion sampling.
- 优化对象：PCB layouts generated at inference.
- 反传/梯度依赖：This is a hybrid: surrogate gradients propose directions and simulator evaluations select updates.
- 持久状态：Generated layouts persist as outputs; diffusion-model weight updates are not described.
- 决定：排除。RF circuit inverse design, not language-model/VLM optimization.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 26. Stein Guidance without Gradients: Discretization Uniform Diffusion Inference Time Scaling beyond Particle SMC

- OpenReview：[JOo32CtWHH](https://openreview.net/forum?id=JOo32CtWHH)
- 命中查询：derivative-free, without gradients
- 实际机制：The method uses Gaussian-Stein value-weighted candidate selection and a derivative-free whole-path independence-MH correction for diffusion inference.
- 优化对象：Diffusion proposal trajectories during inference.
- 反传/梯度依赖：Guidance and MH correction use values rather than target gradients; how the value function is obtained is left open.
- 持久状态：Trajectory states are transient; no model-weight update is stated.
- 决定：排除。Generic diffusion sampling theory with no text/LLM application in the abstract.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 27. The Multi-Query Paradox in Zeroth-Order Optimization

- OpenReview：[7Yl2JKKec1](https://openreview.net/forum?id=7Yl2JKKec1)
- 命中查询：zeroth-order
- 实际机制：The paper analyzes query allocation for ZO-Avg and projection-based ZO-Align across standard objective classes.
- 优化对象：Generic optimization variables.
- 反传/梯度依赖：Both analyzed algorithms use function-value queries rather than explicit gradients.
- 持久状态：Optimized variables persist, but no model/application is identified.
- 决定：排除。Generic zeroth-order theory with no language-model experiment or analysis.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 28. Value-Twisted Sequential Monte Carlo for Task-Aware Missing-Modality Connectome Completion

- OpenReview：[zndZYf5lWa](https://openreview.net/forum?id=zndZYf5lWa)
- 命中查询：gradient-free
- 实际机制：VT-SMC samples diffusion-generated brain connectomes from a utility-tilted distribution using frozen uncertainty-aware task feedback and corrected particles.
- 优化对象：Missing-modality connectomes and particle states.
- 反传/梯度依赖：The framework admits a gradient-free variant; the main/final variant and training dependencies are not fully distinguished in the abstract.
- 持久状态：Generated connectomes are outputs; task-feedback/model parameters are frozen during inference.
- 决定：排除。Medical imaging/connectome completion without language-model relevance.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 29. When Does Derivative Supervision Help? A Study of Label Construction and Noise

- OpenReview：[ayiQSugiuW](https://openreview.net/forum?id=ayiQSugiuW)
- 命中查询：finite difference
- 实际机制：The study compares constructions and noise levels for derivative labels under a shared neural training procedure.
- 优化对象：Derivative-supervision labels and ordinary scientific predictors.
- 反传/梯度依赖：Finite differences construct labels; they are not a derivative-free optimization method, and training remains conventional.
- 持久状态：Predictor weights persist after training.
- 决定：排除。Scientific derivative-supervision study without language-model application.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.

## 30. ZOBA: An Efficient Single-loop Zeroth-order Bilevel Optimization Algorithm

- OpenReview：[4tp5TPhaoL](https://openreview.net/forum?id=4tp5TPhaoL)
- 命中查询：zeroth-order, finite difference
- 实际机制：ZOBA/HF-ZOBA reuse delayed function values for finite-difference hypergradient approximations in single-loop bilevel optimization.
- 优化对象：Inner and outer variables of generic bilevel problems.
- 反传/梯度依赖：Outer hypergradients are approximated from function values; inner-solver gradient requirements are not resolved by the abstract.
- 持久状态：Inner/outer optimization variables persist.
- 决定：排除。Generic theory and an unspecified adversarial-ML task; no LLM/VLM application.
- 待核实：Only the official submission abstract was reviewed; implementation, supplement, code, authorship disclosure, and cross-platform first-public date were not independently verified.
