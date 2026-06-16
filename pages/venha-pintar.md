---
layout: default
title: Venha Pintar
description: Aulas e mentorias de pintura com Victor Alarcon.
permalink: /venha-pintar/
---

<section class="page-hero">
  <div class="container">
    <div class="page-hero__eyebrow">
      <span class="label">Venha Pintar</span>
    </div>
    <h1 class="page-hero__titulo">Venha Pintar</h1>
  </div>
</section>

<section class="cursos-lista container">
  {% assign cursos = site.cursos | where: "ativo", true | sort: "ordem" %}
  {% for curso in cursos %}
  <a href="{{ curso.url | relative_url }}" class="curso-item">
    <h2 class="curso-item__titulo">{{ curso.title }}</h2>
    <span class="curso-item__seta">→</span>
  </a>
  {% endfor %}
</section>
