---
layout: default
title: Obras
description: Portfólio de Victor Alarcon — xilogravura, têmpera de ovo, gouache, escultura.
permalink: /obras/
destaques:
  - gatos-com-acesso-a-rua-vivem-menos
  - mar-salgado
  - comer-e-dormir-como-um-porco
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

{%- comment -%}
  Ordem: primeiro as obras listadas em destaques (na ordem da lista),
  depois todas as outras, da mais recente para a mais antiga.
{%- endcomment -%}
{% assign destacadas = "" | split: "" %}
{% for slug in page.destaques %}
  {% assign d = site.obras | where: "slug", slug | first %}
  {% if d %}{% assign destacadas = destacadas | push: d %}{% endif %}
{% endfor %}

{% assign por_ano = site.obras | sort: 'ano' | reverse %}
{% assign restantes = "" | split: "" %}
{% for o in por_ano %}
  {% unless page.destaques contains o.slug %}
    {% assign restantes = restantes | push: o %}
  {% endunless %}
{% endfor %}

{% assign obras = destacadas | concat: restantes %}

<section class="obras-grid container">
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