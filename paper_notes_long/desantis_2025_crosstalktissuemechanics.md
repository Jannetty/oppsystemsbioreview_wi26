# De Santis et al. 2025 — Mechanochemical symmetry breaking in human gastruloids

## Citation

- **Cite key**: `desantis_2025_crosstalktissuemechanics`
- **Authors**: De Santis et al.
- **Journal**: *Nature Communications*
- **Year**: 2025
- **DOI**: 10.1016/j.stem.2025.09.006
- **PDF**: [Link to PDF](../papers/desantis_2025_gastruloid_symmetry_breaking.pdf)
- **Code**: [github](https://github.com/laurentjutrasdube/Optogenetic-Programmable_Human_Embryo_Models)

---

## One-sentence takeaway

Coupling tissue-scale mechanics to molecular morphogen dynamics reveals that symmetry breaking in human gastruloids requires mechanochemical feedback, not morphogen signaling alone.

---

## Why this paper belongs in the review

- **Model alignment**: Shows two models, first a model that doesn't take into account shape/multiscale mechanical feedback on morphogen distribution and makes incorrect predictions about differentiation trajectories of cells, and then a model that incorperates multiscale mechanical feedback and makes correct predictions.
  - Provides a clear example where a single-scale morphogen model fails without mechanical coupling.
  - Demonstrates how tissue mechanics gates molecular patterning, reversing the usual “molecules → shape” narrative.
  - The system’s behavior fundamentally changes when mechanics are removed, even with identical molecular rules.
- **Subject alignment**: Development of morphology, in close collaboration with experiments (iterating back and forth in the paper).
  - Strong case study of mechanochemical multi-scale necessity in early development.

---

## Biological context

- Human gastrulation involves symmetry breaking that establishes germ layers and body axes.
- Traditional models emphasize morphogen gradients (BMP, WNT, NODAL) as primary drivers.
- Recent experiments show that geometric confinement and mechanical stress strongly affect fate patterning.
- How mechanics and signaling integrate to control symmetry breaking remained unresolved.

---

## Modeling framework

- **Model type**: Reaction–diffusion–transport PDEs on evolving tissue geometry.
- **Dimensionality**: 2D tissue-scale representations of gastruloids.
- **Biological entities**:
  - Morphogens: BMP4, WNT3, NODAL
  - Mechanotransducers: YAP/TAZ
  - Cell fate markers: SOX2, ISL1, BRA
  - Tissue-scale tension and geometry
- **What is imposed vs emergent**:
  - Imposed: initial geometry, ligand application, constitutive kinetic rules.
  - Emergent: symmetry breaking, elongation patterns, spatial fate domains.

---

## Scales spanned and how they are coupled

### Molecular / subcellular scale

- Morphogen concentrations (BMP4, WNT, NODAL) modeled as continuous fields.
- Nuclear YAP/TAZ modulates signaling sensitivity and production.

### Cellular scale

- Cell fate transitions depend on local morphogen levels and mechanotransduction state.
- Signaling sensitivity is regulated by YAP localization (mechanically controlled).

### Tissue scale

- Tissue geometry and tension fields evolve over time.
- Confinement, elongation, and stress patterns shape morphogen distribution.

### Key couplings

- Tissue → molecular: mechanical stress regulates morphogen production and signaling thresholds via YAP.
- Molecular → cellular: morphogen fields determine fate decisions.
- Tissue → signaling geometry: evolving shape reshapes diffusion and transport patterns.
- Cellular → tissue: fate patterning influences mechanical properties and elongation.

---

## Core multi-scale insights

- Tissue mechanics acts as a gatekeeper for molecular patterning, not just a downstream consequence.
- Symmetry breaking is a mechanochemical instability, not a purely chemical one.
- Geometry and stress can bias or suppress morphogen-driven patterning entirely.
- Robust fate patterning emerges from reciprocal coupling between mechanics and signaling, not either alone.

---

## Evidence & parameterization

- **In vitro data**: Human gastruloids under geometric confinement and controlled BMP4 induction.
- **Imaging**: Spatial fate maps and YAP localization patterns.
- **Parameterization**:
  - Ligand kinetics from literature.
  - Mechanical coupling inferred from experimental perturbations.
- **Validation**:
  - Model reproduces fate patterns across confinement geometries.
  - Predicts failure of symmetry breaking in mechanically permissive but unconfined contexts.
- **Limitations**:
  - Tissue treated as a continuum (no explicit single-cell mechanics).
  - Mechanics represented phenomenologically rather than force-based at cell level.

---

## Conceptual contributions to multi-scale modeling

- Demonstrates that in some systems (especially development) mechanics should be considered a regulatory layer.
  - Shows how geometry and force fields can function as regulatory variables.

---

## Open questions and testable predictions

- Which specific mechanical cues (tension vs curvature vs strain rate) most strongly regulate YAP–WNT coupling?
- Can similar mechanochemical gating explain symmetry breaking failures in aging or disease?
- How do single-cell mechanical properties aggregate into tissue-scale regulatory fields?
- Would disrupting YAP-mediated feedback abolish symmetry breaking even with intact morphogen gradients?

---

## Quotes / figures to remember

> “Mechanical context determines whether morphogen signaling can induce mesoderm formation.” (paraphrased)

---

## Tags

#development #morphogenesis
#multiscale #mechanochemical
#scale_molecular #scale_cellular #scale_tissue
#pde
#data_in_vitro #data_imaging #data_expression #data_perturbation
#param_qualitative #validation_qualitative
