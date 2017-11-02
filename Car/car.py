class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def display_all(self):
        print "This car costs: $" + str(self.price + self.tax*self.price)
        print "This car goes: " + str(self.speed) + "mph"
        print "The gas tank is " + str(self.fuel)
        print "Mileage: " + str(self.mileage) + "mpg"


car1 = Car(2000, 35, "Full", 15)
car2 = Car(2000, 5, "Not Full", 105)
car3 = Car(2000, 15, "Kind of Full", 95)
car4 = Car(2000, 25, "Full", 25)
car5 = Car(2000, 45, "Empty", 25)
car6 = Car(20000000, 35, "Empty", 15)

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()


    
    