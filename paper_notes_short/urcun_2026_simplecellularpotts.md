# Urcun et al. (2025) — CPM scratch-assay model for healthy vs keloid fibroblast migration

## Short note

- **Paper**: Urcun et al. (2025) — CPM scratch-assay model for healthy vs keloid fibroblast migration
- **Question**: Is loss of contact inhibition of locomotion sufficient to reproduce keloid-like scratch-assay closure dynamics?
- **Model**: 2D Cellular Potts Model of fibroblast migration in scratch assays, calibrated to in vitro data.
- **Imposed**: Fibroblasts are represented as deformable CPM cells whose movement is impacted by (i) a contact law that transitions from adhesion to repulsion as contact area increases, (ii) surface and elongation constraints that depend on crowding, and (iii) a motility term that is either reduced by contact (CIL) or not (no CIL).
- **Varied**: Whether fibroblasts obey CIL or not; fibroblast type (healthy vs keloid); macrophage secretome condition (control, M1, M2); and calibrated migration/crowding parameters controlling motility, max spread area, and contact inhibition threshold.
- **Measured**: Wound closure over time (percent closure at 20h and 36h), plus inferred parameter shifts across conditions from calibration.
- **Conclusion**: Loss of CIL is sufficient to reproduce keloid-like closure dynamics, linking a local cell–cell interaction rule to tissue-scale pathology
