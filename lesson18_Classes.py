class Vehicle:
    def __init__(self, make, model): # self refers to self, need self in parameters
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")

my_car = Vehicle("Tesla", "Model 3")
# print(my_car.make)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle("Cadillac", "Escalade")
your_car.get_make_model()
your_car.moves()


class Airplane(Vehicle): # inheritance
    def __init__(self, make, model, faa_id):
        super().__init__(make, model) # will inherit from parent
        self.faa_id = faa_id
    def moves(self): # overrides vehicle moves method
        print("Flies along...")

class Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")

class GolfCart(Vehicle):
    pass # classes can't be empty so put pass to inherit everything as is


cessna = Airplane("Cessna", "Skyhawk", "N-1234")
mack = Truck("Mack", "Pinnacle")
golfwagon = GolfCart("Yamaha", "GC100")

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()



print("\n\n\n\n")

for v in (my_car, your_car, cessna, golfwagon, mack):
    v.get_make_model()
    v.moves()
    # polymorphism: ability to act different in response to same input




# The self parameter in Python class methods serves as a reference to the instance of the class. When a method is called on an object, Python automatically passes the object itself as the first argument, which is conventionally named self. This mechanism allows methods to access and modify the attributes and other methods of the specific instance they are called upon.
# Without self, methods would not know which instance they are interacting with, leading to ambiguity and errors, especially when multiple instances of the same class exist. The explicit passing of the instance as self ensures that each method call operates within the correct object context. While self is a convention and not a keyword, deviating from it is strongly discouraged for readability and maintainability reasons.

