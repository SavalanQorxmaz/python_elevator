import logging
from elevator import Elevator
from passengers import f_new_waiting_passenger, passengers_waiting, passengers_boarding, f_go_on, f_go_out, f_select_direction, f_select_destination
from utils import users

logging.basicConfig(
    level= logging.NOTSET,
    filename='logging.log',
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a'
)
info = logging.info
error = logging.error


elevator = Elevator(floors=12, capacity=10)
    
def f_elevator_process():
            if len(users) > 0:
                passenger = f_new_waiting_passenger(elevator=elevator)
                info(f'New waiting: {passenger}')
            first_waiting = None

            if len(passengers_boarding) == 0:
                if len(passengers_waiting) > 0:
                    first_waiting = passengers_waiting[0]
                if first_waiting is None:
                    return True
                else:
                    elevator.destination = first_waiting.current_floor
                    f_select_direction(elevator=elevator)
                    if elevator.direction is not None:
                        elevator.move()
                    else:
                        f_go_on(elevator=elevator, p=first_waiting)
                        elevator.destination = first_waiting.want_to_go
                        f_select_direction(elevator=elevator)

            else:
                if len(passengers_waiting) > 0:
                    for p in passengers_waiting:
                        if p.current_floor == elevator.current_floor and elevator.direction == p.direction:
                            f_go_on(elevator=elevator, p=p)
                for p in passengers_boarding:
                    if p.want_to_go == elevator.current_floor:
                        f_go_out(elevator=elevator)
                        info(f'Arriwed: {p}')
                if len(passengers_boarding) > 0:
                    elevator.destination = f_select_destination(elevator=elevator)
                    f_select_direction(elevator=elevator)
                    elevator.move()
                else:
                    waitings_current_floor = []
                    if len(passengers_waiting) > 0:
                        for p in passengers_waiting:
                            if p.current_floor == elevator.current_floor:
                                waitings_current_floor.append(p)
                    if len(waitings_current_floor) == 1:
                        f_go_on(elevator=elevator, p=waitings_current_floor[0])
                        elevator.destination = waitings_current_floor[0].want_to_go
                        f_select_direction(elevator=elevator)
                        elevator.move()
                    elif len(waitings_current_floor) > 1:
                        ups = [*filter(lambda x: x.direction == 'up', waitings_current_floor)]  
                        downs = [*filter(lambda x: x.direction == 'down', waitings_current_floor)]
                        # print(ups)
                        # print(downs)
                        if len(ups) > len(downs):
                            [f_go_on(elevator=elevator, p=pas) for pas in ups ]  
                        else:
                            [f_go_on(elevator=elevator, p=pas) for pas in downs ] 
                        elevator.destination = f_select_destination(elevator=elevator)
                        f_select_direction(elevator=elevator)
                        elevator.move()