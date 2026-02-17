#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import http.server
import os
import socketserver
import sys
import textwrap
import webbrowser
from pathlib import Path


HTML_TEMPLATE = """<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Cafeína vs “Mateína”</title>
  <style>
    :root {{
      --bg: #0b0f17;
      --card: #111827;
      --text: #e5e7eb;
      --muted: #9ca3af;
      --accent: #22c55e;
      --accent2: #60a5fa;
      --border: rgba(255,255,255,.08);
      --code: #0f172a;
    }}
    body {{
      margin: 0; font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
      background: radial-gradient(1200px 800px at 15% 10%, rgba(34,197,94,.14), transparent 60%),
                  radial-gradient(900px 700px at 85% 20%, rgba(96,165,250,.16), transparent 60%),
                  var(--bg);
      color: var(--text);
      line-height: 1.55;
    }}
    .wrap {{ max-width: 980px; margin: 0 auto; padding: 28px 16px 48px; }}
    .hero {{
      border: 1px solid var(--border);
      background: linear-gradient(180deg, rgba(17,24,39,.92), rgba(17,24,39,.72));
      border-radius: 18px;
      padding: 22px;
      box-shadow: 0 12px 40px rgba(0,0,0,.35);
    }}
    h1 {{ margin: 0 0 6px; font-size: 30px; letter-spacing: .2px; }}
    .sub {{ color: var(--muted); margin: 0 0 14px; }}
    .badges {{ display: flex; flex-wrap: wrap; gap: 10px; margin-top: 14px; }}
    .badge {{
      font-size: 13px; padding: 6px 10px; border-radius: 999px;
      border: 1px solid var(--border); color: var(--text);
      background: rgba(255,255,255,.03);
    }}
    .grid {{
      display: grid; grid-template-columns: 1.1fr .9fr; gap: 16px; margin-top: 16px;
    }}
    @media (max-width: 900px) {{
      .grid {{ grid-template-columns: 1fr; }}
    }}
    .card {{
      border: 1px solid var(--border);
      background: rgba(17,24,39,.72);
      border-radius: 18px;
      padding: 18px;
    }}
    .card h2 {{ margin: 0 0 10px; font-size: 18px; }}
    .muted {{ color: var(--muted); }}
    .ok {{ color: var(--accent); font-weight: 700; }}
    .warn {{ color: #fbbf24; font-weight: 700; }}
    code, pre {{
      background: rgba(15,23,42,.75);
      border: 1px solid var(--border);
      border-radius: 12px;
    }}
    pre {{
      padding: 12px; overflow: auto; margin: 10px 0 0;
      font-size: 13px; color: #e5e7eb;
    }}
    .img {{
      width: 100%; max-width: 420px;
      border-radius: 16px;
      border: 1px solid var(--border);
      background: rgba(255,255,255,.02);
      padding: 10px;
    }}
    a {{ color: var(--accent2); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .footer {{ margin-top: 18px; color: var(--muted); font-size: 13px; }}
    ul {{ margin: 8px 0 0 18px; }}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="hero">
      <h1>Cafeína vs “Mateína” ☕🧉</h1>
      <p class="sub">Misma molécula. Diferente planta. Diferente contexto. Diferente relato.</p>

      <div class="badges">
        <span class="badge">Identidad molecular: <span class="ok">mismas</span></span>
        <span class="badge">Diferencia percibida: contexto + co-compuestos</span>
        <span class="badge">Segmentación “darwiniana”: memética cultural</span>
      </div>

      <div class="grid">
        <div class="card">
          <h2>1) Identidad molecular (química)</h2>
          <p>Si la <b>fórmula</b> y la <b>estructura</b> coinciden, hablamos del <b>mismo compuesto</b>.</p>

          <pre>{identity_block}</pre>

          <p class="muted">
            Nota: “mateína” es un nombre popular/cultural que se usa para el estimulante del mate,
            pero en lo químico el alcaloide principal es la <b>cafeína</b>.
          </p>
        </div>

        <div class="card">
          <h2>Estructura</h2>
          <p class="muted">La misma para cafeína / “mateína”.</p>
          <img class="img" src="/{image_name}" alt="Estructura de cafeína">
          <div class="footer">Archivo: <code>{image_name}</code></div>
        </div>

        <div class="card">
          <h2>2) ¿De dónde sale la “diferencia”?</h2>
          <ul>
            <li><b>Planta</b>: Mate (<i>Ilex paraguariensis</i>) vs Café (<i>Coffea</i> spp.)</li>
            <li><b>Matriz de consumo</b>: mate fraccionado (cebadas) vs café más concentrado por taza</li>
            <li><b>Co-compuestos</b>: polifenoles/taninos/ácidos, modulan percepción y tolerancia</li>
            <li><b>Expectativas</b> (set & setting): el cerebro interpreta distinto según contexto</li>
          </ul>
        </div>

        <div class="card">
          <h2>3) Segmentación “darwiniana” (memética)</h2>
          <p>
            No es selección natural de moléculas. Es selección cultural de <b>etiquetas/relatos</b>.
            Sobrevive el término que mejor se propaga y cumple una función:
          </p>
          <ul>
            <li><b>Identidad</b>: “mate ≠ café”</li>
            <li><b>Explicación simple</b>: “me pega distinto” sin bioquímica</li>
            <li><b>Propagación</b>: suena técnico y se repite fácil</li>
          </ul>
          <p class="footer">Resultado: químicamente iguales, culturalmente diferenciados.</p>
        </div>
      </div>
    </div>

    <div class="footer">
      Tip: si querés subirle el nivel, se puede agregar un “modo laboratorio” con inputs (dosis, tasa de ingesta) y un mini modelo de percepción.
    </div>
  </div>
</body>
</html>
"""


