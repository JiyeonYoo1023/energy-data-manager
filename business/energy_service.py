from model.energy_record import EnergyRecord

def display_one_record(records, index):

    if 0 <= index < len(records):
        record = records[index]
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

    if 0 <= index < len(records):
        removed = records.pop(index)
        return removed
    else:
        print("Invalid index")
        return None
