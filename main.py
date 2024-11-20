import random
import time
from elevator import Elevator
from passenger import Passenger
from passengers import f_new_waiting_passenger, passengers_waiting
from utils import users
elevator = Elevator(floors=12, capacity=10)
    



if __name__ == '__main__':
    finish = False
    while not finish:  
        if len(users) > 0:
            passenger = f_new_waiting_passenger(elevator=elevator)
            time.sleep(1)
        
        if len(elevator.passengers) == 0 :
            if len(passengers_waiting) > 0:
                current = passengers_waiting.pop(0)
                elevator.current_floor = current.current_floor
                elevator.add(current)
                print(current)
                print(elevator)
                time.sleep(1)
            else:
                finish = True
        else:
            finish = True
             
        time.sleep(1)
    