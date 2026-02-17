#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Demostración "lógica" + "contextual" de:
- Identidad molecular: mateína == cafeína (misma molécula: 1,3,7-trimetilxantina, C8H10N4O2)
- Diferencia percibida: origen vegetal + matriz de consumo + co-compuestos + relato cultural
- Segmentación darwiniana (memética): sobreviven etiquetas útiles para identidad/explicación social

Incluye visualización de una imagen (estructura de la molécula).
"""

from __future__ import annotations

import argparse
import os
import sys
import textwrap


CAFFEINE_FORMULA = "C8H10N4O2"
CAFFEINE_STRUCTURE = "1,3,7-trimetilxantina"


def same_molecule(formula_a: str, structure_a: str, formula_b: str, structure_b: str) -> bool:
    """Criterio mínimo de identidad molecular (didáctico)."""
    return (formula_a.strip() == formula_b.strip()) and (structure_a.strip().lower() == structure_b.strip().lower())


def show_image(image_path: str) -> None:
    """
    Muestra la imagen:
    - Si hay matplotlib: la abre en una ventana.
    - Si no: intenta abrir con el visor por defecto del sistema (Windows).
    """
    if not os.path.exists(image_path):
        print(f"[WARN] No encontré la imagen en: {image_path}")
        return

    # Intento 1: matplotlib (más portable)
    try:
        import matplotlib.pyplot as plt  # type: ignore
        import matplotlib.image as mpimg  # type: ignore

        img = mpimg.imread(image_path)
        plt.figure()
        plt.imshow(img)
        plt.axis("off")
        plt.title("Estructura (cafeína / 'mateína')")
        plt.tight_layout()
        plt.show()
        return
    except Exception:
        pass

    # Intento 2: visor por defecto (Windows)
    try:
        if sys.platform.startswith("win"):
            os.startfile(os.path.abspath(image_path))  # type: ignore[attr-defined]
        else:
            print("[INFO] No pude usar matplotlib y no estoy en Windows para abrir con os.startfile().")
            print("[INFO] Abrí manualmente la imagen:", os.path.abspath(image_path))
    except Exception as e:
        print("[WARN] No pude abrir la imagen automáticamente:", e)
        print("[INFO] Abrí manualmente la imagen:", os.path.abspath(image_path))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Demo: 'mateína' vs cafeína — misma molécula, diferencia contextual/cultural.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "--image",
        default="caffeine_structure.png",
        help="Ruta a la imagen de la estructura (por defecto: caffeine_structure.png)",
    )
    parser.add_argument(
        "--no-image",
        action="store_true",
        help="No abrir/mostrar la imagen (solo texto).",
    )
    args = parser.parse_args()

    # --- "Mateína": etiqueta popular para el estimulante del mate (químicamente cafeína)
    mateina_formula = CAFFEINE_FORMULA
    mateina_structure = CAFFEINE_STRUCTURE

    cafeina_formula = CAFFEINE_FORMULA
    cafeina_structure = CAFFEINE_STRUCTURE

    # --- Prueba de identidad molecular
    identity = same_molecule(
        mateina_formula, mateina_structure,
        cafeina_formula, cafeina_structure
    )

    print("=" * 78)
    print("DEMO: 'MATEÍNA' vs CAFEÍNA")
    print("=" * 78)

    print("\n[1] Identidad molecular (química)")
    print(f"    - mateína:  fórmula={mateina_formula}, estructura={mateina_structure}")
    print(f"    - cafeína:  fórmula={cafeina_formula}, estructura={cafeina_structure}")

    if identity:
        print("\n    VEREDICTO QUÍMICO: SON LA MISMA MOLÉCULA ✅")
        print("    (Cambian el nombre/relato, no el compuesto principal.)")
    else:
        print("\n    VEREDICTO QUÍMICO: NO SON LA MISMA MOLÉCULA ❌")

    # --- Diferencia real: contexto (planta + consumo + co-compuestos)
    print("\n[2] 'Diferencia' (percepción / fisiología práctica)")
    print(textwrap.dedent("""\
        La sensación puede variar aunque la molécula principal sea la misma, por:
          A) Origen vegetal (matriz distinta)
             - Mate:  Ilex paraguariensis
             - Café:  Coffea spp.

          B) Matriz de consumo (cómo entra al cuerpo)
             - Mate: dosis fraccionada (cebadas), ingesta sostenida.
             - Café: dosis más concentrada por taza, a veces más "de golpe".

          C) Co-compuestos (acompañantes) que modulan la experiencia
             - Polifenoles / taninos / ácidos, etc.
             - Efectos GI, percepción de "nervios", tolerancia, set & setting.

          D) Expectativas y aprendizaje (tu cerebro 'predice' el efecto)
             - Si esperás que mate sea distinto, tu interpretación subjetiva cambia.
    """).rstrip())

    # --- Segmentación darwiniana (memética/cultural)
    print("\n[3] Segmentación darwiniana (memética): por qué sobrevive 'mateína'")
    print(textwrap.dedent("""\
        Idea central:
          - No hay selección natural de moléculas acá.
          - Hay selección cultural de ETIQUETAS y RELATOS (memes).

        Regla "darwiniana" (social):
          - Sobrevive el nombre/relato que mejor cumple una función en su entorno.

        Función de la etiqueta "mateína" en cultura matera:
          - Identidad: 'mate no es café' (marca de pertenencia).
          - Simplificación: explica diferencias percibidas sin bioquímica.
          - Propagación: es fácil de repetir y suena "técnico".

        Función de "cafeína":
          - Estándar científico y universal (útil en nutrición, medicina, etiquetado).
    """).rstrip())

    # --- Conclusión compacta
    print("\n[4] Conclusión")
    print("    - Químicamente: 'mateína' == cafeína (misma molécula principal).")
    print("    - Prácticamente: cambia el 'pack': planta + consumo + co-compuestos + relato.")
    print("=" * 78)

    if not args.no_image:
        print("\n[IMG] Mostrando imagen de la estructura...")
        show_image(args.image)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Demostración "lógica" + "contextual" de:
- Identidad molecular: mateína == cafeína (misma molécula: 1,3,7-trimetilxantina, C8H10N4O2)
- Diferencia percibida: origen vegetal + matriz de consumo + co-compuestos + relato cultural
- Segmentación darwiniana (memética): sobreviven etiquetas útiles para identidad/explicación social

Incluye visualización de una imagen (estructura de la molécula).
"""

