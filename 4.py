# 4. Реализуйте базовый класс Car.
#
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40
# (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        print("Машина поехала")
    def stop(self):
        print("Машина остановилась")
    def turn(self, direction):
        print("Машина повернула", direction)
    def show_speed(self):
        print(f"Скорость составляет: {self.speed} км/ч")
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость превышена и составляет: {self.speed} км/ч")
        else:
            print(f"Скорость составляет: {self.speed} км/ч")
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость превышена и составляет: {self.speed} км/ч")
        else:
            print(f"Скорость составляет: {self.speed} км/ч")
class SportCar(Car):
    pass
class PoliceCar(Car):
    pass
car_1 = TownCar("TownCar", 70, "red", False)
car_2 = WorkCar("WorkCar", 30, "green", False)
car_3 = SportCar("SportCar", 90, "blue", False)
car_4 = PoliceCar("PoliceCar", 80, "white", True)
print(f"Тип машины: {car_1.name}; Скорость: {car_1.speed}; Цвет: {car_1.color}; Машина полиции: {car_1.is_police}")
print(f"Тип машины: {car_2.name}; Скорость: {car_2.speed}; Цвет: {car_2.color}; Машина полиции: {car_2.is_police}")
print(f"Тип машины: {car_3.name}; Скорость: {car_3.speed}; Цвет: {car_3.color}; Машина полиции: {car_3.is_police}")
print(f"Тип машины: {car_4.name}; Скорость: {car_4.speed}; Цвет: {car_4.color}; Машина полиции: {car_4.is_police}")
car_1.go()
car_1.stop()
car_1.turn("налево")
car_1.show_speed()
car_2.show_speed()
