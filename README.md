# Selenium Hybrid Framework - OrangeHRM

This project is a **Hybrid Test Automation Framework** built using **Selenium WebDriver**, **Pytest**, and **Python**. It automates test cases for the OrangeHRM application, supporting data-driven testing, page object model, logging, and HTML reporting.

---

## 🧰 Tech Stack

- **Language**: Python
- **Automation**: Selenium WebDriver
- **Testing Framework**: Pytest
- **Reporting**: pytest-html
- **Logging**:  built-in logging
- **Data Source**: Excel (via `openpyxl`)
- **Design Pattern**: Page Object Model (POM)

---

## 📁 Project Structure

```
selenium_hybrid_framework/
│
├── configurations/            # Configuration files (if any)
│   └── config.ini
├── logs/                      # Logs
│   └── automation.log
│
├── page_objects/              # Page Object Model classes
│   ├── __init__.py
│   ├── add_employee.py
│   ├── home_page.py
│   ├── login_page.py
│   └── search_employee.py
│
├── reports/                   # Test reports
│   ├── assets/
│   └── reports.html
│
├── screenshot/                # Screenshots on test failure
│   ├── test_homePageTitle.png
│   └── test_login.png
│
├── test_cases/                # Test scripts
│   ├── __init__.py
│   ├── conftest.py
│   ├── pytest.ini
│   ├── test_addemployee.py
│   ├── test_login.py
│   ├── test_login_ddt.py
│   ├── test_searchemployee_by_id.py
│   └── test_searchemployee_by_name.py
│
├── test_data/                 # Test data files
│   └── login_data.xlsx
│
├── utilities/                 # Utility/helper methods
│   ├── __init__.py
│   ├── customLogger.py
│   ├── read_properties.py
│   └── xlutils.py
│
└── run.bat                    # Batch file to run tests
```

---

## ✅ Features

- **Page Object Model (POM)** for maintainability
- **Data-driven testing** using Excel
- **HTML reports** via `pytest-html`
- **Logging and Screenshots** on failure
- Supports **modular and scalable** test case design

---

## 🚀 How to Run Tests

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd selenium_hybrid_framework
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Tests with HTML Report

```bash
pytest --html=reports/reports.html --browser=chrome
```

> Make sure to update browser settings if using a different driver.

---

## 🧪 Test Modules

- `test_login.py` — Valid login test
- `test_login_ddt.py` — Data-driven login test
- `test_addemployee.py` — Add employee functionality
- `test_searchemployee_by_id.py` — Search employee by ID
- `test_searchemployee_by_name.py` — Search employee by name

---

## 📊 Test Data

Located in: `test_data/login_data.xlsx`

Used for data-driven tests like login DDT.

---

## 📷 Screenshots

Screenshots of failed test steps are saved to the `screenshot/` directory.

---

## 📝 Reports

After test execution, a detailed HTML report is generated in `reports/reports.html`.

---

## 🔒 Logs

Execution logs are written to `logs/automation.log`.

---

## 🤝 Contributions

Feel free to fork the repo and submit PRs for improvements or additional test cases.

---

## 🧑‍💻 Author

**Aniket Sonar**

---
