from collections import defaultdict

bin_values = []
count = defaultdict(int)
bin_len = None
total_lines = None

with open("data.txt") as f:
    bin_values = list(line.strip() for line in f.readlines())
    bin_len = len(bin_values[0])
    total_lines = len(bin_values)

for line in bin_values:
    for index, bit in enumerate(line):
        if bit == "0":
            pass
        elif bit == "1":
            count[index] += 1
        else:
            print("Unhandled input at: ", line, bit)
            exit(1)

gamma_rate = []
epsilon_rate = []
for index in range(bin_len):
    if count[index] > total_lines//2:
        gamma_rate.append("1")
        epsilon_rate.append("0")
    else:
        gamma_rate.append("0")
        epsilon_rate.append("1")

print(int("".join(gamma_rate), 2)*int("".join(epsilon_rate), 2))

