data = {}
with open('dataset_3380_5.txt') as f:
    for line in f:
        cls, _, h = line.split()
        cls, h = int(cls), int(h)
        data[cls] = data.get(cls, [0, 0])
        data[cls][0] += h
        data[cls][1] += 1

with open('output.txt', 'w') as f:
    for c in range(1, 12):
        if c in data:
            f.write(f"{c} {data[c][0] / data[c][1]}\n")
        else:
            f.write(f"{c} -\n")