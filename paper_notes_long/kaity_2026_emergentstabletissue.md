# Kaity & Lobo 2026 — Emergent stable tissue shapes from morphogen–growth feedback

## Citation

- **Cite key**: `kaity_2026_emergentstabletissue`
- **Authors**: Kaity, Lobo
- **Journal**: Journal of Theoretical Biology
- **Year**: 2026
- **DOI**: 10.1016/j.jtbi.2025.112354
- **PDF**: [Link to PDF](../papers/kaity_2026_emergentstabletissue.pdf)
- **Link to code**: NO LINK! They say they used MatLab but don't have their code public!

---

## One-sentence takeaway

Bidirectional feedback between morphogen patterning and cell growth enables tissues to self-regulate size and shape, revealing shape homeostasis as an emergent multi-scale property rather than an imposed target.

---

## Why this paper belongs in the review

- **Model alignment**: Multi-scale abm that integrates closed-loop multi-scale feedback between molecular patterning and tissue growth.
  - Shows that stable tissue shapes emerge only when growth and signaling are mutually coupled.
- **Subject alignment**: Agnostic to a specific study system but generally releavant to morphology/development, investigates shape homeostasis as a cross-scale control problem, could also be relevent to regeneration/healing.

---

## Biological context

- Regenerating organisms (e.g. planarians) maintain correct body shape across large size changes.
- Morphogens pattern tissues, but tissue growth also reshapes morphogen fields.
- How patterning and growth remain coordinated over time is poorly understood.

---

## Modeling framework

- **Model type**: Center-based agent model coupled to reaction–diffusion PDEs.
- **Platform**: Custom simulation framework.
- **Dimensionality**: 2D tissue domains.
- **Core processes**: Cell growth, division, apoptosis, mechanical interactions.
- **What is imposed vs emergent**:
  - Imposed: morphogen kinetics, growth rules.
  - Emergent: tissue size, shape, stability, regeneration dynamics.

---

## Scales spanned and how they are coupled

### Molecular scale

- Morphogens represented as diffusing concentration fields.
- Patterning depends on reaction–diffusion dynamics and domain geometry.

### Cellular scale

- Cells respond to local morphogen levels by modulating growth and survival.
- Cell behaviors collectively drive tissue expansion or contraction.

### Tissue scale

- Tissue shape, size, and boundaries evolve dynamically.
- Geometry feeds back to influence morphogen diffusion and patterning.

### Key couplings

- Molecular → cellular: morphogens regulate growth and apoptosis.
- Cellular → tissue: cell-level behaviors define tissue geometry.
- Tissue → molecular: tissue shape constrains morphogen fields.

---

## Core multi-scale insights

- Shape homeostasis requires bidirectional coupling across molecular, cellular, and tissue scales.
  - Stable shapes do not emerge when morphogens act on a fixed domain.
  - Stable shapes do not emerge when growth occurs without feedback to patterning.
- Tissue-scale stability is an emergent consequence of cross-scale feedback loops.
- Tissue shape is a dynamic variable, not a boundary condition.
- Growth–pattern feedback stabilizes morphology across size changes.
- Regeneration and degrowth rely on the same multi-scale control principles.
- Robustness emerges from feedback..

---

## Evidence & parameterization

- **Parameterization**: Qualitative, theory-driven.
- **Validation**: Reproduction of known regenerative behaviors and stable morphologies.
- **Limitations**: Abstract morphogen identities; 2D geometry.

---

## Implications for health and longevity

- Loss of growth–pattern feedback may underlie age-related tissue degeneration.
- Shape homeostasis provides a framework for understanding regenerative failure.
- Suggests intervention points beyond single pathways or cell types.

---

## Open questions

- How are morphogen–growth feedback loops implemented molecularly?
- How does aging disrupt pattern–growth coupling?
- Do similar principles apply in mammalian tissues?

---

## Tags

#development #regeneration
#multiscale #hybrid_model #abm #pde
#scale_molecular #scale_cellular #scale_tissue
#param_qualitative #validation_qualitative
#nocode
