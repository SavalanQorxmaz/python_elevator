import time
from passenger import Passenger
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

class Elevator:
    def __init__(self, *, floors, capacity) -> None:
        self.floors = floors
        self.current_floor = 1
        self._destination = 0
        self.direction = 'down' if self.current_floor > self.destination else 'up'
        self.capacity = capacity
        self.passengers = []
    
    @property
    def destination(self):
        return self._destination
    
    @destination.setter
    def destination(self, number):
        self._destination = number
        if self._destination < self.current_floor:
            self.direction = 'down'
        else:
            self.direction = 'up'
    
    def add(self, passenger):
        self.passengers.append(passenger)
    
    
    def move(self):
        print(self.current_floor, self.destination)
        if self.current_floor < self.destination:
            self.current_floor += 1
        elif self.current_floor > self.destination:
            self.current_floor -= 1
        time.sleep(1)
    
    def __str__(self) -> str:
        return f'{self.passengers}'
    
    def __repr__(self) -> str:
        return self.passengers
    
