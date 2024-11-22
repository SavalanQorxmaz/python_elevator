
class Elevator:
    def __init__(self, *, floors, capacity) -> None:
        self.floors = floors
        self.current_floor = 1
        self._destination = 0
        self.direction = None
        self.capacity = capacity
    
    @property
    def destination(self):
        return self._destination
    
    @destination.setter
    def destination(self, number):
        self._destination = number
        if self._destination < self.current_floor:
            self.direction = 'down'
        elif self._destination > self.current_floor:
            self.direction = 'up'
        elif self.capacity == 0:
            self.direction = 'empty'
    
    def add(self, passenger):
        self.passengers.append(passenger)
    
    
    def move(self):
        if self.direction == 'up':
            self.current_floor += 1
        elif self.direction == 'down':
            self.current_floor -= 1
    
    def __str__(self) -> str:
        return f'{self.passengers}'
    
    def __repr__(self) -> str:
        return self.passengers
    
