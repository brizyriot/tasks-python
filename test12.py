import re

def decode_string(compressed):
    return re.sub(r'(\D)(\d+)', lambda m: m.group(1) * int(m.group(2)), compressed)

with open('dataset_3363_2.txt', 'r') as f:
    compressed = f.read().strip()

decoded = decode_string(compressed)

with open('output.txt', 'w') as f:
    f.write(decoded)