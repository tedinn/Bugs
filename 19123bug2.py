class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.miles_driven = 0

    def drive(self, miles):
        self.miles_driven += miles

# Creating an instance of Car
my_car = Car("Toyota", "Camry", 2015)

# Driving the car
my_car.drive(100)
print("Miles driven:", my_car.miles_driven)

# Trying to access a non-existent attribute
print("Color:", my_car.color)