from __future__ import annotations

import argparse
import os
import sys
import textwrap


CAFFEINE_FORMULA = "C8H10N4O2"
CAFFEINE_STRUCTURE = "1,3,7-trimetilxantina"


def same_molecule(formula_a: str, structure_a: str, formula_b: str, structure_b: str) -> bool:
    """Criterio mínimo de identidad molecular (didáctico)."""
    return (formula_a.strip() == formula_b.strip()) and (structure_a.strip().lower() == structure_b.strip().lower())


def show_image(image_path: str) -> None:
    """
    Muestra la imagen:
    - Si hay matplotlib: la abre en una ventana.
    - Si no: intenta abrir con el visor por defecto del sistema (Windows).
    """
    if not os.path.exists(image_path):
        print(f"[WARN] No encontré la imagen en: {image_path}")
        return

    # Intento 1: matplotlib (más portable)
    try:
        import matplotlib.pyplot as plt  # type: ignore
        import matplotlib.image as mpimg  # type: ignore

        img = mpimg.imread(image_path)
        plt.figure()
        plt.imshow(img)
        plt.axis("off")
        plt.title("Estructura (cafeína / 'mateína')")
        plt.tight_layout()
        plt.show()
        return
    except Exception:
        pass

    # Intento 2: visor por defecto (Windows)
    try:
        if sys.platform.startswith("win"):
            os.startfile(os.path.abspath(image_path))  # type: ignore[attr-defined]
        else:
            print("[INFO] No pude usar matplotlib y no estoy en Windows para abrir con os.startfile().")
            print("[INFO] Abrí manualmente la imagen:", os.path.abspath(image_path))
    except Exception as e:
        print("[WARN] No pude abrir la imagen automáticamente:", e)
        print("[INFO] Abrí manualmente la imagen:", os.path.abspath(image_path))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Demo: 'mateína' vs cafeína — misma molécula, diferencia contextual/cultural.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "--image",
        default="caffeine_structure.png",
        help="Ruta a la imagen de la estructura (por defecto: caffeine_structure.png)",
    )
    parser.add_argument(
        "--no-image",
        action="store_true",
        help="No abrir/mostrar la imagen (solo texto).",
    )
    args = parser.parse_args()

    # --- "Mateína": etiqueta popular para el estimulante del mate (químicamente cafeína)
    mateina_formula = CAFFEINE_FORMULA
    mateina_structure = CAFFEINE_STRUCTURE

    cafeina_formula = CAFFEINE_FORMULA
    cafeina_structure = CAFFEINE_STRUCTURE

    # --- Prueba de identidad molecular
    identity = same_molecule(
        mateina_formula, mateina_structure,
        cafeina_formula, cafeina_structure
    )

    print("=" * 78)
    print("DEMO: 'MATEÍNA' vs CAFEÍNA")
    print("=" * 78)

    print("\n[1] Identidad molecular (química)")
    print(f"    - mateína:  fórmula={mateina_formula}, estructura={mateina_structure}")
    print(f"    - cafeína:  fórmula={cafeina_formula}, estructura={cafeina_structure}")

    if identity:
        print("\n    VEREDICTO QUÍMICO: SON LA MISMA MOLÉCULA ✅")
        print("    (Cambian el nombre/relato, no el compuesto principal.)")
    else:
        print("\n    VEREDICTO QUÍMICO: NO SON LA MISMA MOLÉCULA ❌")

    # --- Diferencia real: contexto (planta + consumo + co-compuestos)
    print("\n[2] 'Diferencia' (percepción / fisiología práctica)")
    print(textwrap.dedent("""\
        La sensación puede variar aunque la molécula principal sea la misma, por:
          A) Origen vegetal (matriz distinta)
             - Mate:  Ilex paraguariensis
             - Café:  Coffea spp.

          B) Matriz de consumo (cómo entra al cuerpo)
             - Mate: dosis fraccionada (cebadas), ingesta sostenida.
             - Café: dosis más concentrada por taza, a veces más "de golpe".

          C) Co-compuestos (acompañantes) que modulan la experiencia
             - Polifenoles / taninos / ácidos, etc.
             - Efectos GI, percepción de "nervios", tolerancia, set & setting.

          D) Expectativas y aprendizaje (tu cerebro 'predice' el efecto)
             - Si esperás que mate sea distinto, tu interpretación subjetiva cambia.
    """).rstrip())

    # --- Segmentación darwiniana (memética/cultural)
    print("\n[3] Segmentación darwiniana (memética): por qué sobrevive 'mateína'")
    print(textwrap.dedent("""\
        Idea central:
          - No hay selección natural de moléculas acá.
          - Hay selección cultural de ETIQUETAS y RELATOS (memes).

        Regla "darwiniana" (social):
          - Sobrevive el nombre/relato que mejor cumple una función en su entorno.

        Función de la etiqueta "mateína" en cultura matera:
          - Identidad: 'mate no es café' (marca de pertenencia).
          - Simplificación: explica diferencias percibidas sin bioquímica.
          - Propagación: es fácil de repetir y suena "técnico".

        Función de "cafeína":
          - Estándar científico y universal (útil en nutrición, medicina, etiquetado).
    """).rstrip())

    # --- Conclusión compacta
    print("\n[4] Conclusión")
    print("    - Químicamente: 'mateína' == cafeína (misma molécula principal).")
    print("    - Prácticamente: cambia el 'pack': planta + consumo + co-compuestos + relato.")
    print("=" * 78)

    if not args.no_image:
        print("\n[IMG] Mostrando imagen de la estructura...")
        show_image(args.image)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
