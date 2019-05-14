import csv
import math

grethe = (596674.0, 6648240.0) # east, north
distToGrethe = 100

def distance_to_point(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    distance = math.sqrt(dx**2 + dy**2)
    return distance

file = open("output/grethes_neighbors.txt", "w")

with open('input/matrikkelenAdresse.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    x = 1
    for row in reader:
        north = float(row["Nord"])
        east = float(row["Øst"])
        dist = distance_to_point(grethe[0], grethe[1], east, north)

        if(dist < distToGrethe):
            text = row["adressenavn"] + " " + row["nummer"] + \
                  row["bokstav"] + ", Gnr/Bnr " + row["gardsnummer"] + \
                  "/" + row["bruksnummer"]
            print(text)
            file.write(text + "\n")
        x+=1

file.close()
