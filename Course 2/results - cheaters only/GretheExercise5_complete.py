from GretheExercise4_complete import write_pdf
import os

# First make sure the directory exists
directory = "pdfs"
if not os.path.exists(directory):
    os.mkdir(directory)

file = open("output/grethes_neighbors.txt", "r")
lines = file.readlines()
i = 0
for line in lines:
    print(line, end="")
    #Write your code here

    parts = line.split(",")
    adress = parts[0]

    gnrbnr = parts[1][9:]
    gnrbnr = gnrbnr.strip()
    parts = gnrbnr.split("/")
    gnr = parts[0]
    bnr = parts[1]

    neighbor = "Nabo " + str(i)

    write_pdf(directory + "/Varsel "+adress+".pdf", "input/Hans Martin Eikerol - signatur.png", \
              neighbor, str(gnr), str(bnr),adress)
    
    i += 1
    

file.close()
