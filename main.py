import csv
from model.energy_record import EnergyRecord


with open('download.csv', 'r') as f:
    content = csv.reader(f)
    next(content)
    for row in content:
        print(row)

