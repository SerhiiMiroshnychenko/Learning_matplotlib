import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Створити випадкове блукання поки діаграма активна
for k in range(20):
    rw = RandomWalk(250_000)  # Створюємо екземпляр класу RandomWalk
    rw.fill_walk()  # Викликаємо метод fill_walk
    # Нанести на графік точки блукання
    plt.style.use('dark_background')  # Задаємо стиль
    fig, ax = plt.subplots(figsize=(24, 12))  # figsize=(12, 9) -- Задаємо розмір вікна в дюймах

    ax.axis('off')  # Прибираємо рамку та осі

    point_numbers = range(rw.num_points)  # Генеруємо послідовність чисел, довжиною в кількість точок блукання
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.ocean, edgecolor='none', s=1)
    # edgecolor='none' -- позбавляємося чорних контурів навколо кожної точки
    # Передаємо значення координат методові scatter

    file_name = f'{k}_2.png'
    plt.savefig(f"C:/Users/admin/Desktop/Plots/{file_name}", bbox_inches='tight')
