"""Reusable analysis functions for the Bella Stationery case."""
from pathlib import Path
import pandas as pd

REFERENCE_DATE = pd.Timestamp("2026-08-08")


def load_sales(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    df = pd.read_excel(path) if path.suffix.lower() in {".xlsx", ".xls"} else pd.read_csv(path)
    df["Data da Venda"] = pd.to_datetime(df["Data da Venda"])
    df["Data de Envio"] = pd.to_datetime(df["Data de Envio"])
    df["Futuro"] = df["Data da Venda"] > REFERENCE_DATE
    df["Margem Calculada"] = df["Lucro"] / df["Faturamento"].replace(0, pd.NA)
    return df


def kpis(df: pd.DataFrame) -> dict:
    revenue = float(df["Faturamento"].sum())
    profit = float(df["Lucro"].sum())
    return {
        "revenue": revenue,
        "profit": profit,
        "margin": profit / revenue if revenue else 0,
        "orders": int(df["Order ID"].nunique()),
        "rows": int(len(df)),
        "shipping": float(df["Custo de Envio"].sum()),
        "discount": float((df["Faturamento"] * df["Desconto"]).sum()),
        "loss_rows": int((df["Lucro"] < 0).sum()),
        "returns": int((df["Foi devolvido?"] == 1).sum()),
    }


def grouped_profitability(df: pd.DataFrame, dimension: str) -> pd.DataFrame:
    out = df.groupby(dimension, dropna=False).agg(
        revenue=("Faturamento", "sum"), profit=("Lucro", "sum"),
        shipping=("Custo de Envio", "sum"), discount=("Desconto", "mean"),
        rows=("Row ID", "count"), returns=("Foi devolvido?", "sum")
    ).reset_index()
    out["margin"] = out["profit"] / out["revenue"].replace(0, pd.NA)
    out["return_rate"] = out["returns"] / out["rows"]
    return out.sort_values("profit")


def monthly_profitability(df: pd.DataFrame) -> pd.DataFrame:
    out = df.set_index("Data da Venda").resample("MS").agg(revenue=("Faturamento", "sum"), profit=("Lucro", "sum"))
    out["margin"] = out["profit"] / out["revenue"].replace(0, pd.NA)
    return out.reset_index()
