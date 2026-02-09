# Siegel et al. 2025 — Multiscale modeling of urothelial proliferation and regeneration

## Short note

- **Paper**:  Siegel et al. (2025) — Proliferation and regeneration of the healthy human urothelium: a multi-scale simulation approach with 16 hypotheses of cell differentiation
- **Question**: We know the urothelium is slow-turnover at steady state but can regenerate extremely quickly after injury. Which imposed cell-state logic for division and differentiation is sufficient to produce both realistic wound healing and long-term homeostasis?
- **Model**: 2D Glazier–Graner–Hogeweg / Cellular Potts (CompuCell3D) tissue model linking single-cell mechanics + cell fate rules to tissue-scale stratification and turnover.
- **Imposed**:
  - A stratified epithelium with progenitor/basal/intermediate/umbrella cell types, differential adhesion, contact inhibition, apoptosis, and periodic “voiding” that removes apical cells.  ￼
  - A fixed lineage ordering (Progenitor → Basal → Intermediate → Urothelium) and 16 alternative hypotheses for how progenitor/basal/intermediate cells divide and differentiate (including stem-cell-like division vs population asymmetry, and contact-dependent differentiation).
- **Varied**:
  - The cell-state rule set (16 hypotheses for fate logic).  ￼
  - Parameters tuned per rule set (e.g., division probabilities in population-asymmetry models, cell-type growth/apoptosis rates) to test whether a given logic can robustly stabilize.
- **Measured**:
  - Tissue outcomes classified as stable, chaotic, overgrowing (linear/exponential), or atrophic.
  - Quantitative “fitness” capturing correct layer ordering + volume distribution over long simulations (~2 years), plus regeneration time to form an umbrella barrier.
- **Conclusion**:
  - Only a narrow subset of fate-rule hypotheses produce both rapid wound healing and long-term stable stratification, showing that urothelial homeostasis is highly sensitive to imposed cell-state logic rather than to any single mechanical parameter.  ￼
  - The best-performing hypotheses share a key multiscale coupling: differentiation is regulated by spatial contact context (basal contact and medium contact), meaning tissue-scale architecture stabilizes because cell fates are explicitly coordinated with microenvironmental position.
