class Car:
    className = 'Car'
    objectsCount = 0

    def __init__(self, tank_capacity, fuel_consumption, average_speed):
        self._tank_capacity = tank_capacity
        self._fuel_consumption = fuel_consumption
        self._average_speed = average_speed
        Car.objectsCount = Car.objectsCount + 1

    def distance_till_empty(self):
        return self._tank_capacity / self._fuel_consumption

    def __add__(self, other):
        if isinstance(other, Car):
            total_tank_capacity = self._tank_capacity + other._tank_capacity
            total_fuel_consumption = self._fuel_consumption + other._fuel_consumption
            total_average_speed = (self._average_speed + other._average_speed) / 2
            return Car(total_tank_capacity, total_fuel_consumption, total_average_speed)
        else:
            raise TypeError("Unsupported operand type for +: Car and {}".format(type(other)))

car1 = Car(tank_capacity=50, fuel_consumption=5, average_speed=60)
car2 = Car(tank_capacity=70, fuel_consumption=7, average_speed=55)

combined_car = car1 + car2

print(f'OPERATION + :')
print("Combined Tank Capacity:", combined_car._tank_capacity)
print("Combined Fuel Consumption:", combined_car._fuel_consumption)
print("Combined Average Speed:", combined_car._average_speed)
print('\n')


class Truck(Car):
    className = 'Truck'

    def __init__(self, tank_capacity, fuel_consumption, average_speed, cargo_weight):
        super().__init__(tank_capacity, fuel_consumption, average_speed)
        self.cargo_weight = cargo_weight

    def cargo_fuel_ratio(self):
        return (self.cargo_weight / self._tank_capacity) * 250


class Bus(Car):
    className = 'Bus'

    def __init__(self, tank_capacity, fuel_consumption, average_speed, num_passengers):
        super().__init__(tank_capacity, fuel_consumption, average_speed)
        self.num_passengers = num_passengers

    def passengers_fuel_ratio(self):
        return (self.num_passengers / self._tank_capacity) * 250



truck =(Truck(tank_capacity=100, fuel_consumption=10, average_speed=60, cargo_weight=500))
print(f'Тип: {Truck.className}')
print(f'Расстояние до полного опустошения бака: {truck.distance_till_empty()} км')
print(f'Соотношение веса груза к количеству топлива на 250 км: {truck.cargo_fuel_ratio()}')

print('\n')

bus = Bus(tank_capacity=80, fuel_consumption=8, average_speed=50, num_passengers=30)
print(f'Тип: {Bus.className}')
print(f'Расстояние до полного опустошения бака:{bus.distance_till_empty()}')
print(f'Соотношение числа пассажиров к количеству топлива на 250 км{bus.passengers_fuel_ratio()}')