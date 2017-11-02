# Odd and Even Count to 2000

def odd_even():
    for i in range(1, 2001):
        if(i % 2 == 0):
            print "Number is {}. This is an even number.".format(i)
        else:
            print "Number is {}. This is an odd number.".format(i)

odd_even()



# Multiply by 5 Function

myList = [2, 4, 10, 16]
def multiply(list, num):
    for i in range(len(list)):
        list[i] *= num
    return list

b = multiply(myList, 5)
print b

