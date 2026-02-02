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

## 2. Morphogenesis: Shape Emerges from Multiscale Coordination

- In all computational models, certain dynamics are imposed.
  - These imposed dynamics constitute the model’s assumptions. Other features of the system, including large-scale tissue form, may then emerge from the interaction of these assumed dynamics.
- Here, we organize these models using an interpretive lens: **At what biological scale does the model impose asssumed organizing dynamics, and at what scale is tissue shape allowed to emerge from those assumptions?**

---

### 2.1 Tissue shape can emerge when models impose cell-environment interactions (environment can be extracellular or intracellular, but interacting components are subcellular in size)

In these models, the imposed dynamics are at the level of individual cells and their interactions with molecular intracellular and or extracellular environments. Tissue-scale morphology is emergent.

- **Johnson et al. — CNCC stream confinement**
  - **Model:** Hybrid agent-based model of migrating cells coupled to PDEs for molecular signaling fields.
  - This paper shows that large-scale tissue organization during early vertebrate development can emerge because cells actively construct the constraints that stabilize their collective behavior.
    - Migrating cells both *sense* and *reshape* their signaling environment
    - Molecular fields in turn regulate collective cell behavior
  - Stable stream confinement, coherence, and controlled inter-stream exchange emerge without imposed geometric barriers or predefined boundaries.

- **Kaity & Lobo — Emergent stable tissue shapes from morphogen–growth feedback**
  - **Model:** Hybrid cell-based growth model coupled to PDEs for morphogen dynamics.
  - This paper shows that stable tissue and organ shapes can emerge when patterning signals and tissue growth are coupled in a closed feedback loop.
    - Morphogen distributions regulate local growth rates and directional expansion.
    - Tissue growth and deformation, in turn, advect, dilute, and reshape morphogen fields.
  - Shape evolution is dynamic rather than prescribed, and stable shape arises only when this reciprocal coupling is intact.
    - When morphogen–growth feedback is disrupted, tissues fail to converge on stable forms despite unchanged molecular rules.

- **Venturini & Sáez — A multiscale clutch model for adhesion complex mechanics**
  - **Model:** Multiscale model imposing subcellular mechanical interaction rules for adhesion complexes and force transmission.
  - This paper shows that coordinated cellular mechanical behavior can emerge from explicitly specified rules governing how cells interact with their subcellular mechanical environment.
    - The model encodes molecular-scale clutch dynamics, including binding, unbinding, and force-dependent unfolding within adhesion complexes.
    - Cell-scale traction forces, adhesion stability, and mechanosensitive responses are not prescribed, but emerge from the integration of many subcellular interactions.
    - Altering molecular interaction rules propagates upward to change collective cellular force generation.
  - Here, tissue-relevant mechanical coordination emerges from imposed subcellular interaction dynamics, rather than from assumed tissue-scale mechanics.

- **Li et al - Basal actomyosin pulses expand epithelium coordinating cell flattening and tissue elongation**
- **Model:** Vertex model incorporating subcellular actomyosin pulse dynamics
- This paper shows that tissue-scale epithelial expansion and elongation can emerge from explicitly specified subcellular actomyosin dynamics, without imposing tissue-level growth or mechanical rules.

---

### 2.2 Tissue shape can emerge when models impose spatial rules for cell–cell interaction

In these models, the imposed dynamics are the structure of cell interactions across space. The model encodes how cells are coupled to one another, while local cell responses and morphology emerge from that coupling.

- **Manicka et al. — Bioelectric information integration in morphogenesis**
  - **Model:** Multiscale ODE model of bioelectric patterning with spatially coupled membrane voltage states.
  - This paper shows that morphogenetic outcomes depend on how cells interpret tissue-wide bioelectric patterns rather than absolute local voltages.
    - Cells respond to relative voltage differences, spatial gradients, and pattern-wide context.
    - Perturbations that preserve local voltages but alter spatial organization produce distinct developmental outcomes.
  - Shape arises because cells decode distributed electrical patterns that persist despite local variability.

