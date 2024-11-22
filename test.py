import unittest
from elevator import Elevator
from passenger import Passenger



class ElevatorTest(unittest.TestCase):
    elevator = Elevator(floors=20, capacity=10)
    passenger1 = Passenger(name='Passenger1', current_floor=3, want_to_go=19)
    passenger2 = Passenger(name='Passenger2', current_floor=8, want_to_go=10)
    def test_elevator(self): 
        self.assertEqual(self.elevator.floors, 20)

    def test_passenger_direction(self):
        self.assertEqual(self.passenger1.direction, 'up')


if __name__ == '__main__':
    unittest.main(verbosity=2)