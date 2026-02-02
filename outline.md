# Spatiotemporal multi-scale models for advancing human health and longevity

---

## 1. Introduction

- Healthy tissues emerge from coordinated activity across levels of biological organization
  - subcellular signaling, cellular behaviors, and tissue structure continuously interact, shaping one another's dynamics
- Establishing this coordination during development and maintaining it over time is essential for sustained tissue health
  - Many pathologies arise from breakdowns in coordination like mistimed signaling, mislocalized spatial cues, or improper integration of otherwise normal processes
    - Regeneration vs fibrosis, ordered morphogenesis vs disorganization, healthy tissue vs cancer
- Experimental approaches face fundamental limits in disentagling thesse coordination.
  - Limited observability: Emergent tissue behaviors depend on intermediate cross-scale interactions that are difficult if not impossible to observe simultaneously across space and time.
  - Limited controlability: Spatiotemporal organization itself is often the key variable of interest, but cannot be independently controlled in living systems
- Multi-scale models provide a complementary way to study coordinated tissue dynamics.
  - High obserability: By representing molecular, cellular, and tissue-scale processes within a single framework, multi-scale models make intermediate cross-scale interactions explicit, enabling direct examination of how local decisions propagate into tissue-level outcomes over space and time.
  - High controlability: Because timing, spatial organization, interaction rules, and tissue context are specified computationally, these models allow systematic and independent variation of coordination patterns in silico, supporting causal tests of how specific cross-scale relationships drive regeneration, morphogenesis, or pathology.
- Here we review recent multi-scale modeling studies to show how robust tissue form and function depend on coordination across biological scales. We focus on case studies in development, gynopathology, and senescence that demonstrate how multi-scale models function as in-silico test beds, enabling tests of timing, spatial organization, and cross-scale integration that are difficult or impossible to isolate experimentally.
- This review is intended for researchers studying development, regeneration, aging, and disease who are interested in how multiscale models are used to investigate the establishment, maintenance, and breakdown of coordinated biological function across space and time.

### Multiscale models incorporate cross-level dependence

- Here, we define spatiotemporal multiscale models as computational frameworks that couple biological processes across multiple levels of organization by explicitly representing their spatial structure, temporal dynamics, and reciprocal regulatory interactions.

---

## 2. Morphogenesis: How Robust Shape Emerges from Multiscale Coordination

- The studies in this section use multiscale models to address a central question in developmental biology: **Where does the information that stabilizes tissue shape reside?**
- Here, *stability* refers to a tissue’s ability to reliably form and maintain coherent structure despite variability, noise, and stochasticity at molecular and cellular scales. Stability reflects where in the system information is stored that allows form to persist, self-correct, or recover following perturbation.
- Recent multiscale modeling work shows that this stabilizing information resides across scales.

---

### 2.1 Tissue shape can be stabilized by cells actively constructing their signaling environment

In these models, stability is not imposed externally but emerges because cells continuously remodel the molecular fields that guide their own behavior.

- **Johnson et al. — CNCC stream confinement**
  - **Model:** Hybrid agent-based model of migrating cells coupled to PDEs for molecular signaling fields.
  - This paper shows that large-scale tissue organization during early vertebrate development can emerge because cells actively construct the constraints that stabilize their collective behavior.
    - Migrating cells both *sense* and *reshape* their signaling environment:
      - Cells move toward attractant cues (VEGF) that they locally sculpt by degrading the signal as they migrate.
      - Cells remove inhibitory signals (Dan), creating spatial “memory” that alters future migration speed and organization.
    - Molecular fields in turn regulate collective cell behavior by:
      - Modulating speed (Dan),
      - Promoting cohesion and directional alignment (Trail, Colec12),
      - Establishing leader–follower organization (VEGF).
  - Stable stream confinement, coherence, and controlled inter-stream exchange emerge without imposed geometric barriers or predefined boundaries.

- **Kaity & Lobo — Emergent stable tissue shapes from morphogen–growth feedback**
  - **Model:** Hybrid cell-based growth model coupled to PDEs for morphogen dynamics.
  - This paper shows that stable tissue and organ shapes can emerge when patterning signals and tissue growth are coupled in a closed feedback loop.
    - Morphogen distributions regulate local growth rates and directional expansion.
    - Tissue growth and deformation, in turn, advect, dilute, and reshape morphogen fields.
    - Shape evolution is therefore dynamic rather than prescribed, and stability arises only when this reciprocal coupling is intact.
  - When morphogen–growth feedback is disrupted, tissues fail to converge on stable forms despite unchanged molecular rules.

In these systems, stabilizing information resides in the dynamically maintained signaling environment that cells themselves construct. Shape persists because cells continually reinforce the constraints that guide their collective organization.

---

### 2.2 Tissue shape can be stabilized by cellular interpretation of distributed spatial patterns

In these models, stability is not tied to local signal values or explicit boundary construction, but to how cells interpret distributed spatial patterns across the tissue.

- **Manicka et al. — Bioelectric information integration in morphogenesis**
  - **Model:** Multiscale ODE model of bioelectric patterning with spatially coupled membrane voltage states.
  - This paper shows that morphogenetic outcomes depend on how cells interpret tissue-wide bioelectric patterns rather than absolute local voltages.
    - Cells respond to relative voltage differences, spatial gradients, and pattern-wide context.
    - Perturbations that preserve local voltages but alter spatial organization produce distinct developmental outcomes.
  - Stability arises because cells decode distributed electrical patterns that persist despite local variability.

