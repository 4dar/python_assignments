myList = [1,2,3,4,5,6,7,8]
odd = "* * * *"
even = " * * * *"

for i in myList:
    if i % 2 == 0:
        print even
    else:
        print odd
