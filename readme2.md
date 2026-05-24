<br />
<div align="center">

  <h1 align="center">Django Blog App</h1>

  <p align="center">
    A hand-crafted blogging application powered by Django 6.0.5
    <br />
  </p>

  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=yellow" alt="Python Badge" />
    <img src="https://img.shields.io/badge/Django-6.0.5-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django Badge" />
    <img src="https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite Badge" />
    <img src="https://img.shields.io/badge/CSS3-Custom-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3 Badge" />
    <img src="https://img.shields.io/badge/Render-Ready-46E3B7?style=for-the-badge&logo=render&logoColor=white" alt="Render Badge" />
  </p>
</div>

---

## Table of Contents

*   [Key Features](#key-features)
*   [Technology Stack](#technology-stack)
*   [Files](#files)
*   [Getting Started](#getting-started)
*   [Security & Environment Settings](#security--environment-settings)

---


## Key Features

*   **Authentication System**: Secure accounts module supporting fully functional signup, user login, and logout. No authorisation yet unfortunately.
*   **CRUD Operations**: Registered users can create new posts, read detailed views, edit, or delete existing posts.
*   **Deployment Configs**: Deployment setup utilizing `gunicorn` and `whitenoise` for compressed & cached static asset delivery.
*   **Developer Superuser Script**: An automated script `createsuperuser.py` to seed administrators using environment variables or local test credentials, since free version of render doesn't support shell I had to use this script to inject admin information during build process. 

---


## Technology Stack

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.14 | Core Backend Language |
| **Web Framework** | Django 6.0.5 | MVC Web Application Framework |
| **Database** | SQLite 3 | Lightweight relational database storage |
| **Styling** | Vanilla CSS3 | Styling |
| **Assets Manager** | WhiteNoise | Compressed static assets serving |
| **WSGI Server** | Gunicorn | Production-ready HTTP application server |


---

## Files

Here is a visual map of the hand-crafted repository architecture:

```text
blog-app/
│
├── django_project/          # Core Project Configurations
│   ├── settings.py          # Static files, apps, databases, and middleware
│   ├── urls.py              # Root routing mapping accounts, blog, and admin
│   └── wsgi.py / asgi.py    # Production server gateways
│
├── blog/                    # Blog App Engine
│   ├── models.py            # Post entity definition (Title, Body, Author)
│   ├── views.py             # Class-Based Views (List, Detail, Create, Update, Delete)
│   ├── urls.py              # Pattern mapping for routing blog views
│   └── tests.py             # Comprehensive test suites
│
├── accounts/                # Authentication Module
│   ├── views.py             # SignUpView utilizing UserCreationForm
│   └── urls.py              # User authentication paths
│
├── templates/               # UI HTML Layouts
│   ├── base.html            # Main base for the webpage
│   ├── home.html            # Home page containing blog feed
│   ├── registration/        # Signup and login pages
│   └── post_*.html          # Sub-templates for CRUD interactions
│
├── static/                  # Static assets
│   └── css/                 # base.css (the only AI part 😭)
│
├── requirements.txt         # Core dependencies
└── createsuperuser.py       # Admin automated script
```

---

## Getting Started

Follow these steps to run the application locally on your computer.

Follow [this](https://www.notion.so/Deployment-CheckList-for-Render-365e2135265480ceafbaf96bb1d11768?source=copy_link) for my deployment checklist for [Render](https://render.com/).

### Prerequisites

*   Python 3.14 or higher installed.
*   pip (Python Package Installer).

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/farzanfaisal77/blog-app.git
   cd blog-app
   ```

2. **Set up a Virtual Environment**:
   ```bash
   # Create environment
   python -m venv .venv

   # Activate environment (Linux/macOS)
   source .venv/bin/activate

   # Activate environment (Windows)
   .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Make superuser or run createsuperuser.py script to create a superuser**:

   ```bash
   python manage.py createsuperuser
   ```
 and enter your own details 

 OR

   ```bash
   python createsuperuser.py
   ```
   *Default login details created: Username: **farzan** | Password: **admin123***

6. **Start the Dev Server**:
   ```bash
   python manage.py runserver
   ```
   Open your browser and navigate to `http://127.0.0.1:8000/` to explore the interface

---

## Security & Environment Settings

For security and deployment purposes, please note the following configuration values inside `django_project/settings.py`:
*   `DEBUG`: Configured to `True` for ease of local development.
*   `ALLOWED_HOSTS`: Set up to support Render hosts (`.onrender.com`), `localhost`, and loopback addresses.
*   `STORAGES`: Integrated with `whitenoise.storage.CompressedManifestStaticFilesStorage` to handle high-performance asset minification and caching out-of-the-box.

---


<div align="center">
  <sub>Built with ❤️ and 🚀 by <a href="https://github.com/farzanfaisal77">Farzan Faisal</a> as part of a Python Django Learning Journey.</sub>
</div>