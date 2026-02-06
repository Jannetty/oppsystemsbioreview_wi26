# Spatiotemporal multi-scale models for advancing human health and longevity

---

## 1. Introduction

- Healthy tissues emerge from coordinated activity across scales of biological organization
  - subcellular signaling, cellular behaviors, and tissue structure continuously interact, shaping one another's dynamics
- Establishing this coordination during development and maintaining it over time is essential for sustained tissue health
  - Many pathologies arise from breakdowns in coordination like mistimed signaling, mislocalized spatial cues, or improper integration of otherwise normal processes
- Experimental approaches face fundamental limits in studying regulation and misregulation across scales.
  - Limited observability: Emergent tissue behaviors depend on intermediate cross-scale interactions that are difficult if not impossible to observe simultaneously across space and time.
  - Limited controlability: Spatiotemporal organization itself is often the key variable of interest, but cannot be independently controlled in living systems
- Multi-scale models provide a complementary way to study coordinated multi-scale dynamics.
  - High obserability: By representing molecular, cellular, and tissue-scale processes within a single framework, multi-scale models make intermediate cross-scale interactions explicit, enabling direct examination of how local decisions propagate into tissue-level outcomes over space and time.
  - High controlability: Because timing, spatial organization, interaction rules, and tissue context are specified computationally, these models allow systematic variation of coordinating variables in silico and assessment of resulting impact on emergent behavior.
- Here we review recent multi-scale modeling studies to show how robust tissue form and function depend on coordination across biological scales. We focus on case studies in development, gynopathology, and senescence that demonstrate how multi-scale models function as in-silico test beds, enabling tests of timing, spatial organization, and cross-scale integration that are difficult or impossible to isolate experimentally.
- In this review, we address the question “Why use spatiotemporal multiscale modeling?” through case studies showing how these models are used to study how multi-scale biological coordination is established in development and how its disruption can drive pathology.
- This review is intended for researchers studying development, regeneration, aging, and disease who are interested in how multiscale models are used to investigate the establishment, maintenance, and breakdown of coordinated biological function across space and time.

### Multiscale models incorporate cross-level dependence

- Here, we define spatiotemporal multiscale models as ~computational frameworks~ that couple biological processes across multiple levels of organization by explicitly representing their spatial structure, temporal dynamics, and reciprocal regulatory interactions.
- Here are some different types of spatiotemporal models, and some frameworks for ABMs specifically...

---

## 2. Development: Shape and Function Emerge from Multiscale Coordination

- In all computational models, certain dynamics are imposed.
  - These imposed dynamics constitute the model’s assumptions. Other features of the system, including large-scale tissue form, may then emerge from the interaction of these assumed dynamics.
- Here, we organize these models of development using an interpretive lens: **At what biological scale does the model impose asssumed organizing dynamics, and at what scale are emergent consequences of those assumptions impacting tissue shape?**

---

### 2.1 Tissue shape can emerge when models impose cell–microenvironment interaction rules

In these models, the primary assumptions are encoded at the scale of individual cells interacting with local biochemical or mechanical context (intracellular cues, extracellular cues, ECM, or force subcellular transmission). Tissue-scale shape is then treated as an emergent consequence of these local rules.

- Multiscale models can replace externally imposed tissue constraints with mechanistic local interactions.

  - **Johnson et al. — CNCC stream confinement** [[paper_notes_short/johnson_2025_streamconfinementneuralcrestcells]]
    - ABM + PDE fields. Shows stream confinement can emerge from local cue–cell feedbacks without artificial boundaries.

  - **Kaity & Lobo — Emergent stable tissue shapes from morphogen–growth feedback** [[paper_notes_short/kaity_2026_emergentstabletissue]]
    - Center-based cell model + morphogen PDEs. Shows stable tissue shape can emerge from reciprocal coupling between growth and patterning.

  - Together these studies show tissue-scale organiation can arise without imposing boundaries or target shapes, when cells sense and reshape their microenvironment.

