class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def cover_asphalt(self, mass, thick):
        return self._length * self._width * mass * thick


track = Road(2000, 30)
print(track._length)
print(track._width)
print(track.cover_asphalt(25, 5))
