
depths = []

with open("data.txt") as f:
    depths = list(int(l.strip()) for l in f.readlines())

depth = sum(r - l > 0 for (l, r) in zip(depths[:-1], depths[1:]))

print(depth)