def same_molecule(formula_a: str, struct_a: str, formula_b: str, struct_b: str) -> bool:
    return (formula_a.strip() == formula_b.strip()) and (struct_a.strip().lower() == struct_b.strip().lower())


def main() -> int:
    parser = argparse.ArgumentParser(description="Servidor local: cafeína vs 'mateína'")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8000, type=int)
    parser.add_argument("--image", default="caffeine_structure.png")
    parser.add_argument("--no-open", action="store_true", help="No abrir navegador automáticamente.")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    image_path = (root / args.image)

    # Datos "demo"
    formula = "C8H10N4O2"
    structure = "1,3,7-trimetilxantina"

    identity_ok = same_molecule(formula, structure, formula, structure)

    identity_block = textwrap.dedent(f"""\
        mateína:
          fórmula   = {formula}
          estructura= {structure}

        cafeína:
          fórmula   = {formula}
          estructura= {structure}

        veredicto químico: {"MISMA MOLÉCULA ✅" if identity_ok else "DISTINTAS ❌"}
    """).rstrip()

    # Servidor HTTP: servimos HTML en "/" y estáticos desde la carpeta.
    class Handler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == "/" or self.path.startswith("/?"):
                html = HTML_TEMPLATE.format(
                    identity_block=identity_block.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"),
                    image_name=args.image,
                ).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(html)))
                self.end_headers()
                self.wfile.write(html)
                return
            return super().do_GET()

        def log_message(self, format, *args_):
            # más prolijo: sin spam de logs
            return

    if not image_path.exists():
        print(f"[WARN] No encuentro la imagen: {image_path}")
        print("[WARN] La página abrirá igual pero la imagen no cargará.")

    os.chdir(root)

    with socketserver.TCPServer((args.host, args.port), Handler) as httpd:
        url = f"http://{args.host}:{args.port}/"
        print(f"[OK] Servidor corriendo en: {url}")
        if not args.no_open:
            webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[INFO] Cerrando servidor...")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
