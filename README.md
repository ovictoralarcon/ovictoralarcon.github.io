# ovictoralarcon.github.io

Site pessoal. Jekyll + GitHub Pages.

## Estrutura

```
├── _config.yml          # Configuração geral
├── _layouts/            # Templates HTML
│   ├── default.html     # Layout base (header + footer)
│   ├── post.html        # Layout para textos do blog
│   └── obra.html        # Layout para obras individuais
├── _obras/              # Coleção de obras (um .md por obra)
├── _posts/              # Posts do blog (YYYY-MM-DD-titulo.md)
├── pages/               # Páginas estáticas
│   ├── obras.md
│   ├── oficinas.md
│   ├── textos.md
│   ├── sobre.md
│   └── contato.md
├── assets/
│   ├── css/main.css     # Todo o CSS em um arquivo
│   └── img/             # Imagens (obras em assets/img/obras/)
└── index.md             # Homepage
```

## Rodar localmente

```bash
bundle install
bundle exec jekyll serve
```

Abre em `http://localhost:4000`.

## Adicionar uma obra

Crie um arquivo em `_obras/nome-da-obra.md`:

```yaml
---
layout: obra
title: "Nome da Obra"
tecnica: "Xilogravura"
ano: 2024
dimensoes: "30 × 40 cm"
serie: "Nome da série"
imagem: "/assets/img/obras/nome-do-arquivo.jpg"
disponivel: true
---

Texto descritivo opcional.
```

## Adicionar um post

Crie um arquivo em `_posts/YYYY-MM-DD-titulo-do-post.md`:

```yaml
---
layout: post
title: "Título do post"
subtitle: "Subtítulo opcional"
category: "crítica"
date: 2024-01-15
---

Conteúdo em Markdown.
```

## Formulário de contato

O formulário usa Formspree. Crie uma conta em formspree.io, crie um formulário e substitua `YOUR_FORM_ID` em `pages/contato.md`.

## Deploy

Push para o branch `main`. O GitHub Pages gera o site automaticamente.
