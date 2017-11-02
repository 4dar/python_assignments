name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "giraffes"]

def make_dict(list1, list2):
    new_dict = {}
    if len(list1) >= len(list2):
        new_dict = zip(list1, list2)
    else:
        new_dict = zip(list2, list1)
    new_dict = dict(new_dict)
    print new_dict
    return new_dict

make_dict(name, favorite_animal)