- **Berkemeier & Page — Coupling dynamics of 2D Notch–Delta signaling**
  - **Model:** Deterministic ODEs for Notch–Delta signaling on spatial lattices with varying coupling structure.
  - This paper demonstrates that emergent tissue patterns are governed by the structure of spatial coupling between cells, not by local signaling kinetics alone.
    - Identical intracellular dynamics yield qualitatively different outcomes under different coupling architectures.
  - Pattern stability is determined by interaction structure across the tissue.

- **Urcun et al. — Contact inhibition of locomotion in fibroblast scratch assays**
  - **Model:** Cellular Potts model imposing contact-dependent interaction and motility rules calibrated to scratch assay data.
  - This paper shows that collective wound closure dynamics can be explained by explicitly specified rules governing how cells respond to contact with neighbors.
    - The model encodes contact inhibition of locomotion (CIL) as a surface-dependent interaction rule that modulates cell motility.
    - Cell shape, migration trajectories, and wound closure rates emerge from these imposed cell–cell interaction rules.
    - Loss of CIL is sufficient to reproduce pathological keloid-like migration behavior without introducing new cellular mechanisms.
  - Pathological tissue-scale behavior thus emerges from altered coordination rules at the level of cell–cell interactions, rather than from changes in intrinsic cell motility or tissue mechanics.

**Lavalle et al. - Local control of cellular proliferation underlies neuroblast regeneration in zebrafish**
- **Model:** Minimal 2D Cellular Potts Model of neuromast regeneration with local, cell-type–specific proliferation switches.
- This paper shows that organ-scale regeneration and homeostasis can emerge from strictly local cell–cell interactions, without global regulatory signals.

---

### 2.3 Tissue shape can emerge when models impose tissue-scale physical dynamics

In these models, the imposed dynamics are physical properties imposed at the tissue scale through laws governing growth, geometry, and mechanics. Cellular behaviors are abstracted or omitted, and morphology emerges from collective physical processes.

- **Gill et al. — Divergent buckling patterns in gut morphogenesis**
  - **Model:** Continuum mechanical model of growing tissue without explicit cellular representation.
  - This paper shows that distinct, robust organ-scale patterns arise through growth–geometry feedback that selects between buckling regimes.
    - The same growth processes yield different morphologies depending on tissue geometry and resulting tissue mechanical properties.
  - Stable shape reflects convergence onto a particular tissue-scale dynamical mode.

- **De Santis et al. — Crosstalk between tissue mechanics and morphogen signaling**
  - **Model:** Multiscale model coupling morphogen signaling with tissue geometry and tension during gastrulation.
  - This work shows that tissue shape and mechanical state actively regulate how morphogen signals are interpreted.

- **Duteil et al. — Signaling on evolving tissue geometries**
  - **Model:** Reaction–diffusion equations defined on deforming tissue surfaces.
  - This study demonstrates that evolving geometry alone can modulate signaling outcomes, even in the absence of explicit cell-based models.
  - Signal interpretation depends on the history of tissue deformation.

---

### Section synthesis: Multiscale models enable the study of morphogenesis across organizational scales

- These studies show that multiscale modeling provides a common framework for studying morphogenesis, regardless of whether the primary organizing dynamics are specified at the molecular, cellular, or tissue scale.
- By explicitly representing interactions across scales, multiscale models make it possible to compare systems with very different assumed dynamics and to analyze how tissue-level shape emerges from those assumptions through coordinated cross-scale interactions.

---

## 3. Gynopatholody: Spatiotemporal processes

Relatively short section highlighting opportunitiy and small amount of work that is done here.

---

## 4. Aging & Senescence: Pathology Emerges from Multiscale Desynchronization

- In aging and senescence-related disease, biological processes that are individually functional can become pathological when their coordination across time, space, interactions, or population structure breaks down.
- In computational models, these forms of coordination must be explicitly specified in order to study how their disruption gives rise to disease. Aging phenotypes then emerge from how coordination disruptions propagate across biological scales.
- The studies in this section use multiscale modeling to address a central question:
  **What coordination disruptions can cause age-related pathology to emerge, and how do those disruptions propagate across the system?**
- As in the morphogenesis section, we organize these models by the **scale at which the disrupted coordinating dynamics are imposed**.

