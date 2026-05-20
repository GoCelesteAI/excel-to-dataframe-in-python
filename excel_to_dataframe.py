"""excel_to_dataframe.py — read an .xlsx workbook three ways with pandas.

Run:
  python excel_to_dataframe.py
"""
import pandas as pd

FILE = "stock_summary.xlsx"

# Method 1: single sheet by name
df = pd.read_excel(FILE, sheet_name="Prices")
print(f"single sheet:         {df.shape}")

# Method 2: every sheet at once as a dict
all_sheets = pd.read_excel(FILE, sheet_name=None)
print(f"all sheets:           {[ (k, v.shape) for k, v in all_sheets.items() ]}")

# Method 3: ExcelFile context — read multiple sheets without re-opening
with pd.ExcelFile(FILE) as xl:
  prices = xl.parse("Prices")
  tickers = xl.parse("Tickers")
print(f"ExcelFile parsed:     prices={prices.shape}, tickers={tickers.shape}")
