# Tikka et al. (2022) — Nephron progenitor migration and aggregation during kidney organogenesis

## Short note

- **Paper**: Tikka et al. (2022) — Nephron progenitor migration and aggregation during kidney organogenesis
- **Question**: What minimal combination of chemotactic cues and cell–cell adhesion differences is sufficient to drive nephron progenitor cells to move from the ureteric bud tip to the corner niche and form pretubular aggregates?
- **Model**: 3D Cellular Potts Model (CompuCell3D) of nephron progenitor (NP) and metanephric mesenchyme (MM) cell movement around branching ureteric bud (UB) geometry.
- **Imposed**:
  - UB geometry is fixed and cells move via CPM energy minimization (“cell sorting”)
  - NP cells can chemotax up a chemoattractant gradient
  - Chemoattractant can be secreted by UB cells, NP cells, or both
  - Differential adhesion energies between NP/MM/UB can be included or excluded depending on the model variant
- **Varied**:
  - Whether chemotaxis exists and who secretes chemoattractant (UB vs NP vs both)
  - Whether NP and MM have distinct adhesion properties
  - Parameter values for chemotaxis strength, secretion, and adhesion (fit using particle swarm optimization)
- **Measured**:
  - NP enrichment in the UB corner region (aggregate formation)
  - Tip vs corner migration speeds and speed ratios
  - Final spatial cell configurations relative to UB tips/corners
- **Conclusion**: Neuromast regeneration kinetics and final proportions can emerge from a simple, local, cell-type-specific negative feedback rule (“stop dividing once enough same-type neighbors accumulate”), showing that organ-scale homeostasis can be explained without global control signals.
