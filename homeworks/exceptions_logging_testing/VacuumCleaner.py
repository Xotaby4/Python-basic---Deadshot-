from random import randint
import logging

logging.basicConfig(level=logging.INFO)


class VacuumCleaner:
    v_garbage = 1200
    v_water = 230

    def __init__(self, f_garbage, f_water, q_battery, series):
        self.f_garbage = f_garbage
        self.f_water = f_water
        self.q_battery = q_battery
        self.series = series

    @property
    def info(self):
        return f"{self.series}; power - {self.q_battery}%; water tank - " \
               f"{round(self.f_water * 100 / self.v_water)}%; trash tank - " \
               f"{round(self.f_garbage * 100 / self.v_garbage)}%"

    def battery_drain(self):
        if self.q_battery < 5:
            raise LowBattery("Need to recharge")
        else:
            self.q_battery -= 2

    def add_trash(self):
        at = randint(0, 20)
        if self.f_garbage == self.v_garbage:
            raise FullTrashTank
        elif self.f_garbage + at >= self.v_garbage:
            self.f_garbage = self.v_garbage
        else:
            self.f_garbage += at

    def wet_cleaning(self):
        if self.f_water == 0:
            raise EmptyWatterTank
        elif self.f_water <= 20:
            self.f_water = 0
            raise EmptyWatterTank
        else:
            self.f_water -= 20


print("1. ----")
rowenta = VacuumCleaner(10, 200, 100, "RR7687WH")
print(rowenta.info)
print("** ----")


# 2. ----
class LowBattery(Exception):
    pass


class FullTrashTank(Exception):
    pass


class EmptyWatterTank(Exception):
    pass


# ** ----

# 3. ----
# 4. ----
def start_cleaning(obj: VacuumCleaner, wet_cleaning: bool, time: int):
    logging.info(f"{obj.info} STARTED CLEANING")
    for i in range(time):
        try:
            obj.battery_drain()
            obj.add_trash()
        except LowBattery:
            logging.error("LowBattery")
            logging.info(f"{obj.info} FINISHED CLEANING")
            return False
        except FullTrashTank:
            logging.error("FullTrashTank")
            logging.info(f"{obj.info} FINISHED CLEANING")
            return False
        if wet_cleaning:
            try:
                obj.wet_cleaning()
            except EmptyWatterTank:
                wet_cleaning = False
                logging.error("EmptyWatterTank")
    logging.info(f"{obj.info} FINISHED CLEANING")
    return True

print(start_cleaning(rowenta, True, 43))
# True
# INFO:root:RR7687WH; power - 100%; water tank - 87%; trash tank - 1% STARTED CLEANING
# ERROR:root:EmptyWatterTank
# INFO:root:RR7687WH; power - 14%; water tank - 0%; trash tank - 38% FINISHED CLEANING