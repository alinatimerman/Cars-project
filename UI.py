from Domain.Car import Car
from Service.CarRepository import CarRepository

def printInstructions():
    print("\t1 - Add a car")
    print("\t2 - Print the list of the cars")
    print("\t3 - Get the list of the cars by a given year")
    print("\t4 - Apply a discount of 5% for a given brand of cars")
    print("\t0 - Exit")

def UI():
    repo = CarRepository()
    repo.addCar(Car("Toyota", 2010, 2000))
    repo.addCar(Car("VW", 2000, 1500))
    repo.addCar(Car("Audi", 2019, 10000))

    printInstructions()
    while(True):
        choice = int(input("Enter your choice - "))
        if choice == 1:
            name = input("Enter the name of the car - ")
            year = int(input("Enter the year - "))
            price = int(input("Enter the price - "))
            repo.addCar(Car(name, year, price))

        if choice == 2:
            repo.printList()

        if choice == 3:
            year = int(input("Enter the year - "))
            repo.getByYear(year)

        if choice == 4:
            name = input("Enter the name - ")
            ok = repo.update(name)
            if ok == 1:
                print("The list after:")
                repo.printList()

        if choice == 0:
            print("The app is closing....")
            break


