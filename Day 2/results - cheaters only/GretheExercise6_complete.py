import csv
import math
import os
from GretheExercise4 import write_pdf

grethe = (596674.0, 6648240.0) # east, north
distToGrethe = 100 # try modifying this

def distance_to_point(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    distance = math.sqrt(dx**2 + dy**2)
    return distance


# First make sure the directory exists
directory = "pdfs"
if not os.path.exists(directory):
    os.mkdir(directory)

i = 1
with open('input/matrikkelenAdresse.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")

    for row in reader:
        north = float(row["Nord"])
        east = float(row["Øst"])
        dist = distance_to_point(grethe[0], grethe[1], east, north)

        if(dist < distToGrethe):
            neighbor = "Nabo " + str(i)
            adress = row["adressenavn"] + " " + row["nummer"] + row["bokstav"]
            write_pdf(directory + "/Varsel "+adress+".pdf", \
                  "input/Hans Martin Eikerol - signatur.png", \
                  neighbor, str(row["gardsnummer"]), str(row["bruksnummer"]),adress)
            i += 1
