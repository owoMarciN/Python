# Instructions used to create AI_Parkison.ipynb

## Exercise 1. 
- **Data preperation**:
    - [ ] Setup and load the dataset
    - [ ] Normalize features, perform 80/20 stratified train/test split.
    - [ ] Visualize class distributions and pairwise relationships.

- **Supervised Baseline**:
    - [ ] Implement a 30–16–1 MLP (ReLU–Sigmoid, BCE Loss).
    - [ ] Train with fixed optimizer (```Adam```) and report metrics: ```Accuracy```, ```Precision```, ```Recall```, ```F1```, ```AUC```.
  
- **Unsupervised Representations**:
    - [ ] Compare three dimensionality-reduction techniques:
        - [ ] ```K-means``` clustering: Distances to K-centroids.
        - [ ] ```PCA```: Top components explaining ≥95% variance.
        - [ ] ```Autoencoder```: 30–16–8–16–30 structure (extract 8-D bottleneck).

- **Combined Experiment**:
    - [ ] Feed transformed features (K-means, PCA, Autoencoder) into MLP and compare against the raw baseline.
        - [ ] Figure: Visual comparison of 2D representations (PCA vs AE).
        - [ ] Table: Effect of representation on model performance.
        - [ ] Section: “Supervised vs Unsupervised Representation Learning.”

-------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------
2 — Comparative Study of Optimizers
Goal:
Empirically analyze how different gradient-based optimizers influence convergence and generalization.
Optimizers:
SGD, Momentum, RMSProp, Adam.
Tasks:

    Train the baseline MLP using each optimizer (fixed hyperparameters).
    Plot and compare:
        Loss vs Epoch curves.
        Validation F1 vs Epoch.
        Add learning rate scheduling (StepLR or CosineAnnealing).
    Discuss convergence smoothness, speed, and final accuracy.

Deliverables:

    Figure 2: Loss curves for all optimizers.
    Table 1b: Accuracy, F1, and convergence speed.
    Section 3.1: “Effect of Optimizer Choice on Learning Stability.”

-------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------
3 — Advanced Hyperparameter Optimization Methods
Goal:
Explore five classes of hyperparameter optimization algorithms and analyze their efficiency and results; including

    Grid Search — Evaluate every combination (deterministic).
    Random Search — Randomly sample λ (efficient for large spaces).
    Bayesian Optimization — Build surrogate model of performance.
    Hyperband / BOHB — Adaptive resource allocation.
    Evolutionary / Metaheuristic Search — GA, PSO, DE for AutoML

Experimental Protocol:
Define search space:
Λ={η,μ,h,λ,batch size}\Lambda = \{ \eta, \mu, h, \lambda, \text{batch size}\}Λ={η,μ,h,λ,batch size}
Example ranges:
η ∈ [1e−4, 1e−1], µ ∈ [0.7, 0.99], h ∈ {8, 16, 32}, λ ∈ [0, 0.01].

    Apply all five tuning methods for a fixed budget (e.g., 25 trials).
    Evaluate validation F1 and total computational cost.
    Compare efficiency (# of trials to reach top performance).

Deliverables:

    Figure 3: Performance trajectory (best F1 vs iteration) for each tuning algorithm.
    Table 1.1: Best hyperparameters and performance summary.
    Section 3.2: “Comparative Analysis of Hyperparameter Optimization Methods.”

-------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------
4 — Representation × Optimizer × Tuning Synergy
Goal: Investigate interaction effects between feature representation, optimizer type, and tuning method.
Tasks:

    Combine each optimized configuration (from 3) with different feature representations (raw, K-means, PCA, Autoencoder).
    Evaluate performance for all optimizers (SGD, Momentum, RMSProp, Adam).
    Record training time, loss stability, and generalization metrics.

-------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------
5 — Research Paper Compilation
Goal:
Transform empirical results into a 3–4 page mini-paper (IEEE/GECCO template).
Outline:

    Abstract (≈150 words): Summarize findings.
    Introduction: Motivation for optimizing both model parameters and meta-parameters.
    Methodology: Based on Experiments 1–4.
    Results and Discussion: Key figures and tables.

Conclusion:

    Which optimizer and tuning strategy performed best?
    How did unsupervised representations influence stability?
    What are the implications for AutoML in medical datasets?

Optional Research Extension:

    Extend Bayesian/DE-based tuning to architecture-level AutoML.
    Compare on 2 new datasets (Pima Diabetes, Heart Disease)
    Target short paper submission (EvoApplications, GECCO Education track).
