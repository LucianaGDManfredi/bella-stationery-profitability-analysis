# Analytical notebook

The reusable analysis is in `src/analysis.py`. A notebook can import the same functions to avoid duplicated business logic:

```python
from src.analysis import load_sales, kpis, grouped_profitability
sales = load_sales('data/raw/retail_store_sales.xlsx')
kpis(sales)
grouped_profitability(sales, 'Sub-Categoria do Produto')
```
