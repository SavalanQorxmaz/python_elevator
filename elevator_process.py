import random
import time
import logging
from elevator import Elevator
from passenger import Passenger
from utils import users
from printing import f_print_process

logging.basicConfig(
    level= logging.NOTSET,
    filename='logging.log',
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='w'
)
info = logging.info
error = logging.error

def f_new_waiting_passenger(elevator:Elevator):
    if users:
        floors = elevator.floors
        current_floor=random.randint(1, floors)
        allowed_floors = [x for x in range(1, floors+1) if x != current_floor]
        passenger = Passenger(name=users.pop(), current_floor=current_floor, destination=random.choice(allowed_floors))
        return passenger
    return

def process(*, elevator: Elevator):
    p = f_new_waiting_passenger(elevator=elevator)
    time.sleep(1)
    if p:
        elevator.waitings.append(p)
        info(f'New Waiting: {p}')
    elevator.go_out()
    elevator.go_on()
    if elevator.boardings:
        p_destinations = [p.destination for p in elevator.boardings]
        p_destinations.sort()
        if elevator.current_floor < p_destinations[0]:
            elevator.destination =  p_destinations[0]
        elif elevator.current_floor > p_destinations[0]:
            elevator.destination =  p_destinations[-1]
        elevator.move()
        f_print_process(elevator=elevator)
        return process(elevator=elevator)
    elif elevator.waitings:
        elevator.destination = elevator.waitings[0].current_floor
        elevator.move()
        f_print_process(elevator=elevator)
        return process(elevator=elevator)
    else:
        f_print_process(elevator=elevator)
        return False
