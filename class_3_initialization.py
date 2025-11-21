class House:
    elementary_school = "FV Elementary"
    middle_school = "FV Middle"
    high_school = "FV High"

    # initialization method with two instance attributes
    def __init__(self):
        self.plan = "Eden"   # instance attribute
        self.size = 2000     # instance attribute


    # TODO: create an initialization method, and two instance attributes:
    # attribute name "plan" with string value "Eden"
    # attribute name "size" with int value 2000
h1 = House()
print(h1.plan)  # Eden
print(h1.size)  # 2000
