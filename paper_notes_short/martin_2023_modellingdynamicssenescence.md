# Martin et al. 2023 — Modelling the dynamics of senescence spread

## Short note

- **Paper**: Martin et al. (2023) — Modelling the dynamics of senescence spread
- **Question**: We know senescent cells can induce senescence in nearby cells via SASP and contact-dependent signaling, but in vitro senescent lesions often remain spatially bounded even without immune clearance. What interaction rules are sufficient to prevent senescence from spreading indefinitely across a tissue-like cell layer?
- **Model**: Minimal mathematical model + stochastic spatial simulation linking ligand diffusion/binding to spatial propagation of cell-state transitions.
- **Imposed**:
  - Cells are non-motile circles in a 2D layer under a 3D media layer; SASP ligands diffuse in the media and bind to receptors.  ￼
  - A cell becomes senescent via paracrine signaling if ligand–receptor binding exceeds a threshold rate; senescent cells secrete ligands at a fixed rate.
  - A cell can also become senescent via juxtacrine (NOTCH-mediated) signaling through direct contact with senescent neighbors; juxtacrine-induced secondary senescent cells are assumed to have reduced or absent SASP secretion.
  - The model can include a time delay between senescence induction and full SASP-producing senescence.
- **Varied**:
  - Strength and reach of paracrine signaling (ligand emission NE, ligand threshold ND, diffusion coefficient, receptor number Rtot, binding rates).
  - Presence/absence of juxtacrine secondary senescence, and whether juxtacrine secondary cells produce SASP.  ￼
  - Delays in paracrine vs juxtacrine induction timing.  ￼
  - SASP strength of secondary senescent cells relative to primary cells.
- **Measured**:
  - Whether senescence spreads at all, and if so, whether spread is finite vs runaway.  ￼
  - Spatial extent of the senescent region over time, and the relative abundance of juxtacrine vs paracrine secondary senescent cells
- **Conclusion**: Controlled senescence spread can emerge from interaction structure alone. Juxtacrine-induced senescent cells can act as a “firebreak” that absorbs SASP without amplifying it, and time-dependent induction (juxtacrine first, paracrine later) prevents explosive lesion growth. The model predicts that differences in SASP secretion between primary and secondary senescent subtypes are a plausible mechanism for keeping senescence spatially local even in the absence of immune clearance.
