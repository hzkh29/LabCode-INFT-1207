import unittest
from src.temperature_sensor import validate_temperature, process_temperatures


class TestTemperatureSensor(unittest.TestCase):
    def test_validate_temperature_valid(self):
        self.assertEqual(validate_temperature("25"), 25.0)
        self.assertEqual(validate_temperature("-50"), -50.0)
        self.assertEqual(validate_temperature("150"), 150.0)

    def test_validate_temperature_invalid(self):
        self.assertRaises(validate_temperature("abc"))
        self.assertRaises(validate_temperature("200"))

    def test_process_temperatures_valid(self):
        temps = ["20", "30", "40"]
        expected = "Min: 20.0°C, Max: 40.0°C, Avg: 30.0°C"
        self.assertEqual(process_temperatures(temps), expected)

    def test_process_temperatures_invalid(self):
        temps = ["20", "abc", "30"]
        expected = "An invalid input was provided."
        self.assertEqual(process_temperatures(temps), expected)


if __name__ == '__main__':
    unittest.main()
