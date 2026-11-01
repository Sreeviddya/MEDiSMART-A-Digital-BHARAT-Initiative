# 📌 Project Issues & Action Tracker

This document tracks all identified technical debt, bugs, architectural problems, and enhancement issues for **MEDiSMART : A Digital BHARAT Initiative**.

---

## 📋 Issue Summary

| ID | Issue Title | Severity | Category | Status |
|---|---|---|---|---|
| **#01** | [Syntax error in `using System;.py` (non-Python C# file)](#issue-01-syntax-error-in-using-systempy) | 🔴 High | Bug | ⏳ Open |
| **#02** | [Flat directory clutter and duplicate/stray prototype scripts](#issue-02-flat-directory-clutter-and-redundant-prototype-scripts) | 🟡 Medium | Refactor | ⏳ Open |
| **#03** | [Incompatible pinned dependency in `requirements.txt` (`opencv-python==4.5.5.64`)](#issue-03-incompatible-pinned-dependency-in-requirementstxt) | 🔴 High | Dependencies | ⏳ Open |
| **#04** | [Fragile relative file paths for assets, models, and databases](#issue-04-fragile-relative-file-paths-for-assets-models-and-databases) | 🔴 High | Architecture | ⏳ Open |
| **#05** | [App load latency & crash risk from un-cached module-level model unpickling](#issue-05-app-load-latency-and-crash-risk-from-un-cached-model-loading) | 🔴 High | Performance | ⏳ Open |
| **#06** | [User registration does not persist to database; login restricted to demo user](#issue-06-user-registration-does-not-persist-to-database) | 🔴 High | Bug / Feature | ⏳ Open |

---

### Issue #01: Syntax error in `using System;.py`
- **Category**: Bug / Code Cleanliness
- **Severity**: 🔴 High
- **Affected Files**: `using System;.py`
- **Status**: ⏳ Open

#### Problem Description
The file `using System;.py` in the root repository is a C# source file containing process scheduling logic (`using System; class Process...`) mistakenly named with a `.py` extension. This causes `SyntaxError: invalid syntax` whenever Python tools, linters, or test suites scan the repository.

#### Steps to Reproduce
```powershell
python -m py_compile "using System;.py"
```
Output:
```text
File "using System;.py", line 1
  using System;
        ^^^^^^
SyntaxError: invalid syntax
```

#### Proposed Fix
- Remove this file or move it to a dedicated `archive/` folder if needed for external reference.

---

### Issue #02: Flat directory clutter and redundant prototype scripts
- **Category**: Architecture / Refactoring
- **Severity**: 🟡 Medium
- **Affected Files**: 
  - Redundant versions: `app1.py`, `app2.py`, `full_app.py`, `appointment_reminder.py`, `e-prescription.py`
  - Stray / Prototype files: `import streamlit as st.py`, `medico streamlit web.py`, `medics.py`, `python.py`
  - Datasets (`.csv`), Notebooks (`.ipynb`), Models (`.pkl`) mixed with app code in root.
- **Status**: ⏳ Open

#### Problem Description
The root folder contains 77 files with no modular directory separation. Machine learning binaries (`.pkl`), raw datasets (`.csv`), and Jupyter notebooks are mixed directly with application logic, making navigation, maintenance, and git management difficult.

#### Proposed Fix
Organize repository into standard modular directories:
- `modules/` - UI and feature pages
- `data/` - CSV datasets
- `models/` - Pre-trained `.pkl` model binaries
- `notebooks/` - Jupyter analysis & training notebooks
- `assets/` - Images and static UI elements
- `utils/` - Shared database, auth, and helper routines
- Archive or clean up obsolete duplicate scripts.

---

### Issue #03: Incompatible pinned dependency in `requirements.txt`
- **Category**: Dependencies / Build
- **Severity**: 🔴 High
- **Affected Files**: `requirements.txt`
- **Status**: ⏳ Open

#### Problem Description
`requirements.txt` specifies `opencv-python==4.5.5.64`. This pinned release lacks pre-built wheels for modern Python environments (3.11 and 3.12), causing `pip install -r requirements.txt` to fail during local setup or deployment on Streamlit Cloud. Additionally, several runtime imports (`Pillow`, `requests`, `numpy`) are missing from the file.

#### Steps to Reproduce
```bash
pip install -r requirements.txt
```
(Fails during build on Python 3.11/3.12).

#### Proposed Fix
- Update `opencv-python==4.5.5.64` to `opencv-python>=4.8.0`.
- Add explicit entries for `pillow`, `requests`, and `numpy`.

---

### Issue #04: Fragile relative file paths for assets, models, and databases
- **Category**: Architecture / Bug
- **Severity**: 🔴 High
- **Affected Files**: `app.py`, `smart_doctor.py`, `parkinsons.py`, `digital_health_records.py`
- **Status**: ⏳ Open

#### Problem Description
Several modules load assets (`"logo.jpg"`), database connections (`"health_records.db"`), and models (`"svc.pkl"`, `"parkinsons_model.pkl"`) using naked relative strings. If a user runs Streamlit from the parent directory or any other working folder, the app throws `FileNotFoundError`.

#### Proposed Fix
- Introduce a centralized `config.py` using `pathlib.Path(__file__).resolve().parent` to reliably resolve absolute file paths to `data/`, `models/`, `assets/`, and the database.

---

### Issue #05: App load latency and crash risk from un-cached model loading
- **Category**: Performance / Stability
- **Severity**: 🔴 High
- **Affected Files**: `smart_doctor.py`
- **Status**: ⏳ Open

#### Problem Description
`smart_doctor.py` executes `pickle.load(open("svc.pkl", "rb"))` at the top level of the module without caching. On modern scikit-learn installations, unpickling this model takes over 11 seconds. Because it runs on every page reload/import, and calls `st.stop()` if the model path is unresolved, it causes significant lag and risks halting the entire application.

#### Proposed Fix
- Wrap model loading in a dedicated helper using `@st.cache_resource` in `utils/model_loader.py`.
- Implement graceful error handling with algorithmic fallback if pickle version mismatches occur.

---

### Issue #06: User registration does not persist to database
- **Category**: Bug / Core Feature
- **Severity**: 🔴 High
- **Affected Files**: `login.py`, `register.py`
- **Status**: ⏳ Open

#### Problem Description
`register.py` prompts the user for personal information, verifies an OTP, and displays a success notification, but does not write the newly registered account into the database. As a result, users cannot log in with their newly created credentials, and `login.py` only permits authentication via a single hardcoded demo user (`ViddyaKS`).

#### Proposed Fix
- Initialize a `users` table in the local SQLite database (`health_records.db`).
- Save new account records (with password hashing) upon successful OTP verification in `register.py`.
- Update `login.py` to authenticate against the database while preserving `ViddyaKS` as a pre-seeded demo user.

