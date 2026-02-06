# Gomez et al. 2025 — Highly dynamic mechanical transitions in embryonic cell populations during Drosophila gastrulation

## Short note

- **Paper**: Gomez et al. 2025 — Highly dynamic mechanical transitions in embryonic cell populations during Drosophila gastrulation
- **Question**: Are dynamic, spatially patterned changes in cell material properties (not just active forces) required for robust tissue folding during gastrulation?
- **Model**: A CPM of ventral furrow formation implemented in compucell3d, informed by in vivo 3D Brillouin microscopy measurements of longitudinal stiffness.
- **Imposed**:
  - A ventral embryo cross-section with apical constriction forces based on measured myosin dynamics
  - Cells split into apical/core/basal compartments (apical–basal polarity)
  - Spatially localized + time-varying stiffness (longitudinal modulus proxy) in mesoderm sub-apical regions
- **Varied**:
  - Sub-apical vs sub-basal stiffness
  - Central vs peripheral mesoderm stiffness gradients
  - Whether stiffness changes are static vs dynamic over minutes
  - Microtubule disruption (Colcemid) and impaired folding (twist mutants) as mechanistic perturbations
- **Measured**:
  - 3D spatial maps of Brillouin shift (longitudinal modulus proxy) across cell populations during gastrulation
  - Furrow depth / fold success in the physical model
  - Association between stiffness dynamics and cell-shape behaviors
- **Conclusion**: Gastrulation-scale folding is not explained by actomyosin-driven forces alone: rapid, spatially restricted, and dynamically timed stiffening—likely mediated by microtubule reorganization—is required to translate apical constriction into robust tissue invagination.
