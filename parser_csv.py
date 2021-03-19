import csv

with open('config_data.csv') as csvfile:
    reader = csv.DictReader(csvfile)                               # advantage of header row to create dictionary
    for row in reader:
        print(row)



