# Fruleux et al. 2024 — Growth couples temporal and spatial fluctuations during morphogenesis

## Citation

- **Cite key**: `fruleux_2024_growthcouplestemporal`
- **Authors**: Fruleux, Hong, Roeder, Li, Boudaoud
- **Journal**: PNAS
- **Year**: 2024
- **DOI**: 10.1073/pnas.2318481121
- **PDF**: [Link to PDF](../papers/fruleux_2024_growth_couples_spatiotemporal_fluctuations.pdf)
- **Link to code**: [zenodo](https://zenodo.org/records/11105905)

---

## One-sentence takeaway

A minimal growth-advection + memory model predicts that tissue expansion “stretches” temporally persistent fluctuations into long-range spatial correlations, and Arabidopsis live-imaging data collapse onto the predicted cross-scale relationship.

---

## Why this paper belongs in the review

- **Model alignment**: Describes a minimal, general multi-scale mechanism linking temporal persistence (memory) to spatial correlations through tissue growth. Multi-scale and explicit about how changes in both the spatial and temporal scales of elements of the system impact emergent morphology.
- **Subject alignment**: Morphology; Shows how scale coupling converts heterogeneous datasets (genotypes/conditions/stages) into a single unified curve.

---

## Biological context

- Developing tissues show fluctuations in growth and mechanical properties across scales.
- Fluctuations may support sensing, patterning, and robustness, but can also destabilize morphology.
- Key question: do fluctuations remain local, or become tissue-spanning during growth?

---

## Modeling framework

- **Model type**: Minimal stochastic field model (PDEs) with growth advection + relaxation (memory) + noise; tested against live imaging.
- **Dimensionality**: General D; applied to thin 2D organ (Arabidopsis sepal epidermis).
- **Key mechanism**: “Fluctuation stretching” — growth expands the spatial length-scale of persistent fluctuations.
- **What is imposed vs emergent**:
  - Imposed: mean growth rate, persistence/relaxation, noise statistics.
  - Emergent: long-range spatial correlations, parameter collapse across conditions.

---

## Scales spanned and how they are coupled

### Subcellular / cellular timescale (memory)

- A persistence time (correlation time) represents how long a property retains “memory” (e.g., wall/cytoskeletal remodeling).

### Cellular scale (growth variability)

- Cell areal growth rates fluctuate; analysis uses a cellular Fourier transform (CFT).

### Tissue scale (spatial correlations)

- Long-range spatial correlations in growth fluctuations emerge across the organ.

### Key couplings

- Tissue growth couples time → space: higher persistence + growth → longer-range spatial correlations (“stretching”).
- Empirical coupling: temporal correlation statistic + spatial correlation exponent + growth rate satisfy a single relationship.

---

## Core multi-scale insights

- Spatial correlations cannot be interpreted without accounting for:
  - **growth (advection/expansion)** and
  - **temporal persistence (memory)**
- The central result is a cross-scale constraint: spatial correlation structure is predicted from temporal persistence and growth rate (and vice versa).
- Long-range correlations are predicted to be generic for any temporally persistent quantity in a growing medium.
- Growth doesn’t just add variability — it transforms the spatial organization of fluctuations.
- Mutations altering mechanical feedback shift temporal correlations and spatial correlation range, consistent with the stretching mechanism.
- Robustness may be improved by reducing persistence (increasing relaxation), limiting tissue-spanning correlations.

---

## Evidence & parameterization

- **Data**: Live imaging + segmentation of Arabidopsis sepals; cell growth computed across ~24h intervals.
- **Analyses**:
  - Cellular Fourier transform to quantify multi-scale spatial structure (seems a little convoluted to me idk).
  - Temporal persistence estimated via Kendall correlation of detrended growth across timepoints.
- **Validation**: Parameter collapse onto predicted relationship combining growth rate, spatial exponent, and temporal correlation.

---

## Conceptual contributions to multi-scale modeling

- Multi-scale coupling can be statistical/kinematic, not only mechanistic or hybrid-formalism.

---

## Open questions

- How does persistence time map onto specific molecular/mechanical processes?
- Does fluctuation stretching apply similarly in animal epithelia (anisotropic growth, convergent extension)?
- Can interventions that tune persistence time improve robustness without impairing patterning?

---

## Tags

#development #morphogenesis
#multiscale
#scale_cellular #scale_tissue
#data_in_vivo #data_imaging
#data_scale_cellular #data_scale_tissue
#param_quantitative #validation_quantitative
