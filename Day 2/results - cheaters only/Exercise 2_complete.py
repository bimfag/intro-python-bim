file = open("output/numbers1to100.txt", "r")

x = 0
for row in file.readlines():
    if x % 3 == 0:
        print(row, end = '')
    x+=1

file.close()
