import matplotlib.pyplot as plt

from random_walk import RandomWalk


rw = RandomWalk(150_000)  # Створюємо екземпляр класу RandomWalk
rw.fill_walk()  # Викликаємо метод fill_walk
# Нанести на графік точки блукання
plt.style.use('Solarize_Light2')  # Задаємо стиль
fig, ax = plt.subplots(figsize=(12, 9))
point_numbers = range(rw.num_points)  # Генеруємо послідовність чисел, довжиною в кількість точок блукання
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.cividis, edgecolor='none', s=1)
# edgecolor='none' -- позбавляємося чорних контурів навколо кожної точки
# Передаємо значення координат методові scatter

# Виокремити першу та останню точки
ax.scatter(0, 0, color=(0.15, 0.45, 0.65), edgecolor='none', s=50)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='yellow', edgecolor='none', s=100)

# Приховати осі
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)


plt.show()
