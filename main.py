from car import Car
from truck import Truck

def main():

    my_car = Car("Toyota", "Corolla", 4)
    my_truck = Truck("Ford", "F-150", 1000)

    my_car.drive()
    my_car.honk()

    my_truck.drive()
    my_truck.load(1200)


if __name__ == "__main__":
    main()