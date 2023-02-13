from fpdf import FPDF

pdf = FPDF(orientation="p", unit="mm", format="A4")

pdf.add_page()

pdf.set_font(family="Arial", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello there!", align="L", ln=1, border=0)

pdf.output("output.pdf")