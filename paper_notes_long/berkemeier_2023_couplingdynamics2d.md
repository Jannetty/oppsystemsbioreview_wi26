# Berkemeier & Page 2023 — Coupling dynamics of 2D Notch–Delta signaling

## Citation

- **Cite key**: `berkemeier_2023_couplingdynamics2d`
- **Authors**: Berkemeier, Page
- **Journal**: Physical Biology
- **Year**: 2023
- **DOI**: 10.1088/1478-3975/acb6b0
- **PDF**: [Link to PDF](../papers/berkemeier_2023_couplingdynamics2d.pdf)

---

## One-sentence takeaway

Extending Notch–Delta lateral inhibition from 1D to 2D reveals that spatial coupling geometry fundamentally alters pattern stability, symmetry breaking, and robustness, demonstrating how tissue-scale organization emerges from local signaling rules.

---

## Why this paper belongs in the review

- **Model alignment**: Shows that multi-scale coupling (cell–cell signaling + tissue geometry) qualitatively changes emergent patterning behavior.
  - Tissue-scale outcomes cannot be predicted from single-cell or 1D models alone.
  - Demonstrates that spatial embedding is itself a regulatory layer.
- **Conceptual alignment**: Provides a minimal, mechanistic example of how collective patterning arises from local rules — foundational for morphogenesis and regeneration.
- **Relevance to health/longevity**: Notch–Delta governs stem cell maintenance, differentiation, regeneration, and cancer — this work clarifies the multiscale logic underlying these systems.

---

## Biological context

- Notch–Delta signaling controls fate decisions via lateral inhibition.
- Classical models focus on 1D chains or mean-field assumptions.
- Real tissues are 2D or 3D, where neighborhood geometry can reshape patterning behavior.
- How spatial structure modifies signaling dynamics remains poorly understood.

---

## Modeling framework

- **Model type**: Deterministic ODEs for Notch–Delta signaling on spatial lattices.
- **Dimensionality**: 2D cellular lattices (square, hexagonal).
- **Biological entities**:
  - Cells with internal Notch and Delta levels.
  - Local coupling via membrane-bound signaling.
- **What is imposed vs emergent**:
  - Imposed: signaling rules, neighborhood geometry.
  - Emergent: spatial patterns, symmetry breaking, oscillatory vs stable domains.

---

## Scales spanned and how they are coupled

### Molecular / subcellular scale

- Notch and Delta levels within each cell.
- Regulatory feedback loops determine activation and inhibition.

### Cellular scale

- Each cell integrates signals from immediate neighbors.
- Fate-like states emerge via mutual inhibition.

### Tissue / collective scale

- Spatial patterns of high/low Notch activity.
- Emergent stripes, spots, oscillations, and disordered states.

### Key couplings

- Molecular → cellular: signaling kinetics determine individual cell states.
- Cellular → collective: neighbor interactions generate tissue-scale patterns.
- Tissue → cellular: geometry and connectivity alter single-cell stability and fate.

---

## Why multi-scale coupling is essential in this model

- The same intracellular signaling rules produce **different outcomes** depending on spatial embedding.
- 1D models cannot predict:
  - Pattern stability in 2D
  - Sensitivity to noise
  - Domain shape and orientation
- Tissue-scale geometry becomes an active regulatory factor, not just a passive substrate.

---

## Core multi-scale insights

- Spatial geometry changes the bifurcation structure of Notch–Delta dynamics.
- Some patterns are only stable in 2D, not in 1D.
- Robust patterning depends on both biochemical feedback and spatial connectivity.
- Tissue architecture can stabilize or destabilize fate decisions.

---

## Evidence & parameterization

- **Parameterization**: Literature-based signaling kinetics.
- **Validation**: Theoretical consistency with known lateral inhibition behaviors.
- **Strength**: Systematic comparison of lattice geometries and coupling regimes.
- **Limitations**: No direct fitting to experimental tissue data; idealized geometries.

---

## Conceptual contributions to multi-scale modeling

- Demonstrates that **space is a regulatory variable**, not just a container.
- Shows how multiscale models can reveal *qualitative regime changes* absent from reduced systems.
- Provides a minimal, extensible template for spatial signaling models in development, regeneration, and cancer.

---

## Relevance to health & longevity

- Notch–Delta governs:
  - Stem cell niches
  - Tissue regeneration
  - Tumor heterogeneity
  - Aging-associated fate drift
- This work clarifies how spatial context may buffer or destabilize these systems over time.

---

## Open questions

- How do these 2D dynamics extend to curved or growing tissues?
- How does coupling to mechanics or morphogen gradients reshape these regimes?
- Can aging-related architectural changes destabilize Notch-based patterning?

---

## Tags

#development #stem_cells #patterning
#multiscale #ode #spatial_model
#scale_molecular #scale_cellular #scale_collective #scale_tissue
#param_qualitative #validation_theoretical