def ten_scores():

    from random import *
    randy = randint(60, 100)
    
    if randy < 70:
        grade = "D"
    elif randy < 80:
        grade = "C"
    elif randy < 90:
        grade = "B"
    elif randy <= 100:
        grade = "A"
        
    print "Score: {}; Your grade is {}" .format(randy, grade)


ten_scores()

