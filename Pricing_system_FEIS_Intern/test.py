import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
import pandas as pd
file_path = "ISIN_code_test.xlsx"  # 記得替換成你的Excel檔案路徑
df = pd.read_excel(file_path, engine="openpyxl")
row = df[df["ISIN"] == "ab"].iloc[0]
print(row)

print(row["SBC"])