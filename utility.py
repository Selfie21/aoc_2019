class Utility:

    @staticmethod
    def read_commastxt(line):
        inputs = []
        for number in line.split(','):
            inputs.append(int(number))
        return inputs

    @staticmethod
    def read_linestxt(file):
        return file.read().splitlines()

    @staticmethod
    def print_solution(first, second):
        print("First: " + str(first) + ", Second " + str(second))

    @staticmethod
    def enlarge_list(offset, list):
        for i in range(offset):
            list.append(0)

    @staticmethod
    def moon_parser(file):
        moons = []
        for moon in file.read().splitlines():
            coordinates = []
            for _ in range(3):
                cut_first = moon.find('=')
                cut_last = moon.find(',')
                num = moon[cut_first + 1:cut_last]
                moon = moon[cut_last + 1:]
                coordinates.append(int(num))
            moons.append(coordinates)
        return moons
