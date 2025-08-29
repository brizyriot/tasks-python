word_count = {}
with open('dataset_3363_3.txt', 'r') as f:
    for line in f:
        words = line.strip().lower().split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

# Находим слово с максимальным счётчиком, при равенстве — лексикографически первое
most_frequent = min(word_count, key=lambda x: (-word_count[x], x))
print(most_frequent, word_count[most_frequent])