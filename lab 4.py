class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Driver(Person):
    def __init__(self, name, experience):
        super().__init__(name)
        self.experience = experience

    def get_experience(self):
        return self.experience


class Engine:
    def __init__(self, power, manufacturer):
        self.power = power
        self.manufacturer = manufacturer

    def get_power(self):
        return self.power

    def get_manufacturer(self):
        return self.manufacturer


class Car:
    def __init__(self, brand, class_, weight, driver, engine):
        self.brand = brand
        self.class_ = class_
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stopping the car")

    def turn_right(self):
        print("Turning right")

    def turn_left(self):
        print("Turning left")

    def __str__(self):
        return f"Car(brand='{self.brand}', class_='{self.class_}', weight={self.weight}, driver={self.driver}, engine={self.engine})"


class Lorry(Car):
    def __init__(self, brand, class_, weight, driver, engine, cargo_capacity):
        super().__init__(brand, class_, weight, driver, engine)
        self.cargo_capacity = cargo_capacity

    def get_cargo_capacity(self):
        return self.cargo_capacity

    def __str__(self):
        return f"Lorry(cargo_capacity={self.cargo_capacity}, brand='{self.brand}', class_='{self.class_}', weight={self.weight}, driver={self.driver}, engine={self.engine})"


class SportCar(Car):
    def __init__(self, brand, class_, weight, driver, engine, max_speed):
        super().__init__(brand, class_, weight, driver, engine)
        self.max_speed = max_speed

    def get_max_speed(self):
        return self.max_speed

    def __str__(self):
        return f"SportCar(max_speed={self.max_speed}, brand='{self.brand}', class_='{self.class_}', weight={self.weight}, driver={self.driver}, engine={self.engine})"