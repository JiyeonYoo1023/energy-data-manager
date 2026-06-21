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

def save_records(records):
    new_filename = str(uuid.uuid4()) + ".csv"

    with open(new_filename, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(["CSDUID", "CSD", "Period",
                         "IndicatorSummaryDescription",
                         "UnitOfMeasure", "OriginalValue"])

        for record in records:
            writer.writerow([
                record.get_CSDUID(),
                record.get_CSD(),
                record.get_Period(),
                record.get_IndicatorSummaryDescription(),
                record.get_UnitOfMeasure(),
                record.get_OriginValue()
            ])

    print(f"Saved to file: {new_filename}")

    return new_filename
