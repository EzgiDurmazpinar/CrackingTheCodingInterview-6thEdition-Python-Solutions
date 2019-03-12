class Car():
    def __init__(self,needed_spot,plate):
        self.needed_spot = needed_spot
        self.plate = plate
class ParkingLot():
    def __init__(self):
        self.cars = {}      #dictiniory
        self.available_spots = 25
        self.num_of_levels = 3

    def park_car(self,car):
        if car.needed_spot <= self.available_spots:
            self.cars[car] = True
            self.available_spots -= car.needed_spot
        else:
            print('sorry all spots are taken!! for this car {}'.format(car.plate))

    def unpark_car(self,car):
        del self.cars[car]
        self.available_spots += car.needed_spot

    def print_parked_cars(self):
        for key,value in self.cars.items():
            print(key.plate)

def main():
    my_car = Car(5,'06hzw13')
    second_car = Car(15,'2345gfh1')
    third_car = Car(5,'76276dxc2')
    b = Car(1,'rewrte4567')
    parking_lot = ParkingLot()
    parking_lot.park_car(my_car)
    parking_lot.park_car(second_car)
    parking_lot.park_car(third_car)
    parking_lot.unpark_car(third_car)
    parking_lot.park_car(b)
    parking_lot.print_parked_cars()

if __name__ == '__main__':
    main()
