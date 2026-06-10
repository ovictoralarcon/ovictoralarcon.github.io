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
  </div>
</section>

<section class="obras-grid container">
  {% assign obras = site.obras | sort: 'ano' | reverse %}
  {% if obras.size > 0 %}
    {% for obra in obras %}
      {% assign primeira_imagem = obra.content | split: '![' | last | split: '](' | last | split: ')' | first %}
      <a href="{{ obra.url | relative_url }}" class="obra-card">
        <div class="obra-card__imagem">
          {% if primeira_imagem contains 'http' %}
            <img src="{{ primeira_imagem }}" alt="{{ obra.titulo }}" loading="lazy">
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
