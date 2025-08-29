import requests

# Читаем URL из файла
with open('dataset_3378_2.txt', 'r') as f:
    url = f.read().strip()

# Скачиваем файл по URL
response = requests.get(url)
text = response.text

# Подсчитываем количество строк
line_count = len(text.splitlines())

# Выводим результат (можно записать в файл или вывести на экран)
print(line_count)