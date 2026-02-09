# Weatherley et al. 2026 — Oligodendrocyte resilience can stabilize MS lesion dynamics in a spatial ABM

## Short note

- **Paper**: Weatherley et al. (2026) — Therapeutic targeting of oligodendrocytes in an agent-based model of multiple sclerosis
- **Question**: We know MS lesion progression reflects repeated immune “relapse” events and that existing therapies often focus on suppressing immune entry into the CNS. The authors are curious about the reparative capabilities of oligodendrocytes following immune damage to the CNS. Can targeting oligodendrocyte resilience (rather than immune trafficking alone) stabilize lesion dynamics and preserve myelin?
- **Model**: Spatial agent-based model of CNS lesion development coupling immune infiltration, macrophage activity, oligodendrocyte stress responses, and myelin loss/repair (implemented in MATLAB).
- **Imposed**:
  - Primed T cells enter the CNS through a BBB permeability parameter, driving relapse-like immune activation.
  - Oligodendrocytes transition between myelinating, non-myelinating, and apoptotic behaviors depending on accumulated stress (“integrated stress response” abstraction) governed by two tolerance thresholds (ω and λ).
- **Varied**:
  - BBB-targeted therapy timing (immediate vs delayed reduction of permeability bR).  ￼
  - Oligodendrocyte “resilience” therapies modeled as increased stress tolerances (ω, λ).  ￼
  - Remyelination therapies modeled as partial or full restoration of oligodendrocyte populations at intervention time.
- **Measured**:
  - Reactivated T-cell population trajectories under BBB-targeted strategies.  ￼
  - Fraction of intact myelin over time, including whether remyelination occurs after relapses.  ￼
  - Oligodendrocyte population state composition (myelinating vs apoptotic) as a function of ω and λ.
- **Conclusion**: This model suggests that reducing immune entry across the BBB is often insufficient to prevent long-term lesion progression, because relapses still overwhelm local repair. In contrast, therapies that increase oligodendrocyte stress tolerance (ISR-targeting) can stabilize lesion dynamics by preserving the local “repair capacity,” enabling remyelination even when immune activity is not eliminated.
