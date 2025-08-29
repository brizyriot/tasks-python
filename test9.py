import requests

# Базовый URL
base_url = "https://stepik.org/media/attachments/course67/3.6.3/"

# Начальный файл
current_file = "699991.txt"

# Цикл для перехода по цепочке файлов
while True:
    print(f"Чтение файла: {current_file}")
    response = requests.get(base_url + current_file)
    response.raise_for_status()
    content = response.text.strip()

    # Проверяем, начинается ли содержимое с "We"
    if content.startswith("We"):
        print("Достигнут последний файл.")
        break

    # Иначе — содержимое указывает имя следующего файла
    current_file = content

# Выводим содержимое последнего файла
print(content)