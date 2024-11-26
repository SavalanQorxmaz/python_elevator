
class Passenger:
    def __init__(self, *, name: str, current_floor: int, destination: int) -> None:
        self.name = name
        self.current_floor = current_floor
        self.destination = destination
        
    @property       
    def direction(self):
        temp = self.destination - self.current_floor
        if temp > 0:
            return 'up'
        else:
            return 'down'

    def __str__(self):
        return f'{self.name}({self.current_floor}->{self.destination})'
    
    def __repr__(self):
        return f'{self.name}({self.current_floor}->{self.destination})'
    

    