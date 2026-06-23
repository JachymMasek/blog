#Začal jsem dělat design
#Zeptal jsem see claudea na vylepšení mazání a upravování příspěvků ale došly tickety
#To je vše myslim ig lmao


"""
{% extends 'base.html' %}

{% block title %}O nás – MySite{% endblock %}

{% block extra_head %}
<style>
  .about-grid {
    padding: 5rem 3rem;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 5rem;
    align-items: start;
    border-bottom: 1px solid rgba(15,14,12,.1);
  }
  @media (max-width: 720px) { .about-grid { grid-template-columns: 1fr; gap: 2.5rem; } }

  .about-grid h1 {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(2.5rem, 5vw, 4rem);
    line-height: 1.08; letter-spacing: -.03em;
  }
  .about-grid h1 em { color: var(--accent); font-style: italic; }

  .about-text p {
    color: var(--muted); line-height: 1.8; font-size: 1rem; margin-bottom: 1.2rem;
  }
  .about-text p:last-child { margin-bottom: 0; }

  .divider {
    width: 40px; height: 2px;
    background: var(--accent);
    margin: 2rem 0;
  }

  .team {
    padding: 4rem 3rem;
    border-bottom: 1px solid rgba(15,14,12,.1);
  }
  .team-label {
    font-size: .78rem; letter-spacing: .14em; text-transform: uppercase;
    color: var(--muted); margin-bottom: 2.5rem;
  }
  .team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 2rem;
  }
  .member { border-top: 1.5px solid var(--ink); padding-top: 1rem; }
  .member-avatar {
    width: 64px; height: 64px; border-radius: 50%;
    background: var(--ink);
    display: flex; align-items: center; justify-content: center;
    color: var(--paper);
    font-family: 'DM Serif Display', serif;
    font-size: 1.4rem;
    margin-bottom: 1rem;
  }
  .member h3 { font-size: .95rem; font-weight: 500; }
  .member span { font-size: .8rem; color: var(--muted); }

  .values {
    padding: 4rem 3rem;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 2rem;
  }
  .value-item { padding: 2rem; border: 1px solid rgba(15,14,12,.12); }
  .value-item h3 {
    font-family: 'DM Serif Display', serif;
    font-size: 1.3rem; margin-bottom: .6rem;
  }
  .value-item p { font-size: .88rem; color: var(--muted); line-height: 1.65; }
</style>
{% endblock %}

{% block content %}
<div class="about-grid">
  <div class="fade-up">
    <h1>Kdo <em>jsme</em><br>a co děláme.</h1>
    <div class="divider"></div>
    <a href="{% url 'contact' %}" style="font-size:.88rem;font-weight:500;color:var(--accent);text-decoration:none;letter-spacing:.06em;text-transform:uppercase;">Napište nám →</a>
  </div>
  <div class="about-text fade-up-2">
    <p>Jsme malý tým vývojářů a designérů, kteří věří, že web může být zároveň krásný i funkční. Pracujeme s Django, protože nám dává svobodu soustředit se na to, co je důležité — uživatele.</p>
    <p>Tento projekt vznikl jako ukázka toho, jak jednoduše lze postavit vícestránkový web s čistou navigací, sdílenou šablonou a bez zbytečné složitosti.</p>
    <p>Proklikejte se, prozkoumejte, a neváhejte nás kontaktovat, pokud máte zájem o spolupráci.</p>
  </div>
</div>

<div class="team">
  <p class="team-label">Náš tým</p>
  <div class="team-grid">
    <div class="member fade-up">
      <div class="member-avatar">AK</div>
      <h3>Adam Kovář</h3>
      <span>Backend Developer</span>
    </div>
    <div class="member fade-up-2">
      <div class="member-avatar">MN</div>
      <h3>Monika Novák</h3>
      <span>UI / UX Designer</span>
    </div>
    <div class="member fade-up-3">
      <div class="member-avatar">JP</div>
      <h3>Jan Procházka</h3>
      <span>Frontend Developer</span>
    </div>
  </div>
</div>

<div class="values">
  <div class="value-item fade-up">
    <h3>Poctivost</h3>
    <p>Kód píšeme tak, abychom za něj nebyli ráno červení. Žádné zkratky, žádné hacky bez komentáře.</p>
  </div>
  <div class="value-item fade-up-2">
    <h3>Jednoduchost</h3>
    <p>Nejlepší řešení je to nejjednodušší, které splňuje požadavky. Django a čisté HTML stačí.</p>
  </div>
  <div class="value-item fade-up-3">
    <h3>Otevřenost</h3>
    <p>Sdílíme znalosti, přijímáme zpětnou vazbu a věříme, že spolu dotáhneme věci dál.</p>
  </div>
</div>
{% endblock %}

"""