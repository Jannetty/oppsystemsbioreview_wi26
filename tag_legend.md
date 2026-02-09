# Tag legend

This repository uses structured tags to annotate **biological scale**, **model structure**, and **data usage** for each paper note.

---

## Biological scale tags

*Which biological scales are explicitly represented or analyzed in the model.*

- `#scale_molecular`
  Molecular or subcellular components (e.g. signaling molecules, morphogens, gene expression fields).

- `#scale_cellular`
  Individual cells represented explicitly (e.g. agents with position, speed, phenotype).

- `#scale_collective`
  Population-level behaviors not attributable to single cells or global tissue alone (allows for emergent behaviors, e.g. streams, chains, coherence, collective polarity).

- `#scale_tissue`
  Tissue- or domain-level structure and geometry (e.g. migratory corridors, compartments, growing domains).

---

## Multiscale / model-structure tags

*How multiple scales or mathematical formalisms are combined.*

- `#multiscale`
  The model spans more than one biological scale and explicitly couples them.

- `#temporal_coupling`
  Model investigates temporal coupling across scales in addition to spatial coupling across scales

- `#hybrid_model`
  The model combines different mathematical representations (e.g. discrete agents + continuous fields).

- `#abm`
  Agent-based modeling.

- `#pde`
  Partial differential equations (typically for fields such as chemical concentrations).

- `#cpm`
  Cellular potts model.

---

## Data to build model type tags

*What types of experimental data inform or motivate the model.*

- `#data_in_vitro`
  Cell culture or controlled experimental assays.

- `#data_in_vivo`
  Whole-organism or tissue-context experiments.

- `#data_imaging`
  Microscopy, live imaging, or spatial imaging data.

- `#data_expression`
  Gene or protein expression data (e.g. spatial patterns, up/downregulation).

- `#data_perturbation`
  Loss-of-function, gain-of-function, or other experimental perturbations.

---

## Data to build model scale tags

*Which biological scale(s) the data directly constrain.*

- `#data_scale_molecular`
  Data constrain molecular or subcellular quantities (e.g. expression levels, gradients).

- `#data_scale_cellular`
  Data constrain single-cell behaviors (e.g. speed, morphology, polarity).

- `#data_scale_collective`
  Data constrain group-level behaviors (e.g. stream integrity, collective migration patterns).

- `#data_scale_tissue`
  Data constrain tissue- or domain-level organization.

---

## Parameterization and validation tags

*How experimental data are used in the model.*

- `#param_qualitative`
  Parameters chosen to reproduce qualitative behaviors or trends.

- `#param_quantitative`
  Parameters fit or inferred quantitatively from data.

- `#validation_qualitative`
  Model validated by qualitative agreement with observed patterns.

- `#validation_quantitative`
  Model validated using quantitative comparisons or statistical metrics.

---

## Domain tags

*Broad biological context.*

- `#development`
  Developmental biology context.
- `#aging`
  Aging or senescence context.
