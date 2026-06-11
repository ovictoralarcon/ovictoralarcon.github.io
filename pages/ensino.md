---
layout: default
title: Ensino
description: Aulas e oficinas de pintura com Victor Alarcon — gouache, têmpera de ovo.
permalink: /ensino/
---

<section class="page-hero">
  <div class="container">
    <div class="page-hero__eyebrow">
      <span class="label">Ensino</span>
    </div>
    <h1 class="page-hero__titulo">Ensino</h1>
    <p class="page-hero__subtitulo">Aulas individuais e oficinas em grupo. Técnica tradicional, materiais reais, sem conversa.</p>
  </div>
</section>

<section class="cursos-lista container">
  {% assign cursos = site.cursos | where: "ativo", true | sort: "ordem" %}
  {% for curso in cursos %}
  <a href="{{ curso.url | relative_url }}" class="curso-item">
    <div class="curso-item__info">
      <span class="label">{{ curso.formato | upcase }}</span>
      <h2 class="curso-item__titulo">{{ curso.title }}</h2>
      {% if curso.descricao %}<p class="curso-item__desc">{{ curso.descricao }}</p>{% endif %}
    </div>
    <div class="curso-item__meta">
      {% if curso.preco %}<span class="curso-item__preco">{{ curso.preco }}</span>{% endif %}
      <span class="curso-item__seta">→</span>
    </div>
  </a>
  {% endfor %}
</section>
