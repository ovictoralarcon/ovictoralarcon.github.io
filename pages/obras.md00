---
layout: default
title: Obras
description: Portfólio de Victor Alarcon — xilogravura, têmpera de ovo, gouache, escultura.
permalink: /obras/
---

<section class="page-hero">
  <div class="container">
    <div class="page-hero__eyebrow">
      <span class="label">Portfólio</span>
    </div>
    <h1 class="page-hero__titulo">Obras</h1>
    <p class="page-hero__subtitulo"><a href="{{ '/catalogo/' | relative_url }}" style="border-bottom: 1px solid currentColor;">Ver obras disponíveis →</a></p>
    <a href="{{ '/assets/pdf/portfolio.pdf' | relative_url }}" target="_blank">Portfólio PDF →</a>
  </div>
</section>

<section class="obras-grid container">
  {% assign obras = site.obras | sort: 'ano' | reverse %}
  {% if obras.size > 0 %}
    {% for obra in obras %}
    <a href="{{ obra.url | relative_url }}" class="obra-card">
      <div class="obra-card__imagem">
        {% if obra.imagem %}
          <img src="{{ obra.imagem }}" alt="{{ obra.titulo | default: obra.title }}" loading="lazy">
        {% endif %}
      </div>
      <div class="obra-card__meta">
        {% if obra.tecnica %}<span class="label">{{ obra.tecnica | upcase }}</span>{% endif %}
        {% if obra.ano %}<span class="label">{{ obra.ano }}</span>{% endif %}
      </div>
      <h2 class="obra-card__titulo">{{ obra.titulo | default: obra.title }}</h2>
      {% if obra.dimensoes %}<p class="obra-card__info">{{ obra.dimensoes }}</p>{% endif %}
    </a>
    {% endfor %}
  {% else %}
    <p style="color: var(--cor-secundario); font-size: var(--escala-sm);">Obras em breve.</p>
  {% endif %}
</section>
