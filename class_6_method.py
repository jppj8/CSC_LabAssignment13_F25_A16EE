class WashingMachine:
    # class attributes
    brand = "Samsung"
    type = "Front Load"

    def __init__(self, capacity, owner):
        self.capacity = capacity  # kg
        self.owner = owner
        self.is_running = False
        self.mode = "Normal"

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False

    def set_mode(self, mode):
        self.mode = mode


def test():
    # create one instance of class WashingMachine
    machine = WashingMachine(13, "Eve")
    # call method "set_mode()" with argument "Spin"
    machine.set_mode("Spin")
    # return the instance
    return machine
m = test()
print(m.owner)     # Eve
print(m.capacity)  # 13
print(m.mode)      # Spin