- **Berkemeier & Page — Coupling dynamics of 2D Notch–Delta signaling**
  - **Model:** Deterministic ODEs for Notch–Delta signaling on spatial lattices with varying coupling structure.
  - This paper demonstrates that emergent tissue patterns are governed by the structure of spatial coupling between cells, not by local signaling kinetics alone.
    - Identical intracellular dynamics yield qualitatively different outcomes under different coupling architectures.
  - Pattern stability is therefore determined by interaction structure across the tissue.

Here, stabilizing information is carried by tissue-wide spatial patterns and coupling architecture, which guide cell behavior even when local signals are noisy or ambiguous.

---

### 2.3 Tissue shape can be stabilized by convergence onto tissue-scale dynamical regimes

In these models, stability emerges at the tissue scale itself through collective dynamics driven by growth, geometry, and physical constraint. Shape is stabilized not by cellular interpretation or local rules, but by convergence onto specific large-scale behaviors of the system.

- **Gill et al. — Divergent buckling patterns in gut morphogenesis**
  - **Model:** Continuum mechanical model of growing tissue without explicit cellular representation.
  - This paper shows that distinct, robust organ-scale patterns arise through growth–geometry feedback that selects between buckling regimes.
    - The same growth processes yield different morphologies depending on tissue geometry.
    - Pattern selection does not require fine-tuned material parameters.
  - Stability reflects convergence onto a particular tissue-scale dynamical mode.

- **De Santis et al. — Crosstalk between tissue mechanics and morphogen signaling**
  - **Model:** Multiscale model coupling morphogen signaling with tissue geometry and tension during gastrulation.
  - This work shows that tissue shape and mechanical state actively regulate how morphogen signals are interpreted.
  - Morphogen-only models fail unless tissue-scale geometry and tension are included as regulatory variables.

- **Duteil et al. — Signaling on evolving tissue geometries**
  - **Model:** Reaction–diffusion equations defined on deforming tissue surfaces.
  - This study demonstrates that evolving geometry alone can modulate signaling outcomes, even in the absence of explicit cell-based models.
  - Signal interpretation depends on the history of tissue deformation.

**In these systems, stabilizing information resides in tissue-scale dynamical regimes**, where geometry and growth constrain the space of possible outcomes and enforce reproducible form.

---

### Section synthesis: Stability in morphogenesis can reside at multiple organizational levels

- These studies show that robust morphogenesis does not rely on a single stabilizing mechanism.
- By making these distinctions explicit, multiscale models reveal not only how tissues form, but where stabilizing information is stored, providing a foundation for understanding how similar developmental programs fail when coordination across scales breaks down in disease or aging.

---

## 3. Gynopatholody: Spatiotemporal processes

Relatively short section highlighting opportunitiy and small amount of work that is done here.

---

## 4. Aging & Senescence: Multiscale Desynchronization as a Failure Mode

- Aging emerges when existing biological processes fall out of sync across time, space, interaction structure, or population dynamics.
- The studies in this section use multiscale modeling to address a central question:
  **How does coordinated biological function break down across scales to produce aging and senescence-related disease?**
- The subsections below organize aging and senescence models by the primary mode of multiscale desynchronization, highlighting where coordination fails and how that failure propagates across scales to generate aging phenotypes.

### 4.1 Timing mismatches in senescent state transitions can drive age-related pathology

- **Chandrasegaran et al. — Senescence in wound healing**
  - **Model:** Hybrid agent-based model of wound healing with senescent cell states coupled to tissue-level repair dynamics.
  - This paper shows that senescence can either promote regeneration or drive pathological outcomes depending on when and where senescent cells arise.

Aging-related pathology can emerge from mistimed coordination of otherwise normal mechanisms, rather than from fundamentally new biological processes.

---

### 4.2 Altered interaction structures, rather than single drivers, can drive age-related pathology

- **Haase et al. — Multiscale cytokine interactions in muscle regeneration**
  - **Model:** Multiscale Cellular Potts Model coupled to spatially resolved cytokine fields and vascular remodeling.
  - This paper shows that regeneration outcomes cannot be predicted from the behavior of individual cytokines, but instead depend on their combined interaction structure.
  - THIS PAPER DOES NOT TALK ABOUT AGING JUST REGENERATION so we will have to frame regeneration as something aging researchers should be concerned about (which makes sense, along the lines of wound healing really)

---

### 4.3 Spatial miscoordination of cellular actions can drive age-related pathology

- **Weathered et al. — Microglial control of amyloid plaque dynamics**
  - **Model:** Spatial agent-based model of microglial behavior coupled to diffusive and aggregating Aβ species.
  - This paper shows that immune effectiveness in combating Alzheimer's disease depends on where and when immune actions occur, not simply on their intensity.

---

### 4.4 Population-level aging emerges from accumulation of cross-scale variability

- **Rat et al. — Telomere-driven senescence in yeast**
  - **Model:** Stochastic, lineage-resolved population model linking telomere dynamics to cellular fate decisions and population growth.
  - This paper shows that replicative senescence emerges from misalignment across molecular, cellular, and population scales, rather than from a single molecular trigger.

Aging can emerge from desynchronization between molecular clocks, cellular decision-making, and population-level selection, even when underlying mechanisms remain unchanged.

---

### Section synthesis: Aging reflects multiscale desynchronization rather than new biology

- Across these models, aging and senescence emerge as failures of coordination across scales rather than as the appearance of novel mechanisms.
- These studies help explain why many single-target interventions fail: tissue-scale outcomes reflect integrated, spatiotemporally coordinated dynamics that cannot be corrected by modifying individual components in isolation.
