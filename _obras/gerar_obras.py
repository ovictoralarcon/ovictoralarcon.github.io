#!/usr/bin/env python3
"""
Converte .md do banco de dados (portfolio-inventario)
para .md do Jekyll (ovictoralarcon.github.io/_obras/)

Uso:
    python3 gerar_obras.py
    python3 gerar_obras.py --dry-run   # mostra o que faria sem salvar
"""

import os
import re
import argparse
from pathlib import Path

ENTRADA = Path("/home/victor/portfolio-inventario/obras")
SAIDA   = Path("/home/victor/Site/ovictoralarcon.github.io/_obras")

# Arquivos que não são obras — ignorar
IGNORAR = {"bio.md", "capa.md", "curriculo.md", "_template.md", "indice.md"}


def extrair_frontmatter(texto):
    match = re.match(r"^---\n(.*?)\n---\n?(.*)", texto, re.DOTALL)
    if not match:
        return None, ""
    return match.group(1), match.group(2)


def parse_yaml_simples(yaml_str):
    dados = {}
    for linha in yaml_str.splitlines():
        if ":" not in linha:
            continue
        chave, _, valor = linha.partition(":")
        chave = chave.strip()
        valor = valor.strip()
        if (valor.startswith('"') and valor.endswith('"')) or \
           (valor.startswith("'") and valor.endswith("'")):
            valor = valor[1:-1]
        if valor in ("null", "~", ""):
            valor = None
        elif valor == "[]":
            valor = []
        dados[chave] = valor
    return dados


def extrair_imagem_cloudinary(corpo):
    """Pega a primeira URL do Cloudinary. Ignora caminhos locais."""
    match = re.search(r"!\[.*?\]\((https://res\.cloudinary\.com/[^)]+)\)", corpo)
    if match:
        return match.group(1)
    return None


def extrair_descricao(corpo):
    match = re.search(r"##\s*Descrição\s*\n(.*?)(?=##|\Z)", corpo, re.DOTALL)
    if not match:
        return None
    texto = re.sub(r"<!--.*?-->", "", match.group(1), flags=re.DOTALL).strip()
    return texto if texto else None


def slugify(titulo):
    slug = titulo.lower()
    for a, b in [("áàãâä","a"),("éèêë","e"),("íìîï","i"),("óòõôö","o"),("úùûü","u"),("ç","c")]:
        for c in a:
            slug = slug.replace(c, b)
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def converter(md_entrada, dry_run=False):
    nome_lower = md_entrada.name.lower()

    # Ignora arquivos que não são obras
    if nome_lower in IGNORAR:
        print(f"  IGNORADO (não é obra): {md_entrada.name}")
        return

    texto = md_entrada.read_text(encoding="utf-8")
    yaml_str, corpo = extrair_frontmatter(texto)

    if yaml_str is None:
        print(f"  IGNORADO (sem frontmatter): {md_entrada.name}")
        return

    dados = parse_yaml_simples(yaml_str)

    titulo    = dados.get("titulo")
    ano       = dados.get("ano")
    dimensoes = dados.get("dimensoes")

    # Ignora se não tiver título, ano e dimensões — provavelmente não é obra
    if not titulo or not ano or not dimensoes:
        print(f"  IGNORADO (sem título/ano/dimensões): {md_entrada.name}")
        return

    imagem = extrair_imagem_cloudinary(corpo)
    descricao = extrair_descricao(corpo)

    # Monta frontmatter de saída
    linhas = ["---", "layout: obra", f'title: "{titulo}"']

    campos_texto = ("tecnica", "suporte", "ano", "dimensoes", "serie",
                    "tiragem_total", "numero_exemplar", "status",
                    "localizacao", "data_registro")
    for campo in campos_texto:
        valor = dados.get(campo)
        if valor is not None and valor != [] and valor != "":
            linhas.append(f'{campo}: "{valor}"')

    # preco sem aspas para permitir ordenação numérica no Jekyll
    preco = dados.get("preco")
    if preco is not None and preco != "":
        try:
            linhas.append(f'preco: {float(str(preco).replace(",", ".")):.2f}')
        except ValueError:
            linhas.append(f'preco: "{preco}"')

    if imagem:
        linhas.append(f'imagem: "{imagem}"')

    linhas.append("---")

    if descricao:
        linhas.append("")
        linhas.append(descricao)

    conteudo_saida = "\n".join(linhas) + "\n"

    slug = slugify(titulo)
    nome_saida = f"{slug}.md"
    caminho_saida = SAIDA / nome_saida

    if dry_run:
        print(f"\n{'─'*60}")
        print(f"  {md_entrada.name}  →  {nome_saida}")
        print(conteudo_saida)
    else:
        SAIDA.mkdir(parents=True, exist_ok=True)
        caminho_saida.write_text(conteudo_saida, encoding="utf-8")
        print(f"  {md_entrada.name}  →  {nome_saida}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true",
                        help="Mostra o resultado sem salvar")
    args = parser.parse_args()

    arquivos = sorted(ENTRADA.glob("*.md"))
    if not arquivos:
        print(f"Nenhum .md encontrado em {ENTRADA}")
        return

    print(f"{'DRY RUN — ' if args.dry_run else ''}Convertendo {len(arquivos)} arquivo(s)...\n")
    for arq in arquivos:
        converter(arq, dry_run=args.dry_run)

    if not args.dry_run:
        print(f"\nPronto. Arquivos salvos em {SAIDA}")


if __name__ == "__main__":
    main()
