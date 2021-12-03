
depths = []

with open("data.txt") as f:
    depths = list(int(l.strip()) for l in f.readlines())

three_sum = 0
previous = None
for (a, b, c) in zip(depths[:-2], depths[1:-1], depths[2:]):
    current = a + b + c
    if previous is not None and current > previous:
        three_sum += 1
    previous = current

print(three_sum)

