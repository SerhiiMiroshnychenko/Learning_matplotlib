import control
import matplotlib.pyplot as plt
import tbcontrol
import pandas as pd

tbcontrol.expectversion("0.1.10")

Greal = control.TransferFunction([1, 2], [2, 3, 4, 1])

# Зчитування даних з файлу Excel
data = pd.read_excel('data.xlsx', header=None)
ts = data.iloc[0].tolist()  # Перший рядок - ts
ym = data.iloc[1].tolist()  # Другий рядок - ym
print(f'{ts=}')
print(len(ts))
print(f'{ym=}')
print(len(ym))

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(ts, ym, color='steelblue')
ax.plot(ts, ym, color='deepskyblue', linewidth=3)
ax.set(xlabel='Часові моменти ts', ylabel='Змішана відповідь системи ym',
       title='Залежність № 1')
ax.grid(True)


if __name__ == "__main__":
    fig.savefig("plot_1.png")
    plt.show()

