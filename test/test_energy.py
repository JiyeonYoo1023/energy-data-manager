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

import unittest
from business.energy_service import sort_records, create_record

class TestSortRecords(unittest.TestCase):
    """
    Unit tests for the sort_records function in the business layer.
    """

    def test_sort_by_origin_value_ascending(self):
        """
        Verifies that sorting by OriginValue in ascending order
        correctly orders records from smallest to largest value.
        """
        records = []
        create_record(records, "1", "A", "2024Q1", "Energy use", "kwh", "300")
        create_record(records, "2", "B", "2024Q1", "Energy use", "kwh", "100")
        create_record(records, "3", "C", "2024Q1", "Energy use", "kwh", "200")

        sorted_records = sort_records(records, "OriginValue", reverse=False)

        self.assertEqual(sorted_records[0].get_OriginValue(), "100")
        self.assertEqual(sorted_records[1].get_OriginValue(), "200")
        self.assertEqual(sorted_records[2].get_OriginValue(), "300")