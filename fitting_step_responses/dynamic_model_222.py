import scipy.optimize
from tbcontrol.responses import fopdt, sopdt
import matplotlib.pyplot as plt
from dynamic_model_111 import ts, ym


[K, tau, theta, y0], _ = scipy.optimize.curve_fit(fopdt, ts, ym, [2, 4, 1, 10])
print([K, tau, theta, y0])

[K_2, tau_2, zeta_2, theta_2, y0_2], _ = scipy.optimize.curve_fit(sopdt, ts, ym, [2, 2, 1.5, 1, 10])
print([K_2, tau_2, zeta_2, theta_2, y0_2])

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(ts, ym, color='steelblue', label='Data')
ax.plot(ts, fopdt(ts, K, tau, theta, y0), color='orange', label='FOPDT fit')
ax.plot(ts, sopdt(ts, K_2, tau_2, zeta_2, theta_2, y0_2), color='gold', label='SOPDT fit')
try:
    plt.legend(loc='best')
except Exception as e:
    print(e.__class__, e)
ax.set(xlabel='Часові моменти ts', ylabel='Відповідь системи',
       title='Залежність № 2')
ax.grid(True)


if __name__ == "__main__":
    fig.savefig("plot_2.png")
    plt.show()
