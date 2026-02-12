# de Jong et al. 2024 — Gastruloid elongation from convergent extension (crawling + adhesion)

## Short note

- **Paper:** de Jong et al. (2024) — Gastruloid elongation is consistent with convergent extension driven by active crawling + differential adhesion
- **Question:** We know gastruloids elongate in vitro in a way that resembles embryonic axis extension. What minimal set of cell-level mechanical interaction rules is sufficient to reproduce the observed elongating shapes?
- **Model:** Cellular Potts model (tissue simulation toolkit, C++) of a multicellular aggregate, used to test alternative hypotheses for the mechanism driving elongation.
- **Imposed:** Cell-level mechanical rules representing (i) differential adhesion and (ii) active cell crawling that together generate convergent extension-like rearrangements.
- **Varied:** Presence/absence and strength of differential adhesion vs active crawling; perturbation of convergent-extension machinery via ROCK inhibition (experimental validation).
- **Measured:** Gastruloid shape features during elongation, and whether simulations reproduce observed elongating morphologies.
- **Conclusion:** Gastruloid elongation can be explained as convergent extension emerging from the combination of active crawling and differential adhesion; differential adhesion alone cannot reproduce the observed shapes.
