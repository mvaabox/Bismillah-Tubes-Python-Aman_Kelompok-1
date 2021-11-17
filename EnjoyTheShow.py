import csv


import csv

# Baca file
file = 'dataset1.csv'
with open(file, 'r') as iqro:
    for line in csv.reader(iqro):
        print(line)