- Multiscale models can connect subcellular force-generation rules to emergent cell and tissue mechanics

  - **Venturini & Sáez — A multiscale clutch model for adhesion complex mechanics** [[paper_notes_short/venturini_2023_multiscaleclutchadhesion]]
    - Subcellular mechanochemical model. Shows cell-scale traction emerges from molecular-scale force-transmission assumptions.

  - **Li et al - Basal actomyosin pulses expand epithelium coordinating cell flattening and tissue elongation** [[li_2024_basalactomyosinpulses]]
    - Vertex model + subcellular activity rules. Shows tissue elongation can emerge from pulsatile cytoskeletal dynamics coupled to adhesion and growth.

  - Together, these studies show how tissue-relevant mechanical behaviors can be explained by explicitly imposed molecular or subcellular dynamics.

- Multiscale models can be used as predictive “failure detectors” for developmental defects.

  - **Berkhout et al. — In silico prediction of neural tube closure defects** [[berkhout_2025_computationaldynamicsystems]]
    - CMP + dynamic gene regulatory networks in cells. Shows how multiscale coupling enables prediction of when neural tube closure fails, not just how it proceeds.

Throughline: These studies show how, by encoding local biochemical and mechanical interaction rules and assumptions, multiscale models can function as an in silico test bed to ask what tissue-scale organization is possible or impossible under those assumptions.

---

### 2.2 Tissue shape can emerge when models impose spatial rules for cell–cell interaction

In these models, the imposed dynamics are the structure of cell interactions across space. The model encodes how cells are coupled to one another. Tissue-scale patterning emerges from the architecture of coupling.

- Multiscale models can test whether tissue-scale outcomes require pattern-level context, or can be explained by strictly local coupling.

  - **Lavalle et al. - Local control of cellular proliferation underlies neuroblast regeneration in zebrafish** [[lavalle_2026_localcontrolcellular]]
    - Shows that organ-scale (neuromast) regeneration can be reproduced using only local neighbor-dependent proliferation rules, without introducing a global control signal

  - **Manicka et al. — Bioelectric information integration in morphogenesis** [[paper_notes_short/manicka_2023_informationintegrationbioelectric]]
    - Shows that a tissue can, in principle, map multicellular voltage patterns to distinct gene-expression outputs, suggesting a plausible route by which tissue-level bioelectric context could be interpreted during development.

  - Together, these studies illustrate that both local interaction rules and distributed tissue-level patterns can be sufficient organizing substrates in multiscale models.

- Multiscale models can reveal how emergent tissue patterns depend on the geometry and range of cell coupling.

  - **Berkemeier & Page — Coupling dynamics of 2D Notch–Delta signaling** [[paper_notes_short/berkemeier_2023_couplingdynamics2d]]
    - Shows that changing coupling architecture alone can switch tissue-scale pattern outcomes.

  - **Tikka et al. — Nephron progenitor movement and aggregation during kidney organogenesis** [[tikka_2022_computationalmodellingnephron]]
    - Shows that nephron progenitor aggregation can emerge when cells follow locally defined migration and adhesion rules that depend on nearby neighbors and contact structure, rather than from an imposed target aggregate shape.

- Multiscale models can explain pathological tissue-scale behavior as an emergent consequence of altered interaction rules.

  - **Urcun et al. — Contact inhibition of locomotion in fibroblast scratch assays** [[urcun_2026_simplecellularpotts]]
    - Shows that scar-like closure dynamics can emerge from disrupting contact-dependent coupling rules, without requiring new intrinsic motility programs.

Throughline: These studies show how multiscale models can be used to test which forms of spatial coupling are sufficient to produce coordinated tissue outcomes, and how tissue-scale organization can fail when coupling rules are altered.

---

### 2.3 Tissue shape can emerge when models impose tissue-scale physical dynamics

In these models, the primary assumptions are encoded at the scale of tissues: growth laws, geometry, material properties, and mechanical constraints. Cells may be absent, simplified, or treated as materials. Tissue morphology then emerges as a consequence of physical dynamics operating over space and time.

