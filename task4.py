class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'The {self.name} went.'

    def stop(self):
        return f'\nThe {self.name} stopped.'

    def turn(self, direction):
        return f'\nThe {self.name} turned {direction}'

    def show_speed(self):
        return f'\nYour speed is {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nYour speed is higher than allow! Your speed is {self.speed}'
        else:
            return f'Speed of {self.name} is normal'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nYour speed is higher than allow! Your speed is {self.speed}'
        else:
            return f'Speed of {self.name} is normal'


class PoliceCar(Car):
    pass


town = TownCar('Reno', 70, 'blue', False)
print('\n' + town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop())

sport = SportCar('BUHANKA', 1000, 'red', False)
print('\n' + sport.go(), sport.show_speed(), sport.turn('360'), sport.stop())

work = WorkCar('WAZIK', 10, 'red', False)
print('\n' + work.go(), work.show_speed(), work.turn('left'), work.stop())

police = PoliceCar('Mercedes', 100, 'yellow', True)
print('\n' + police.go(), police.show_speed(), police.turn('left'), police.stop())
print(police.is_police)