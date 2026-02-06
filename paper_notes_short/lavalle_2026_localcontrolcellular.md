# Lavalle et al. (2026) — Local control of proliferation in zebrafish neuromast regeneration

## Short note

- **Paper**: Lavalle et al. (2026) — Local control of proliferation in zebrafish neuromast regeneration
- **Question**: Can organ-level regeneration (correct size + correct cell-type proportions) be explained by purely local control of cell proliferation?
- **Model**: Minimal 2D Cellular Potts Model (CPM) of neuromast regeneration after laser ablation.
- **Imposed**:
  - A spatial CPM tissue with three cell types (hair, sustentacular/support, mantle) with adhesion + shape constraints.
  - Division probabilities and fate outcomes for sustentacular vs mantle cells.
  - A delayed “regeneration onset” after injury.
  - A local negative-feedback rule: cells stop dividing when they exceed a type-specific threshold of same-type neighbors.
- **Varied**:
  - Proliferation “switch” thresholds (neighbor-count cutoffs), separately for sustentacular vs mantle cells.
  - Presence/absence of a post-ablation delay in proliferation onset.
  - Ablation geometries (nearly complete ablation vs half ablation vs mantle-only ablation).
- **Measured**:
  - Total cell number vs time after injury.
  - Cell-type proportions (hair/support/mantle) over time.
  - Spatial tissue architecture and symmetry recovery.
  - Distribution of same-type neighbor counts at division (compared to experiment).
- **Conclusion**: Neuromast regeneration kinetics and final proportions can emerge from a simple, local, cell-type-specific negative feedback rule (“stop dividing once enough same-type neighbors accumulate”), showing that organ-scale homeostasis can be explained without invoking global control signals.
