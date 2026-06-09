# Hydraulic Network Analytics: Data-Driven Anomaly Detection & Financial Audit

[🇪🇸 Versión en Español](README.es.md)

## 📌 Executive Summary
This repository presents an advanced computational framework designed to audit and diagnose a municipal water distribution network comprising 136 infrastructure nodes. By synthesizing fluid mechanics, rigorous data engineering, and non-linear machine learning architectures, this system exposes hidden operational anomalies, quantifies massive financial losses, and scientifically maps the predictability boundaries of the physical network.

---

## 👁️ Core Pillars 

### 1. Scientific Foundation & Domain Expertise
Unlike standard data science generic portfolios, this project rejects purely empirical assumptions. It is structurally anchored in the laws of fluid dynamics and thermodynamics. 

* **The Problem:** Raw sensor ingestion introduced severe telemetry noise, showing non-physical pressures exceeding millions of PSI.
* **The Solution:** Implemented a rigorous hydraulic domain filter to isolate the normative operating window ($22\text{ a }58\text{ PSI}$), transforming chaotic datasets into clean, production-grade infrastructure analytics.

### 2. The Computational Civil Engineer Continuum
This framework addresses a critical global blind spot: the intersection of heavy infrastructure engineering and elite software development. 

* **Traditional Engineering Blind Spot:** Relying on closed commercial software (e.g., WaterGEMS, EPANET) restricts real-time optimization.
* **Data Science Blind Spot:** Traditional analysts lack the domain context of head loss, pipe roughness, and Darcy-Weisbach friction constraints.
* **The Anomalous Profile:** This repository acts as a proof of concept for autonomous infrastructure software design, capable of overriding black-box tool dependencies.

### 3. Executive Financial Impact
Technical complexity must yield financial justification to align with stakeholder objectives. By implementing strict conditional logic metrics, the system translates physical stress into economic variables:

* **Critical Infrastructure Diagnostic:** Isolated 36 severely compromised nodes driving severe operational inefficiencies.
* **Quantified Loss KPI:** Systemic inefficiencies represent an estimated **$43,200 USD/month** in direct operational losses.

---

## 🔬 Algorithmic Audit & Mathematical Bounds (Machine Learning)

The analytical engine evaluated multiple mathematical paradigms to model pressure behavior as a function of terrain elevation, uncovering critical system boundaries:

| Algorithmic Paradigm | Test Metric ($R^2$) | Root Mean Squared Error ($RMSE$) | Diagnostic Verdict |
| :--- | :--- | :--- | :--- |
| **Simple Linear Regression** | $-0.0507$ | $12.1693\text{ PSI}$ | **Underfitting.** Invalid positive slope violating Bernoulli's principles due to artificial system interventions. |
| **Polynomial Regression (Deg. 2)** | $-0.0531$ | $12.1833\text{ PSI}$ | **Insufficient.** Geometric curvature fails to capture stochastically altered environments. |
| **Random Forest Regressor** | $-0.8051$ | $13.4260\text{ PSI}$ | **Severe Overfitting.** Greedy tree constraints memorized training noise, destroying generalization boundaries. |
| **Multivariable Feature Engineering** | $0.0050$ | $9.9681\text{ PSI}$ | **Information Limit Reached.** Synthetic spatial features stabilized variance but confirmed thermodynamic indeterminacy. |

### 📊 Visual Evidence of Thermodynamic Boundary
The final visualization module highlights the physical reality of the network:

![Model Audit](reports/figures/diagnostico_modelo.png)

* **Conclusion:** The convergence of $R^2 \approx 0$ across all algorithms scientifically proves that elevation alone contains zero predictive signal within artificially balanced networks. The operational state is stochastic under current data constraints, establishing a technical mandate to integrate dynamic hidden features (flow rate demands, pipe diameters, and source proximity).

---

## 🛠️ Stack & Engineering Standards
* **Core Ingestion:** Python 3.11 (Pandas, NumPy)
* **Statistical Modeling:** Scikit-Learn
* **Data Architecture:** Robust path virtualization via `pathlib` (Zero hardcoded absolute paths).
* **Business Intelligence:** Power BI (Advanced DAX modeling).
