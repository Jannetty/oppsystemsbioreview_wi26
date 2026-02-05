# Gill et a. 2024 - Divergent buckling patterns in the chick gut

## Citation

- **Cite key**: 'gill_2024_developmentalmechanicsdivergent`
- **Authors**: Gill et al.
- **Journal**: PNAS
- **Year**: 2024
- **DOI**: 10.1073/pnas.2310992121
- **PDF**: [Link to PDF](../papers/gill_2024_developmentalmechanicsdivergent.pdf)
- **Link to code**: [Zendono](https://zenodo.org/records/11995760)

---

## One-sentence takeaway

Coupling measured tissue geometry, growth, and material properties across scales reveals how distinct gut regions adopt unique, multiscale folding patterns from a common developmental precursor.

---

## Why this paper belongs in the review

- **Model alignment**: Describes mechanics-driven multiscale modeling grounded in experimental measurements.
  - Provides a clear example where tissue-scale identity emerges from cross-scale physical constraints, not new molecular programs
  - Two tissue layers are independently modeled to see how different physical properties affect emergent shape at organ-region level.
- **Subject alignment**: Morphology development (in this case in gut). Includes iteration with experimentalists.

---

## Biological context

- The foregut, midgut, and hindgut arise from a common embryonic tube.
- Despite shared molecular patterning, these regions develop distinct epithelial folding architectures.
- The mechanical basis of this regionalization has been unclear.

---

## Modeling framework

- **Model type**: Continuum mechanics model of differential growth and elasticity.
- **Mathematical formalism**: Nonlinear elasticity with multiplicative growth decomposition.
- **Dimensionality**: 2D cross-sectional (plane-strain) models.
- **Key biological components**: Endoderm, mesenchyme, smooth muscle layers.
- **What is imposed vs emergent**:
  - Imposed: measured geometry, stiffness, growth profiles.
  - Emergent: primary and secondary buckling patterns, multiscale morphologies.

---

## Scales spanned and how they are coupled

### Sub-tissue/Cellular scale

- Endoderm and mesenchyme treated as mechanically distinct layers.
- Growth and stiffness reflect underlying cellular composition.

### Tissue scale

- Tube geometry, muscle constraints, and axial prestretch.
- Region-specific buckling modes and postbuckling behavior.

### Cross-scale coupling

- Sub-tissue-scale material properties constrain tissue-scale deformation.
- Growth anisotropy couples developmental timing to mechanical instability.
- Secondary buckling emerges from history-dependent stress accumulation.

---

## Core multi-scale insights

- No single parameter (growth, stiffness, or geometry alone) explains regional morphology.
- Distinct folding patterns emerge only when multiple scales are coupled simultaneously.
- Secondary and multiscale buckling cannot be predicted from static or single-scale models.
- Regional identity is encoded in gradients of physical properties, not just gene expression.
- Multiscale morphologies arise from sequential mechanical instabilities.
- Developmental timing controls when tissues cross mechanical bifurcation thresholds.

---

## Evidence & parameterization

- **Data sources**: In vivo chick gut imaging, thickness measurements, mechanical testing.
- **Parameterization**: Quantitative fitting of geometry and modulus ratios.
- **Validation**: Reproduction of observed morphologies across gut regions.
- **Limitations**: 2D geometry, absence of explicit molecular regulation.

---

## Conceptual contributions to multi-scale modeling

- Highlights mechanics as a control mechanism.
- Complements signaling-based multiscale models by explaining form without explicit molecular dynamics.

---

## Tags

#development
#multiscale #continuum_model #mechanics
#scale_cellular #scale_tissue
#data_in_vivo #data_imaging
#param_quantitative #validation_qualitative
