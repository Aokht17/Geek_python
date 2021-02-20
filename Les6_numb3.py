class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'full name is {self.name} {self.surname}')

    def get_total_income(self):
        return self._income['wage'] * 12 + self._income['bonus']


worker_1 = Position('Vasya', 'Pupkin', 'manager', 60, 20)
print(worker_1.name, worker_1.surname, worker_1.position, worker_1._income)
worker_1.get_full_name()
print(worker_1.get_total_income())
