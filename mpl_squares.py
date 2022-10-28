import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Викликаємо функцію subplots(піддіаграми)
fig, ax = plt.subplots()  # fig - увесь набір діаграм; ax - репрезентує одну діаграму
ax.plot(input_values, squares, linewidth=3)  # Метод plot - будує діаграму на основі переданих даних
# linewidth - товщина лінії

# Задати назву для графіка та кожної осі
ax.set_title('Квадрати чисел', fontsize=24)  # Назва діаграми. fontsize - розмір шрифту.
ax.set_xlabel('Величина', fontsize=14)  # Назва осі х
ax.set_ylabel('Квадрат величини', fontsize=14)  # Назва осі у

# Задати розмір шрифту для підписів на розмітці
ax.tick_params(axis='both', labelsize=14)

plt.show()  # Відкриває переглядач
