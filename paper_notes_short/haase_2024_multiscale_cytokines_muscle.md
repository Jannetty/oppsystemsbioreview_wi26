# Haase et al. 2024 — Multiscale cytokine interactions in muscle regeneration

## Short note

- **Paper**: Haase et al. 2024 — Multiscale cytokine interactions in muscle regeneration
- **Question**: We know muscle regeneration is orchestrated by many cytokines and immune/stromal cell types, but single-cytokine interventions often fail. Which cytokine dynamics (diffusion, decay, and cross-talk) most strongly control tissue-scale regeneration outcomes?
- **Model**: Spatial agent-based Cellular Potts model (compucell3d) linking cell behaviors (immune, fibroblast, stem/progenitor) with cytokine diffusion fields and microvascular remodeling.
- **Imposed**:
  - Literature-derived rules for recruitment, chemotaxis, phagocytosis, secretion/uptake, proliferation, differentiation, and apoptosis across multiple cell types
  - explicit diffusion and decay for multiple cytokines
  - tissue injury geometry derived from histology.
- **Varied**:
  - Cytokine knockouts and injections (e.g., VEGF dose response)
  - Immune/stem cell depletion
  - Hindered angiogenesis
  - Systematic sweeps of cytokine diffusion and decay parameters (including multi-parameter combinations).
- **Measured**:
  - Muscle fiber cross-sectional area recovery
  - cell counts over time (SSC, fibroblast, macrophage subtypes, neutrophils)
  - capillary density
  - collagen/ECM density
  - cytokine concentration trajectories
- **Conclusion**: Regeneration is controlled by nonlinear, time-dependent interactions between cytokines rather than any single factor; model-guided multi-cytokine perturbations produce larger recovery improvements than single-cytokine changes, showing why multiscale coupling is necessary to predict tissue-scale healing outcomes.
