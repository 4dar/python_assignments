class Products(object):
    def __init__(self, name, price, weight, brand):
        self.name = name
        self.price = price
        self.weight = weight
        self.brand = brand
        self.status = "For Sale" 

    def display_item(self):
        print "Item name: {}".format(self.name)
        print "Price is ${}".format(self.price)
        print "Item weighs " + str(self.weight)
        print self.brand + " made"
        print self.status
        return self

    def sold(self):
        self.status = "Sold"
        print "This item is: " + str(self.status)
        return self

    def addtax(self, tax):
        self.tax = tax
        print "After tax: ${}".format(self.price + (self.tax*self.price))
        return self

    def returned(self, reason):
        self.reason = reason
        if reason == "Defective":
            self.status = "Defective"
            self.price = 0
            print self.status
            print "Item returned defective. New Price: $" + str(self.price)
        elif reason == "Unboxed":
            self.status = "New"
            print "Item returned untouched" + item1.display_item()
        elif reason == "Opened":
            self.status = "Used"
            print "Item returned Used. Discounted price: $" + str(self.price - (self.price*.20))

        return self

        


item1 = Products("Black Shirt", 80, "3lb", "Gucci")
item2 = Products("White Shirt", 65, "2lb", "Polo")

item1.display_item().addtax(.08).sold().returned("Opened")