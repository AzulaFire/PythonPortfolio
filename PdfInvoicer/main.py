import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path

# A python script to read .xlsx invoices to generate pdf invoices

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    TOTAL = 0.00
    # get file name without the extention
    filename = Path(filepath).stem
    invoice_num, invoice_date = filename.split("-")
    # create PDF
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    # Set font for encoding
    pdf.add_font("Arial", "", "arial.ttf", uni=True)
    pdf.set_font(family="Arial", size=16, style="B")
    # using ln 1 will put the next text on the next line
    pdf.cell(w=50, h=8, txt=f"Invoice #{invoice_num}", ln=1)
    pdf.set_font(family="Arial", size=12, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {invoice_date}")
 
    df = pd.read_excel(filepath)
    pdf.ln(20)

    # get headers from df columns
    headers = list(df.columns)
    # use list comprehension to replace _ with space and make title case
    headers = [item.replace("_", " ").title() for item in headers]

    x = 0
    for index, row in df.iterrows():
        # Add headers - run 1 time
        if x == 0:
            pdf.set_font(family="Arial", size=10, style="B")
            pdf.set_fill_color(211, 211, 211)
            pdf.cell(w=30, h=8, txt=str(headers[0]), border=1, fill=True)
            pdf.cell(w=60, h=8, txt=str(headers[1]), border=1, fill=True)
            pdf.cell(w=40, h=8, txt=str(headers[2]), border=1, fill=True)
            pdf.cell(w=30, h=8, txt=str(headers[3]), border=1, fill=True)
            pdf.cell(w=30, h=8, txt=str(headers[4]), border=1, fill=True, ln=1)
            x += 1
        
        # Add row data
        pdf.set_font(family="Arial", size=10)
        pdf.set_text_color(80, 80, 80)

        # Remove ¥ and comma from string for total before calculating total
        total = ''.join(c for c in row["total_price"] if c not in '¥,')

        TOTAL = TOTAL + float(total)

        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=60, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=40, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.multi_cell(w=30, h=8, txt=str(row["total_price"]) + "\n", border=1)
 
    # Add totals row
    pdf.set_font(family="Arial", size=12, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(211, 211, 211)
    pdf.cell(w=30, h=8, txt="Totals", border=1, fill=True)
    pdf.cell(w=60, h=8, txt="", border=1)
    pdf.cell(w=40, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    # Both combined along with the currency symbol(in this case ¥)
    amount_due = "¥{:,.2f}".format(TOTAL)
    pdf.cell(w=30, h=8, txt=f"{amount_due}", border=1, fill=True, ln=1)

    # Add amount owed and logo file
    pdf.set_font(family="Arial", size=12, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=22, txt=f"The total amount due is: {amount_due}", border=0, ln=1)
    pdf.image("logo.png", w=60, h=40)


    pdf.output(f"PDFs/{filename}.pdf")
