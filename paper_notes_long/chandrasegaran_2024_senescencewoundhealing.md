# Chandrasegaran et al. 2025 — Multiscale dynamics of senescent cells in wound healing

## Short note

- **Paper**: Chandrasegaran et al. 2025 —  Spatiotemporal senescence dynamics in wound healing, chronic wounds, and fibrosis
- **Question**: We know senescent cells can both promote wound repair and drive chronic pathology. When and where do senescent cells become beneficial vs harmful, and how does the timing of their appearance shift healing toward chronic wounds or fibrosis?
- **Model**: Multiscale Cellular Potts wound-healing model (compucell3d) coupling cell-state transitions (senescence phenotypes) to spatial tissue repair dynamics.
- **Imposed**: A spatial wound environment with migrating/proliferating fibroblasts and inflammatory cells; senescence induction rules with a time constraint (senescence is only allowed after a specified phase); temporally structured SASP behavior (fibrogenic vs fibrolytic influence on repair); ECM deposition and remodeling as tissue-scale outputs of local cell states.
- **Varied**: Probability that myofibroblasts become senescent (PSNC); timing constraint for senescence induction (TSEN); presence/absence of background inflammatory senescence to represent aged tissue conditions.
- **Measured**: Time courses of ECM accumulation and cell populations; classification of emergent repair regimes (healthy healing vs chronic inflammation vs fibrotic repair) across parameter sweeps.
- **Conclusion**: Wound pathology can emerge without changing core repair machinery, by shifting when senescent cells arise and how many are present: early/background inflammatory senescence drives chronic wounds, while absent or delayed senescence drives fibrosis, showing that tissue outcomes depend on spatiotemporal coordination of senescent fate dynamics (not senescence as a single static state).

## Citation

- **Cite key**: `chandrasegaran_2025_senescencewoundhealing`
- **Authors**: Chandrasegaran, Sluka, Shanley
- **Journal**: PLOS Computational Biology
- **Year**: 2025
- **DOI**: 10.1371/journal.pcbi.1012298
- **PDF**: [Link to PDF](../papers/chandrasegaran_2025_senescence_wound_healing.pdf)
- **Link to code**: [Github repo](https://github.com/Sharm8/Senescence_wound_healing_model)

---

## One-sentence takeaway

Coupling cell-level fate decisions with molecular-scale SASP dynamics reveals how timing, persistence, and heterogeneity of senescence drive divergent tissue-scale outcomes in wound healing.

---

## Why this paper belongs in the review

- **Model alignment**: Demonstrates a hybrid, multi-scale CPM–PDE model where pathological outcomes arise from altered cross-scale timing, not new mechanisms.
  - Provides a strong example of multi-scale necessity: tissue-level outcomes cannot be predicted from single-scale dynamics.
    - Identical cellular rules produce different tissue outcomes depending on timing and persistence of molecular signals.
    - Senescence is not intrinsically “good” or “bad”; its spatiotemporal coordination across scales determines function.
    - Pathology emerges from misalignment between cell fate timing and tissue repair stage, not new cell behaviors.
- **Subject alignment**: Shows how temporal misalignment across scales (senescence induction vs healing stage) leads to fibrosis or chronic wounds. Aligns due to aging/senescence and wound healing.

---

## Biological context

- Senescent cells play both beneficial and pathological roles in wound healing.
- SASP composition is temporally regulated (fibrogenic → fibrolytic).
- Disruption of senescence timing or clearance is linked to fibrosis and chronic inflammation.

---

## Modeling framework

- **Model type**: Cellular Potts Model (CPM) coupled to reaction–diffusion PDEs.
- **Platform**: CompuCell3D.
- **Dimensionality**: 2D dermal wound cross-section.
- **Cell types**: Fibroblasts, myofibroblasts, macrophages, senescent myofibroblasts, ECM.
- **Fields**: PDGF, CSF1, MMP, inflammatory SASP.
- **Stochasticity**: Included via CPM dynamics and probabilistic fate transitions.
- **What is imposed vs emergent**:
  - Imposed: basic wound geometry, baseline cell behaviors.
  - Emergent: healing vs fibrosis vs chronic inflammation.

---

## Scales spanned and how they are coupled

### Molecular scale

- SASP components modeled as diffusing, decaying fields.
- Distinct SASP phases encoded temporally (fibrogenic → fibrolytic).

### Cellular scale

- Cells undergo growth, differentiation, senescence, apoptosis.
- Fate transitions depend on local field values and contact interactions.

### Collective scale

- Population-level shifts in cell composition and phenotype.
- Secondary senescence (juxtacrine and paracrine) emerges from interactions.

### Tissue scale

- Wound closure, ECM accumulation, fibrosis, chronic inflammation.

### Key couplings

- Molecular → cellular: growth, differentiation, senescence thresholds.
- Cellular → molecular: SASP secretion, ECM production, proteolysis.
- Temporal coupling across scales determines repair outcome.

---

## Core multi-scale insights

- Timing of senescence induction is as important as senescent cell abundance.
- SASP phase transitions act as molecular-scale switches that reprogram tissue fate.
- Clearance dynamics couple immune-cell behavior to long-term tissue remodeling.

---

## Evidence & parameterization

- **Calibration**: Qualitative timelines of healthy wound healing.
- **Quantitative parameter fitting**: Particle swarm optimization using literature-derived cell counts and closure rates.
- **Validation**: Reproduction of known fibrotic and chronic wound phenotypes.
- **Limitations**: 2D geometry, simplified inflammation representation.

---

## Conceptual contributions to multi-scale modeling

- Demonstrates that temporal coupling across scales (not just spatial coupling) is essential: identical spatial mechanisms yield regenerative or pathological outcomes depending on the timing and persistence of senescence and SASP.
- Identifies senescence as a scale-bridging regulatory mechanism, structurally linking molecular secretion programs, cell fate decisions, immune dynamics, and tissue remodeling.
- Shows that hybrid CPM–PDE architectures can explain divergent phenotypes through shared mechanisms, avoiding outcome-specific rules or overfitting.

---

## Open questions

- Which SASP components most strongly control phase transitions?
- What data are needed to quantitatively constrain senescence timing?
- How robust are these outcomes to 3D tissue geometry?

---

## Tags

#development #aging #wound_healing
#multiscale #hybrid_model #cpm #pde #abm #temporal_coupling
#scale_molecular #scale_cellular #scale_collective #scale_tissue
#data_in_vivo #data_in_vitro #data_expression #data_imaging
#param_qualitative #param_quantitative
#validation_qualitative
