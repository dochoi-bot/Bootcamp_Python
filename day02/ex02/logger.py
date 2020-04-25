# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/25 17:52:11 by dochoi            #+#    #+#              #
#    Updated: 2020/04/25 18:51:27 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
from random import randint

class CoffeMachine(object):

    water_level = 100

    def log(func):
        def wrapper(*args, **kwargs):
            temp = func.__name__.split("_")
            func_name = temp[0].capitalize() + " " + temp[1].capitalize()
            dbgstr = "(dochoi)Running: "+ func_name
            base = time.time()
            rv = func(*args, **kwargs)
            exec_t = time.time() - base
            exec_t *= 1000
            unitt = "ms"
            if (exec_t > 1000):
                unitt = "s "
                exec_t /= 1000
            dbgstr2 = "[ exec_time = %.3f " % exec_t + unitt +" ]\n"
            dbgstr = "%-30s%30s" % (dbgstr, dbgstr2)
            fd = open("machine.log", "a")
            fd.write(dbgstr)
            return rv

        return wrapper
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self,water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    fd = open("machine.log", "w")
    fd.close()
    machine = CoffeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)