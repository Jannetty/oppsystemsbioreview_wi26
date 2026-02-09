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

## Citation

- **Cite key**: `haase_2024_multiscale_cytokines_muscle`
- **Authors**: Haase, Comlekoglu, Petrucciani, Peirce, Blemker
- **Journal**: eLife
- **Year**: 2024
- **DOI**: 10.7554/eLife.91924
- **PDF**: [Link to PDF](../papers/haase_2024_multiscale_cytokines_muscle.pdf)
- **Link to code**: [Zenodo link](https://zenodo.org/records/10403014)

---

## One-sentence takeaway

An agent-based, multiscale model shows that nonlinear interactions among cytokines—not individual cytokine effects—determine whether muscle injury resolves through regeneration or pathological repair.

---

## Why this paper belongs in the review

- **Model alignment**: Multi-scale model in CompuCell3D that explores nonlinear cytokine-cell interactions during muscle injury repair.
  - Shows that tissue-scale outcomes cannot be predicted from single-cytokine perturbations.
  - Highlights interaction structure as a cross-scale control mechanism, distinct from spatial or temporal coupling alone.
- **Subject alignment**: Wound healing/development

---

## Biological context

- Muscle regeneration depends on tightly coordinated interactions between immune cells, fibroblasts, satellite stem cells, vasculature, and cytokines.
- Experimental perturbations of individual cytokines show inconsistent or context-dependent effects.
- Prior models lacked spatial cytokine dynamics and microvascular remodeling.

---

## Modeling framework

- **Model type**: Cellular Potts Model (agent-based) coupled to cytokine PDEs.
- **Platform**: CompuCell3D.
- **Dimensionality**: 2D muscle cross-section.
- **Cell types**: Muscle fibers, SSCs, fibroblasts, neutrophils, macrophages (M1/M2), microvessels, lymphatics.
- **Fields**: Multiple cytokines with ECM-dependent diffusion and decay.
- **What is imposed vs emergent**:
  - Imposed: injury geometry, baseline cell rules.
  - Emergent: CSA recovery, fibrosis, immune dynamics, angiogenesis.

---

## Scales spanned and how they are coupled

### Molecular scale

- Cytokines modeled as spatially resolved diffusive fields with nonlinear decay.
- ECM binding alters effective diffusion and availability.

### Cellular scale

- Cells respond to local cytokine concentrations via migration, proliferation, differentiation.
- Immune phenotypes (M1/M2) dynamically regulated.

### Collective scale

- Population-level shifts in immune and progenitor cells.
- Coordinated angiogenesis and fibroblast expansion.

### Tissue scale

- Muscle cross-sectional area recovery.
- Fibrosis vs healthy regeneration outcomes.

### Key couplings

- Molecular → cellular: cytokines regulate cell fate and behavior.
- Cellular → molecular: cells secrete and remodel cytokine fields.
- Cross-scale nonlinearity: combined molecular perturbations produce emergent tissue responses.

---

## Core multi-scale insights

- No single cytokine parameter predicts regeneration outcome.
  - Beneficial effects arise only from specific combinations of diffusion and decay across scales.
  - Therapeutic insights emerge from nonlinear cross-scale interactions, not isolated mechanisms.
- Cytokine spatial dynamics are as important as concentration.
- Tissue regeneration is governed by parameter interactions, not parameter values.
- Hybrid models enable exploration of therapeutic spaces inaccessible to experiments alone.

---

## Evidence & parameterization

- **Calibration**: Quantitative fitting to CSA recovery, SSC and fibroblast counts over time.
- **Validation**: Independent comparison to macrophage, neutrophil, and capillary data.
- **Prediction**: In silico perturbations reproduce published experimental trends.
- **Limitations**: 2D geometry, large parameter space, literature-derived heterogeneity.

---

## Conceptual contributions to multi-scale modeling

- Highlights the necessity of spatial cytokine modeling.
- Demonstrates the value of quantitative calibration in large hybrid models.
- Provides another template for using ABMs as in silico experimental platforms.

---

## Tags

#development #regeneration #wound_healing
#multiscale #hybrid_model #abm #cpm #pde
#scale_molecular #scale_cellular #scale_collective #scale_tissue
#data_in_vivo #data_in_vitro #data_expression #data_imaging #data_perturbation
#data_scale_molecular #data_scale_cellular #data_scale_collective #data_scale_tissue
#param_quantitative #validation_quantitative