### 4.1  Age-related pathology can emerge when models disrupt imposed cell-environment interaction dynamics (environment can be extracellular or intracellular, but interacting components are subcellular in size)

In these models, interactions between cells and extra and intracellular signals are imposed. The models enable assessment of how disrupting those interactions affects aging tissue health.

- **Haase et al. — Multiscale cytokine interactions in muscle regeneration**
  - **Model:** Multiscale Cellular Potts Model coupled to spatially resolved cytokine fields and vascular remodeling.
  - This paper shows that regeneration outcomes cannot be predicted from the behavior of individual cytokines, but instead depend on their combined interaction structure.
  - THIS PAPER DOES NOT TALK ABOUT AGING JUST REGENERATION so we will have to frame regeneration as something aging researchers should be concerned about (which makes sense, along the lines of wound healing really)

- **Weathered et al. — Microglial control of amyloid plaque dynamics**
  - **Model:** Spatial agent-based model of microglial behavior coupled to diffusive and aggregating Aβ species.
  - This paper shows that immune effectiveness in combating Alzheimer's disease depends on where and when immune actions occur, not simply on their intensity.

- **Thapa et al. - Senescent mesothelial matrix promotes ovarian cancer colonization**
  - **Model:** Multiscale CPM of mesothelial-cancer cell interactions coupled to experimentally measured changes in extracellular matrix composition.
  - This paper shows that age- or therapy-induced senescence can primite metastatic invasion by altering how cells interact with their microenvironment rather than by changing cancer cell intrinsic properties
    - Senescence mesothelial cells alter extracellular matrix
    - Mactrix changes increase cancer cell adhesion
  - Pathological tissue-scale invalsion emerges from disrupted coordination between cell state (senescence), ECM conposition, and cell-cell interaction rules rather  than from increase oncofenic signaling alone.

- **Haga et al. - Feedback-driven bistability in TGF-β signaling underlies skin aging**
- **Model:** ODE model of TGF-β/VEGF signaling
- This paper shows that cellular senescence can emerge from imposed intracellular signaling logic that creates irreversible state transitions rather than from cumulative damage alone
  - ODE model of feedback system is bistable
- Aging emerges from misaligned signal-response dynamics within cells

- **Lazebnik & Friedman _ Spatio-temporal modeling of senescence-aware combination therapy in metastatic prostate cancer**
- **Model:** PDE coupling tumor cell populations, senescent cells, immune dynamics, angiogenesis and drug pharmacokinetics
- This paper demonstrates that therapy-induced senescence can destabilize coordinated cell-signal interactions producing treatment resistence and accelerated disease progression
- Disease progression emerges from misalignment between cell fate decisions and tissue-level signaling dynamics

---

### 4.2 Age-related pathology can emerge when models disrupt imposed rules for cellular senescent state timing

In these models, cell state rules dictating cell behaviors are imposed along with criteria that specifies when a cell enters a certain state. These models enable analysis of how disrupting these state transitions impacts emergent tissue health

- **Chandrasegaran et al. — Senescence in wound healing**
  - **Model:** Hybrid agent-based model of wound healing with senescent cell states coupled to tissue-level repair dynamics.
  - This paper shows that senescence can either promote regeneration or drive pathological outcomes depending on when and where senescent cells arise.

---

### 4.3 Population-level aging can emerge when models disrupt how intracellular fate rules interact with population-level selection

In these models, rules determining which cells persist in a population are imposed. These models enable analysis of the emergent consequences of cell persistence regemes in the context of aging tissue.

- **Rat et al. — Telomere-driven senescence in yeast**
  - **Model:** Stochastic, lineage-resolved population model linking telomere dynamics to cellular fate decisions and population growth.
  - This paper shows that replicative senescence emerges from misalignment across intracellular, cellular, and population scales, rather than from a single molecular trigger.

---

### Section synthesis: Aging reflects multiscale desynchronization rather than new biology

- Across these models, aging and senescence emerge as failures of coordination across scales rather than as the appearance of novel mechanisms.
- These studies help explain why many single-target interventions fail: tissue-scale outcomes reflect integrated, spatiotemporally coordinated dynamics that cannot be corrected by modifying individual components in isolation.
