
def show_menu():

    print("\n --- Energy Records Menu ---")
    print("Program by Jiyeon Yoo")
    print("1. Reload data from file")
    print("2. Save data to file")
    print("3. Display all records")
    print("4. Display one record")
    print("5. Create new record")
    print("6. Update record")
    print("7. Delete record")
    print("8. Exit")

    choice = input("Enter number: ")

    return choice

def get_record_input():
    csduid = input("CSDUID: ")
    csd = input("CSD: ")
    period = input("Period: ")
    indicator = input("Indicator: ")
    unit = input("Unit: ")
    value = input("Value: ")

    return csduid, csd, period, indicator, unit, value