import pandas as pd
import sys

try:
    # Try reading with xlrd engine for .xls
    xls = pd.ExcelFile('施工日報模板.xls')
    print(f"Sheet Names: {xls.sheet_names}")
    for sheet in xls.sheet_names:
        df = pd.read_excel('施工日報模板.xls', sheet_name=sheet)
        print(f"\n--- Sheet: {sheet} ---")
        print(f"Columns: {df.columns.tolist()}")
        print("Sample Data:")
        print(df.head(10))
except Exception as e:
    print(f"Error: {e}")
