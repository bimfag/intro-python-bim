import csv

with open('input/matrikkelenAdresse.csv') as csvfile:
    reader = csv.reader(csvfile)
    x = 1
    for row in reader:
        if (x % 1000 == 0):
            print(x) # Print for every thousand row
        if (x % 1000000 == 0):
            break # Make sure we kill the process at some point
        x+=1
