# latexmk-Konfiguration: `latexmk main.tex` reicht — kein -lualatex-Flag nötig
$pdf_mode = 4;        # 4 = lualatex (Uni-Vorgabe: fontspec/Arial braucht lualatex)
$aux_dir  = 'build';  # Hilfsdateien nach build/, main.pdf bleibt im Projekt-Root
