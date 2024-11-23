import random
from passenger import Passenger
from elevator import Elevator
from utils import users

passengers_waiting = []
passengers_boarding = []

def f_new_waiting_passenger(elevator:Elevator):
    floors = elevator.floors
    current_floor=random.randint(1, floors)
    allowed_floors = [x for x in range(1, floors+1) if x != current_floor]
    passenger = Passenger(name=users.pop(), current_floor=current_floor, want_to_go=random.choice(allowed_floors))
    passengers_waiting.append(passenger)
    return passenger


def f_go_out(*, elevator: Elevator):
        for p in passengers_boarding:
            if p.want_to_go == elevator.current_floor:
                passengers_boarding.remove(p)
                elevator.capacity -= 1
        f_select_direction(elevator=elevator)

def f_go_on(*, elevator: Elevator, p:Passenger):
        passengers_boarding.append(p)
        passengers_waiting.remove(p)
        elevator.capacity += 1

def f_select_direction(*, elevator: Elevator):
    if elevator.current_floor == elevator.destination:
          elevator.direction = None
    elif elevator.destination > elevator.current_floor:
          elevator.direction = 'up'
    else:
          elevator.direction = 'down'
          
def f_select_destination(*, elevator: Elevator):
    return min([dest.want_to_go for dest in passengers_boarding]) \
        if elevator.direction == 'up' \
            else max([dest.want_to_go for dest in passengers_boarding])

