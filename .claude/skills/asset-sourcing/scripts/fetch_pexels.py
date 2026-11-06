#!/usr/bin/env python3
"""Buscar y descargar una foto de Pexels en una app (licencia: consultar Pexels).

Uso: PEXELS_API_KEY=... python fetch_pexels.py --query 'friends cafe' --output public/images/friends.jpg
Escribirá un .source.json junto a la imagen para registrar procedencia y créditos.
"""
import argparse
import json
import os
from pathlib import Path
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen

MAX_SIZE = 15 * 1024 * 1024

def request_json(url: str, key: str) -> dict:
    req = Request(url, headers={"Authorization": key, "User-Agent": "Claude-Asset-Sourcing/1.0"})
    with urlopen(req, timeout=20) as response:
        return json.load(response)

def download_image(url: str, output: Path):
    hostname = urlparse(url).hostname or ""
    if hostname != "images.pexels.com":
        raise ValueError(f"Host de imagen inesperado: {hostname}")
    req = Request(url, headers={"User-Agent": "Claude-Asset-Sourcing/1.0"})
    with urlopen(req, timeout=30) as response:
        content_type = response.headers.get("Content-Type", "").split(";")[0]
        if content_type not in ("image/jpeg", "image/png", "image/webp", "image/avif"):
            raise ValueError(f"Respuesta no es una imagen compatible: {content_type}")
        data = response.read(MAX_SIZE + 1)
        if len(data) > MAX_SIZE:
            raise ValueError("La imagen supera 15 MB; elegí una versión más pequeña")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(data)
    return content_type, len(data)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True, help="Preferiblemente en inglés")
    parser.add_argument("--output", required=True, help="Ej.: public/images/hero.jpg")
    parser.add_argument("--orientation", choices=("landscape", "portrait", "square"))
    parser.add_argument("--index", type=int, default=0, help="Índice de resultado (0-9); evaluar candidatos")
    args = parser.parse_args()
    key = os.getenv("PEXELS_API_KEY")
    if not key:
        raise SystemExit("Falta PEXELS_API_KEY; agregarla al entorno, nunca al repositorio")
    params = {"query": args.query, "per_page": 10}
    if args.orientation: params["orientation"] = args.orientation
    data = request_json("https://api.pexels.com/v1/search?" + urlencode(params), key)
    photos = data.get("photos", [])
    if not photos:
        raise SystemExit("Pexels no devolvió fotos. Refiná la consulta")
    print("Candidatos disponibles (revisar las URLs antes de elegir):")
    for i, photo in enumerate(photos):
        print(f"{i}: {photo.get('id')} — {photo.get('photographer')} — {photo.get('url')}")
    if not (0 <= args.index < len(photos)):
        raise SystemExit(f"Índice fuera de rango: 0-{len(photos)-1}")
    photo = photos[args.index]
    src = photo.get("src", {}).get("large") or photo.get("src", {}).get("original")
    if not src:
        raise SystemExit("La API no devolvió una URL de archivo utilizable")
    path = Path(args.output)
    mime, size = download_image(src, path)
    metadata = {
        "provider": "Pexels",
        "photo_id": photo.get("id"),
        "source_page": photo.get("url"),
        "photographer": photo.get("photographer"),
        "photographer_page": photo.get("photographer_url"),
        "license_page": "https://www.pexels.com/license/",
        "api_guidelines": "https://www.pexels.com/api/documentation/",
        "downloaded_from": src,
        "mime_type": mime,
        "bytes": size,
        "query": args.query,
        "attribution_note": "La API de Pexels exige enlace visible a Pexels; acreditar al fotógrafo cuando sea posible",
    }
    path.with_name(path.name + ".source.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Guardado: {path} ({size} bytes), y {path.name}.source.json")

if __name__ == "__main__":
    main()
