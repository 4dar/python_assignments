my_dict = {
    "name": "Adar",
    "age": "24",
    "country of birth": "United States",
    "favorite language": "Python"}


def about_me():
    for a,b in my_dict.iteritems():
        print "My {} is {}" .format(a, b)

about_me()