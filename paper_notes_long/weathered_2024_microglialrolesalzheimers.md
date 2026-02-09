# Weathered et al. 2024 — Microglial control of amyloid plaque dynamics

## Short note

- **Paper**: Weathered et al. (2024) — Microglial roles in Alzheimer’s disease: an agent-based model of spatiotemporal response to Aβ
- **Question**: Microglial “activation” is not a single control knob: different microglial behaviors can influence different plaque outcomes. This model asks which functional components of the microglial response—chemotaxis, phagocytosis, and proliferation—most strongly regulate plaque growth and barrier coverage.
- **Model**: 3D spatial agent-based model of microglia coupled to diffusive/aggregating Aβ species in brain tissue (implemented using Repast simphony?)
- **Imposed**: Aβ monomer is produced from a point source, diffuses, oligomerizes, and polymerizes into immobile plaques; microglia activate above an Aβ threshold, then chemotax up gradients, phagocytose monomer locally, and (for a subset) proliferate.
- **Varied**:  Microglial activation threshold, chemotaxis probability, phagocytosis rate, replication fraction/doubling time; in silico “knockouts” disabling activation, chemotaxis, phagocytosis, or replication.
- **Measured**: Plaque volume (object count), microglial plaque coverage (barrier fraction), activated microglia counts, and timing of microglial arrival/activation relative to plaque growth.
- **Conclusion**: Plaque outcomes are not determined by microglial “activation” as a single switch. Instead, different microglial functions control different aspects of disease: phagocytosis most strongly limits plaque growth, while chemotaxis most strongly controls barrier formation. This shows that Alzheimer’s progression depends on which immune behaviors occur, and where and when they occur—not just whether microglia are broadly reactive.

## Citation

- **Cite key**: `weathered_2024_microgliaamyloid`
- **Authors**: Weathered et al.
- **Journal**: CPT: Pharmacometrics & Systems Pharmacology
- **Year**: 2024
- **DOI**: 10.1002/psp4.13095
- **PDF**: [Link to PDF](../papers/weathered_2024_microglialrolesalzheimers.pdf)
- **Link to code**: [Purr.purdue](https://purr.purdue.edu/publications/4158/1)

---

## One-sentence takeaway

Spatial coupling of molecular Aβ diffusion with agent-based microglial behaviors reveals that chemotaxis, phagocytosis, and activation timing exert distinct and non-intuitive control over plaque size and barrier formation.

---

## Why this paper belongs in the review

- **Model alignment**: Multiscale hybrid ABM shows that multi-scale coupling is required to understand emergent impacts of immune cell behaviors.
  - Shows that different cellular mechanisms dominate different tissue-level outcomes, which cannot be inferred from single-scale models.
- **Model alignment**: Alzhiemers which is aging relevant?

---

## Biological context

- Alzheimer’s disease is characterized by Aβ plaque accumulation and microglial responses.
- Microglia form protective barriers around plaques, but the mechanisms governing coverage vs containment are unclear.
- Existing ODE/QSP models lack spatial resolution to address barrier formation.

---

## Modeling framework

- **Model type**: Agent-based model with continuous Aβ diffusion and aggregation.
- **Platform**: Repast Simphony.
- **Dimensionality**: 3D tissue volume (hippocampal subsection).
- **Agents**: Inactive and activated microglia.
- **Fields**: Aβ monomer, oligomer, plaque.
- **What is imposed vs emergent**:
  - Imposed: Aβ production source, activation thresholds.
  - Emergent: plaque barriers, coverage dynamics, plaque size distributions.

---

## Scales spanned and how they are coupled

### Molecular scale

- Aβ monomer diffusion, oligomerization, and plaque formation.
- Spatial gradients drive cellular activation and movement.

### Cellular scale

- Microglia activation, chemotaxis, phagocytosis, and replication.
- Behaviors depend on local Aβ concentrations.

### Collective / tissue scale

- Emergent plaque barrier coverage.
- Relationship between plaque size and immune containment.

### Key couplings

- Molecular → cellular: Aβ gradients regulate activation and chemotaxis.
- Cellular → molecular: phagocytosis reduces monomer availability, indirectly affecting plaque growth.
- Cellular → collective: local rules generate barrier structures.

---

## Core multi-scale insights

- Plaque barriers are spatial emergent structures that cannot be represented without explicit spatial coupling.
- Knockout experiments show that:
  - Phagocytosis controls plaque size.
  - Chemotaxis controls coverage.
- These distinctions only emerge when molecular gradients and cell behaviors interact in space and time.
- Barrier coverage and plaque containment are decoupled outcomes.
- Early cellular-scale timing determines long-term tissue-scale pathology.
- Immune effectiveness depends on where and when cells act, not just how strongly.

---

## Evidence & parameterization

- **Validation**: Qualitative agreement with in vivo mouse data on plaque size vs coverage.
- **Parameterization**: Mixed literature-based and qualitatively tuned parameters.
- **Strength**: Extensive in silico knockouts across mechanisms.
- **Limitation**: Fixed Aβ source; simplified activation states.

---

## Conceptual contributions to multi-scale modeling

- Demonstrates the necessity of spatial ABMs for immune–tissue interactions.
- Shows how multiscale models enable **mechanistic attribution**, not just pattern reproduction.
- Highlights limits of homogeneous QSP approaches in neurodegeneration.

---

## Tags

#neurodegeneration #development
#multiscale #abm #hybrid_model
#scale_molecular #scale_cellular #scale_collective #scale_tissue
#data_in_vivo #data_imaging
#param_qualitative #validation_qualitative
