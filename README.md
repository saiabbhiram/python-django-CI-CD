# Django Application with Jenkins Freestyle Project Integration

A clean, production-ready starter Django application configured for CI/CD integration with a **Jenkins Freestyle Project**.

---

## 📁 Project Structure

```text
.
├── demo_app/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py             # Item model
│   ├── templates/demo_app/
│   │   └── index.html        # UI homepage
│   ├── tests.py              # Unit tests (Views, Health check, Models)
│   ├── urls.py
│   └── views.py              # Index and Health check API
├── myproject/
│   ├── asgi.py
│   ├── settings.py           # Core settings
│   ├── urls.py
│   └── wsgi.py
├── reports/                  # Generated in CI (JUnit XML test reports)
├── .gitignore
├── jenkins_build.bat         # CI script for Windows agents
├── jenkins_build.sh          # CI script for Linux/macOS agents
├── manage.py
├── pytest.ini                # Pytest configuration
├── README.md
└── requirements.txt
```

---

## 🚀 Running Locally

1. **Create and activate virtual environment:**
   ```bash
   # Linux / macOS
   python3 -m venv venv
   source venv/bin/activate

   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Run unit tests:**
   ```bash
   pytest
   # or with Django test runner:
   python manage.py test
   ```

5. **Start development server:**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` for the UI and `http://127.0.0.1:8000/health/` for the health check.
