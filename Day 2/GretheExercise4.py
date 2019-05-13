#Import required packages
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# Define variables
debugGrid = False

def write_pdf(destinationPath, signatureImage, neighbor, gnr, bnr, adress):
    # Your code here

# This code runs only if this python-file gets called directly
if __name__ == "__main__":
    write_pdf("output/dest.pdf", "input/Hans Martin Eikerol - signatur.png", \
              "Kjære nabo", "50", "100","Testveien 1")
