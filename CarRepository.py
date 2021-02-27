class CarRepository:

    def __init__(self):
        self.__data = []

    def addCar(self, object):
        self.__data.append(object)

    def getByYear(self, year):
        l = []
        for elem in self.__data:
            if elem.getYear() == year:
                l.append(elem)

        if len(l) > 0:
            for elem in l:
                print(elem)
        else:
            print("There is no car from " + str(year))

    def update(self, name):
        ok = 0
        for elem in self.__data:
            if elem.getName() == name:
                ok = 1
                break

        if ok == 1:
            for elem in self.__data:
                if elem.getName() == name:
                    elem.setPrice(elem.getPrice() - (elem.getPrice() * 0.05))

        if ok == 0:
            print("We have no " + name + " cars")

        return ok

    def printList(self):
        for elem in self.__data:
            print(elem)
