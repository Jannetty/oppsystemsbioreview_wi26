# Rat et al. 2025 — Telomere-driven senescence emerges from lineage–population desynchronization

## Citation

- **Cite key**: `rat2025_telomere_senescence`
- **Authors**: Anaïs Rat, Veronica Martinez Fernandez, Marie Doumic, Maria Teresa Teixeira, Zhou Xu
- **Journal**: Nature Communications
- **Year**: 2025
- **DOI**: 10.1038/s41467-025-56196-z
- **PDF**: [Link to PDF](../papers/Rat_2025_telomere_senescence.pdf)
- **Link to code**:
  - [github](https://github.com/anais-rat/telomeres)

---

## One-sentence takeaway

An ABM shows that replicative senescence emerges from multiscale desynchronization between telomere dynamics, single-cell fates, and population-level selection, rather than from a single molecular trigger alone.

---

## Why this paper belongs in the review

- **Model alignment**: Explicitly links molecular heterogeneity, stochastic cellular decisions, and population-level dynamics within a single quantitative framework.
  - Demonstrates how mechanisms inferred from single-cell lineages fail to predict population behavior without modeling selection and competition.
  - Reveals emergent senescence dynamics that only appear when multiple scales are coupled.
- **Subject alignment**: Central to aging and senescence, with direct implications for tissue renewal, genomic instability, and cancer escape.
- **Conceptual contribution**: Reframes senescence as a failure of temporal coordination across scales, not simply a molecular countdown.

---

## Biological context

- Telomere shortening limits replicative capacity and triggers senescence in somatic cells.
- Senescence onset is highly heterogeneous at the single-cell level but appears smooth and progressive in populations.
- Experimentally, population assays obscure lineage histories, selection effects, and hidden parameters like shortest telomere length.
- Understanding aging and cancer risk requires reconciling lineage-level mechanisms with population-scale outcomes.

---

## Modeling framework

- **Model type**: Stochastic, agent-based population model with probabilistic state transitions
- **Platform**: Custom mathematical model (Python; validated against microfluidics data)
- **Dimensionality**: Non-spatial, lineage- and population-based
- **Cell types / agents**:
  - Type A cells (deterministic senescence via critically short telomere)
  - Type B cells (stochastic senescence following non-terminal arrests)
- **Fields / signals**:
  - Telomere length distributions (explicit tracking of all chromosome ends)
- **What is imposed vs emergent**:
  - Imposed: Telomere shortening rules, probabilistic arrest laws
  - Emergent: Population growth curves, senescent cell composition, selection dynamics

---

## Scales spanned and how they are coupled

### Molecular / subcellular scale

- Telomere lengths for all chromosome ends are explicitly tracked.
- Senescence triggering depends on the *shortest* telomere, not the mean.
- Molecular heterogeneity evolves stochastically through asymmetric replication.

### Cellular scale

- Cells divide, arrest, or die based on telomere-dependent and telomere-independent probabilities.
- Two distinct senescence pathways (Type A vs Type B) coexist.
- Individual lineage histories strongly influence fate but are experimentally hidden in populations.

### Collective / population scale

- Cells compete through differential proliferation and survival.
- Population composition shifts over time due to selection for longer shortest telomeres.
- Late-stage populations become dominated by stochastic senescence pathways.

### Key couplings

- Molecular → cellular: Shortest telomere length governs arrest and senescence probabilities.
- Cellular → population: Cell cycle duration and death shape population growth.
- Population → cellular: Selection alters which lineage types persist and dominate.

---

## Core multi-scale insights

- Senescence timing is predictable at the lineage level but becomes probabilistic at the population level.
- Population aging cannot be inferred from average telomere length alone.
- Removing population-level selection collapses the model’s ability to reproduce experimental dynamics.
- Aging emerges from misalignment between molecular clocks, cellular decisions, and population structure.

---

## Evidence & parameterization

- **Data sources**:
  - Microfluidics single-cell lineage data
  - Population dilution experiments
- **Calibration**:
  - Probability laws fitted using CMA-ES optimization
- **Validation**:
  - Lineage lifespans
  - Population growth curves
  - Telomere length distributions over time
- **Robustness testing**:
  - Parameter sweeps over mortality, initial telomere distributions
  - Replicated stochastic simulations
- **Limitations**:
  - No spatial tissue context
  - Post-senescence survivors not explicitly modeled

---

## Conceptual contributions to multi-scale modeling

- Demonstrates how lineage-level mechanisms can invert at the population level.
- Establishes population structure as a hidden state variable in aging.
- Shows that heterogeneity and selection are not noise but organizing principles.
- Provides a template for translating single-cell data into population predictions.

---

## Relevance to Health & Longevity

- Explains why senescent cells accumulate before measurable functional decline.
- Clarifies why interventions targeting telomere length alone often fail.
- Highlights how comorbidities (e.g., increased mortality) accelerate aging independently of telomeres.
- Offers a framework for understanding cancer-prone escape from senescence.

---

## Open questions

- How do spatial tissue constraints alter lineage–population desynchronization?
- Can similar Type A / Type B senescence pathways be identified in mammalian tissues?
- How does immune clearance interact with population-level senescence dynamics?
- Can this framework be extended to regenerative or cancerous contexts?

---

## Tags

#aging #senescence #telomeres #replicative_senescence
#multiscale #population_dynamics #lineage_tracking
#stochastic_models #data_calibrated
#scale_molecular #scale_cellular #scale_population
#health_longevity #cancer_risk
