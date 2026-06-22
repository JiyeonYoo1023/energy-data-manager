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
from business.energy_service import create_record

class TestCreateRecord(unittest.TestCase):
    """
    Unit tests for the create_record function in the business layer.
    """

    def test_create_record_adds_to_list(self):
        """
        Verifies that calling create_record adds exactly one new
        EnergyRecord to the in-memory list, and that the record's
        CSDUID field matches the value that was passed in.
        """
        records = []

        create_record(records, "1234", "Ottawa", "2024Q1",
                      "Energy use", "kwh", "100")

        self.assertEqual(1, len(records))
        self.assertEqual(records[0].get_CSDUID(), "1234")

if __name__ == "__main__":
    unittest.main()