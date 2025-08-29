# объявление функции
def draw_triangle():
    for i in range(8):
        spaces = ' ' * (7 - i)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

# основная программа
draw_triangle()  # вызов функции