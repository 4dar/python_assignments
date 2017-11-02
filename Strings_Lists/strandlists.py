words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
new_words = words.replace("day", "month", 1)
print new_words

x = [2,54,-2,7,12,98]
print "Min of List x is", min(x)
print "Max of List x is", max(x)

new_x = ["hello",2,54,-2,7,12,98,"world"]
print "The first value of new_x is", new_x[0]
print "The last value of new_x is", new_x[len(new_x)-1]

myList = [19,2,54,-2,7,12,98,32,10,-3,6]
myList.sort()
print myList
halflist = myList[:len(myList)/2]
print halflist
newlist = myList[5:len(myList)]
print newlist
newlist.insert(0, halflist)
print newlist

