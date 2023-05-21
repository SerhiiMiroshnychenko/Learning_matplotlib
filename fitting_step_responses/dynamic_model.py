import control
import numpy as np
import matplotlib.pyplot as plt
import tbcontrol
import scipy.optimize
from tbcontrol.responses import fopdt, sopdt
from ipywidgets import interact

tbcontrol.expectversion("0.1.10")
Greal = control.TransferFunction([1, 2], [2, 3, 4, 1])
ts, ys = control.step_response(Greal)
yinitial = 10
measurement_noise = np.random.randn(len(ys)) * 0.05
ym = ys + yinitial + measurement_noise

def show_1():
    plt.scatter(ts, ym)
    plt.plot(ts, ys + yinitial, color='red')
    plt.show()


def resultplot(K, tau, theta, y0):
    plt.scatter(ts, ym)
    plt.plot(ts, fopdt(ts, K, tau, theta, y0), color='red')
    plt.show()

interact(resultplot,
         K=(1., 10.),
         tau=(0., 10.),
         theta=(0., 10.),
         y0=(0., 20.))

[K, tau, theta, y0], _ = scipy.optimize.curve_fit(fopdt, ts, ym, [2, 4, 1, 10])
print([K, tau, theta, y0])

[K_2, tau_2, zeta_2, theta_2, y0_2], _ = scipy.optimize.curve_fit(sopdt, ts, ym, [2, 2, 1.5, 1, 10])
print([K_2, tau_2, zeta_2, theta_2, y0_2])


def show_2():
    plt.figure(figsize=(10, 5))
    plt.scatter(ts, ym, label='Data')
    plt.plot(ts, fopdt(ts, K, tau, theta, y0), color='red', label='FOPDT fit')
    plt.plot(ts, sopdt(ts, K_2, tau_2, zeta_2, theta_2, y0_2), color='green', label='SOPDT fit')
    plt.plot(ts, ys + 10, color='blue', label='Original')
    plt.legend(loc='best')
    plt.show()



if __name__ == "__main__":
    show_1()
    show_2()