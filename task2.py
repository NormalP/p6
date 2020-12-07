class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height / 1000
        print(f'you need {round(asphalt_mass)}ton of asphalt ')


r = Road(int(input()),int(input()))
r.asphalt_mass()