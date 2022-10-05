import csv
# https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html
# The link is to create more csv in case you wnat more fake data
rows = []

# cat file.txt | nano
with open("load.csv", 'r' ) as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)