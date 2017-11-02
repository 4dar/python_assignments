x = [4, 6, 1, 3, 5, 7, 25]
def draw_stars():
    for i in x:
        print i*"*"

draw_stars()


x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars(list):
    for i in list:
        if type(i) is int:
            print i*"*"
        if type(i) is str:
            print i[0].lower() * len(i)
            
draw_stars(x)