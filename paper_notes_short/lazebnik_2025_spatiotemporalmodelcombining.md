# Lazebnik and Friedman (2025) — Senescence-aware combination therapy in metastatic prostate cancer

## Short note

- **Paper**: Lazebnik and Friedman (2025) — Senescence-aware combination therapy in metastatic prostate cancer
- **Question**: We know that standard prostate cancer therapies induce senescence, and that senescent cells can promote tumor progression via SASP. How does therapy-induced senescence alter treatment efficacy across space and time, and can senolytic drugs (drugs that target and kill senescent cells) restore coordinated tumor control?
- **Model**: Spatial PDE model coupling tumor growth, senescent and resistant cancer cell populations, immune dynamics, angiogenesis, oxygen, and drug pharmacokinetics (implemented in python, scipy is only dependency).
- **Imposed**: Rules for cell fate transitions under ADT and chemotherapy (proliferative → senescent or resistant), VEGF-mediated angiogenesis from senescent cells, immune killing, diffusion of cells and signaling factors, and pharmacokinetics of ADT, chemotherapy, and senolytics.
- **Varied**: Drug doses and schedules (ADT, chemotherapy, senolytic), timing of senolytic administration relative to chemotherapy, and combinations of treatments.
- **Measured**: Tumor volume over time, senescent cell burden, VEGF levels, angiogenesis, and synergy scores for combination therapies.
- **Conclusion**: The model shows that therapy-induced senescence can desynchronize cell-fate decisions from tissue-scale signaling, promoting angiogenesis and tumor persistence. Restoring coordination by eliminating senescent cells (especially when senolytics are administered immediately after chemotherapy) substantially improves treatment outcomes. This study demonstrates the importance of explicitly modeling multiscale interactions between cell states, signaling, and therapy timing.
