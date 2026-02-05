# Duteil et al. 2025 — Multiscale modeling of EGFR signaling on a growing tissue manifold

## Citation

- **Cite key**: `duteil_2025_computationalframeworkstudy`
- **Authors**: Duteil, Revaitis, Niepielko, Klein, Yakoby, Piccoli
- **Journal**: PLOS Computational Biology
- **Year**: 2025
- **DOI**: 10.1371/journal.pcbi.1013802
- **PDF**: [Link to PDF](../papers/duteil_2025_computationalframeworkstudy.pdf)
- **Code & data**: [figshare](https://doi.org/10.6084/m9.figshare.30043216)

---

## One-sentence takeaway

Coupling reaction–diffusion signaling to evolving tissue geometry reveals that morphogen patterning in Drosophila oogenesis is shaped as much by tissue growth and cell movement as by molecular kinetics.

---

## Why this paper belongs in the review

- **Model alignment**: Paper describes novel multiscale reaction diffusion transport PDE on imposed spatial structure that couples molecular signaling, tissue growth, and cell rearrangement.
  - Shows how multi-scale modeling enables exploration of experimentally inaccessible perturbations (due to lethality).
  - Claims to provide a reusable framework for signaling on growing tissues applicable beyond oogenesis.
- **Subject alignment**: Shows that morphological change inherent in development itself modulates signal distribution, not just vice versa (bidirectional feedback between morphogen gradients influencing morphology and morphology influencing morphogen gradients).

---

## Biological context

- EGFR signaling via Gurken (GRK) patterns follicle cells during Drosophila oogenesis.
- Proper GRK/dpERK distribution is essential for AP and DV axis formation.
- Classical models assume static tissue geometry and steady-state signaling.
- How tissue growth and cell movement influence signaling remained unclear.

---

## Modeling framework

- **Model type**: Reaction–diffusion–transport PDEs on evolving manifolds
- **Platform**: Custom MATLAB framework
- **Dimensionality**: 2D curved surface embedded in 3D (prolate spheroid)
- **Biological entities**:
  - Ligand: GRK
  - Receptor: EGFR
  - Signal: dpERK
  - Inhibitors: KEK1, STY
- **What is imposed vs emergent**:
  - Imposed: tissue growth rates, nuclear movement, FC rearrangement
  - Emergent: dpERK spatial distribution, anisotropy, how signaling patterns are affected by manifold growth

---

## Scales spanned and how they are coupled

### Molecular scale

- GRK diffusion, binding, internalization, degradation.
- Negative feedback via KEK1 and STY modeled explicitly.
- Represented via coupled PDE–ODE systems.

### Cellular scale

- Follicle cells act as spatially moving reaction sites.
- EGFR internalization and signal generation occur on FCs.
- FC rearrangement modeled as tangential transport.

### Tissue / geometric scale

- Egg chamber growth alters curvature and domain size.
- Growth dynamically modifies diffusion via time-dependent Laplace–Beltrami operators.
- Geometry is not static but co-evolves with signaling.

### Key couplings

- Geometry → signaling: curvature and growth reshape diffusion anisotropy.
- Signaling → geometry: ligand source and receptor localization tied to tissue architecture.
- Cellular motion → signaling: FC shifts alter where signal is received and interpreted.

---

## Core multi-scale insights

- Signal patterns cannot be reproduced under static geometry assumptions, tissue growth fundamentally alters morphogen diffusion and signaling geometry.
- Cell rearrangement contributes to signal elongation independently of ligand kinetics.
  - Growth alters diffusion operators, producing anisotropic and stage-dependent patterning.
  - Relative motion between ligand source and receptor-bearing cells reshapes signaling domains.
- Morphogen patterning emerges from interactions between transport, geometry, and reaction, not any single scale.
  - Morphology is a dynamic regulator of molecular patterning.

---

## Evidence & parameterization

- **Data sources**:
  - In vivo imaging of GRK and dpERK patterns.
  - Quantitative AP and DV intensity profiles.
  - Egg chamber geometry measurements across stages.
- **Parameterization**:
  - Molecular rates from literature.
  - Geometry and movement from experimental measurements.
  - Inhibitor strengths calibrated to imaging data.
- **Validation**:
  - Reproduces WT patterns.
  - Predicts effects of EGFR and STY RNAi perturbations.
- **Limitations**:
  - Focused on 2D surface, neglects internal cytoplasmic flows.

---

## Conceptual contributions to multi-scale modeling

- Demonstrates necessity of coupling evolving geometry to signaling dynamics.
- Provides a generalizable framework for morphogen transport on growing tissues.
- Suggests tissue morphology should be treated as an active regulatory variable in signaling models.

---

## Relevance to human health & longevity

- Offers a modeling paradigm for:
  - regenerative tissues,
  - aging epithelia,
  - tumor growth where geometry and signaling co-evolve.
- Highlights how morphological drift with age may reshape signaling landscapes independent of molecular changes.

---

## Open questions

- How robust is signaling to geometric noise or asymmetric growth?
- How would stochastic cell behaviors alter these deterministic predictions?
- Can this framework be extended to 3D volumetric tissues?

---

## Tags

#development
#multiscale #hybrid_model #pde
#scale_molecular #scale_cellular #scale_tissue
#data_in_vivo #data_imaging #data_expression
#data_scale_molecular #data_scale_tissue
#param_quantitative #validation_quantitative
