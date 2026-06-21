import unittest
from business.energy_service import create_record

class TestCreateRecord(unittest.TestCase):

    def test_create_record_adds_to_list(self):

        records = []

        create_record(records, "1234", "Ottawa", "2024Q1",
                      "Energy use", "kwh", "100")

        self.assertEqual(1, len(records))
        self.assertEqual(records[0].get_CSDUID(), "1234")

if __name__ == "__main__":
    unittest.main()