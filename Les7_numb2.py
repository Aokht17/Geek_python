import math


class Cloth:
    def __init__(self, name, size_height, cloth_type):
        self.name = name
        self.size = size_height
        self.cloth_type = cloth_type

    @property
    def fabric_waste(self):
        if self.cloth_type == 'suit':
            self.__fabric = 2 * self.size + 0.3
        elif self.cloth_type == 'coat':
            self.__fabric = self.size / 6.5 + 0.5
        else:
            return f'no formula for counting fabric consumption for {self.cloth_type}'
        return f'About {math.ceil(self.__fabric)}m is required for {self.name} {self.cloth_type}'


r = Cloth('bizarr', 48, 'coat')
print(r.name)
print(r.size)
print(r.fabric_waste)

c = Cloth('appel', 1.67, 'suit')
print(c.name)
print(c.size)
print(c.fabric_waste)

d = Cloth('summ', 42, 'dress')
print(d.fabric_waste)
