# 3. Реализовать базовый класс Worker (работник).
#
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
# (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 0, "bonus": 0}
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position)
        self._income["wage"] = wage
        self._income["bonus"] = bonus
    def get_full_name(self):
        print(f"Полное имя сотрудника: {self.surname} {self.name}")
    def get_total_income(self):
        income = self._income["wage"] + self._income["bonus"]
        print(f"Доход с учётом премии: {income}")

job = Position("Иван", "Иванов", "Рабочее место", 10000, 2000)
print(job.name)
print(job.surname)
print(job.position)
print(job._income)
job.get_full_name()
job.get_total_income()
