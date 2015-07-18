import random
# String Concatnation #
########################

# person = {'lang': 'python', 'age': 26, 'name': 'baylee'}
# person['lang'] --> 'python'

# MANIPULATING STRINGS AND ARRAYS  #
#
# string = "this is a string"
# array = ["cat", "dog", "rabbit", "bird"]
#
# print array.index("cat")  # -> 0

# print string.index("is")  # ->2
# print string.find("is", 0) # ->2
# print string.find("is", 4)  # ->5

###################
#       OOP       #
###################
# #
# class Car(object):
#     def __init__(self, speed, make, color="grey", direction=0):  #non-default variables must come first
#         if color == "red":
#             self.color = "white"
#         else:
#             self.color = self
#         self.speed = speed
#         self.direction = direction
#         self.make = make
#
#     def __repr__(self):  # What actually is returned when user types name of object
#         return "{} {}".format(self.speed, self.make)
#
#     def accelerate(self):
#         self.speed += 10
#
#     def brake(self):
#         self.speed -= 10
#
#     def turn_left(self):
#         self.direction -= 90
#
# # Toyota object is an instance of the Car class #
#
# ferrari = Car(300, "ferrari", color="red", direction=90)
# print ferrari.color
# ferrari.accelerate()
# ferrari.accelerate()
# ferrari.accelerate()
# ferrari.accelerate()
# ferrari.turn_left()
#
# print ferrari, ferrari.direction


# class Airplane(object):
#     def __init__(self, speed=800, altitude=0, distance = 0, flight_time = 0):
#         self.speed = speed
#         self.altitude = altitude
#         self.distance = 0
#         self.flight_time = 0
#
#     def fly(self, hours):
#         self.altitude = 15000
#         self.distance = self.distance + self.speed * int(hours)
#         print "You've gone {} miles".format(self.distance)
#
#
# G5 = Airplane()
# G5.fly(2)
#
# class Bicycle(object):
#     def __init__(self, speed=0, direction=90):
#         self.accessories = []
#         self.speed = speed
#         self.direction = direction
#
#
#     def add_accessories(self, accessory):
#         self.accessories.append(accessory)
#
#     def remove_accessories(self, accessory):
#         self.accessories.remove(accessory)
#
#     def ride(self, minutes):
#         self.speed = 10
#         distance = self.speed * float(minutes) / float(60)
#         return "You went for a {} minute bike ride and covered {} miles!".format(minutes, distance)
#
#     def __repr__(self):
#         return "You have the following accessories: {}".format(', '.join(self.accessories))
#
# red_Bicycle = Bicycle()
# red_Bicycle.add_accessories("Basket")
# red_Bicycle.add_accessories("Cool Light")
# red_Bicycle.add_accessories("Fender")
# red_Bicycle.add_accessories("NOS")
# print red_Bicycle.ride(20)
# print red_Bicycle


# SubClass(ParentClass)


class Vehicle(object):
    def __init__(self, color):
        self.speed = 0
        self.direction = 0
        self.color = color
        self.acceleration = 1

    def accelerate(self):
        self.speed += max(0, self.acceleration)
        print "I'm accelerating to this speed: {}".format(self.speed)

    def brake(self):
        self.speed -= max(0, self.acceleration)
        print "I'm deccelerating to this speed: {}".format(self.speed)

    def turn_left(self):
        self.direction -= 90
        print "I'm turning to this direction: {}".format(self.direction)

    # Static methods doesn't need to pass 'self'
    @staticmethod
    def random_car_color():
        colors = ['red', 'silver', 'yellow']
        return random.choice(colors)

    @staticmethod
    def random_car_direction():
        return random.randint(-180, 180)

    @classmethod
    def make_random_color(cls):
        color = cls.random_car_color()
        return cls(color)

    @classmethod
    def copy_vehicle(cls, vehicle):
        # speed color and direction = apply to new instance.
        new_thing = cls()
        new_thing.speed = vehicle.speed
        new_thing.color = vehicle.color
        new_thing.direction = vehicle.direction
        return new_thing

#### MY MIXIN ####
# Typically, do not initialize anything. It gets confusing.
# Usually reserved for "utility" methods

class CarMixin(object):
    def start_wipers(self):
        self.wipers = "on"
        print "Wipers are now {}.".format(self.wipers)

    def stop_wipers(self):
        self.wipers = "off"
        print "Wipers are now {}.".format(self.wipers)

class RadioMixin(object):
    def radio_on(self, station):
        self.station = station
        self.radio = "on"
        print "Radio station is tuned to {}".format(self.station)

    def radio_off(self):
        self.radio = "off"
        print "Radio is turned off. All is quiet."

### MANUAL TRANS AUTOS ###

class ManualTrans(Vehicle):
    def __init__(self, color):
        super(ManualTrans, self).__init__(color)  # Preserves SuperClass functionality, but not required
        self.clutch_in = False

    def engage_clutch(self):
        self.clutch_in = True

    def disengage_clutch(self):
        self.clutch_in = False

    def brake(self):
        self.engage_clutch()
        super(ManualTrans, self).brake()  # Runs parent's brake() method
        self.disengage_clutch()

class Motorbike(ManualTrans):
    pass

class ManualCar(ManualTrans):
    pass

class StreetCar(ManualCar, CarMixin):
    def __init__(self, color):
        super(StreetCar, self).__init__(color)
        self.acceleration = 3

class RaceCar(ManualCar, CarMixin):
    def __init__(self, color):
        super(RaceCar, self).__init__(color)
        self.acceleration = 5

### AUTO TRANS ###

class AutoTrans(Vehicle):
    pass

class AutoCar(AutoTrans, CarMixin):
    pass

class Boat(AutoTrans, RadioMixin):
    def __init__(self):
        self.text = "This is a boat"


# vroom = RaceCar("red")
# vroom.start_wipers()

# ferrari = StreetCar("blue")
# print ferrari.make_random_color().color
# print Vehicle.make_random_color().color
# print Vehicle.make_random_color().color

vehicle = Vehicle("red")
vehicle.accelerate()
vehicle.turn_left()
print vehicle.speed, vehicle.color, vehicle.direction
boat = Boat.copy_vehicle(vehicle)
print boat.speed, boat.color, boat.direction
print boat.text
# #
# # vespa = Motorbike("purple")
# # honda = AutoCar("blue")
# titanic = Boat("white")
# titanic.radio_on("94.9")
#
# color = Vehicle.random_car_color()
# print color

