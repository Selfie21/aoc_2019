def read_linestxt(file):
    return file.read().splitlines()


def print_solution(first, second):
    print("First: " + str(first) + ", Second " + str(second))


f = open("first.txt", "r")
inputs = read_linestxt(f)
first = second = 0

for x in inputs:
    s = int(x)
    first += int(s / 3) - 2


for x in inputs:
    s = int(x)
    while int(s / 3) - 2 > 0:
        s = int(s / 3) - 2
        second += s

print_solution(first, second)