- Multiscale models can show that tissue-scale mechanics can be sufficient to drive robust morphogenetic outcomes.

  - **Gill et al. — Divergent buckling patterns in gut morphogenesis** [[paper_notes_short/gill_2024_developmentalmechanicsdivergent]]
    - Shows that distinct organ-scale morphologies can emerge from the same growth program when tissue geometry and mechanical constraints place the system into different buckling regimes.

- Multiscale models can treat tissue geometry as an active regulator of signaling rather than a passive outcome of signaling.

  - **Duteil et al. — Signaling on evolving tissue geometries** [[paper_notes_short/duteil_2025_computationalframeworkstudy]]
    - Shows that morphogen patterning outcomes chhanges when signaling unfolds on a deforming tissue surface, even when biochemical rules are unchanged.

  - **De Santis et al. — Crosstalk between tissue mechanics and morphogen signaling** [[paper_notes_short/desantis_2025_crosstalktissuemechanics]]
    - Shows that morphogen interpretation depends on tissue mechanical state, so signaling-only models fail when geometry and tension are omitted.

- Multiscale models can test whether correct morphogenesis requires time-resolved mechanical programs, not just static material assumptions.

  - **Gomez et al. — Highly dynamic mechanical transitions in embryonic cell populations during Drosophila gastrulation** [[gomez_2025_highlydynamicmechanical]]
    - Shows that robust tissue folding depends on spatially localized, time-varying changes in cell/tissue material properties, meaning that timing of mechanical transitions can be a controlling variable.

- Multiscale models can reveal that tissue-scale growth dynamics can generate long-range structure without explicitly encoding long-range coordination.

  - **Fruleux et al. — Growth couples temporal and spatial fluctuations of tissue properties during morphogenesis** [[paper_notes_short/fruleux_2024_growthcouplestemporal]]
    - Shows that long-range spatial correlations in tissue growth can emerge from tissue-scale growth dynamics that convert temporal persistence into spatial structure.

---

### Section synthesis: Multiscale models enable the study of morphogenesis across organizational scales

- Conclusion

---

## 3. Gynopatholody: A high-impact area of opportunity for spatiotemporal modeling.

- Spatial and temporal dynamics are increasingly recognized as central to the development and progression of gynopathologies such as endometriosis and ovarian cancer.
  - Experimental spatial “omics” data are being generated to study these pathologies ([Nature Comms review], DOI:10.1038/s41467-025-67492-z; DOI:10.1038/s41467-022-28568-2)
  - multiscale models offer complementary means to test mechanistic hypotheses about how coordination across scales contributes to disease onset, progression, and treatment outcomes.
- Here we feature some modeling work and highlight this area of work as a high-impact opportunity for modelers.

- **Miller et al. — Innate immune surveillance as a bistable switch in endometriosis lesion onset** [[miller_2025_mathematicalmodellingmacrophage]]
  - Shows that multiscale models can be used to test whether lesion onset  in endometriosis reflects a threshold transition in immune surveillance, rather than a gradual accumulation of ectopic tissue.
  - Shows how tissue-level pathology can emerge when otherwise normal processes (cell influx, clearance, inflammation) become misaligned in time.

- **Dutt et al. — Rheological transition driven by matrix makes cancer spheroids resilient under confinement** [[dutt_2025_rheologicaltransitiondriven]]
  - Shows that multiscale models can link microenvironmental structure (ECM composition and mechanics) to emergent, tissue-relevant physical phenotypes such as ovarian cancer spheroid resilience under stress.
  - Shows that ovarian cancer metastatic success can depend on a mechanically mediated coordination between cell collectives and their extracellular context.

- **Koprinski et al. — Optimising chemotherapy for advanced high-grade serous ovarian cancer via delay-differential equations** [[koprinski_2026_optimisingchemotherapyadvanced]]
  - Shows that multiscale models can function as in silico test beds for ovarian cancer treatment timing.
  - Shows how therapeutic outcomes can emerge from coordination (or miscoordination) between tumor response, toxicity, and recovery timescales.

Gynopathology modeling is a high-impact opportunity for modeling researchers.

