def coin_toss():
    attempts = 0
    countheads = 0
    counttails = 0

    for i in range(1, 5001):
        from random import *
        randy = randint(0,1)


        if randy is 0:
            attempts += 1
            countheads += 1
            print "Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tails so far" .format(attempts, countheads, counttails)
        else:
            attempts += 1
            counttails += 1
            print "Attempt #{}: Throwing a coin... It's a tail! ... Got {} head(s) so far and {} tails so far" .format(attempts, countheads, counttails)


coin_toss()