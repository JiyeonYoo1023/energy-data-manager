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


