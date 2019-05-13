import csv

print("----------------")

with open('test.csv', 'r') as f:
  reader = csv.reader(f)
  for row in reader:
      print(row)


print("----------------")

with open('test.csv', 'r') as f:
  reader = csv.DictReader(f)
  for row in reader:
      print(row)

print("----------------")


with open('test.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)

print(your_list)

print("----------------")
