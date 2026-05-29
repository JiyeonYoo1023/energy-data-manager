"""
Author: Jiyeon Yoo
Course: CST8002 040 Programming Language Research Project
Assignment: Practical Project 01
Professor: Eric Torunski
Due Date: May 31, 2026
References:

[1] GeeksforGeeks. (n.d.). Constructors in Python. geeksforgeeks.org. [online] Available at:
https://www.geeksforgeeks.org/python/constructors-in-python/ [Accessed on May 29, 2026]

[2] GeeksforGeeks. (n.d.). Getter and Setter in Python. geeksforgeeks.org. [online] Available at:
https://www.geeksforgeeks.org/python/getter-and-setter-in-python/ [Accessed on May 29, 2026]

[3] T. Morsels. (2023, Jan 23). Reading a CSV file in Python. pythonmorsels.com. [online] Available at:
https://www.pythonmorsels.com/csv-reading/ [Accessed on May 29, 2026]

[4] GeeksforGeeks. (2021, Dec 20). Reading Rows from a CSV File in Python. geeksforgeeks.org. [online] Available at:
https://www.geeksforgeeks.org/computer-science-fundamentals/reading-rows-from-a-csv-file-in-python/
[Accessed on May 29, 2026]

[5] Stack Overflow. (2018). "Difference between csv.reader and read when importing CSV file." stackoverflow.com.
[online] Available at:
https://stackoverflow.com/questions/50466932/difference-between-csv-reader-and-read-when-importing-csv-file/
[Accessed on May 29, 2026]

[6] GeeksforGeeks. (n.d.). Python Try Except. geeksforgeeks.org. [online]
Available at: https://www.geeksforgeeks.org/python/python-try-except/ [Accessed on May 29, 2026]
"""

import csv
from model.energy_record import EnergyRecord

print("Author: Jiyeon Yoo")

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

        print("-" * 150)
        print(f"{'CSDUID':<25} {'CSD':<34} {'Period':<10}"
              f"{'IndicatorSummaryDescription':<32}"
              f"{'UnitOfMeasure':<22} {'OriginValue':<10}")
        print("-" * 150)

        for record in records:
            print(
                f"{record.get_CSDUID():<10}",
                f"{record.get_CSD():<50}",
                f"{record.get_Period():<10}",
                f"{record.get_IndicatorSummaryDescription():<35}",
                f"{record.get_UnitOfMeasure():<15}",
                f"{record.get_OriginValue():<10}")

    print("-"*150)
    print("Author: Jiyeon Yoo")

except FileNotFoundError:
    print("File Not Found")