---

## 4. Senescence & Chronic Disease: Pathology Emerges from Multiscale Desynchronization

- This review focuses on spatiotemporal models to study cellular effects of senescence and aging on health. Readers looking for a review of non-spatial network models and dynamical models can consult Su and Hao 2024.

- In senescence-associated and chronic diseases, biological processes that are individually functional can become pathological when their coordination across time, space, interactions, or population structure breaks down.
- In computational models, these forms of coordination must be explicitly specified in order to study how their disruption gives rise to disease. Aging phenotypes then emerge from how coordination disruptions propagate across biological scales.
- The studies in this section use multiscale modeling to address a central question:
  **What coordination disruptions can cause senescence-like or chronic pathology, and how do those disruptions propagate across the system?**
- As in the morphogenesis section, we organize these models by the **scale at which the disrupted coordinating dynamics are imposed**.

### 4.1 Pathology can emerge when models disrupt imposed cell–microenvironment coupling

In these models, the primary assumptions are encoded in how cells sense, reshape, and mechanically interact with their local environment. The “microenvironment” may be extracellular (diffusible signals, ECM, tissue geometry) or intracellular (organelle structure and spatial transport). Pathology emerges when cell–microenvironment coupling rules are altered.

- **Khan et al. — Stochastic co-translational targeting drives mitochondrial protein heterogeneity in senescence**
  - **Model:** Stochastic kinetics + diffusion model coupling mRNA localization, protein targeting, and mitochondrial fragmentation.
  - This paper shows that senescence-associated mitochondrial dysfunction can emerge when mitochondrial fragmentation disrupts coordination between stochastic protein delivery and organelle-scale geometry, producing heterogeneous protein composition across fragments rather than stable mitochondrial stoichiometry.

- **Weathered et al. — Microglial control of amyloid plaque dynamics** [[weathered_2024_microglialrolesalzheimers]]
  - **Model:** Spatial agent-based model of microglial behavior coupled to diffusive and aggregating Aβ species.
  - This paper shows that immune effectiveness in Alzheimer’s disease depends on the spatial and temporal coordination of microglial actions relative to plaque growth.

- **Thapa et al. - Senescent mesothelial matrix promotes ovarian cancer colonization**
  - **Model:** Multiscale CPM of mesothelial-cancer cell interactions coupled to experimentally measured changes in extracellular matrix composition.
  - This paper shows that age- or therapy-induced senescence can prime metastatic colonization by altering cell–ECM interaction rules (adhesion and invasion permissiveness).

- **Khuu & McCulloch — Multicell modeling of the skeletal muscle microenvironment**
  - **Model:** 3D multi-cell model in CompuCell3D of satellite cell recruitment to injury, with imposed HGF secretion from damaged tissue.
  - This paper shows that age-related decline in muscle repair can emerge from weakened coupling between injury-derived growth factor signaling and satellite-cell recruitment dynamics, even when the intrinsic repair program of the cells is unchanged.

- **Haase et al. — Multiscale cytokine interactions in muscle regeneration** [[haase_2024_multiscale_cytokines_muscle]]
  - **Model:** Multiscale Cellular Potts Model coupled to spatially resolved cytokine fields and vascular remodeling.
  - This paper shows that regeneration outcomes depend on the spatiotemporal interaction structure among cytokines, meaning tissue-scale repair cannot be predicted from the behavior of individual signals in isolation.

- **Li et al. — How the spleen reshapes and retains young and old red blood cells**
  - **Model:** Multiscale, particle-based mechanical model of red blood cells traversing spleen.
  - This paper shows that red blood cell aging and clearance can emerge from purely mechanical cell–environment coupling: age-associated changes in cell geometry become incompatible with fixed splenic constraints, producing retention and lysis without requiring an explicit molecular damage-sensing program.

- **Lazebnik & Friedman _ Spatio-temporal modeling of senescence-aware combination therapy in metastatic prostate cancer**
  - **Model:** PDE coupling tumor cell populations, senescent cells, immune dynamics, angiogenesis and drug pharmacokinetics
  - This paper shows that therapy-induced senescence can destabilize tumor control by reshaping the tissue microenvironment over time, producing resistance and accelerated progression through cross-scale feedback rather than tumor-intrinsic growth changes alone.

