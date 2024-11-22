import random
from passenger import Passenger
from elevator import Elevator
from utils import users

passengers_waiting = []
passengers_boarding = []

def f_new_waiting_passenger(elevator:Elevator):
    floors = elevator.floors
    current_floor=random.randint(1, floors)
    # print(current_floor)
    allowed_floors = [x for x in range(1, floors+1) if x != current_floor]
    # print(allowed_floors)
    passenger = Passenger(name=users.pop(), current_floor=current_floor, want_to_go=random.choice(allowed_floors))
    # print(passenger)
    passengers_waiting.append(passenger)
    return passenger


def f_go_out(*, elevator: Elevator):
        for p in passengers_boarding:
            if p.want_to_go == elevator.current_floor:
                passengers_boarding.remove(p)
                elevator.capacity -= 1
        f_select_destination(elevator=elevator)

def f_go_on(*, elevator: Elevator):
        for p in passengers_waiting:
            if len(passengers_boarding) > 0 and p.current_floor == elevator.current_floor and elevator.capacity > len(passengers_boarding) and elevator.direction == p.direction or len(passengers_boarding) == 0 and p.current_floor == elevator.current_floor == elevator.destination:
                    passengers_boarding.append(p)
                    passengers_waiting.remove(p)
                    elevator.capacity += 1
                      
        f_select_destination(elevator=elevator)

def f_select_destination(*, elevator: Elevator):
    if len(passengers_boarding) > 0:
        destinations = [x.want_to_go for x in passengers_boarding]
        destinations.sort()
        if elevator.current_floor > destinations[-1]:
            destinations.reverse()
            elevator.destination = destinations[0]
        return False
    else:
        return True
    
    

