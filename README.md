# 🗓️ Date Calc Flask

![Déploiement Azure](https://github.com/pom2terre/date_tools/actions/workflows/azure-deploy.yml/badge.svg)
![Version](https://img.shields.io/github/v/tag/pom2terre/date_tools?label=version&sort=semver)
![Azure](https://img.shields.io/badge/Azure-Deployed-blue?logo=microsoft-azure)
![Licence](https://img.shields.io/github/license/pom2terre/date_tools)

Calculateur de dates en Flask : durée entre deux dates, jour de la semaine, et plus.  
Déployé automatiquement sur Azure Web Apps via GitHub Actions.

---

## 🚀 Aperçu

🧮 **Fonctionnalités** :
- Calcul de durée entre 2 dates (en jours, semaines, mois, années…)
- Détection du jour de la semaine
- Support des calendriers dynamiques (Flatpickr)
- Interface moderne responsive (avec Tailwind CSS)
- Mode debug/détection d’environnement visible dans le footer
- Déploiement continu avec version dynamique (`APP_VERSION`)

🔗 **Démo** : [https://my-python-app123.azurewebsites.net](https://my-python-app123.azurewebsites.net)  
📦 [Voir les versions](https://github.com/pom2terre/date-calc-flask/releases)

---

## 🧰 Stack technique

- **Python 3.11** + Flask
- **HTML + Jinja2**
- **Tailwind CSS**
- **Flatpickr** pour la sélection de dates
- **Azure App Service** pour l'hébergement
- **GitHub Actions** pour le CI/CD

---

## 🛠️ Déploiement automatique

Chaque `git push` sur `main` :

1. 📦 Crée une archive `deploy.zip`
2. 🏷️ Génére un tag Git (ex: `v2025.05.03.2102`)
3. 📤 Déploie l'app vers Azure via `az webapp deploy`
4. 🔄 Met à jour la variable `APP_VERSION`
5. 🧪 Lance des tests sur `/`, `/hello`, `/calculate-duration`…
6. 📋 Publie un résumé Markdown en artefact
7. 🗞️ Crée une GitHub Release à partir du tag

---

## 📂 Structure du projet

<pre>├── main.py # Entrée Flask
├── wsgi.py # Serveur WSGI
├── templates/
│ ├── _layout.html # Layout global
│ ├── _footer.html # Footer dynamique
│ ├── calculate_duration.html
│ └── day_of_week.html
├── static/ # Fichiers JS/CSS (si présents)
├── requirements.txt
└── azure-deploy.yml # GitHub Actions
</pre>

---

## 👤 Auteur

Développé par [@pom2terre](https://github.com/pom2terre)  
📧 Contact : pomme.deterre9@gmail.com

---

## 📝 Licence

Ce projet est distribué sous la licence [MIT](LICENSE).
