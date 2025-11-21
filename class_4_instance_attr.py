class House:
    elementary_school = "FV Elementary"
    middle_school = "FV Middle"
    high_school = "FV High"

    # initialization method with three instance attributes
    def __init__(self, owner, address):
        self.size = 2500      # fixed default value
        self.owner = owner    # from argument
        self.address = address  # from argument


    # TODO: create an initialization method, and three instance attributes:
    # attribute name "size" with int value 2500
    # attribute name "owner" from argument during class calling
    # attribute name "address" from argument during class calling
h1 = House("John", "123 Main St")
print(h1.size)     # 2500
print(h1.owner)    # John
print(h1.address)  # 123 Main St
