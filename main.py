from elevator import Elevator
from elevator_process import process

elevator = Elevator(capacity=10, floors=12, waitings=[])

if __name__ == '__main__':
    
    process(elevator=elevator)