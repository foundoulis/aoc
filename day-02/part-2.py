
moves = []

with open("moves.txt") as f:
    moves = list((line.split()[0], int(line.split()[1])) for line in f.readlines())

forward = 0
depth = 0
aim = 0
for (move, dist) in moves:
    if move == "down":
        aim += dist
    elif move == "up":
        aim -= dist
    elif move == "forward":
        forward += dist
        depth += aim*dist
    else: 
        print("Malformed input on: ", move, dist)
        exit(1)

print(forward*depth)

