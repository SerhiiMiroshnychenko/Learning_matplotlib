import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Створити випадкове блукання поки діаграма активна
while True:
    rw = RandomWalk()  # Створюємо екземпляр класу RandomWalk
    rw.fill_walk()  # Викликаємо метод fill_walk
    # Нанести на графік точки блукання
    plt.style.use('seaborn-v0_8')  # Задаємо стиль
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, c="gray", s=15)
    # Передаємо значення координат методові scatter
    plt.show()

