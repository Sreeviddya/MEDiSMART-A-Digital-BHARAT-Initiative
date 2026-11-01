# 📦 Archive & Legacy File Documentation

This document provides a detailed breakdown of all legacy, backup, prototype, and oddly named files moved to the `archive/` directory during the repository refactoring.

---

## 📑 File Inventory & Details

### 1. `import streamlit as st.py`
* **Original Purpose**: Ambulance Tracking system.
* **What It Actually Does**: Contains a full 699-line Streamlit application for GPS ambulance tracking, distance calculation using `geopy.distance.geodesic`, Folium map rendering, priority tagging (Critical/High/Medium), and driver dispatch logic.
* **Why It Has This Name**: When developing in VS Code or another editor, a new file was likely created and mistakenly named after the first line of code (`import streamlit as st`) instead of `ambulance_tracking.py`.
* **Active Replacement**: [`modules/ambulance_tracking.py`](../modules/ambulance_tracking.py).
* **Archive Reason**: Complete duplicate of the ambulance tracking module with an accidental filename.

---

### 2. `medico streamlit web.py`
* **Original Purpose**: Early standalone disease prediction prototype.
* **What It Actually Does**: A 130-line standalone Streamlit script that loads the Support Vector Classifier model (`svc.pkl`) using `pickle.load(open("svc.pkl", "rb"))`. It maps 96 user-selected symptoms to a 132-length one-hot encoded vector to predict one of 54 diseases.
* **Why It Has This Name**: Named as an ad-hoc test web script ("medico streamlit web") during early proof-of-concept testing.
* **Active Replacement**: [`modules/smart_doctor.py`](../modules/smart_doctor.py).
* **Archive Reason**: Deprecated standalone prototype. Its core prediction logic was incorporated and expanded into `smart_doctor.py`.

---

### 3. `medics.py`
* **Original Purpose**: Multi-model diagnostic testing workbench.
* **What It Actually Does**: A 396-line prototype script that attempts to load **6 different machine learning models simultaneously** at startup:
  ```python
  model = pickle.load(open("svc.pkl", "rb"))
  bp_model = pickle.load(open("bp_model.pkl", "rb"))
  lung_model = pickle.load(open("lung_cancer_model.pkl", "rb"))
  heart_model = pickle.load(open("heart_disease_model.pkl", "rb"))
  diabetes_model = pickle.load(open("diabetes_model.pkl", "rb"))
  parkinsons_model = pickle.load(open("parkinsons_model.pkl", "rb"))
  ```
  It contains expanded dictionaries of 100+ symptoms and diseases.
* **Why It Has This Name**: Short working title for a medical diagnosis experiment.
* **Active Replacement**: Individual modularized diagnosis pages under [`modules/`](../modules/):
  - `smart_doctor.py`
  - `bp_diagnosis.py`
  - `diabetes.py`
  - `heart_disease.py`
  - `lung_cancer.py`
  - `parkinsons.py`
* **Archive Reason**: Monolithic test file replaced by modular, per-condition pages.

---

### 4. `python.py`
* **Original Purpose**: National eHospital Implementation Dashboard experiment.
* **What It Actually Does**: A 155-line Streamlit script embedding a custom HTML, jQuery DataTables, and Highcharts Indian map (`countries/in/in-all.js`) to display hospital implementation metrics (Active, Onboarding, Planned) across Indian states.
* **Why It Has This Name**: Mistakenly named `python.py` when saving an experimental Python script.
* **Active Replacement**: [`modules/dashboard.py`](../modules/dashboard.py) and [`modules/hospital_directory.py`](../modules/hospital_directory.py).
* **Archive Reason**: Standalone prototype embedding raw HTML/JS that was not connected to the main application navigation.

---

### 5. `app1.py` & `app2.py`
* **Original Purpose**: Early version backups of the main application.
* **What They Actually Do**:
  * `app1.py` (574 lines): Intermediate version of `app.py`. Contains navbar and sidebar routing for 8 primary pages, but lacks the 12 facility cards on the home page.
  * `app2.py` (544 lines): Even earlier iteration with basic styling and fewer routed modules.
