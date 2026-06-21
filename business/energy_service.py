from model.energy_record import EnergyRecord

def display_one_record(records, index):

    pass

def display_all_records(records):

    pass

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

def update_record(records, index, ...):
    pass

def delete_record(records, index):
    pass

