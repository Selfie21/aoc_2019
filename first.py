from utility import Utility

f = open("first.txt", "r")
inputs = Utility.read_linestxt(f)
first = second = 0

for x in inputs:
    s = int(x)
    first += int(s / 3) - 2


for x in inputs:
    s = int(x)
    while int(s / 3) - 2 > 0:
        s = int(s / 3) - 2
        second += s

Utility.print_solution(first, second)
