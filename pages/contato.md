---
layout: default
title: Contato
description: Entre em contato com Victor Alarcon.
permalink: /contato/
---

<section class="page-hero">
  <div class="container">
    <div class="page-hero__eyebrow">
      <span class="label">Contato</span>
    </div>
    <h1 class="page-hero__titulo">Fale comigo</h1>
  </div>
</section>

<section class="contato-corpo">
  <div class="container">
    <div class="contato-grid">

      <div class="contato-info">
        <p>Para perguntas sobre obras, oficinas ou qualquer outro assunto. Respondo por aqui ou por e-mail.</p>
      </div>

      <!-- Formulário via Formspree — substitua YOUR_FORM_ID pelo seu ID -->
      <form class="contato-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">

        <div class="form-field">
          <label for="nome">Nome</label>
          <input type="text" id="nome" name="nome" required>
        </div>

        <div class="form-field">
          <label for="email">E-mail</label>
          <input type="email" id="email" name="email" required>
        </div>

        <div class="form-field">
          <label for="assunto">Assunto</label>
          <select id="assunto" name="assunto">
            <option value="">Selecione</option>
            <option value="oficinas">Oficinas / mentoria</option>
            <option value="obras">Obras / aquisiçao</option>
            <option value="imprensa">Imprensa / curadoria</option>
            <option value="outro">Outro</option>
          </select>
        </div>

        <div class="form-field">
          <label for="mensagem">Mensagem</label>
          <textarea id="mensagem" name="mensagem" rows="5" required></textarea>
        </div>

        <div>
          <button type="submit" class="btn">Enviar mensagem</button>
        </div>

      </form>

    </div>
  </div>
</section>
