import glob
from pathlib import Path
from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

filepaths = glob.glob("files/*.txt")
# reverse the order of the list
filepaths = filepaths[::-1]

for filepath in filepaths:
    # get file name without the extention
    filename = Path(filepath).stem
    # get animal name from file name
    animal = filename.split("/")
    # set x to number of animals in the array
    x = len(animal) - 1

    # create PDF
    pdf.add_page()
    
    # add title from the name of the file
    pdf.set_font(family="Arial", size=16, style="B")
    pdf.cell(w=50, h=12, txt=filename.capitalize())
    with open(filepath, "r") as file:
        content = file.read()
    pdf.ln(18)

    # add animal image
    pdf.image(f"images/{animal[x]}.png", x=70, w=70, h=60)
    pdf.ln(19)
    
    # add text content from text file
    pdf.set_font(family="Arial", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)
    x -= 1

pdf.output("PDFs/Final.pdf")

