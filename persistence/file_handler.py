"""
Author: Jiyeon Yoo
Course: CST8002 040 Programming Language Research Project
Assignment: Practical Project 03
Professor: Eric Torunski
Due Date: Jul 21, 2026
References:

[1] Python Software Foundation. (n.d.). uuid — UUID objects according to RFC 9562.
docs.python.org. [online] Available at: https://docs.python.org/3/library/uuid.html
[Accessed on June 21, 2026]

[2] Python Software Foundation. (n.d.). unittest — Unit testing framework.
docs.python.org. [online] Available at: https://docs.python.org/3/library/unittest.html
[Accessed on June 21, 2026]

[3] GeeksforGeeks. (n.d.). Python Unittest Tutorial. geeksforgeeks.org. [online]
Available at: https://www.geeksforgeeks.org/python/unit-testing-python-unittest/
[Accessed on June 21, 2026]

[4] Python Software Foundation. (n.d.). Sorting Techniques. docs.python.org.
[online] Available at: https://docs.python.org/3/howto/sorting.html
[Accessed on Jul 26, 2026]

[5] Python Software Foundation. (n.d.). Built-in Functions — sorted().
docs.python.org. [online] Available at:
https://docs.python.org/3/library/functions.html#sorted
[Accessed on Jul 26, 2026]

"""

import csv
from model.energy_record import EnergyRecord
import uuid


def load_records(filename="download.csv"):
    """
    Opens and reads a CSV file, parsing up to the first 100 rows into
    EnergyRecord objects. Handles the case where the file is missing.

    Args:
        filename (str): Name of the CSV file to read. Defaults to "download.csv".

    Returns:
        list: A list of EnergyRecord objects parsed from the file.
              Returns an empty list if the file is not found.
    """
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
    """
    Writes the in-memory list of EnergyRecord objects to a new CSV file.
    The filename is generated using a UUID to guarantee uniqueness and
    avoid overwriting previously saved files.

    Args:
        records (list): The list of EnergyRecord objects to save.

    Returns:
        str: The generated filename the records were saved to.
    """
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
