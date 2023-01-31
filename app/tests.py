from django.test import TestCase
from app import models

# Create your tests here.


class TestTaxi(TestCase):
    def test_can_create_taxi(self):
        taxi = models.add_taxi(
            False,
            4,
            0,
            2.50,
            "Van",
            0,
            "None",
        )

        self.assertEqual(taxi.id, 1)
        self.assertFalse(taxi.occupied, False)
        self.assertEqual(taxi.capacity, 4)
        self.assertEqual(taxi.current_passengers, 0)
        self.assertEqual(taxi.fare, 2.50)
        self.assertEqual(taxi.taxi_type, "Van")
        self.assertEqual(taxi.taxi_number, 111)
        self.assertEqual(taxi.notes, "None")

        taxi2 = models.add_taxi(
            True,
            2,
            2,
            3.50,
            "Car",
            0,
            "Hi",
        )

        self.assertEqual(taxi2.id, 2)
        self.assertTrue(taxi2.occupied, True)
        self.assertEqual(taxi2.capacity, 2)
        self.assertEqual(taxi2.current_passengers, 2)
        self.assertEqual(taxi2.fare, 3.50)
        self.assertEqual(taxi2.taxi_type, "Car")
        self.assertEqual(taxi2.taxi_number, 122)
        self.assertEqual(taxi2.notes, "Hi")

        taxi3 = models.add_taxi(
            True,
            2,
            2,
            3.50,
            "Car",
            0,
            "Hi",
        )

        self.assertEqual(taxi3.id, 3)
        self.assertTrue(taxi3.occupied, True)
        self.assertEqual(taxi3.capacity, 2)
        self.assertEqual(taxi3.current_passengers, 2)
        self.assertEqual(taxi3.fare, 3.50)
        self.assertEqual(taxi3.taxi_type, "Car")
        self.assertEqual(taxi3.taxi_number, 133)
        self.assertEqual(taxi3.notes, "Hi")

    def test_start_fare(self):
        taxis = [
            {
                "occupied": False,
                "capacity": 4,
                "current_passengers": 0,
                "fare": 2.50,
                "taxi_type": "Van",
                "taxi_number": 0,
                "notes": "None",
            },
            {
                "occupied": True,
                "capacity": 3,
                "current_passengers": 3,
                "fare": 4.00,
                "taxi_type": "Van",
                "taxi_number": 0,
                "notes": "None",
            },
            {
                "occupied": False,
                "capacity": 2,
                "current_passengers": 0,
                "fare": 1.50,
                "taxi_type": "car",
                "taxi_number": 0,
                "notes": "None",
            },
            {
                "occupied": False,
                "capacity": 6,
                "current_passengers": 0,
                "fare": 5.50,
                "taxi_type": "Yukon",
                "taxi_number": 0,
                "notes": "None",
            },
        ]

        for taxi in taxis:
            models.add_taxi(
                taxi["occupied"],
                taxi["capacity"],
                taxi["current_passengers"],
                taxi["fare"],
                taxi["taxi_type"],
                taxi["taxi_number"],
                taxi["notes"],
            )

        taxi = models.start_fare(5)
        self.assertEqual(taxi.id, 4)
        self.assertEqual(taxi.taxi_type, "Yukon")
        self.assertEqual(taxi.current_passengers, 5)
        self.assertEqual(taxi.taxi_number, 144)
