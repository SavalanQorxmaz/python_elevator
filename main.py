import random
import math
import time
from elevator import Elevator
from passenger import Passenger
from passengers import f_new_waiting_passenger, passengers_waiting, passengers_boarding, f_go_on, f_go_out, f_select_destination
from utils import users
from printing import f_print_process

elevator = Elevator(floors=12, capacity=10)


if __name__ == '__main__':

    finish = False

    while not finish:  
        if len(users) > 0:
            passenger = f_new_waiting_passenger(elevator=elevator)

        if len(passengers_boarding) > 0:
                f_go_on(elevator=elevator)
                f_go_out(elevator=elevator)
                finish = f_select_destination(elevator=elevator)
                elevator.move()
        else:
            if  elevator.destination == 0:
                if len(passengers_waiting) > 0:
                    elevator.destination = passengers_waiting[0].current_floor
                else:
                    finish = True 
            else:
                f_go_on(elevator=elevator)
                elevator.move()
         
        
        # print(elevator.current_floor, elevator.destination)
        print(passengers_boarding)
