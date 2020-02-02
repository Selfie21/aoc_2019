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
