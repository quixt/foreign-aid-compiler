import csv
f = open("test.csv","r")
r = csv.reader(f)
for row in r:
    print(row)
f.close()