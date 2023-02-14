import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path

# A python script to read .xlsx invoices to generate pdf invoices

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    # get file name without the extention
    filename = Path(filename).stem
    invoice_num = filename.split("-")[0]
    # create PDF
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice #{invoice_num}")
    pdf.output(f"PDFs/{filename}.pdf")
