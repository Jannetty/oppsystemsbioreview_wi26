# Duteil et al. 2025 — Multiscale modeling of EGFR signaling on a growing tissue manifold

## Short note

- **Paper**: Duteil et al. 2025 — Multiscale modeling of EGFR signaling on a growing tissue manifold
- **Question**: How do tissue growth, changing geometry, and relative compartment movement reshap morphogen distribution and signaling over developmental time?
- **Model**: Transport–reaction–diffusion model for Gurken (GRK) secretion, diffusion, receptor binding/internalization, and dpERK output, solved on a time-evolving curved surface (prolate spheroid) representing the perivitelline space
- **Imposed**:
  - GRK is secreted from a moving source near the oocyte nucleus, diffuses on the curved perivitelline surface, and activates EGFR in follicle cells
  - Egg chamber growth changes the geometry and thus the diffusion operator (time-varying Laplace–Beltrami).
  - Follicle cells shift posteriorly over time, modeled as an additional advection term for receptor/signaling variables.
  - EGFR dynamics include binding/unbinding, internalization, recycling/degradation, and negative feedback via KEK1 and Sprouty.
- **Varied**:
  - Ligand dosage (1x, WT, 4x GRK).
  - Genetic perturbations: styRNAi, egfrRNAi (modeled as reduced production or receptor availability).
  - Morphological perturbations that are experimentally lethal: stopping oocyte nucleus movement, stopping follicle-cell shift, stopping growth.
- **Measured**: GRK and dpERK spatial profiles along A–P and D–V axes across stages 7–10A; dpERK intensity and elongation under morphological perturbations.
- **Conclusion**: Tissue morphogenesis can directly re-pattern signaling: the relative motion of follicle cells over the growing oocyte, nuclear repositioning, and growth-driven geometry changes are sufficient to reshape the EGFR activation field—meaning signaling patterns are not determined by reaction–diffusion alone, but by reaction–diffusion on a moving, deforming domain.
