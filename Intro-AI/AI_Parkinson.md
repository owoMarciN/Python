# Instructions - AI_Parkinson.ipynb

## Exercise 1. 
- **Data preperation**:
    - [x] Setup and load the dataset
    - [x] Normalize features, perform 80/20 stratified train/test split.
    - [x] Visualize class distributions and pairwise relationships.

- **Supervised Baseline**:
    - [x] Implement a 30–16–1 `MLP` (ReLU–Sigmoid, BCE Loss).
    - [x] Train with fixed optimizer (```Adam```) and report metrics: ```Accuracy```, ```Precision```, ```Recall```, ```F1```, ```AUC```.
  
- **Unsupervised Representations**:
    - [x] Compare three dimensionality-reduction techniques:
        - [x] ```K-means``` clustering: Distances to K-centroids.
        - [x] ```PCA```: Top components explaining ≥95% variance.
        - [x] ```Autoencoder```: 30–16–8–16–30 structure (extract 8-D bottleneck).

- **Combined Experiment**:
    - [x] Feed transformed features (```K-means```, ```PCA```, ```Autoencoder```) into `MLP` and compare against the raw baseline.

- **Report**:
	- [x] `Figure`: Visual comparison of 2D representations (```PCA``` vs ```AE```).
	- [ ] `Table`: Effect of representation on model performance.
	- [ ] `Section`: “Supervised vs Unsupervised Representation Learning.”

## Exercise 2.
- **Study of Optimizers**:
	- [x] Train the baseline `MLP` using each optimizer (`SGD`, `Momentum`, `RMSProp`, `Adam`) with fixed hyper-parameters.
	- [x] Plot and compare:
		- [x]  `Loss` vs `Epoch` curves.
		- [ ] Validation `F1` vs `Epoch`.
		- [ ] Add learning rate scheduling (`StepLR` or `CosineAnnealing`).
    - [ ] Discuss `convergence smoothness`, `speed`, and final `accuracy`.

- **Report**:
	- [x] `Figure`: Loss curves for all optimizers.
	- [x] `Table`: `Accuracy`, `F1`, and `convergence speed`.
	- [ ] `Section`: “Effect of Optimizer Choice on Learning Stability.”

## Exercise 3.
- **Advanced Hyper-parameter Optimization Methods:**
	- [ ]  `Grid Search` — Evaluate every combination (deterministic).
    - [ ] `Random Search` — Randomly sample `λ` (efficient for large spaces).
    - [ ] `Bayesian Optimization` — Build surrogate model of performance.
    - [ ] `Hyperband` / `BOHB` — Adaptive resource allocation.
    - [ ] `Evolutionary` / `Metaheuristic Search` — `GA`, `PSO`, `DE` for `AutoML`.

 - **Experimental Protocol**:
	- [ ] Define search space Λ = \{η, μ, h, λ, batch size\}, with :
		η ∈ [1e−4, 1e−1], µ ∈ [0.7, 0.99], h ∈ {8, 16, 32}, λ ∈ [0, 0.01].
	- [ ] Apply all five tuning methods for a fixed budget (e.g., 25 trials).
    - [ ] Evaluate validation `F1` and total computational cost.
    - [ ] Compare efficiency of each trials to reach top performance.

- **Report**:
	- [ ] `Figure`: Performance trajectory (best F1 vs iteration) for each tuning algorithm.
	- [ ] `Table`: Best hyper-parameters and performance summary.
	- [ ] `Section`: “Comparative Analysis of Hyper-parameter Optimization Methods.”

## Exercise 4.
- **Representation × Optimizer × Tuning Synergy:**
	- [ ]  Combine each optimized configuration (from Ex. 3) with different feature representations (`baseline`, `K-means`, `PCA`, `Autoencoder`).
	- [ ] Evaluate performance for all optimizers (`SGD`, `Momentum`, `RMSProp`, `Adam`).
	- [ ] Record training time, loss stability, and generalization metrics.

## Exercise 5.
- **Research Paper Compilation:**
	- [ ] **Abstract (≈150 words)**: Summarize findings.
	- [ ] **Introduction**: Motivation for optimizing both model parameters and meta-parameters.
	- [ ] **Methodology**: Based on Experiments 1–4.
	- [ ] **Results and Discussion**: Key figures and tables.
	- [ ] **Conclusion**:
		- [ ] Which optimizer and tuning strategy performed best?
		- [ ] How did unsupervised representations influence stability?
		- [ ] What are the implications for `AutoML` in medical datasets?

	- [ ] **Optional Research Extension**:
		- [ ] Extend `Bayesian`/`DE-based` tuning to architecture-level `AutoML`.
		- [ ] Compare on 2 new datasets (`Pima Diabetes`, `Heart Disease`)
		- [ ] Target short paper submission (`EvoApplications`, `GECCO Education track`).


    
    
    


    
    
    
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNDYxMTE2NDEsODkyMDk4NjYzLDE1MD
gwODAyMjMsLTk3ODg5NDUxOF19
-->