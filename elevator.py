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
        self.current_floor = 0
        self.direction = 'up'
        self.capacity = capacity
        self.passengers = []
    
    
    def add(self, passenger):
        self.passengers.append(passenger)
    
    def remove(self, passenger):
        self.passengers.remove(passenger)
    
    def fprint(self):
        [print(x) for x in range(self.floors, -1, -1)]
    
    def __str__(self) -> str:
        return f'{self.passengers}'
    
    def __repr__(self) -> str:
        return self.passengers