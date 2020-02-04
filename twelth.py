from utility import Utility


class Moontracker:

    def __init__(self, positions, velocities):
        self.positions = positions
        self.velocities = velocities

    def get_velocity(self, first_moon, second_moon):
        if first_moon < second_moon:
            return 1
        elif first_moon > second_moon:
            return -1
        elif first_moon == second_moon:
            return 0

    def update_velocity(self):
        for moon_index, moon in enumerate(self.positions):
            for i in range(3):
                for comparators in self.positions:
                    velocity = self.get_velocity(moon[i], comparators[i])
                    self.velocities[moon_index][i] += velocity

    def update_positions(self):
        for moon_index, moon in enumerate(self.positions):
            for i in range(3):
                moon[i] += self.velocities[moon_index][i]

    def get_energy(self):
        total = 0
        for moon_index, moon in enumerate(self.positions):
            position = 0
            velocity = 0
            for i in range(3):
                position += abs(moon[i])
                velocity += abs(self.velocities[moon_index][i])
            total += (position * velocity)
        return total


f = open("twelth.txt", "r")
moon_position = Utility.moon_parser(f)
moon_velocity = [[0 for x in range(3)] for y in range(4)]
tracker = Moontracker(moon_position, moon_velocity)
second = 0
status = set()
while True:
    tracker.update_velocity()
    tracker.update_positions()

    configuration = ()
    for moon_index, moon in enumerate(moon_position):
        x, y, z = moon[0], moon[1], moon[2]
        xv, yv, zv = moon_velocity[moon_index][0], moon_velocity[moon_index][1], moon_velocity[moon_index][2]
        moon_status = (x, y, z, xv, yv, zv)
        configuration += moon_status
    if configuration in status:
        break
    else:
        status.add(configuration)
        second += 1

first = tracker.get_energy()
Utility.print_solution(first, second)