* **Why They Have These Names**: Standard manual version-number backups created before making significant changes (`app` $\rightarrow$ `app1` $\rightarrow$ `app2`).
* **Active Replacement**: [`app.py`](../app.py) (The official, fully integrated entry point with multilingual support and 25+ connected pages).
* **Archive Reason**: Outdated milestone backups replaced by the production `app.py`.

---

### 6. `full_app.py`
* **Original Purpose**: Experimental draft combining all prospective features.
* **What It Actually Does**: A 690-line script that attempted to merge all pages into one router. However, it references unbuilt placeholder functions (e.g., `emergency_alerts`, `pharmacy_locator`, `laboratory_reports`) that caused broken links.
* **Why It Has This Name**: Created as an experiment to assemble the "full" application in one file.
* **Active Replacement**: [`app.py`](../app.py) (Clean, verified routing dispatch).
* **Archive Reason**: Unstable monolithic draft superseded by the refined `app.py`.

---

### 7. `appointment_reminder.py` (Singular)
* **Original Purpose**: Appointment scheduling and reminder UI.
* **What It Actually Does**: A 37,286-byte script with top-level Streamlit commands that renders without a wrapping `show_page()` function.
* **Why It Has This Name**: Early iteration named in the singular (`appointment_reminder.py`).
* **Active Replacement**: [`modules/appointment_reminders.py`](../modules/appointment_reminders.py) (plural).
* **Key Difference**: The active plural version (`appointment_reminders.py`) wraps the entire logic inside `def show_page():`, allowing `app.py` to import and call it dynamically on demand.
* **Archive Reason**: Replaced by the modular `appointment_reminders.py`.

---

### 8. `e-prescription.py` (Hyphenated)
* **Original Purpose**: Prescription upload, OCR analysis, and medication scheduling.
* **What It Actually Does**: 16,961-byte prescription processing tool using Tesseract OCR and medical specialty mapping.
* **Why It Has This Name**: Named with a hyphen (`e-prescription.py`). In Python, hyphens in filenames are invalid identifier syntax (e.g., `import e-prescription` causes a `SyntaxError`).
* **Active Replacement**: [`modules/e_prescription.py`](../modules/e_prescription.py) (using an underscore `_`).
* **Archive Reason**: Replaced by `e_prescription.py` with valid Python naming syntax so it can be cleanly imported into `app.py`.

---

### 9. `ProcessScheduling.cs` (formerly `using System;.py`)
* **Original Purpose**: Operating Systems CPU burst-time & priority scheduling algorithm.
* **What It Actually Does**: 95 lines of pure C# code implementing a `Process` class (`pid`, `bt`, `priority`) and `findWaitingTime`, `findTurnAroundTime`, and `findavgTime` methods.
* **Why It Has This Name**: Originally saved as `using System;.py` because the first line of C# code is `using System;`. Renamed to `.cs` to reflect its true language.
* **Active Replacement**: None (Unrelated to the MEDiSMART healthcare portal).
* **Archive Reason**: Preserved for reference without interfering with Python linters or compilers.

---

## 📊 Summary Reference Matrix

| File Name | Real Purpose | Why Archived | Active Equivalent |
|---|---|---|---|
| `import streamlit as st.py` | Ambulance Tracking | Accidental filename | `modules/ambulance_tracking.py` |
| `medico streamlit web.py` | Symptom Disease Predictor | Standalone prototype | `modules/smart_doctor.py` |
| `medics.py` | Multi-model ML Testbed | Monolithic experiment | `modules/*_diagnosis.py` |
| `python.py` | eHospital Map Dashboard | Prototype with raw HTML | `modules/dashboard.py` |
| `app1.py` | Main App Backup (v1) | Obsolete milestone | `app.py` |
| `app2.py` | Main App Backup (v2) | Obsolete milestone | `app.py` |
| `full_app.py` | Experimental Draft | Broken placeholder calls | `app.py` |
| `appointment_reminder.py` | Appointment System | Missing `show_page()` wrapper | `modules/appointment_reminders.py` |
| `e-prescription.py` | Prescription OCR Tool | Invalid hyphen in filename | `modules/e_prescription.py` |
| `ProcessScheduling.cs` | CPU Scheduling (C#) | Unrelated OS algorithm | None (Archived reference) |

