import VacuumCleanerExeption
from random import randint
import logging

logging.basicConfig(level=logging.INFO)


class VacuumCleaner:
    v_garbage = 1200
    v_water = 500

    def __init__(self, f_garbage, f_water, q_battery, series):
        self.series = series
        if 0 <= f_garbage <= self.v_garbage:
            self.f_garbage = f_garbage
        else:
            raise ValueError
        if 0 <= f_water <= self.v_water:
            self.f_water = f_water
        else:
            raise ValueError
        if 0 <= q_battery <= 100:
            self.q_battery = q_battery
        else:
            raise ValueError

    @property
    def info(self):
        return f"{self.series}; power - {self.q_battery}%; water tank - " \
               f"{round(self.f_water * 100 / self.v_water)}%; trash tank - " \
               f"{round(self.f_garbage * 100 / self.v_garbage)}%"

    def battery_drain(self):
        if self.q_battery < 5:
            self.q_battery = 0
            raise VacuumCleanerExeption.LowBattery()
        else:
            self.q_battery -= 2

    def add_trash(self):
        at = randint(0, 20)
        if self.f_garbage == self.v_garbage:
            raise VacuumCleanerExeption.FullTrashTank
        elif self.f_garbage + at >= self.v_garbage:
            self.f_garbage = self.v_garbage
        else:
            self.f_garbage += at

    def wet_cleaning(self):
        if self.f_water == 0:
            raise VacuumCleanerExeption.EmptyWatterTank
        elif self.f_water <= 20:
            self.f_water = 0
            raise VacuumCleanerExeption.EmptyWatterTank
        else:
            self.f_water -= 20

    # 3. ----
    # 4. ----
    def start_cleaning(self, wet_cleaning: bool, time: int):
        logging.info(f"{self.info} STARTED CLEANING")
        for i in range(time):
            try:
                self.battery_drain()
                self.add_trash()
            except VacuumCleanerExeption.LowBattery:
                logging.error("LowBattery")
                logging.info(f"{self.info} FINISHED CLEANING")
                return False
            except VacuumCleanerExeption.FullTrashTank:
                logging.error("FullTrashTank")
                logging.info(f"{self.info} FINISHED CLEANING")
                return False
            if wet_cleaning:
                try:
                    self.wet_cleaning()
                except VacuumCleanerExeption.EmptyWatterTank:
                    logging.error("EmptyWatterTank")
                    return False
        logging.info(f"{self.info} FINISHED CLEANING")
        return True


# ** ----
# ** ----

rowenta = VacuumCleaner(10, 200, 100, "RR7687WH")
print(f"1. ----\n{rowenta.info}\n** ----")
# RR7687WH; power - 100%; water tank - 40%; trash tank - 1%


print(f"3./4. ----\n{rowenta.start_cleaning(True, 43)}\n** ----")
# 3./4. ----
# True
# ** ----
# INFO:root:RR7687WH; power - 100%; water tank - 87%; trash tank - 1% STARTED CLEANING
# ERROR:root:EmptyWatterTank
# INFO:root:RR7687WH; power - 14%; water tank - 0%; trash tank - 34% FINISHED CLEANING
