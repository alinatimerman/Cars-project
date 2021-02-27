class Car:
    def __init__(self, name, year, price):
        self.__name = name
        self.__year = year
        self.__price = price


    def getName(self):
        return self.__name

    def getYear(self):
        return self.__year

    def getPrice(self):
        return self.__price

    def setName(self, name):
        self._name = name

    def setYear(self, year):
        self.__year = year

    def setPrice(self, price):
        self.__price = price

    def __str__(self):
        return "A " + self.__name + " from " + str(self.__year) + " at a price of " + str(self.__price) + "$"