# Expediční atlas — Za hranice času

Doprovodná publikace k cestě Utah/Arizona 2026. Česky, formát A4 PDF.

## Soubory

- `atlas.md` — zdrojový text knihy (markdown + HTML rámečky)
- `svg/` — schematické mapy a diagramy (vkládají se přes `{{svg:název}}`)
- `build_atlas.py` — sestavení PDF (`python3 atlas/build_atlas.py`)
- `za-hranice-casu.pdf` — hotová kniha
- `expedicni_atlas_plan.md` — původní pracovní plán/zadání

## Jak po cestě doplnit fotografie a zápisky (verze 2)

1. Fotky uložte do `atlas/photos/`.
2. V `atlas.md` nahraďte rámeček `<div class="after">…</div>` na konci kapitoly obrázkem:
   `<img src="photos/nazev.jpg" style="width:100%">` + odstavec se zápisky.
3. Znovu spusťte `python3 atlas/build_atlas.py`.

Rámečky „Zápisník“ v tištěné verzi slouží k psaní tužkou přímo na cestě — po
návratu se přepíší sem.

## Poznámky

- Údaje o požárech platí k 5. 7. 2026 — před cestou ověřit (InciWeb, BLM, NPS).
- Mapy jsou schémata, ne navigační podklad.
