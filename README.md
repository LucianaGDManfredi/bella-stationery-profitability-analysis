# Bella Stationery | Retail Profitability Analytics

[![CI](https://github.com/<YOUR-USERNAME>/<YOUR-REPOSITORY>/actions/workflows/ci.yml/badge.svg)](https://github.com/<YOUR-USERNAME>/<YOUR-REPOSITORY>/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)

> A transparent retail analytics case that diagnoses margin erosion and translates transactional sales data into practical profitability decisions.

<p align="center">
  <img src="reports/logo_bella_stationery.png" alt="Bella Stationery logo" width="160" />
</p>

**Author:** Luciana Gomes Dias Manfredi  
**Case:** Retail Store Sales Data  
**Analysis reference date:** August 8, 2026

---

## Executive summary

Bella Stationery is growing revenue, but profit is not keeping pace. This project uses transactional retail data to identify where value is being created, where it is being destroyed, and which commercial and operational decisions deserve priority.

The analysis is intentionally focused on **descriptive, diagnostic, and prescriptive analytics**. It does not claim to have trained a predictive machine-learning model or measured model-performance metrics that were not actually produced.

### Core conclusion

> **Bella Stationery does not need to choose between growth and profitability. It needs to choose where to grow.**

---

## Business problem

Revenue growth alone does not guarantee a healthier retail operation. The case investigates why revenue is not translating into proportional profit and evaluates the role of:

- Product categories, sub-categories, and individual SKUs;
- Discounts and promotional pressure;
- Shipping method and cost-to-serve;
- Customer segments and geographic regions;
- Returns and potential product or fulfillment issues;
- Future-dated records in the source data.

## Business questions

1. Why is profit margin declining even though revenue is increasing?
2. How can Bella Stationery reverse the decline in profit margin?
3. Which products are reducing the company's margin?
4. Which products should the company prioritize to increase profitability?

The complete business questions and analytical answers are available in [the PDF report](reports/bella-stationery-business-questions.pdf).

---

## Key results

| KPI | Result |
|---|---:|
| Total revenue | **R$14,915,600.82** |
| Total profit | **R$1,521,767.96** |
| Consolidated margin | **10.2%** |
| Sales records | **8,399** |
| Unique orders | **5,496** |
| Loss-making records | **4,264 — 50.8%** |
| Recorded returns | **872 — 10.4%** |

### Main insights

- **Furniture is large but weak economically:** approximately R$5.18M in revenue and R$117.4K in profit, a margin of about 2.3%.
- **Shipping economics matter:** Road transportation has an estimated margin of 4.3%, versus 14.7% for Standard Air in the analyzed data.
- **Returns deserve investigation:** Office Supplies accounts for 461 recorded returns, the largest category count.
- **Loss-making SKUs are material:** examples include Okidata Pacemark 4410N, Canon imageCLASS 2200, Global High-Back Leather Tilter, and Epson DFX-8500.
- **Profitable growth opportunities exist:** Binders & Accessories, Labels, Envelopes, Telephones & Communication, Copiers & Fax, and Office Machines show positive profitability signals.
- **Small Business is the strongest segment by margin** at approximately 11.3%, while Home Office is lower at approximately 8.9%.

These results should be treated as evidence-based management signals and validated with commercial, logistics, finance, and operations teams.

---

## Recommended actions

1. Establish a minimum margin floor by SKU and sub-category.
2. Reprice, renegotiate, redesign, or discontinue recurring loss-making products.
3. Review Furniture, Tables, and Bookcases before pursuing additional volume.
4. Analyze road freight, carrier costs, routes, and service-level policies.
5. Replace blanket discounts with margin-aware bundles and volume conditions.
6. Monitor returns by product, region, segment, and shipping method.
7. Shift commercial focus toward product families with positive and scalable margins.

### 90-day action plan

| Timing | Initiative | Control metric |
|---|---|---|
| Immediate | Review promotions for deficit SKUs | Profit and margin by SKU |
| 30 days | Simulate price, freight, and supplier scenarios | Margin by sub-category |
| 60 days | Review road transportation economics | Shipping cost / revenue |
| 60 days | Redesign promotions around margin | Margin after discount |
| 90 days | Expand profitable product families selectively | Incremental profit and sell-through |
| Continuous | Monitor returns and loss-making orders | Return rate and net margin |

---

## Interactive dashboard

The repository includes an offline, self-contained HTML dashboard that can be opened directly in a browser without an external server or internet connection.

It presents:

- Revenue, profit, margin, orders, freight, returns, and discount KPIs;
- Monthly revenue and profit evolution;
- Profitability by category, sub-category, shipping method, region, and segment;
- Tables showing revenue, profit, margin, and return rate;
- Decision signals for value leakage, selective growth, logistics review, and discount governance;
- A note identifying future-dated records after August 8, 2026.

Open [the interactive dashboard](reports/bella-stationery-dashboard-Luciana-Gomes-Dias-Manfredi.html).

> The current dashboard is a static analytical view generated from the source data. Interactive filters and additional visual modules are planned enhancements, not current capabilities of this repository version.

---

## Repository structure

```text
bella-stationery-profitability-analysis/
├── README.md
├── .gitignore
├── requirements.txt
├── Makefile
├── .github/
│   └── workflows/
│       └── ci.yml
├── data/
│   ├── raw/
│   │   └── retail_store_sales.xlsx
│   └── processed_sales.csv
├── notebooks/
│   └── README.md
├── reports/
│   ├── dashboard.html
│   ├── bella-stationery-business-questions.pdf
│   ├── logo_bella_stationery.png
│   └── README.md
├── src/
│   ├── analysis.py
│   └── build_dashboard.py
└── tests/
    └── test_analysis.py
```

### Folder responsibilities

- **`data/raw/`** — source Excel workbook used in the case.
- **`data/processed_sales.csv`** — processed analysis-ready extract.
- **`notebooks/`** — guidance for reusing the analytical functions in a notebook; no `.ipynb` notebook is currently included.
- **`src/`** — reusable loading, KPI, grouped profitability, monthly analysis, and dashboard-generation logic.
- **`reports/`** — dashboard, PDF report, and brand asset.
- **`tests/`** — unit tests for the analytical functions.
- **`.github/workflows/`** — automated tests and dashboard generation on push and pull request.

---

## Data pipeline

### 1. Load

- Read the Excel workbook with Pandas and OpenPyXL.
- Support the processed CSV format through the reusable loader.
- Parse sales and shipping dates explicitly.

### 2. Prepare

- Preserve all source records.
- Create a `Futuro` flag for sales dates after **August 8, 2026**.
- Calculate `Margem Calculada` as `Lucro / Faturamento`.
- Keep negative-profit transactions because they are central to the business diagnosis.

### 3. Analyze

- Calculate global KPIs.
- Aggregate revenue, profit, margin, shipping cost, discounts, volume, and returns.
- Compare product, logistics, geographic, and customer dimensions.
- Resample performance by month.

### 4. Diagnose

- Identify high-revenue areas with weak profit conversion.
- Rank loss-making dimensions and products.
- Compare shipping economics and return rates.
- Translate findings into decision-oriented signals.

### 5. Recommend

- Define pricing, assortment, freight, promotion, and monitoring actions.
- Prioritize the response through a 90-day action plan.

---

## Technology and reproducibility

The repository currently uses:

- **Python 3.11**
- **Pandas** for data preparation and aggregation
- **NumPy** for numerical support
- **OpenPyXL** for Excel ingestion
- **HTML, CSS, and JavaScript** for the self-contained dashboard
- **Pytest** for unit tests
- **Makefile** for repeatable local commands
- **GitHub Actions** for automated tests and dashboard generation

No Docker environment, software license, linting configuration, or predictive-modeling pipeline is claimed in this version of the project.

## Quick start

```bash
git clone https://github.com/<YOUR-USERNAME>/<YOUR-REPOSITORY>.git
cd <YOUR-REPOSITORY>

python -m venv .venv

# macOS/Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

### Run the tests

```bash
PYTHONPATH=. pytest -q
```

### Rebuild the dashboard

```bash
make dashboard
```

Or run both dashboard generation and tests:

```bash
make all
```

Then open `reports/dashboard.html` in a browser.

---

## Testing and engineering practices currently implemented

- Unit tests for core KPI and grouped-profitability calculations;
- Separation between reusable analysis logic and presentation generation;
- Repeatable Makefile commands;
- GitHub Actions workflow for tests and dashboard generation;
- `.gitignore` for temporary Python and notebook artifacts.

The repository does **not** currently include Black, Flake8, a Jupyter notebook, or predictive model evaluation. Those are possible future improvements rather than completed deliverables.

---

## Modeling scope and metrics

This is a descriptive, diagnostic, and prescriptive analytics case. No predictive model was trained in the current implementation. Therefore, accuracy, precision, recall, F1-score, ROC-AUC, SHAP, and LIME results are not presented.

Potential future modeling applications include:

- Predicting return probability;
- Predicting loss-making orders;
- Forecasting demand and profit;
- Classifying products at risk of margin erosion.

Any future model should be evaluated with time-based validation, calibration, interpretability, and business-cost metrics rather than accuracy alone.

---

## Limitations and benchmark note

This is an internal case analysis based only on the supplied transactional dataset. It is **not** an external market benchmark and does not compare Bella Stationery with other retailers.

The source data does not contain all variables required for a complete net-profitability model, including supplier-cost evolution, inventory availability, competitor prices, campaign cost, customer lifetime value, detailed return reasons, and refund amounts. The recommendations are therefore hypotheses to validate with business teams.

Future-dated records after August 8, 2026 were preserved and flagged, not removed. This choice keeps the source dataset transparent but should be considered when interpreting time-based results.

---

## Business impact

Applied in a real retail setting, this analysis could support:

- More disciplined price and promotion governance;
- Reduction of recurring SKU-level losses;
- Better freight and cost-to-serve decisions;
- Lower avoidable returns;
- Selective expansion of profitable product families;
- A shift from revenue-only reporting to contribution-oriented management.

The next analytical increment is an order-level net-margin view after freight and returns, supported by alerts for deficit transactions.

---

## Roadmap

- [x] Load and structure transactional sales data
- [x] Preserve and flag future-dated records
- [x] Build reusable profitability functions
- [x] Create KPI and segment-level analysis
- [x] Generate an offline dashboard
- [x] Produce the business questions and answers report
- [x] Add unit tests and GitHub Actions
- [x] Add Makefile commands
- [ ] Add a fully narrated Jupyter notebook
- [ ] Add dashboard filters and richer visual modules
- [ ] Add order-level net margin after returns and freight
- [ ] Add time-based profit forecasting
- [ ] Add return-risk and loss-order predictive models
- [ ] Add SHAP/LIME explainability
- [ ] Add external market or competitor benchmarks
- [ ] Add Black and Flake8 enforcement

---

## Author

**Luciana Gomes Dias Manfredi**  
Data Analytics | Business Intelligence | Profitability Analytics

This case was created to demonstrate an end-to-end analytical thought process: from raw transactional data to business diagnosis, decision support, and an actionable profitability roadmap.
