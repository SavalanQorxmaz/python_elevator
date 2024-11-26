import os
from elevator import Elevator

colors = dict(
    RED     = '\x1b[1;39;41m',
    GREEN   = '\x1b[1;37;42m',
    YELLOW  = '\x1b[1;30;43m',
    WHITE   = '\x1b[1;30;47m',
    RESET   = '\x1b[1;39;49m',
)

def f_print_process(*, elevator: Elevator):

    def colored_elevator(func):
         def wrapper(*args):
            red = colors['RED']
            reset = colors['RESET']
            white = colors['WHITE']
            result = func(*args)
            if elevator.current_floor == args[0]:
                 return red + f'{result}'[:50].ljust(50,' ') + reset
            return white + ''[:50].ljust(50,' ') + reset
         return wrapper
    
    def colored_waitings_floors(func):
         def wrapper(*args):
            green = colors['GREEN']
            reset = colors['RESET']
            yellow = colors['YELLOW']
            result = func(*args)
            if len(result) > 0:
                   return green + f'{result}'[:50].ljust(50,' ') + reset
            return yellow + f'{result}'[:50].ljust(50,' ') + reset
         return wrapper

    @colored_waitings_floors
    def waiting_row(i: int):
        waiting = [*filter(lambda x: x.current_floor == i, elevator.waitings)]
        waiting = [f'{p.name} --> {p.destination}' for p in waiting]
        return waiting
    @colored_elevator
    def boarding_row(i:int):
        boarding = [f'{p.name} --> {p.destination}' for p in elevator.boardings] if elevator.current_floor == i else ''
        return boarding
         
    os.system('cls')
    [
        print(f'{i:2}{waiting_row(i)}{boarding_row(i):50}') 
        for i in range(elevator.floors, 0, -1)
    ]