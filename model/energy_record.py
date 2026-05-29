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


class EnergyRecord:
    """
    Record object representing a single row from the energy dataset.
    Stores energy production data for a given region and period.
    """

    def __init__(self):
        """
        Constructor for EnergyRecord.
        Initializes all fields to None.
        """
        self.__CSDUID = None
        self.__CSD = None
        self.__Period = None
        self.__IndicatorSummaryDescription = None
        self.__UnitOfMeasure = None
        self.__OriginalValue = None

    def get_CSDUID(self):
        """Returns the CSDUID value."""
        return self.__CSDUID

    def set_CSDUID(self, CSDUID):
        """Sets the CSDUID value."""
        self.__CSDUID = CSDUID

    def get_CSD(self):
        """Returns the CSD value."""
        return self.__CSD

    def set_CSD(self, CSD):
        """Sets the CSD value."""
        self.__CSD = CSD

    def get_Period(self):
        """Returns the Period value."""
        return self.__Period

    def set_Period(self, Period):
        """Sets the Period value."""
        self.__Period = Period

    def get_IndicatorSummaryDescription(self):
        """Returns the IndicatorSummaryDescription value."""
        return self.__IndicatorSummaryDescription

    def set_IndicatorSummaryDescription(self, IndicatorSummaryDescription):
        """Sets the IndicatorSummaryDescription value."""
        self.__IndicatorSummaryDescription = IndicatorSummaryDescription

    def get_UnitOfMeasure(self):
        """Returns the UnitOfMeasure value."""
        return self.__UnitOfMeasure

    def set_UnitOfMeasure(self, UnitOfMeasure):
        """Sets the UnitOfMeasure value."""
        self.__UnitOfMeasure = UnitOfMeasure

    def get_OriginValue(self):
        """Returns the OriginalValue value."""
        return self.__OriginalValue

    def set_OriginValue(self, OriginValue):
        """Sets the OriginalValue value."""
        self.__OriginalValue = OriginValue


