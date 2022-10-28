import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.YlOrBr, s=10)

ax.set_title('Квадрати чисел', fontsize=24)
ax.set_xlabel('Величина', fontsize=14)
ax.set_ylabel('Квадрат величини', fontsize=14)

ax.tick_params(axis='both', labelsize=14)

# Задати діапазон для кожної осі
ax.axis([0, 1100, 0, 1100000])  # ax.axis([min_x, max_x, min_y, max_y])

plt.savefig('squares_plot.png', bbox_inches='tight')  # Збереження діаграми в файл, де:
# plt.savefig("ім'я файлу", bbox_inches='tight' -> видаляє зайвий пробільний простір (можна не вказувати)
