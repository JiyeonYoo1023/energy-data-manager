"""
Author: Jiyeon Yoo
Course: CST8002 040 Programming Language Research Project
Assignment: Practical Project 02
Professor: Eric Torunski
Due Date: Jun 21, 2026
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

"""

from model.energy_record import EnergyRecord

def display_one_record(records, index):
    """
    Displays a single record from the in-memory list at the given index.

    Args:
        records (list): The list of EnergyRecord objects.
        index (int): The index of the record to display.
    """
    if 0 <= index < len(records):
        record = records[index]
        print("-" * 150)
        print(f"{'CSDUID':<25} {'CSD':<34} {'Period':<10}"
              f"{'IndicatorSummaryDescription':<32}"
              f"{'UnitOfMeasure':<22} {'OriginValue':<10}")
        print("-" * 150)
        print(
            f"{record.get_CSDUID():<10}",
            f"{record.get_CSD():<50}",
            f"{record.get_Period():<10}",
            f"{record.get_IndicatorSummaryDescription():<35}",
            f"{record.get_UnitOfMeasure():<15}",
            f"{record.get_OriginValue():<10}")
    else:
        print("Invalid index")

def display_all_records(records):
    """
    Displays every record currently held in the in-memory list.
    Prints the author's name after every 10 records, as required.

    Args:
        records (list): The list of EnergyRecord objects to display.
    """
    print("-" * 150)
    print(f"{'CSDUID':<25} {'CSD':<34} {'Period':<10}"
          f"{'IndicatorSummaryDescription':<32}"
          f"{'UnitOfMeasure':<22} {'OriginValue':<10}")
    print("-" * 150)

    for i, record in enumerate(records):
        print(
            f"{record.get_CSDUID():<10}",
            f"{record.get_CSD():<50}",
            f"{record.get_Period():<10}",
            f"{record.get_IndicatorSummaryDescription():<35}",
            f"{record.get_UnitOfMeasure():<15}",
            f"{record.get_OriginValue():<10}")

        if (i + 1 ) % 10 == 0:
            print("Program by Jiyeon Yoo")

def create_record(records,csduid,csd,period,indicator,unit,value):
    """
    Creates a new EnergyRecord object from the given field values and
    appends it to the in-memory list of records.

    Args:
        records (list): The list of EnergyRecord objects to append to.
        csduid (str): The CSDUID value for the new record.
        csd (str): The CSD value for the new record.
        period (str): The Period value for the new record.
        indicator (str): The IndicatorSummaryDescription value for the new record.
        unit (str): The UnitOfMeasure value for the new record.
        value (str): The OriginalValue value for the new record.

    Returns:
        EnergyRecord: The newly created record object.
    """
    new_record = EnergyRecord()

    new_record.set_CSDUID(csduid)
    new_record.set_CSD(csd)
    new_record.set_Period(period)
    new_record.set_IndicatorSummaryDescription(indicator)
    new_record.set_UnitOfMeasure(unit)
    new_record.set_OriginValue(value)

    records.append(new_record)

    return new_record

def update_record(records, index, csduid, csd, period, indicator, unit, value):
    """
    Updates the field values of an existing record at the given index.

    Args:
        records (list): The list of EnergyRecord objects.
        index (int): The index of the record to update.
        csduid (str): The new CSDUID value.
        csd (str): The new CSD value.
        period (str): The new Period value.
        indicator (str): The new IndicatorSummaryDescription value.
        unit (str): The new UnitOfMeasure value.
        value (str): The new OriginalValue value.

    Returns:
        bool: True if the update succeeded, False if the index was invalid.
    """
    if 0 <= index < len(records):
        record = records[index]

        record.set_CSDUID(csduid)
        record.set_CSD(csd)
        record.set_Period(period)
        record.set_IndicatorSummaryDescription(indicator)
        record.set_UnitOfMeasure(unit)
        record.set_OriginValue(value)


        return True
    else:
        print("Invalid index")
        return False


def delete_record(records, index):
    """
    Removes a record from the in-memory list at the given index.

    Args:
        records (list): The list of EnergyRecord objects.
        index (int): The index of the record to delete.

    Returns:
        EnergyRecord or None: The removed record, or None if the index was invalid.
    """
    if 0 <= index < len(records):
        removed = records.pop(index)
        return removed
    else:
        print("Invalid index")
        return None

def sort_records(records, field, reverse=False):
    """
    Sorts the in-memory list of EnergyRecord objects by the given field.

    Args:
        records (list): The list of EnergyRecord objects to sort.
        field (str): The name of the field to sort by (e.g. "Period").
        reverse (bool): If True, sorts in descending order. Defaults to False.

    Returns:
        list: A new list containing the records sorted by the given field.
    """
    getters = {
        "CSDUID": lambda r: r.get_CSDUID(),
        "CSD": lambda r: r.get_CSD(),
        "Period": lambda r: r.get_Period(),
        "IndicatorSummaryDescription": lambda r: r.get_IndicatorSummaryDescription(),
        "UnitOfMeasure": lambda r: r.get_UnitOfMeasure(),
        "OriginValue": lambda r: float(r.get_OriginValue()) if r.get_OriginValue() not in (None, "") else 0.0,
    }

    key_func = getters.get(field)

    if key_func is None:
        print(f"Invalid field: {field}")
        return records

    return sorted(records, key=key_func, reverse=reverse)