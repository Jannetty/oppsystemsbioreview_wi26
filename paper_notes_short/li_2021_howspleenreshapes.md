# Li et al. 2021 — How the spleen mechanically reshapes young red blood cells and clears old ones

## Short note

- **Paper:** Li et al. (2021) — How the spleen reshapes and retains young and old red blood cells
- **Question:** We know the spleen both helps reticulocytes mature and removes senescent RBCs, but the mechanical mechanisms are hard to observe in vivo. Can spleen-like mechanical constraints alone explain reticulocyte remodeling (pitting/vesiculation) and late-life RBC retention/lysis?
- **Model:** Particle-based multiscale mechanical model (OpenRBC) of RBC membrane + cytoskeleton explicitly passing through splenic interendothelial slits (IES).
- **Imposed:** Realistic RBC membrane architecture (lipid bilayer + spectrin cytoskeleton + transmembrane proteins) and a spleen-like slit geometry that forces extreme deformation; mechanical contact interactions prevent wall penetration.
- **Varied:**
  - Surface-to-volume ratio (S/V) to represent RBC aging (younger cells have higher S/V; older cells have lower S/V).
  - Driving pressure gradient across the splenic slit (how hard the spleen forces cells through).
  - Reticulocyte vs mature RBC structural features, including whether the cell contains a rigid inclusion (Howell–Jolly-body-like) and whether the membrane has excess area that can be shed.
- **Measured:**
  - Passage outcome: successful traversal vs retention vs mechanical rupture/lysis.
  - Extent of vesiculation (how much membrane is shed during deformation)
  - Inclusion “pitting” success (whether an inclusion can be removed without destroying the cell).
  - A phase diagram of outcomes as a function of S/V ratio and pressure gradient, separating regimes of normal passage, maturation-like remodeling, and catastrophic failure.
- **Conclusion:** The model shows that the spleen can act as a mechanical filter and mechanical remodeler. Uunder the same imposed slit geometry, cells with high S/V can pass and shed membrane/inclusions (reticulocyte maturation), while cells with low S/V are mechanically trapped and can rupture. Thus senescent clearance and reticulocyte remodeling can emerge from cross-scale coupling between cell-intrinsic mechanics and tissue-scale constraints, without requiring an explicit molecular aging signal.
