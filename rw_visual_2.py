import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Створити випадкове блукання поки діаграма активна
while True:
    rw = RandomWalk()  # Створюємо екземпляр класу RandomWalk
    rw.fill_walk()  # Викликаємо метод fill_walk
    # Нанести на графік точки блукання
    plt.style.use('Solarize_Light2')  # Задаємо стиль
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)  # Генеруємо послідовність чисел, довжиною в кількість точок блукання
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.copper, edgecolor='none', s=15)
    # edgecolor='none' -- позбавляємося чорних контурів навколо кожної точки
    # Передаємо значення координат методові scatter

    # Виокремити першу та останню точки
    ax.scatter(0, 0, c='brown', s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='brown', edgecolor='none', s=100)
    plt.show()

