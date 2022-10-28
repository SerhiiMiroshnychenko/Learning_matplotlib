import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)  # Де s - розмір точки

ax.set_title('Квадрати чисел', fontsize=24)
ax.set_xlabel('Величина', fontsize=14)
ax.set_ylabel('Квадрат величини', fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()
