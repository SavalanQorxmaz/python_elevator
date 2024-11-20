import random
from elevator import Elevator
from passenger import Passenger
from passengers import f_current_passenger, f_new_waiting_passenger, passengers_waiting

elevator = Elevator(floors=12, capacity=10)
    



if __name__ == '__main__':
    passenger = f_new_waiting_passenger(elevator=elevator)
    passenger = f_new_waiting_passenger(elevator=elevator)
    print(passengers_waiting)