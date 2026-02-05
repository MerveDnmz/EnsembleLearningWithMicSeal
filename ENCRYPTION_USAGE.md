# Encryption Usage — Where SEAL Was Applied

This document lists pipeline stages and whether homomorphic encryption (SEAL CKKS) was applied in this project, and whether the stage can practically be implemented under HE.

| Pipeline Stage | Applied in this Project? | HE-feasible? | Notes / Limitations |
|---|---:|---:|---|
| Data storage / transfer | Yes | Yes | We store / transfer ciphertexts securely. CKKS supports encrypted storage and arithmetic on encoded values.
| Feature engineering (sum/mean/std/product/ratio) | Partially (we measured/encoded test inputs) | Mostly yes | Simple arithmetic (add/mul) works in CKKS. Complex ops (rank, sort) are not practical.
| Data augmentation (SMOTE) | No | No / Difficult | SMOTE requires nearest-neighbor and synthetic-sample generation — impractical under HE.
| Normalization / scaling | No (done in plaintext) | Yes | Scaling is linear — can be done homomorphically with multiplications.
| Model training (fitting) | No (plaintext only) | No / Very difficult | Training algorithms (tree growth, gradient updates) are not practical with current ML libs on HE.
| Base learners (RandomForest, XGBoost, LightGBM) | No (plaintext) | No | Tree ensembles require branching (comparisons) — not HE-friendly.
| Meta-learner (Logistic Regression) | Plaintext training; approximated under HE for inference | Yes (inference) | Logistic inference (linear + sigmoid) can be approximated with polynomials (we used Chebyshev-like approximation).
| Inference (test time) | Hybrid in this project: X_test encrypted; inference simulated via decrypt→predict or polynomial approx | Partially — yes for linear models, no for branch-heavy models | We encrypted `X_test` and measured enc/dec overhead. For encrypted inference we used polynomial sigmoid approx and a hybrid approach for base-learner outputs.
| Evaluation / metrics (AUC, F1) | Computed in plaintext after decrypting approximated probabilities | Yes (post-decrypt) | Metrics computed on decrypted probabilities. Direct metric computation on ciphertexts is possible but not implemented.
| Model storage (saving trained model) | No (plaintext model saved) | Yes (ciphertext model possible but not used) | Storing model parameters encrypted is feasible but not implemented here.

## Summary — What we implemented in this project
- We initialized SEAL CKKS and measured encoding/encryption/decryption overheads for `X_test` (batch experiments).  
- We trained all models in plaintext (scikit-learn / XGBoost / LightGBM) because HE training is impractical with these libraries.  
- For encrypted inference we implemented a hybrid approach: encrypt `X_test`, decrypt per-sample inside a controlled routine to get base-learner outputs, then apply a polynomial approximation of sigmoid for the meta-learner to simulate encrypted activation. We also implemented a fully simulated encrypted inference path where we apply polynomial approximation to the computed logits to produce approximate probabilities (this demonstrates the expected accuracy degradation and compute/memory overhead).

## Practical guidance for readers
- If your goal is **privacy-preserving inference** with minimal model change, prefer linear models (logistic regression) or small neural networks with polynomial activations.  
- If you must use tree ensembles, do evaluation on the server side with encrypted features only for secure storage/transfer, or convert to HE-friendly models.  
- Use ciphertext packing and parameter tuning (poly_modulus_degree, coeff_modulus, scale) to improve throughput and precision; these are the knobs that control security vs performance.

If you want, I can:
- Add this table into `README.md` (I will add a link to this file).  
- Expand the table with exact command outputs (encryption times, batch-size results) for reproducibility.  
- Prepare a separate notebook that demonstrates a small end-to-end HE-friendly logistic regression training and encrypted inference prototype.
