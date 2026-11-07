# SANGAM G SAJJAN
**Software Development Engineer in Test (SDET) | Python • Distributed Systems • TestOps**  
Bengaluru, India *(Open to Remote: US / EU / APAC)* | +91 7483138916 | sangamgsajjan0987@gmail.com  
[GitHub Profile](https://github.com/sangam-sajjan) | [LinkedIn](https://linkedin.com/in/sangam-sajjan) | [Live Allure Portfolio](https://sangam-sajjan.github.io)

---

### PROFESSIONAL SUMMARY
High-leverage **Software Development Engineer in Test (SDET)** specializing in Python-based test architectures, asynchronous microservices validation, and distributed CI/CD pipeline optimization. Proven impact reducing regression cycle times from **3.5 hours to 18 minutes (88% reduction)** via GitHub Actions matrix sharding and hermetic state re-use (`storage_state`). Built end-to-end validation engines spanning modern Web UI, asynchronous REST/HTTPX APIs, and relational database reconciliation with strict Pydantic v2 contract enforcement.

---

### TECHNICAL SKILLS
- **Languages & Core:** Python 3.12+ (Asyncio, OOP, Concurrency, Type Hints), SQL (PostgreSQL, MySQL), Bash / Shell, JSON, YAML
- **Test Frameworks & Architecture:** Pytest, Playwright (Sync/Async), Page Component Model (PCM), Requests, HTTPX, pytest-xdist, pytest-mock
- **Data & Contract Integrity:** Pydantic v2, JSONSchema, Source-to-Target (S2T) Data Reconciliation, Multi-table Joins & Aggregations, Redis, RabbitMQ
- **CI/CD, Cloud & Observability:** Docker, Docker Compose, GitHub Actions (Matrix Sharding, Caching), Linux CLI, Allure Telemetry, Playwright Tracing (`trace.zip`), Ruff, Mypy Strict Mode

---

### PROFESSIONAL EXPERIENCE

#### **SDET / QA Automation Engineer** | Core Engineering Platform *(Sep 2024 – Present | Bengaluru, India / Remote)*
*Focus: Microservices API Reliability, Web UI Automation, Database Reconciliation & Distributed CI/CD*

- **CI/CD Sharding & Pipeline Acceleration:** Architected a distributed regression engine across 400+ microservice and UI test suites using **Pytest, Playwright, and GitHub Actions matrix sharding**, compressing regression turnaround from **3.5 hours to 18 minutes (88% reduction)** while maintaining a **<1.5% flakiness SLA**.
- **Hermetic State Reuse & UI Speedup:** Spearheaded end-to-end automation of critical web workflows in **Playwright Python** using user-facing locators and `browser_context.storage_state()`, eliminating redundant authentication handshakes across 100+ flows and reducing test execution overhead by **65%**.
- **Microservices Contract Enforcement:** Designed an asynchronous API testing framework leveraging **HTTPX and Pydantic v2** to validate strict schema boundaries, dynamic OAuth2/JWT token lifecycles, and rate-limiting across **50+ microservices endpoints**, catching breaking payload mutations prior to deployment.
- **Deterministic Mocking & Quality Gates:** Eliminated third-party flakiness by implementing **Playwright route interception and HAR replay mocking**, achieving deterministic execution for simulated 5xx outages and latency spikes; integrated strict CI quality gates via **Ruff linting, Mypy strict mode, and Allure telemetry**.

---

### SELECTED ENGINEERING PROJECTS

#### **1. Playwright Python Distributed Test Engine** | *Python 3.12, Playwright, Pytest, Pydantic, Allure, Docker, CI/CD*  
*[GitHub Repository: playwright-python-enterprise-engine](https://github.com/sangam-sajjan/playwright-python-enterprise-engine) | [Live Allure Demo](https://sangam-sajjan.github.io/playwright-report)*
- Architected a containerized Web UI test platform executing 120+ end-to-end user journeys across Chromium, Firefox, and WebKit using the **Page Component Model (PCM)** to isolate reusable navigation, modal, and data-grid widgets.
- Implemented hermetic network isolation using Playwright route interception, simulating 5xx outages and edge-case latencies deterministically without staging backend dependencies.
- Integrated automated trace diagnostics (`trace.zip`), visual snapshot masking, and parallel sharding via `pytest-xdist`, compressing suite execution time to **under 4 minutes** in GitHub Actions CI.

#### **2. Microservices API & Data Integrity Reconciliation Engine** | *Python, Pytest, HTTPX, PostgreSQL, Pydantic v2, SQLAlchemy, Docker*  
*[GitHub Repository: api-reliability-data-validator](https://github.com/sangam-sajjan/api-reliability-data-validator)*
- Engineered an asynchronous integration testing engine validating end-to-end multi-service transactions across Order, Inventory, and Payment services using **HTTPX and Pytest**.
- Built automated **Source-to-Target (S2T) database reconciliation** scripts executing multi-table joins and window aggregations, validating data consistency and transactional persistence across 15+ relational tables.
- Implemented multi-tenant authorization boundary testing and token expiration validation, detecting 25+ schema drifts and boundary vulnerabilities prior to staging release.

---

### EDUCATION
**Bachelor of Engineering (B.E.), Computer Science** | Visvesvaraya Technological University (VTU) | Bengaluru, India *(Graduated: May 2024)*
