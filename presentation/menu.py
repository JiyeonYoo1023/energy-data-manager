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

def show_menu():
    """
    Displays the main menu options to the user and prompts for a choice.

    Returns:
        str: The menu option entered by the user.
    """
    print("\n --- Energy Records Menu ---")
    print("Program by Jiyeon Yoo")
    print("1. Reload data from file")
    print("2. Save data to file")
    print("3. Display all records")
    print("4. Display one record")
    print("5. Create new record")
    print("6. Update record")
    print("7. Delete record")
    print("8. Sort records")
    print("9. Filter records")
    print("10. Exit")

    choice = input("Enter number: ")

    return choice

def get_record_input():
    """
    Prompts the user to enter values for each of the six record fields.

    Returns:
        tuple: (csduid, csd, period, indicator, unit, value)
    """
    csduid = input("CSDUID: ")
    csd = input("CSD: ")
    period = input("Period: ")
    indicator = input("Indicator: ")
    unit = input("Unit: ")
    value = input("Value: ")

    return csduid, csd, period, indicator, unit, value

def get_sort_choice():
    """
    Prompts the user to choose a field to sort by and a sort direction.

    Returns:
        tuple: (field, reverse) where field is the column name to sort by
               and reverse is True for descending order, False for ascending.
    """
    print("\nSort by which field?")
    print("1. CSDUID")
    print("2. CSD")
    print("3. Period")
    print("4. IndicatorSummaryDescription")
    print("5. UnitOfMeasure")
    print("6. OriginValue")

    field_map = {
        "1": "CSDUID",
        "2": "CSD",
        "3": "Period",
        "4": "IndicatorSummaryDescription",
        "5": "UnitOfMeasure",
        "6": "OriginValue",
    }

    choice = input("Enter number: ")
    field = field_map.get(choice)

    order = input("Ascending or Descending? (a/d): ").strip().lower()
    reverse = (order == "d")

    return field, reverse

def get_filter_choice():
    """
    Prompts the user to build a set of multi-column filter criteria.
    The user may choose one or more fields and enter a search value for
    each; only records matching ALL entered values will be kept.

    Returns:
        dict: Mapping of field name to the search value entered by the
              user, e.g. {"CSD": "Ottawa", "Period": "2020"}. Empty if
              the user selects no fields.
    """
    field_map = {
        "1": "CSDUID",
        "2": "CSD",
        "3": "Period",
        "4": "IndicatorSummaryDescription",
        "5": "UnitOfMeasure",
        "6": "OriginValue",
    }

    filters = {}

    print("\nBuild your filter (choose as many fields as you like).")
    for key, field in field_map.items():
        print(f"{key}. {field}")
    print("Enter 0 when you are done adding fields.")

    while True:
        choice = input("Enter field number to add (0 to finish): ").strip()

        if choice == "0":
            break

        field = field_map.get(choice)
        if field is None:
            print("Invalid field number.")
            continue

        value = input(f"Value to search for in {field}: ").strip()
        filters[field] = value

    return filters