class Stationery:
    def __init__(self, title='Thing to draw'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой.')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом.')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером.')


a = Stationery()
a.draw()
b = Pen('Pen')
b.draw()
c = Pencil('Pencil')
c.draw()
d = Handle('Handle')
d.draw()
