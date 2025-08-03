# demo-qa-pytest-automation

A Python-based demo project showcasing QA test automation using **Pytest**. Designed for beginners to explore test design, execution, and result reporting.

---

## Project Overview

This repository contains a sample QA automation test suite using Pytest. It is intended for practicing:

* Manual-to-automated testing transition
* Structuring test cases and fixtures
* Basic assertions and test organization

---

## Technologies

* Python (>=3.x)
* Pytest testing framework
* Optional: pytest-xdist for parallel test execution
* Optional: pytest-html or allure-pytest for test reporting

---

## Setup & Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/cinarkahraman/demo-qa-pytest-automation.git
   cd demo-qa-pytest-automation
   ```

2. **Create virtual environment & install dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate  # (Windows: venv\Scripts\activate)
   pip install -r requirements.txt
   ```

3. **Install optional plugins** (if not included already)

   ```bash
   pip install pytest-xdist pytest-html
   # or pip install allure-pytest
   ```

---

## Running Tests

* Default test run:

  ```bash
  pytest
  ```
* Verbose run:

  ```bash
  pytest -v
  ```
* Run in parallel (e.g., 3 workers):

  ```bash
  pytest -n 3
  ```
* Generate HTML report:

  ```bash
  pytest --html=report.html
  ```
* Generate Allure report:

  ```bash
  pytest --alluredir=allure-results
  allure serve allure-results
  ```

---

## Directory Structure

```
demo-qa-pytest-automation/
├── tests/
│   ├── test_example.py
│   └── ...
├── requirements.txt
├── conftest.py (if applicable)
└── README.md
```

---
