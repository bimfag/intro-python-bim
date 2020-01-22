from GretheExercise4 import write_pdf
import os

# First make sure the directory exists
directory = "pdfs"
if not os.path.exists(directory):
    os.mkdir(directory)

file = open("output/grethes_neighbors.txt", "r")
lines = file.readlines()

# Write your code here

file.close()
