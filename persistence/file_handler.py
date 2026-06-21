import csv
from model.energy_record import EnergyRecord
import uuid


def load_records(filename="download.csv"):
    records = []
    try:
        with open(filename, "r") as f:
            content = csv.reader(f)
            next(content)
            for i, row in enumerate(content):
                if i >= 100:
                    break
                record = EnergyRecord()
                record.set_CSDUID(row[0])
                record.set_CSD(row[1])
                record.set_Period(row[2])
                record.set_IndicatorSummaryDescription(row[3])
                record.set_UnitOfMeasure(row[4])
                record.set_OriginValue(row[5])

                records.append(record)

    except FileNotFoundError:
        print("Error: CSV file not found")

    return records
