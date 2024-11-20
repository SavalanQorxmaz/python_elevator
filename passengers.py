import random
from passenger import Passenger
from elevator import Elevator
from utils import users

passengers_waiting = []
passengers_boarding = []

def f_new_waiting_passenger(elevator:Elevator):
    floors = elevator.floors
    current_floor=random.randint(0, floors)
    print(current_floor)
    allowed_floors = [x for x in range(0, floors+1) if x != current_floor]
    print(allowed_floors)
    passenger = Passenger(name=users.pop(), current_floor=current_floor, want_to_go=random.choice(allowed_floors))
    print(passenger)
    passengers_waiting.append(passenger)
    return passenger
    
def f_current_passenger(passenger: Passenger):
    passengers_boarding.append(passenger)
    

