import control
import numpy as np
import matplotlib.pyplot as plt
import tbcontrol
tbcontrol.expectversion("0.1.10")

Greal = control.TransferFunction([1, 2], [2, 3, 4, 1])
ts, ys = control.step_response(Greal)
yinitial = 10
measurement_noise = np.random.randn(len(ys)) * 0.05
ym = ys + yinitial + measurement_noise

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(ts, ym, color='steelblue')
ax.plot(ts, ys + yinitial, color='deepskyblue', linewidth=3)
ax.set(xlabel='Часові моменти ts', ylabel='Змішана відповідь системи ym',
       title='Залежність № 1')
ax.grid(True)


if __name__ == "__main__":
    fig.savefig("plot_1.png")
    plt.show()

