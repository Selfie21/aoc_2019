from intcomputer import Intcomputer
from utility import Utility

f = open("eleventh.txt", "r")
inputs_original = Utility.read_commastxt(f.readline())
Utility.enlarge_list(10000, inputs_original)
computer = Intcomputer()


first = computer.execute_intcode(inputs_original.copy())
Utility.print_solution(first, 0)



R = 30
C = 100
G = [[0 for _ in range(C)] for _ in range(R)]
r,c = R//2,C//2
G[r][c] = 1
d = 0
DR = [-1,0,1,0]
DC = [0,1,0,-1]

def get_color():
    return G[r][c]

painted = set()
P = Program('0', '11.in', get_color)
while True:
    color = P.run()
    if color == None:
        break
    assert r>=0
    assert c>=0
    G[r][c] = color
    painted.add((r,c))
    turn = P.run()
    if turn == 0:
        d = (d+3)%4
    else:
        d = (d+1)%4
    r += DR[d]
    c += DC[d]

for r in range(R):
    for c in range(C):
        print('X' if G[r][c]==1 else ' ', end='')
    print()
print(len(painted))
