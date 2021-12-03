
moves = []

with open("moves.txt") as f:
    moves = list((line.split()[0], int(line.split()[1])) for line in f.readlines())

forward = 0
depth = 0
for (move, dist) in moves:
    if move == "forward":
        forward += dist
    elif move == "up":
        depth -= dist
    elif move == "down":
        depth += dist
    else: 
        print("Malformed input on: ", move, dist)
        exit(1)

print(forward*depth)

