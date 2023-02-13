from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="p", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=10)

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
  pdf.add_page()
  # Header
  pdf.set_text_color(100, 100, 100)
  pdf.set_font(family="Times", style="B", size=24)
  pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1, border=0)
  for y in range(21,285,10):
    pdf.line(x1=10, y1=y, x2=200, y2=y)

  # Footer
  pdf.ln(265)
  pdf.set_font(family="Times", style="I", size=8)
  pdf.set_text_color(180, 180, 180)
  pdf.cell(w=0, h=10, txt=row['Topic'], align="R")

  for i in range(row['Pages'] -1):
      pdf.add_page()
      for y in range(11,285,10):
        pdf.line(x1=10, y1=y, x2=200, y2=y)
      # Footer
      pdf.ln(277)
      pdf.set_font(family="Times", style="I", size=8)
      pdf.set_text_color(180, 180, 180)
      pdf.cell(w=0, h=10, txt=row['Topic'], align="R")

pdf.output("output.pdf")