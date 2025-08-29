# Имя входного файла (часто в заданиях Stepik — dataset_3363_4.txt)
input_filename = 'dataset_3363_4.txt'  # замените при необходимости

students = []
subjects_total = [0, 0, 0]  # суммы по математике, физике, русскому
count = 0

with open(input_filename, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(';')
        surname = parts[0]
        math = int(parts[1])
        physics = int(parts[2])
        russian = int(parts[3])
        
        # Средняя по студенту
        student_avg = (math + physics + russian) / 3
        students.append(student_avg)
        
        # Накопление сумм по предметам
        subjects_total[0] += math
        subjects_total[1] += physics
        subjects_total[2] += russian
        count += 1

# Средние по предметам
math_avg = subjects_total[0] / count
physics_avg = subjects_total[1] / count
russian_avg = subjects_total[2] / count

# Запись результата в файл
with open('output.txt', 'w') as f:
    for avg in students:
        f.write(f"{avg}\n")
    f.write(f"{math_avg} {physics_avg} {russian_avg}\n")