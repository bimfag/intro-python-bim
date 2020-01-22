file = open("output/numbers1to100.txt", "w")

x = 1
while x <= 100:
    file.write(str(x) + "\n")
    x += 1

file.close()
