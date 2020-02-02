from utility import Utility

f = open("third.txt", "r")
A = Utility.read_commastxt(f.readline())
B = Utility.read_commastxt(f.readline())

DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}


def get_points(A):
    x = 0
    y = 0
    length = 0
    ans = {}
    for cmd in A:
        d = cmd[0]
        n = int(cmd[1:])

        for _ in range(n):
            x += DX[d]
            y += DY[d]
            length += 1
            if (x, y) not in ans:
                ans[(x, y)] = length
    return ans


PA = get_points(A)
PB = get_points(B)
both = set(PA.keys()) & set(PB.keys())
part1 = min([abs(x) + abs(y) for (x, y) in both])
part2 = min([PA[p] + PB[p] for p in both])
Utility.print_solution(int(part1, part2))