---

### 4.2 Pathology can emerge when models disrupt imposed cell-state logic and fate transitions

In these models, cell state rules dictating cell behaviors are imposed along with criteria that specifies when a cell enters a certain state. These models enable analysis of how disrupting these state transitions impacts emergent tissue health

- **Chandrasegaran et al. — Senescence in wound healing** [[chandrasegaran_2024_senescencewoundhealing]]
  - **Model:** Hybrid agent-based model of wound healing with senescent cell states coupled to tissue-level repair dynamics.
  - This paper shows that senescence can either promote regeneration or drive pathological outcomes depending on when and where senescent cells arise.

- **Martin et al. — Modelling the dynamics of senescence spread**
  - Model: Minimal mathematical model + stochastic spatial simulation of senescence spread via diffusive SASP ligands and contact-dependent juxtacrine signaling.
- This paper shows that senescence can either spread or self-limit depending on the imposed rules for cell–signal coupling.

- **Siegel et al. — Proliferation and regeneration of the healthy human urothelium**
  - **Model:** Multiscale Cellular Potts / GGH model of urothelial regeneration and homeostasis
  - This paper shows that stable epithelial regeneration and long-term homeostasis depend strongly on the imposed logic of cell state transitions, rather than on any single physical parameter.
    - The model explicitly encodes 16 alternative hypotheses for progenitor and basal cell division (stem-cell-like vs population asymmetry) and for differentiation triggers (including contact-dependent differentiation).
    - Tissue-scale outcomes—including stable stratification, chaotic layering, overgrowth, or atrophy—emerge from how these imposed fate rules interact with tissue turnover processes such as apoptosis and voiding.
  - The study highlights that multiple rule sets can produce realistic short-term wound closure, but only a narrow subset produces long-term homeostatic stability.

- **Haga et al. - Feedback-driven bistability in TGF-β signaling underlies skin aging**
  - **Model:** ODE model of TGF-β/VEGF signaling
  - This paper shows that cellular senescence can emerge from imposed intracellular signaling logic that creates irreversible state transitions rather than from cumulative damage alone
    - ODE model of feedback system is bistable
  - Aging emerges from misaligned signal-response dynamics within cells

- **Weatherley et al. — Therapeutic targeting of oligodendrocytes in an agent-based model of multiple sclerosis**
  - **Model:** Spatial on-lattice agent-based model of MS lesion formation incorporating immune infiltration across a blood–brain barrier, myelin damage/repair dynamics, and oligodendrocyte stress-response state transitions.
  - This paper shows that chronic lesion growth and failed recovery can emerge from imposed state-transition thresholds governing when oligodendrocytes stop remyelinating and undergo apoptosis, even when immune attack dynamics remain unchanged.
  - THIS PAPER DOES NOT EXPLICITELY DISCUSS AGING! And MS is not necessarily an aging related disease. Idk if we should include.

---

### 4.3 Pathology can emerge when models disrupt imposed population renewal and selection dynamics

In these models, rules determining which cells persist in a population are imposed. These models enable analysis of the emergent consequences of cell persistence regemes in the context of aging tissue.

- **Rat et al. — Telomere-driven senescence in yeast** [[rat2025_telomere_senescence]]
  - **Model:** Stochastic, lineage-resolved population model linking telomere dynamics to cellular fate decisions and population growth.
  - This paper shows that replicative senescence emerges from misalignment across intracellular, cellular, and population scales, rather than from a single molecular trigger.

---

### Section synthesis: Aging reflects multiscale desynchronization rather than new biology

- Across these models, aging and senescence emerge as failures of coordination across scales rather than as the appearance of novel mechanisms.
- These studies help explain why many single-target interventions fail: tissue-scale outcomes reflect integrated, spatiotemporally coordinated dynamics that cannot be corrected by modifying individual components in isolation.
