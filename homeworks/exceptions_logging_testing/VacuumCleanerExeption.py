# 2. ----
class LowBattery(Exception):
    def __init__(self, message="Need to recharge"):
        self.message = message
        super().__init__(self.message)


class FullTrashTank(Exception):
    def __init__(self, message="The trash can needs cleaning"):
        self.message = message
        super().__init__(self.message)


class EmptyWatterTank(Exception):
    pass

class ValueError(Exception):
    pass
# ** ----
