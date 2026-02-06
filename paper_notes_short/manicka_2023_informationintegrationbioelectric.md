# Manicka et al. 2023 — Bioelectric information integration in brain morphogenesis

## Short note

- **Paper:** Manicka et al. 2023 — Bioelectric information integration in brain morphogenesis
- **Question:** Can a tissue plausibly decode tissue-scale voltage patterns into distinct gene-expression programs, rather than responding only to local voltage levels?
- **Model:** Minimal dynamical model of spatially coupled bioelectric and gene-regulatory network trained to distinguish between different tissue-scale voltage patterns
- **Imposed:** 2D lattice of cells where each cell contains: simplified ion-channel dynamics producing membrane voltage, and an unspecified genetic regulatory network (essentially the set of genes can be thought of as free parameters that parameter estimation uses to drive the system to recognize tissue-scale patterns). Neighbor cells communicate via symmetric local coupling and voltage-gene interactions are bidirectionally linked
- **Varied:** Input voltage patterns (after parameters are trained to drive the system towards a specific pattern given that pattern as input), tissue size (# of cells), spatial "knockouts" of specific cells/regions to test which parts of the tissue contribute most to pattern recognition.
- **Measured:** Tissue-wide gene expression outputs, pattern discrimination performance, sensitivity structure (which cells and which gene interactions carry the information)
- **Conclusion:** Correct developmental gene expression can emerge from higher-order spatiotemporal information integration, where cells respond to the pattern structure of voltage across the tissue, showing morphogenesis may depend on multicellular-scale bioelectric context, not just local voltage levels.
