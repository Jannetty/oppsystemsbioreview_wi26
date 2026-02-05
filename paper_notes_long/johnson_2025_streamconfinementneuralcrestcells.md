# Johnson et al. 2025 — Stream confinement in cranial neural crest

## Citation

- **Cite key**: `johnson_2025_streamconfinementneuralcrestcells`
- **Authors**: Johnson et al.
- **Journal**: Developmental Dynamics
- **Year**: 2025
- **DOI**: 10.1002/dvdy.70072
- **PDF**: [Link to PDF](../papers/johnson_2025_streamconfinementneuralcrestcells.pdf)
- **Link to code**: [Github repo](https://github.com/SWSJChCh/leaderFollower/tree/main)

---

## One-sentence takeaway

Coupling molecular-scale fields (Trail, Colec12, Dan) to cell-scale agent dynamics reveals that stream confinement, coherence, and controlled exchange emerge from interactions across subcellular, cellular, and tissue scales.

---

## Why this paper belongs in the review

- **Model alignment**: Stochastic multi-scale abm that shows how coupling PDE-based molecular fields to cell agents yields emergent tissue-scale behaviors
  - Shows that different biological functions (confinement, coherence, exchange) arise at different scales.
  - Provides a clear example where multi-scale coupling is required to eliminate artificial boundary conditions.
- **Subject alignment**: Development, morphology of cranial tisssue during early development.

---

## Biological context

- CNCC streams must remain spatially separated during collective migration.
- Experimental evidence implicates Dan, Trail, and Colec12 in stream confinement, but their mechanistic roles are unclear.
- Prior models imposed non-biological zero-flux boundaries, preventing mechanistic insight.

---

## Modeling framework

- **Model type**: Stochastic agent-based model coupled to PDEs for Trail, Colec12, and Dan.
- **Model framework**: Written in python
- **Dimensionality**: 2D abstraction of CNCC collective migration.
- **Key biological structure**: Leader–follower dynamics driven by VEGF.
- **What is imposed vs emergent**:
  - Imposed: spatial expression of Trail/Colec12/Dan.
  - Emergent: stream confinement and collective integrity.

---

## Scales spanned and how they are coupled

### Molecular / subcellular scale

- Trail, Colec12, Dan, and VEGF represented as continuous concentration fields (PDEs).
- Dan is degradable by cells, producing history-dependent spatial profiles.

### Cellular scale

- CNCCs modeled as individual agents with phenotype (leader/follower), speed, protrusive behavior, and adhesion.
- Cell behaviors depend on *local* molecular concentrations.

### Collective / tissue scale

- Emergent properties include stream confinement, coherence, breakup, and inter-stream exchange.
- Domain geometry and CNCC-free zones define tissue-scale constraints.

### Key couplings

- Molecular → cellular: local field values modulate speed, direction, adhesion, and sensing.
- Cellular → molecular: CNCCs degrade VEGF and Dan, reshaping fields.
- Cellular → collective: individual rules give rise to stream-level behaviors.

---

## Mechanistic hypotheses and model findings (I did a really deep dive on this one most aren't this long)

### Colec12-mediated guidance

- **Hypothesis**: Colec12 confines CNCCs by influencing cell morphology and/or directional migration.
- **How modeled**: CNCCs experience Colec12 in adjacent CNCC-free zones, with effects on filopodia; chemotaxis down Colec12 gradients is optionally included.
- **Finding**: Morphological effects alone do not prevent stream breakup. Adding chemotaxis down Colec12 gradients strongly increases confinement.
- **Takeaway**: Colec12 acts primarily as a **directional guidance cue**, not merely a morphological modulator.

### Trail-mediated cohesion

- **Hypothesis**: Trail confines CNCCs by increasing cohesion within migrating collectives.
- **How modeled**: Trail reduces cell speed and increases effective cell–cell adhesion, biasing movement toward regions of higher cell density.
- **Finding**: Increasing the spatial extent of Trail expression increases confinement and maintains collective integrity.
- **Takeaway**: Trail confines streams by reinforcing **collective cohesion** rather than providing directional guidance.

### Combined Trail + Colec12 effects

- **Hypothesis**: Robust confinement requires multiple, complementary mechanisms.
- **How modeled**: Trail and Colec12 are co-expressed in CNCC-free zones.
- **Finding**: Combined expression yields near-complete confinement, exceeding the effect of either factor alone.
- **Takeaway**: **Directional guidance (Colec12) and cohesion (Trail) act synergistically** to maintain stream integrity.

### Dan-mediated speed modulation and collective coherence

- **Hypothesis**: Dan promotes coherent collective migration by slowing CNCC movement, particularly at the leading edge of streams.
- **How modeled**: Dan is represented as a degradable chemical that locally reduces CNCC speed in proportion to its concentration; CNCCs degrade Dan as they migrate, producing a dynamic spatial profile.
- **Finding**: Dynamic Dan degradation creates differential speed modulation, with leader cells moving more slowly than trailing cells. This prevents leader escape and stream breakup, enabling sustained collective migration.
- **Takeaway**: Dan stabilizes CNCC collectives by enforcing **leader–follower speed asymmetry**, increasing robustness of migration and enabling coherence even when Trail and Colec12 are only partially expressed.

### Trail- and Colec12-mediated exchange between adjacent streams

- **Hypothesis**: CNCCs can exchange between adjacent migratory streams through mechanisms that preserve overall collective migration.
- **How modeled**: A modified ABM geometry with two adjacent streams separated by a CNCC-free zone expressing Trail and/or Colec12; exchange occurs when cells cross into and remain in the neighboring stream.
- **Finding**: Trail enables collective, chain-based exchange between streams by increasing cell–cell adhesion, producing bridges without disrupting migration. Colec12 alone permits single-cell exchange via protrusion-mediated exploration or chemotaxis but can lead to diffuse stream edges and migration defects.
- **Takeaway**: Limited inter-stream exchange can arise from **Trail-driven collective bridging**, while Colec12 enhances exchange range but risks disruption when acting alone.

---

## Mechanistic synthesis

- Trail confines CNCC streams by reinforcing collective cohesion.
- Colec12 confines CNCCs via chemotactic guidance of individual cells.
- Dan prevents leader escape through differential speed modulation.
- Together, these mechanisms enable confined, coherent, and robust collective migration.

---

## Evidence & robustness

- Model predictions are consistent with prior in vitro and in vivo observations of Trail, Colec12, and Dan effects.
- Inclusion of Dan increases robustness of collective migration across a wider range of VEGF degradation rates.
- Results depend on simplified assumptions about domain growth and binary leader–follower phenotypes.

---

## Core multi-scale insights

- No single scale is sufficient to reproduce observed CNCC behaviors.
- Molecular-scale fields (Trail, Colec12, Dan) must dynamically interact with cell-scale rules to produce tissue-scale outcomes.
- Eliminating artificial boundary conditions (and thus allowing stream confinment to be an emergent property of the system as opposed to an imposed dynamic) is only possible because:
  - cells reshape molecular fields (Dan, VEGF degradation), and
  - molecular fields reshape cell behavior (speed, direction, adhesion).
- Key findings (confinement, coherence, controlled exchange) do not emerge in single-scale or weakly coupled models.

## Conceptual contributions to multi-scale modeling and CNCC migration

- CNCC stream confinement arises from a division of labor among cues: Colec12 provides directional guidance, Trail enforces collective cohesion, and Dan stabilizes leader–follower dynamics.
- Robust collective migration does not require hard inhibitory boundaries, but emerges from local cell–cue interactions.
- Speed modulation (Dan) is as important as directional guidance (VEGF, Colec12) for maintaining collective coherence.

---

## Open questions and testable predictions

- CNCCs should chemotax down Colec12 gradients in vitro.
- Trail exposure should increase secretion or expression of adhesion- and clustering-related factors.
- The width of Trail/Colec12-positive regions should control the frequency of inter-stream exchange.
- CNCC-mediated degradation of Dan should locally increase inter-stream exchange by reducing speed modulation.

---

## Tags

#development
#multiscale #hybrid_model #abm #pde
#scale_molecular #scale_cellular #scale_collective #scale_tissue
#data_in_vitro #data_in_vivo #data_imaging #data_expression #data_perturbation
#data_scale_molecular #data_scale_cellular #data_scale_collective
#param_qualitative #validation_qualitative
