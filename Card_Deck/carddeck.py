from random import *


class Deck(object):
    def __init__(self):
        self.deck = 52

    def dealhand(self):
        self.deck -= 2
        randomcard1 = randint(1,53)
        randomcard2 = randint(1,53)
        if randomcard2 == randomcard1:
            randomcard2 = randint(1,53)
        print "Cards left in Deck: " + str(self.deck)
        print "First card: " + str(randomcard1)
        print "Second card: " + str(randomcard2)
        return self


class Player(Deck):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hand = []

    def display_info(self):
        print "Name: {}".format(self.name)
        print "Age: {}".format(self.age)
        print "Cards in hand: {}".format(self.hand)
        print randomcard1
        print randomcard2


deck1 = Deck()
adar = Player("Adar", 24)

adar.dealhand()



# mendel = Player("Mendel", 22)
# nazar = Player("Nazar", 21)
# allyson = Player("Allyson", 26)


