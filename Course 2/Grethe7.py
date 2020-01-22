#Import required packages
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# Define variables
debugGrid = False
imagepath = "input/Hans Martin Eikerol - signatur.png"
packet = io.BytesIO()

# Create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=A4)
can.setFont("Times-Roman", 11)
print (can.getAvailableFonts())

can.drawString(65, 700, "Kjære nabo")
can.drawString(80, 637, "Gnr")
can.drawString(138, 637, "Brn")
can.drawString(80, 616, "Adresse")
can.drawImage(imagepath, 440,45, width=60, mask=[250,255,250,255,250,255], preserveAspectRatio=True, anchor="sw") 

# Print debug grid to help with text placement
if debugGrid:
    can.grid(range(0,800,20),range(0,1000,20))
can.save()

####################
# Start writing PDFs
####################

# Move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)

# Read your existing PDF
existing_pdf = PdfFileReader(open("input/nabovarsel-utfylt.pdf", "rb"))
output = PdfFileWriter()

# Add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)

# Finally, write "output" to a real file
outputStream = open("output/destination.pdf", "wb")
output.write(outputStream)
outputStream.close() #Remember to close it

