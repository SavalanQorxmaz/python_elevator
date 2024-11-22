import random
from passenger import Passenger
from elevator import Elevator
from utils import users
import os

passengers_waiting = []
passengers_boarding = []

colors = dict(
    BLACK   = '\x1b[1;39;40m ',
    RED     = '\x1b[1;39;41m ',
    GREEN   = '\x1b[1;37;42m ',
    YELLOW  = '\x1b[1;30;43m ',
    BLUE    = '\x1b[1;37;46m ',
    WHITE   = '\x1b[1;30;47m ',
    UNI     = '\x1b[1;30;47m ',
    RESET   = ' \x1b[1;39;49m',
)
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

def f_go_on(*, elevator: Elevator, p:Passenger):
        passengers_boarding.append(p)
        passengers_waiting.remove(p)
        elevator.capacity += 1

def f_select_destination(*, elevator: Elevator):
    if elevator.current_floor == elevator.destination:
          elevator.direction = None
    elif elevator.destination > elevator.current_floor:
          elevator.direction = 'up'
    else:
          elevator.direction = 'down'

def f_print_process(*, elevator: Elevator):

    def colored_elevator(func):
         def wrapper(*args):
            red = colors['RED']
            reset = colors['RESET']
            result = func(*args)
            if elevator.current_floor == args[0]:
                 result = red + result + reset
            return result
         return wrapper
    def colored_waitings_floors(func):
         def wrapper(*args):
              green = colors['GREEN']
              reset = colors['RESET']
              result = func(*args)
              if len(result) > 0:
                   return green + result + reset
              return result
         return wrapper

    @colored_waitings_floors
    def waiting_row(i: int):
         waiting = [*filter(lambda x: x.current_floor == i, passengers_waiting)]
         waiting = [f'{p.name}-->{p.want_to_go}' for p in waiting]
         waiting_str =  ' '.join(waiting)
         if len(waiting_str) < 40:
              return waiting_str 
         else:
              return waiting_str[:37] + '...'
    @colored_elevator
    def boarding_row(i:int):
        boarding = [f'{p.name}-->{p.want_to_go}' for p in passengers_boarding] if elevator.current_floor == i else ''
        boarding_str = ' '.join(boarding)
        if len(boarding_str) < 40:
            return boarding_str
        else:
            return boarding_str
         
    os.system('cls')
    [
        print(f'{i:2} {waiting_row(i):50}  [{boarding_row(i):50}]') 
        for i in range(elevator.floors, 0, -1)
    ]