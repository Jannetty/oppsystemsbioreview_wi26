# Chandrasegaran et al. 2025 — Multiscale dynamics of senescent cells in wound healing

## Short note

- **Paper**: Chandrasegaran et al. 2025 —  Spatiotemporal senescence dynamics in wound healing, chronic wounds, and fibrosis
- **Question**: We know senescent cells can both promote wound repair and drive chronic pathology. When and where do senescent cells become beneficial vs harmful, and how does the timing of their appearance shift healing toward chronic wounds or fibrosis?
- **Model**: Multiscale Cellular Potts wound-healing model (compucell3d) coupling cell-state transitions (senescence phenotypes) to spatial tissue repair dynamics.
- **Imposed**: A spatial wound environment with migrating/proliferating fibroblasts and inflammatory cells; senescence induction rules with a time constraint (senescence is only allowed after a specified phase); temporally structured SASP behavior (fibrogenic vs fibrolytic influence on repair); ECM deposition and remodeling as tissue-scale outputs of local cell states.
- **Varied**: Probability that myofibroblasts become senescent (PSNC); timing constraint for senescence induction (TSEN); presence/absence of background inflammatory senescence to represent aged tissue conditions.
- **Measured**: Time courses of ECM accumulation and cell populations; classification of emergent repair regimes (healthy healing vs chronic inflammation vs fibrotic repair) across parameter sweeps.
- **Conclusion**: Wound pathology can emerge without changing core repair machinery, by shifting when senescent cells arise and how many are present: early/background inflammatory senescence drives chronic wounds, while absent or delayed senescence drives fibrosis, showing that tissue outcomes depend on spatiotemporal coordination of senescent fate dynamics (not senescence as a single static state).
