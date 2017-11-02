
class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1

    def run(self):
        self.health -= 5

    def display(self):
        print "Current health:", self.health


class Dog(Animal):
    def pet(self):
        self.health += 5



class Dragon(Animal):
    def fly(self):
        self.health -= 10

    def display_health(self):
        print "Current health:",self.health
        if self.health == 0:
            print "Your dragon died!"
        else:
            print "Your dragon lives!"
        



animal1 = Animal("Rabbit", 100)
dog1 = Dog("German Shepherd", 150)
dragon1 = Dragon("Wyvern", 170)
animal2 = Animal("Whale", 1000)

# animal1.walk()
# animal1.walk()
# animal1.walk()
# animal1.run()
# animal1.run()
# animal1.display()

# dog1.walk()
# dog1.walk()
# dog1.walk()
# dog1.run()
# dog1.run()
# dog1.pet()
# dog1.display()

dragon1.fly()
dragon1.fly()
dragon1.fly()
dragon1.fly()
dragon1.fly()
dragon1.fly()
dragon1.fly()
dragon1.fly()
dragon1.fly()
dragon1.fly()
dragon1.fly()
dragon1.fly()
dragon1.fly()
dragon1.fly()
dragon1.fly()
dragon1.fly()
dragon1.fly()
dragon1.display_health()