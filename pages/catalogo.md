---
layout: default
title: Catálogo
description: Obras disponíveis de Victor Alarcon.
permalink: /catalogo/
---

<section class="page-hero">
  <div class="container">
    <div class="page-hero__eyebrow">
      <span class="label">Obras disponíveis</span>
    </div>
    <h1 class="page-hero__titulo">Catálogo</h1>
<p class="page-hero__subtitulo">Para consultar condições de pagamento e envio, <a href="https://wa.me/55119XXXXXXXX" target="_blank" rel="noopener" style="border-bottom: 1px solid currentColor;">me manda uma mensagem</a>.</p>
  </div>
</section>

<section class="catalogo-lista container">
  {% assign obras = site.obras | sort: 'preco' | reverse %}
  {% for obra in obras %}
    {% assign s = obra.status | downcase %}
    {% if s == "disponível" or s == "disponivel" %}
    <a href="{{ obra.url | relative_url }}" class="catalogo-item">
      <div class="catalogo-item__imagem">
        {% if obra.imagem %}
          <img src="{{ obra.imagem }}" alt="{{ obra.titulo | default: obra.title }}" loading="lazy">
        {% endif %}
      </div>
      <div class="catalogo-item__info">
        <h2 class="catalogo-item__titulo">{{ obra.titulo | default: obra.title }}</h2>
        <p class="catalogo-item__tecnica">
          {{ obra.tecnica }}{% if obra.suporte and obra.suporte != "" %} sobre {{ obra.suporte }}{% endif %}
        </p>
        {% if obra.dimensoes %}<p class="catalogo-item__dimensoes">{{ obra.dimensoes }}</p>{% endif %}
        {% if obra.ano %}<p class="catalogo-item__ano">{{ obra.ano }}</p>{% endif %}
      </div>
      {% if obra.preco %}
      <div class="catalogo-item__preco">R$ {{ obra.preco }}</div>
      {% endif %}
    </a>
    {% endif %}
  {% endfor %}
</section>
