import csv

with open('input/matrikkelenAdresse.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    x = 1
    for row in reader:
        north = row["Nord"]
        east = row["Øst"]
        if (x % 1000 == 0):
            print(east, north) # Print for every thousand row
        if (x % 10000 == 0):
            break # Make sure we kill the process at some point
        x+=1
