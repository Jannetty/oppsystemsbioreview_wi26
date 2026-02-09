# Siegel et al. 2025 — Multiscale modeling of urothelial proliferation and regeneration

## Short note

- **Paper**:  Siegel et al. (2025) — Proliferation and regeneration of the healthy human urothelium: a multi-scale simulation approach with 16 hypotheses of cell differentiation
- **Question**: We know the urothelium is slow-turnover at steady state but can regenerate extremely quickly after injury. Which imposed cell-state logic for division and differentiation is sufficient to produce both realistic wound healing and long-term homeostasis?
- **Model**: 2D Glazier–Graner–Hogeweg / Cellular Potts (CompuCell3D) tissue model linking single-cell mechanics + cell fate rules to tissue-scale stratification and turnover.
- **Imposed**:
  - A stratified epithelium with progenitor/basal/intermediate/umbrella cell types, differential adhesion, contact inhibition, apoptosis, and periodic “voiding” that removes apical cells.  ￼
  - A fixed lineage ordering (Progenitor → Basal → Intermediate → Urothelium) and 16 alternative hypotheses for how progenitor/basal/intermediate cells divide and differentiate (including stem-cell-like division vs population asymmetry, and contact-dependent differentiation).
- **Varied**:
  - The cell-state rule set (16 hypotheses for fate logic).  ￼
  - Parameters tuned per rule set (e.g., division probabilities in population-asymmetry models, cell-type growth/apoptosis rates) to test whether a given logic can robustly stabilize.
- **Measured**:
  - Tissue outcomes classified as stable, chaotic, overgrowing (linear/exponential), or atrophic.
  - Quantitative “fitness” capturing correct layer ordering + volume distribution over long simulations (~2 years), plus regeneration time to form an umbrella barrier.
- **Conclusion**:
  - Only a narrow subset of fate-rule hypotheses produce both rapid wound healing and long-term stable stratification, showing that urothelial homeostasis is highly sensitive to imposed cell-state logic rather than to any single mechanical parameter.  ￼
  - The best-performing hypotheses share a key multiscale coupling: differentiation is regulated by spatial contact context (basal contact and medium contact), meaning tissue-scale architecture stabilizes because cell fates are explicitly coordinated with microenvironmental position.

## Citation

- **Cite key**: `siegel_2025_proliferationregenerationhealthy`
- **Authors**: Siegel, Torelli, Mattis, Debatin, Erben, Gumbel
- **Journal**: PLOS ONE
- **Year**: 2025
- **DOI**: 10.1371/journal.pone.0325132
- **PDF**: [Link to PDF](../papers/siegel_2025_proliferationregenerationhealthy.pdf)
- **Link to code**:
  - [Github](https://github.com/informatik-mannheim/Moduro-CC3D)
  - [Github toolbox](https://github.com/informatik-mannheim/Moduro-Toolbox)

---

## One-sentence takeaway

A multi-scale Cellular Potts Model systematically tests 16 hypotheses of urothelial cell differentiation and identifies contact-driven basal progenitor models as the only mechanisms capable of robust regeneration and long-term tissue homeostasis (with correct tissue layering and cell volumes).

---

## Why this paper belongs in the review

- **Model alignment**: Explicitly multiscale, agent-based, hypothesis-driven modeling of epithelial regeneration using CompuCell3D.
  - Tests mechanistic lineage hypotheses rather than tuning a single model.
  - Demonstrates how tissue-scale stability emerges from cell-scale differentiation rules.
- **Subject alignment**: Regeneration, epithelial homeostasis, relevance to aging, development, and healing.
- **Conceptual contribution**: Shows how mechanical contact and spatial context act as regulatory layers, not just constraints.

---

## Biological context

- The urothelium is a slow-regenerating stratified epithelium with rapid regeneration after injury.
- Its structure parallels epidermis but key proliferation and differentiation rules remain unclear.
- Dysregulation of urothelial homeostasis underlies bladder cancer and developmental defects.
- Experimental evidence supports basal progenitors as the main regenerative source.

---

## Modeling framework

- **Model type**: Cellular Potts Model (GGH) with agent-based extensions.
- **Platform**: CompuCell3D.
- **Dimensionality**: 2D tissue cross-section.
- **Cell types**:
  - Progenitor (P)
  - Basal (B)
  - Intermediate (I)
  - Umbrella (U)
- **What is imposed vs emergent**:
  - Imposed: Lineage hypotheses (differentiation cascades), adhesion energies, apoptosis rates, voiding.
  - Emergent: Layered architecture, regeneration speed, long-term stability vs atrophy or overgrowth.

---

## Scales spanned and how they are coupled

### Cellular scale

- Individual cells grow, divide, differentiate, undergo apoptosis.
- Differentiation rules depend on contact with basal membrane or lumen.

### Multicellular / tissue scale

- Emergence of layered stratification (basal → intermediate → umbrella).
- Global behaviors: regeneration, chaotic layering, atrophy, overgrowth.

### Key couplings

- Cell → tissue: Local differentiation rules determine global tissue fate.
- Tissue → cellular: Layer integrity feeds back on survival and proliferation.

---

## Core multi-scale insights

- Only two of 16 lineage models consistently produce healthy, stable urothelium.
- Best models require:
  - Basal progenitor divisions
  - Contact-driven differentiation
- Models with intermediate cell proliferation destabilize tissue organization.
- Tissue regeneration (3–5 days) emerges naturally only in specific multiscale rule sets.
- Demonstrates that tissue-scale robustness is highly sensitive to microscale differentiation logic, not just proliferation rates.

---

## Evidence & parameterization

- **Validation target**: Known urothelial architecture and regeneration times.
- **Fitness function**:
  - Arrangement of layers
  - Volume distributions
- **Robustness**: ≥25 stochastic replicates per model.
- **Comparison**: Quantitative fitness ranking across all hypotheses.
- **Limitations**:
  - 2D geometry
  - Qualitative rather than fully molecular signaling.

---

## Conceptual contributions to multi-scale modeling

- Demonstrates mechanical contact as a regulatory layer, not merely a boundary condition.
- Shows how spatial context can substitute for molecular signaling in lineage control.
- Introduces systematic model selection among biological hypotheses using multiscale ABMs.
- Provides a template for using agent-based models not just to reproduce patterns, but to discriminate competing biological mechanisms.

---

## Relevance to Health & Longevity

- Establishes a baseline model of healthy epithelial regeneration.
- Provides contrast class for:
  - Fibrosis
  - Aged epithelia
  - Cancer initiation via loss of contact regulation
- Highlights how subtle changes in differentiation logic can trigger pathological outcomes over time.

---

## Tags

#regeneration #epithelium #urothelium #homeostasis
#multiscale #abm #cpm #hybrid_model
#scale_cellular #scale_collective #scale_tissue #scale_mechanical
#data_histology #data_regeneration
#param_quantitative #validation_structural #hypothesis_testing
