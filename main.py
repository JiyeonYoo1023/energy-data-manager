import csv
from model.energy_record import EnergyRecord

print("Author: Jiyeon Yoo")
print("-"*150)
print(f"{'CSDUID':<25} {'CSD':<34} {'Period':<10}"
      f"{'IndicatorSummaryDescription':<32}"
      f"{'UnitOfMeasure':<22} {'OriginValue':<10}")
print("-"*150)
records = []
try:
    with open("download.csv", "r") as f:
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


        for record in records:
            print(
                f"{record.get_CSDUID():<10}",
                f"{record.get_CSD():<50}",
                f"{record.get_Period():<10}",
                f"{record.get_IndicatorSummaryDescription():<35}",
                f"{record.get_UnitOfMeasure():<15}",
                f"{record.get_OriginValue():<10}")

    print("-"*150)

except FileNotFoundError:
    print("File Not Found")

