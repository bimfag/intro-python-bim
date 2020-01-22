#Import required packages
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# Define variables
debugGrid = False
def write_pdf(destinationPath, signatureImage, neighbor, gnr, bnr, adress):
    packet = io.BytesIO()

    # Create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=A4)
    can.setFont("Times-Roman", 11)

    can.drawString(65, 700, neighbor)
    can.drawString(80, 637, gnr)
    can.drawString(138, 637, bnr)
    can.drawString(80, 616, adress)
    can.drawImage(signatureImage, 440,45, width=60, mask=[250,255,250,255,250,255], preserveAspectRatio=True, anchor="sw") 

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
    outputStream = open(destinationPath, "wb")
    output.write(outputStream)
    outputStream.close() #Remember to close it

# This code runs only if this python-file gets called directly
if __name__ == "__main__":
    write_pdf("output/dest.pdf", "input/Hans Martin Eikerol - signatur.png", \
              "Kjære nabo", "50", "100","Testveien 1")
