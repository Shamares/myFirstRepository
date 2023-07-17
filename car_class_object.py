class Car(object):
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None

    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_properties(self):
        print("Properties of the Car:")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)


# Creating objects of the Car class
Car1 = Car(200, 50000)
Car1.assign_seating_capacity(5)
Car1.display_properties()

Car2 = Car(180, 75000)
Car2.assign_seating_capacity(4)
Car2.display_properties()
