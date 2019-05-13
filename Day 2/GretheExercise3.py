import csv
import math

grethe = (596674.0, 6648240.0) # east, north
distToGrethe = 100 # try modifying this

def distance_to_point(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    distance = math.sqrt(dx**2 + dy**2)
    return distance

file = open("output/grethes_neighbors.txt", "w")

with open('input/matrikkelenAdresse.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")

    # Your code here...

file.close()
