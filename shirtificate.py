from fpdf import FPDF, Align, YPos

name = input("What's your name? ")

pdf = FPDF(orientation="portrait", format="A4")
pdf.add_page()
pdf.set_font('helvetica', size=42)
pdf.cell(text="CS50 Shirtificate", center = True)
pdf.image("shirtificate.png", x = Align.L, y = 30, w = 185)
pdf.set_y(90)
pdf.set_font('helvetica', size=30)
pdf.cell(text=f"{name} took CS50", center = True)
pdf.output("shirtificate.pdf")
