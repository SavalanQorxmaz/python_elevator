from elevator import Elevator

def f_print_process(*, elevator: Elevator, waitings: list):
    print(elevator.current_floor)
    print(waitings)