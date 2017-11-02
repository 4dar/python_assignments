myList = []
sum = 0
myString = ''

for i in myList:
    if type(i) == str:
        myString += " " + i
    if type(i) == int or type(i) == float:
        sum = sum + i

if sum and myString:
    print "List is a mixed type" 
    print "String: ",myString  
    print "Sum: ",sum
elif myString:
    print "List is all strings"
    print "String: ",myString
else:
    print "List is all integers"
    print "Sum: ",sum





