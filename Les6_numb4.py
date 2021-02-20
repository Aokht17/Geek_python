class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Авто начало движение')

    def stop(self):
        print('Авто остановилось')

    def turn(self, direction):
        print(f'Авто повернуло на{direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.speed} км/ч')
        if self.speed > 60:
            print('Предел скорости превышен. Снизьте скорость')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.speed} км/ч')
        if self.speed > 40:
            print('Предел скорости превышен. Снизьте скорость')



town_car = TownCar(80, 'black', 'Mazda', False)
print(town_car.name)
print(town_car.color)
print(town_car.speed)
print(town_car.is_police)
town_car.go()
town_car.stop()
town_car.turn('лево')
town_car.show_speed()

police_car = PoliceCar(60, 'white', 'Audi', True)
print(police_car.name)
print(police_car.color)
print(police_car.speed)
print(police_car.is_police)
police_car.show_speed()

sport_car = SportCar(120, 'red', 'Sportcar', False)
print(sport_car.name)
print(sport_car.color)
print(sport_car.speed)
print(sport_car.is_police)
sport_car.show_speed()

work_car = WorkCar(30, 'yellow', 'Truck', False)
print(work_car.name)
print(work_car.color)
print(work_car.speed)
print(work_car.is_police)
work_car.show_speed()