import time


class Elevator:
    def __init__(self, *, capacity : int, floors: int, waitings: list) -> None:
        self.floors = floors
        self.capacity = capacity
        self.current_floor = 1
        self._destination = 1
        self.boardings = []
        self.waitings = waitings
        
    @property
    def destination(self):
        return self._destination
    
    @destination.setter
    def destination(self, value):
        self._destination = value
    
    @property
    def direction(self):
        destination = self.destination
        temp = destination - self.current_floor
        if temp > 0:
            return 'up'
        elif temp < 0:
            return 'down'
        else:
            return None
        
    def move(self):
        direction = self.direction
        if direction == 'up' and self.current_floor < self.floors:
            self.current_floor += 1
        elif direction == 'down' and self.current_floor > 0:
            self.current_floor -= 1
    
    def go_on(self):
        if self.waitings:
            if self.boardings:
                direction = self.direction
                waitings_at_current_floor = [*filter(lambda x: x.direction == self.boardings[0].direction and x.current_floor == self.current_floor, self.waitings)]
                if waitings_at_current_floor:
                    for p in waitings_at_current_floor:
                        if len(self.boardings) < self.capacity:
                            self.boardings.append(p)
                            self.waitings.remove(p)
                    return True
                return False
        
            else:
                waitings_at_current_floor = [*filter(lambda x: x.current_floor == self.current_floor == self.destination, self.waitings)]
                if waitings_at_current_floor:
                    direction = waitings_at_current_floor[0].direction
                    waitings_at_current_floor = [*filter(lambda x: x.direction == direction, waitings_at_current_floor)]
                    for p in waitings_at_current_floor:
                        if len(self.boardings) < self.capacity:
                            self.boardings.append(p)
                            self.waitings.remove(p)
                    return True
                return False
            
    def go_out(self):
        if self.boardings:
            arriwed = [*filter(lambda x: x.destination == self.current_floor, self.boardings)]
            if arriwed:
                self.boardings = [*filter(lambda x: x not in arriwed, self.boardings)]
                return True
        return False
       
    def __str__(self):
        return f'{self.boardings=}\n{self.waitings=}\n{self.current_floor}\n{self.destination}\n{self.direction}'