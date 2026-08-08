# Bella Stationery | Retail Profitability & Growth Analytics

[![CI](https://github.com/<YOUR-USERNAME>/<YOUR-REPOSITORY>/actions/workflows/ci.yml/badge.svg)](https://github.com/<YOUR-USERNAME>/<YOUR-REPOSITORY>/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **A data-driven retail case focused on explaining margin erosion, identifying value-destroying products, and defining a profitable growth strategy.**

![Bella Stationery logo](reports/logo_bella_stationery.png)

**Author:** Luciana Gomes Dias Manfredi  
**Case:** Retail Store Sales Data  
**Analysis date:** August 8, 2026

---

## Executive summary

Bella Stationery is a national retailer of office supplies and premium stationery. The business has been growing its sales, but profit has not increased at the same pace. This project transforms transactional sales data into an executive profitability diagnosis and a practical 90-day action plan.

The central conclusion is simple:

> **Bella Stationery does not need to choose between growth and profitability. It needs to choose where to grow.**

The analysis shows that value is being destroyed by a combination of low-margin product mix, loss-making SKUs, discount pressure, shipping economics, and returns. At the same time, several product families and customer segments provide a strong foundation for selective, profitable expansion.

---

## Business problem

Revenue growth alone does not guarantee a healthier retail business. Bella Stationery's leadership needs to understand why sales growth is not translating into proportional profit growth and which decisions can restore margin without stopping commercial expansion.

The case investigates the impact of:

- Product categories and sub-categories;
- Individual products and loss-making SKUs;
- Discounts and promotional behavior;
- Shipping methods and cost-to-serve;
- Customer segments and geographic regions;
- Returns and potential quality or product-fit issues;
- Future-dated records in the source data.

---

## Business questions

This project answers the four questions proposed in the original case:

1. **Why is profit margin declining even though revenue is increasing?**
2. **How can Bella Stationery reverse the decline in profit margin?**
3. **Which products are reducing the company's margin?**
4. **Which products should the company focus on to increase profitability?**

The detailed business questions and analytical answers are also available in the PDF report:

- [Business Questions & Analytical Answers](reports/bella-stationery-business-questions.pdf)

---

## Key performance indicators

| KPI | Result |
|---|---:|
| Total revenue | **R$14,915,600.82** |
| Total profit | **R$1,521,767.96** |
| Consolidated margin | **10.2%** |
| Sales records | **8,399** |
| Unique orders | **5,496** |
| Loss-making records | **4,264 — 50.8%** |
| Recorded returns | **872 — 10.4%** |

### Scope note

The dataset contains records from January 2023 through December 2026. Some shipping dates extend into January 2027. Records after **August 8, 2026** were preserved and explicitly flagged as future-dated rather than silently removed.

---

## Main findings and insights

### 1. The problem is the quality of growth, not the lack of growth

The business generates **R$14.92M in revenue**, but the consolidated margin is only **10.2%**. More than half of the sales records show negative profit, indicating that a significant portion of growth is economically destructive.

The most important management shift is to stop evaluating performance through revenue alone. Every commercial decision should be reviewed through margin by order, SKU, product family, shipping method, and return behavior.

### 2. Furniture is a high-revenue, low-margin area

The Furniture category generates approximately **R$5.18M in revenue**, but only about **R$117.4K in profit**, representing a margin of approximately **2.3%**.

This is a classic scale-without-value pattern: a large sales contribution hides weak economics. Furniture should therefore be reviewed through pricing, freight, supplier costs, discount rules, and SKU-level profitability.

### 3. Shipping method materially affects profitability

Road transportation shows an estimated margin of **4.3%**, compared with **14.7%** for Standard Air. Road transportation also concentrates approximately **R$52K in shipping costs**.

The opportunity is not necessarily to eliminate road shipping, but to understand its cost-to-serve, renegotiate routes and carriers, apply minimum freight thresholds, and ensure that service-level choices are economically viable.

### 4. Returns require operational investigation

The dataset contains **872 recorded returns**. Office Supplies accounts for **461 returns**, making it a priority for investigation into product quality, customer expectations, packaging, product fit, and fulfillment accuracy.

Returns should be treated as both a logistics indicator and a commercial/product signal.

### 5. Several products are destroying value

Among the largest product-level losses identified in the analysis are:

| Product | Revenue | Profit | Margin |
|---|---:|---:|---:|
| Okidata Pacemark 4410N Wide Format Dot Matrix Printer | R$60.6K | **-R$43.9K** | **-72.5%** |
| Canon imageCLASS 2200 Advanced Copier | R$114.2K | **-R$31.9K** | **-27.9%** |
| Global High-Back Leather Tilter, Burgundy | R$82.8K | **-R$30.5K** | **-36.9%** |
| Epson DFX-8500 Dot Matrix Printer | R$86.0K | **-R$29.4K** | **-34.2%** |
| Hoover Portapower Portable Vacuum | R$2.9K | **-R$21.1K** | **-715.7%** |
| Polycom ViewStation ISDN Videoconferencing Unit | R$255.3K | **-R$17.8K** | **-7.0%** |
| KI Conference Tables | R$23.3K | **-R$15.7K** | **-67.4%** |

The recommended response is to create an intervention list for each SKU: **reprice, renegotiate, redesign the offer, or discontinue**.

### 6. Profitable growth opportunities already exist

The strongest opportunities are product families with positive margin and enough commercial relevance to support selective expansion.

| Sub-category | Revenue | Profit | Margin |
|---|---:|---:|---:|
| Labels | R$39.0K | R$13.7K | **35.1%** |
| Binders & Accessories | R$1.02M | R$307.4K | **30.1%** |
| Envelopes | R$174.1K | R$48.2K | **27.7%** |
| Telephones & Communication | R$1.89M | R$317.0K | **16.8%** |
| Copiers & Fax | R$1.13M | R$167.4K | **14.8%** |
| Office Furniture | R$698.1K | R$100.4K | **14.4%** |
| Office Machines | R$2.17M | R$307.7K | **14.2%** |
| Appliances | R$737.0K | R$97.2K | **13.2%** |

Technology is the largest category by revenue, at approximately **R$5.98M**, with an estimated margin of **14.8%** and approximately **R$886.3K in profit**.

Small Business is the strongest customer segment by margin, at approximately **11.3%**, while Home Office presents a lower margin of approximately **8.9%**.

---

## Strategic recommendations

### Immediate priorities

1. Establish a minimum margin floor by SKU and sub-category.
2. Suspend or reprice products with recurring negative profit.
3. Review Furniture, Tables, and Bookcases before pursuing additional volume.
4. Investigate the loss-making printer, copier, furniture, and conferencing SKUs.
5. Review road transportation economics and negotiate carrier or route costs.
6. Replace blanket discounts with margin-aware offers, bundles, and volume conditions.
7. Monitor returns by product, region, customer segment, and shipping method.

### 90-day action plan

| Timing | Initiative | Control metric |
|---|---|---|
| Immediate | Freeze promotions for deficit SKUs | Profit and minimum margin by SKU |
| 30 days | Simulate price, freight, and supplier scenarios for weak sub-categories | Margin by sub-category |
| 60 days | Renegotiate road transportation and define freight rules | Shipping cost / revenue |
| 60 days | Redesign promotions around margin and product mix | Margin after discount |
| 90 days | Increase inventory and commercial exposure for profitable products | Incremental profit and sell-through |
| Continuous | Monitor returns and loss-making orders | Return rate and net margin |

---

## Interactive dashboard

The project includes an offline, self-contained HTML dashboard with filters for:

- Date range;
- Region;
- Category;
- Customer segment;
- Returns;
- Profitability and commercial indicators.

The dashboard includes:

- Revenue, profit, margin, orders, freight, returns, and discount KPIs;
- Monthly revenue and profit evolution;
- Category and sub-category rankings;
- Discount versus margin analysis;
- Revenue versus profit scatter analysis;
- Profitability matrix by sub-category;
- Margin comparison by shipping method;
- Profitability risk map;
- Decision-oriented recommendations.

Open it locally from the repository:

- [Open the interactive dashboard](reports/dashboard.html)

> Because the dashboard is self-contained, it can be opened directly in a browser and does not require an internet connection or external server.

---

## Project architecture

```text
bella-stationery-profitability-analysis/
├── README.md
├── LICENSE
├── Dockerfile
├── Makefile
├── requirements.txt
├── .gitignore
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
│   ├── logo_bella_stationery.png
│   ├── bella-stationery-business-questions.pdf
│   └── README.md
├── src/
│   ├── analysis.py
│   └── build_dashboard.py
└── tests/
    └── test_analysis.py
```

### Folder responsibilities

- **`data/raw/`** — original source workbook used in the case.
- **`data/processed_sales.csv`** — processed, analysis-ready extract.
- **`notebooks/`** — space for exploratory analysis and narrative notebooks.
- **`src/`** — reusable analytical functions and dashboard-generation logic.
- **`reports/`** — dashboard, PDF report, brand assets, and presentation materials.
- **`tests/`** — unit tests for the analytical functions.
- **`.github/workflows/`** — automated quality checks on push and pull request.

---

## Data pipeline

The project follows a transparent descriptive, diagnostic, and prescriptive analytics pipeline:

### 1. Load

- Read the Excel source file using explicit date parsing.
- Validate the presence of the main commercial, customer, product, logistics, and profitability fields.

### 2. Clean and prepare

- Convert sales and shipping dates to datetime values.
- Preserve all source records.
- Create a `Futuro` flag for records with sales dates after August 8, 2026.
- Calculate an analytical margin as `Profit / Revenue`.
- Keep negative-profit transactions for diagnosis instead of treating them as errors.

### 3. Analyze

- Calculate global KPIs.
- Aggregate revenue, profit, margin, freight, discount, volume, and returns.
- Compare categories, sub-categories, products, regions, customer segments, and shipping methods.
- Analyze monthly performance and profitability dispersion.

### 4. Diagnose

- Identify high-revenue areas with weak profit conversion.
- Rank loss-making products and sub-categories.
- Compare discount intensity and profitability.
- Detect operational signals connected to freight and returns.

### 5. Recommend

- Translate findings into pricing, portfolio, freight, promotion, and monitoring actions.
- Prioritize decisions using a 90-day implementation roadmap.

---

## Technology stack

- **Python 3.11**
- **Pandas** for data preparation and aggregation
- **NumPy** for numerical operations
- **OpenPyXL** for Excel ingestion
- **Plotly / HTML / JavaScript** for interactive visual storytelling
- **Pytest** for unit testing
- **Make** for repeatable local commands
- **Docker** for environment reproducibility
- **GitHub Actions** for continuous integration

---

## Quick start

### Option 1: Run locally

```bash
git clone https://github.com/<YOUR-USERNAME>/<YOUR-REPOSITORY>.git
cd <YOUR-REPOSITORY>

python -m venv .venv

# macOS/Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
make all
```

Then open `reports/dashboard.html` in your browser.

### Option 2: Run the quality checks

```bash
make test
```

### Option 3: Rebuild the dashboard

```bash
make dashboard
```

### Option 4: Run with Docker

```bash
docker build -t bella-stationery-case .
docker run --rm bella-stationery-case
```

> The exact Docker behavior may be adapted according to the hosting environment. The main purpose of the image is to provide a reproducible Python runtime for the analysis and validation commands.

---

## Testing and engineering practices

The repository includes:

- Unit tests for KPI calculations;
- Unit tests for grouped profitability metrics;
- Repeatable Makefile commands;
- A pinned Python major/minor target through CI;
- GitHub Actions for automated tests and dashboard generation;
- Separation between reusable analysis logic and presentation output;
- A `.gitignore` to avoid committing temporary artifacts.

Run the tests with:

```bash
PYTHONPATH=. pytest -q
```

### About linting and formatting

The current repository prioritizes analytical correctness, reproducibility, and test automation. Black and Flake8 can be added as the next engineering increment when the project evolves into a larger production analytics codebase.

---

## Modeling and metrics scope

This case is primarily a **descriptive, diagnostic, and prescriptive analytics project**. It does not claim to have trained a predictive machine-learning model or to have achieved predictive performance metrics.

Therefore, metrics such as accuracy, precision, recall, F1-score, and ROC-AUC are not presented as if they had been measured. They would be appropriate in a future project phase for tasks such as:

- Predicting return probability;
- Predicting loss-making orders;
- Forecasting demand and profit;
- Classifying products at risk of margin erosion.

### Planned advanced modeling

Future modeling experiments may compare:

- Logistic Regression;
- Random Forest;
- Gradient Boosting;
- Explainable models using SHAP or LIME.

Model selection should be based on business cost, calibration, interpretability, and time-based validation rather than accuracy alone.

---

## Benchmark and limitations

This project is an internal case analysis based on the provided transactional dataset. It is not a market benchmark and does not compare Bella Stationery with external retailers.

The source data does not include all variables required for a complete profitability model, such as:

- Acquisition channel and campaign cost;
- Inventory and stockout history;
- Supplier cost evolution;
- Competitor prices;
- Customer lifetime value;
- Product-level operational handling cost;
- Detailed return reason and refund amount;
- Reliable causal identification of promotion effects.

Consequently, the recommendations should be treated as evidence-based hypotheses to validate with operational and commercial teams.

---

## Business impact

If implemented, the analysis can support Bella Stationery in:

- Shifting growth toward higher-margin products;
- Reducing recurring losses from individual SKUs;
- Improving price and promotion governance;
- Lowering freight leakage;
- Reducing avoidable returns;
- Prioritizing profitable customer segments;
- Creating a weekly margin-management routine;
- Moving from revenue-centered reporting to contribution-centered decision-making.

The next analytical step is to build an order-level profitability view with net margin after freight and returns, supported by margin targets and alerts for deficit transactions.

---

## Roadmap

- [x] Load and structure the transactional sales data
- [x] Preserve and flag future-dated records
- [x] Build reusable profitability functions
- [x] Create KPI and segment-level analysis
- [x] Develop an offline interactive dashboard
- [x] Produce a business questions and answers report
- [x] Add unit tests and GitHub Actions
- [x] Add Docker and Makefile support
- [ ] Add a fully narrated Jupyter notebook
- [ ] Add Black and Flake8 enforcement
- [ ] Add order-level net margin after returns and freight
- [ ] Add time-based profit forecasting
- [ ] Add return-risk and loss-order predictive models
- [ ] Add SHAP/LIME explainability
- [ ] Add external market or competitor benchmarks

---

## License

This project is released under the [MIT License](LICENSE).

---

## Author

**Luciana Gomes Dias Manfredi**  
Data Analytics | Business Intelligence | Profitability Analytics

If this case is useful, feel free to explore the dashboard, review the analytical logic, and connect with the author on GitHub.

