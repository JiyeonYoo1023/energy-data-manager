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
from persistence.file_handler import load_records, save_records
from business.energy_service import (
    create_record,
    delete_record,
    update_record,
    display_one_record,
    display_all_records
)
from presentation.menu import show_menu, get_record_input

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
        print("Goodbye!")
        break
    else:
        print("Invalid choice")


