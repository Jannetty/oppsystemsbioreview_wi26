# Manicka et al. 2023 — Bioelectric information integration in brain morphogenesis

## Short note

- **Paper:** Manicka et al. 2023 — Bioelectric information integration in brain morphogenesis
- **Question:** Can a tissue plausibly decode tissue-scale voltage patterns into distinct gene-expression programs, rather than responding only to local voltage levels?
- **Model:** Minimal dynamical model of spatially coupled bioelectric and gene-regulatory network trained to distinguish between different tissue-scale voltage patterns
- **Imposed:** 2D lattice of cells where each cell contains: simplified ion-channel dynamics producing membrane voltage, and an unspecified genetic regulatory network (essentially the set of genes can be thought of as free parameters that parameter estimation uses to drive the system to recognize tissue-scale patterns). Neighbor cells communicate via symmetric local coupling and voltage-gene interactions are bidirectionally linked
- **Varied:** Input voltage patterns (after parameters are trained to drive the system towards a specific pattern given that pattern as input), tissue size (# of cells), spatial "knockouts" of specific cells/regions to test which parts of the tissue contribute most to pattern recognition.
- **Measured:** Tissue-wide gene expression outputs, pattern discrimination performance, sensitivity structure (which cells and which gene interactions carry the information)
- **Conclusion:** Correct developmental gene expression can emerge from higher-order spatiotemporal information integration, where cells respond to the pattern structure of voltage across the tissue, showing morphogenesis may depend on multicellular-scale bioelectric context, not just local voltage levels.

## Citation

- **Cite key**: `manicka_2023_bioelectricmorphogenesis`
- **Authors**: Manicka, Pietak, Levin
- **Journal**: Development
- **Year**: 2023
- **DOI**: 10.1242/dev.201000
- **PDF**: [Link to PDF](../papers/manicka_2023_bioelectric_morphogenesis.pdf)
- **Link to code**: [Gitlab (bad choice imo)](https://gitlab.com/smanicka/neuralPlatePatterning)

---

## One-sentence takeaway

Coupling tissue-scale bioelectric patterns to cell-scale gene regulatory responses reveals that embryonic brain morphogenesis depends on distributed information integration across spatial scales, not local voltage alone.

---

## Why this paper belongs in the review

- **Model alignment**: ODE model (with parameters estimated using GA/gradient descent hybrid algorithm) that treats scale-bridging itself as the biological problem, not just a modeling technique. Uses a multi-scale model to make this point.
- **Topic alignment**: Morphology/development.

---

## Biological context

- Bioelectric signaling (transmembrane voltage, ion fluxes) is known to regulate patterning and morphogenesis.
- How spatially distributed bioelectric states are interpreted by cells during development is poorly understood.
- Frog brain morphogenesis provides a system where global pattern disruptions can be induced experimentally without changing cell identity.

---

## Modeling framework

- **Model type**: ODE model with parameters estimated using hybrid of GA and gradient descent.
- **Dimensionality**: 2D tissue representations with spatial voltage distributions.
- **Biological entities**:
  - Cells with membrane voltage states.
  - Tissue-scale voltage patterns across embryonic brain primordium.
  - Downstream transcriptional responses.
- **What is imposed vs emergent**:
  - Imposed: bioelectric perturbations, candidate regulatory interactions.
  - Emergent: pattern-specific gene expression, scaling of morphogenetic outcomes. They claim the parameter estimation itself yields "emergence" of untrained for dynamics (like scaling of voltage pattern to more cells than seen in training).

---

## Scales spanned and how they are coupled

### Molecular / subcellular scale

- Ion channels and membrane voltage regulate intracellular signaling.
- Voltage states influence transcriptional programs indirectly.

### Cellular scale

- Individual cells respond to relationships between voltages across neighboring cells (relative magnitude differences), not absolute values.
- Cell-level gene expression outcomes depend on integrated spatial context.

### Tissue / collective scale

- Global bioelectric patterns encode positional and morphogenetic information.
- Tissue-wide voltage distributions determine organ-scale brain morphology.

### Key couplings

- Tissue → cellular: spatial voltage patterns regulate cell-scale transcription.
- Cellular → tissue: aggregated cell responses shape organ morphology.
- Information integration across scales enables robustness and scaling.

---

## Core multi-scale insights

- Local, single-cell voltage models fail to explain observed gene expression patterns.
  - Correct morphogenesis requires cells to decode non-local, spatially distributed information.
  - Tissue-scale pattern interpretation cannot be reduced to molecular-scale thresholds.
- Multiscale coupling explains how embryos maintain correct proportions despite perturbations.
  - Bioelectric signals function as "distributed information fields", as opposed to local morphogens.
  - Different genes respond to different orders of spatial information (local vs relational vs global).
- Morphogenesis depends on pattern recognition across scales, not signal magnitude alone.
- Scaling robustness emerges from information integration.

---

## Evidence & parameterization

- **In vivo data**: Frog embryo perturbation experiments altering bioelectric states.
- **Expression data**: Spatial gene expression readouts following voltage manipulation.
- **Parameterization**:
  - Qualitative constraints from experimental outcomes.
  - Statistical/ML methods used to explore and rank candidate regulatory models.
- **Validation**: Agreement with experimentally observed phenotypes and scaling behavior.
- **Limitations**: Simplified GRN logic; indirect mapping from voltage to transcription.

---

## Conceptual contributions to multi-scale modeling

- Highlights information flow as a key multiscale variable alongside force and chemical concentration.
- Shows that scale coupling may be computational, not just physical or chemical.
- Suggests that many developmental models may fail by assuming cells only sense local signals.

---

## Open questions and testable predictions

- What molecular mechanisms implement spatial voltage integration in cells?
- Over what spatial ranges do cells integrate bioelectric information?
- Can similar information-integration principles explain regeneration and cancer patterning?
- How general is this mechanism across tissues and species?

---

## Tags

#development #morphogenesis
#multiscale #information_integration
#scale_molecular #scale_cellular #scale_collective #scale_tissue
#data_in_vivo #data_expression #data_perturbation
#param_qualitative #validation_qualitative
