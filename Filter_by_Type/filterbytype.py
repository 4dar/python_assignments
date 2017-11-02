x = ''

if type(x) == int:
    if x >= 100:
        print "That's a big number!"
    if x <100:
        print "That's a small number!"

if type(x) == str:
    if len(x) >= 50:
        print "Long sentence"
    if len(x) < 50:
        print "Short sentence"

if type(x) == list:
    if len(x) >= 10:
        print "Big list!"
    if len(x) < 10:
        print "Short list"

