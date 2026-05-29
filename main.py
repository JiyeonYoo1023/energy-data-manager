import csv
from model.energy_record import EnergyRecord

records = []

try:
    with open('download.csv', 'r') as f:
        content = csv.reader(f)
        next(content)
        for row in content:
            record = EnergyRecord()

            record.set_CSDUID(row[0])
            record.set_CSD(row[1])
            record.set_Period(row[2])
            record.set_IndicatorSummaryDescription(row[3])
            record.set_UnitOfMeasure(row[4])
            record.set_OriginValue(row[5])

            records.append(record)

except FileNotFoundError:
    print("File Not Found")
