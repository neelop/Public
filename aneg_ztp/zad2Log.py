def log(fun):
    def inner(*arg):
        print(fun.__name__, "() called ")
        return fun(*arg)
    return inner
class car:
    def __init__(self, brand=None, model=None):
        self.__brand = brand
        self.__model = model
    @log
    def setbrand(self, brand):
        self.__brand = brand
    @log
    def getbrand(self):
        return self.__brand
    @log
    def delbrand(self):
        del self.__brand
    @log
    def setmodel(self, model):
        self.__model = model
    @log
    def getmodel(self):
        return self.__model
    @log
    def delmodel(self):
        del self.__model

    brand = property(getbrand, setbrand, delbrand)
    model = property(getmodel, setmodel, delmodel)
c1 = car()
c1.brand = " AUDI "
c1.model = " A6 "
print(c1.brand)
print(c1.model)
del c1.brand
del c1.model