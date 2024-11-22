class Passenger:
    def __init__(self, *, name: str, current_floor: int, want_to_go: int) -> None:
        self.name = name
        self.current_floor = current_floor
        self.want_to_go = want_to_go
        self.direction = 'up' 
        if current_floor < want_to_go:
            self.direction = 'up'
        elif current_floor > want_to_go:
            self.direction = 'down'
        self._is_in_elevator = False
       
    @property 
    def is_in_elevator(self):
        return self._is_in_elevator
    
    @is_in_elevator.setter
    def is_in_elevator(self, flag: bool):
        self._is_in_elevator = flag
    
    def __str__(self) -> str:
        return f'Name: {self.name} | He(She) is in {self.current_floor} floor | want to go {self.want_to_go} floor'
    
    def __repr__(self) -> str:
        return f'Name: {self.name} - He(She) is in {self.current_floor} floor - want to go {self.want_to_go} floor'
    