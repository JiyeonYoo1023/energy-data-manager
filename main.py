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


from persistence.file_handler import load_records, save_records
from business.energy_service import (
    create_record,
    delete_record,
    update_record,
    display_one_record,
    display_all_records,
    sort_records
)
from presentation.menu import show_menu, get_record_input, get_sort_choice

print("Author: Jiyeon Yoo")

records = load_records()

while True:
    choice = show_menu()

    if choice == "1":
        records = load_records()
        print("Data reloaded")
    elif choice == "2":
        filename = save_records(records)

    elif choice == "3":
        display_all_records(records)
    elif choice == "4":
        index = int(input("Enter index to display: "))
        display_one_record(records, index)
    elif choice == "5":
        csduid, csd, period, indicator, unit, value = get_record_input()
        create_record(records, csduid, csd, period, indicator, unit, value)
        print("Record created")
    elif choice == "6":
        index = int(input("Enter index to update: "))
        csduid, csd, period, indicator, unit, value = get_record_input()
        update_record(records, index, csduid, csd, period, indicator, unit, value)
        print("Record Updated")
    elif choice == "7":
        index = int(input("Enter index to delete: "))
        delete_record(records, index)
        print("Record deleted")
    elif choice == "8":
        field, reverse = get_sort_choice()
        if field:
            records = sort_records(records, field, reverse)
            print("Records sorted successfully.")
        else:
            print("Invalid field selection.")
    elif choice == "9":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")

