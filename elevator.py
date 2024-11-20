

class Elevator:
    def __init__(self, *, floors, capacity) -> None:
        self.floors = floors
        self.capacity = capacity
        self.passengers = set()
    
    
    def add(self, passenger):
        self.passengers.add(passenger)
    
    def remove(self, passenger):
        self.passengers.discard(passenger)
    
    def __str__(self) -> str:
        return self.passengers
    
    def __repr__(self) -> str:
        return self.passengers