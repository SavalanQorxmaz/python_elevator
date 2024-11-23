
import time
from elevator_process import elevator, f_elevator_process
from printing import f_print_process


if __name__ == '__main__':

    finish = False
    
    while not finish:  
        f_print_process(elevator=elevator)
        finish = f_elevator_process()
        time.sleep(1) 