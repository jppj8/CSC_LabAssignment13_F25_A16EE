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
    # Create two instances of WashingMachine
    machine1 = WashingMachine(15, "Bob")
    machine2 = WashingMachine(12, "Alice")
    
    # Return both instances (machine1 first)
    return machine1, machine2

    # TODO: Create two instances of the class WashingMachine
    # instance "machine1" would send two arguments: int value 15, and string "Bob"
    # instance "machine2" would send two arguments: int value 12, and string "Alice"
    # return two instances with one return statement so that I can use two variables to accept the return (machine1 would be returned first)
m1, m2 = test()
print(m1.owner, m1.capacity)  # Bob 15
print(m2.owner, m2.capacity)  # Alice 12
