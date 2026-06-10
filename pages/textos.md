---
layout: default
title: Textos
description: Textos de Victor Alarcon sobre arte, técnica e crítica.
permalink: /textos/
---

<section class="page-hero">
  <div class="container">
    <div class="page-hero__eyebrow">
      <span class="label">Escrita</span>
    </div>
    <h1 class="page-hero__titulo">Textos</h1>
    <p class="page-hero__subtitulo">Crítica, teoria e técnica. Também no <a href="https://victoralarcon.substack.com/" target="_blank" rel="noopener" style="border-bottom: 1px solid currentColor;">Substack</a>.</p>
  </div>
</section>

<section class="textos-lista container">
  {% assign posts = site.posts %}
  {% if posts.size > 0 %}
    {% for post in posts %}
    <a href="{{ post.url | relative_url }}" class="post-item">
      <span class="post-item__data">{{ post.date | date: "%d %b %Y" }}</span>
      <h2 class="post-item__titulo">{{ post.title }}</h2>
      {% if post.excerpt %}
      <p class="post-item__excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
      {% endif %}
    </a>
    {% endfor %}
  {% else %}
    <p style="color: var(--cor-secundario); font-size: var(--escala-sm); padding-block: var(--espaco-md);">Textos em breve.</p>
  {% endif %}
</section>
