# Excel to DataFrame in Python — pandas Tutorial

> Most finance data lives in spreadsheets.


📺 **Watch:** https://www.youtube.com/watch?v=6mIH3V4NS_U  
📖 **Article:** https://www.codegiz.com/blog/excel-to-dataframe-in-python/  
🎓 **Tutorial + quiz:** https://www.codegiz.com/watch/excel-to-dataframe-in-python/

Part of the **Common Questions in Python** series — short, search-targeted answers to the questions Python data folks actually type into YouTube.

---

## What you'll learn

- pd.read_excel is the canonical Excel-to-DataFrame in Python.
- Pass sheet_name equals None and pandas returns a dictionary.
- pd.ExcelFile is the context manager for repeated reads.
- The engine choice rarely matters for you.
- Excel is not your final layer.

---

## Setup

This demo runs on Python 3.10+ and pandas 2.0+. The other dependencies are installed via the included `requirements.txt`.

```bash
# 1. Clone
git clone https://github.com/GoCelesteAI/excel-to-dataframe-in-python.git
cd excel-to-dataframe-in-python

# 2. Virtual environment
python3 -m venv .venv
source .venv/bin/activate          # macOS / Linux
# .venv\Scripts\activate          # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Run it

```bash
python excel_to_dataframe.py
```

The demo reads from these files (already in the repo root):

- `stock_summary.xlsx`

---

## The code

Here's `excel_to_dataframe.py` in full — it's deliberately short. The video walks through what each block does.

```python
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
```

---

## Why this exists

Most pandas tutorials are written for the curriculum reader who starts at chapter 1. Real working analysts find pandas through search — `"how do I X in pandas"` typed into Google or YouTube. This series answers each of those questions as a self-contained 4–6 minute single, with a runnable demo you can copy, paste, and adapt to your own data.

---

🤖 *Channel run by Claude AI. Tutorials AI-produced; reviewed and published by Codegiz.* More: [codegiz.com](https://codegiz.com) · [@GoCelesteAI on YouTube](https://www.youtube.com/@GoCelesteAI)
