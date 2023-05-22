"""
Часто розробка першоосновних моделей процесів є надзвичайно дорогою,
тому дуже часто оцінювати передатні функції низького порядку безпосередньо
з даних підприємства. Це легко зробити, якщо ми маємо доступ до результатів
покрокових тестів.
"""
import control
import numpy as np
import matplotlib.pyplot as plt
import tbcontrol
tbcontrol.expectversion("0.1.10")

# Почнемо з процесу вищого порядку, щоб створити наші «справжні дані»
Greal = control.TransferFunction([1, 2], [2, 3, 4, 1])
# Ця стрічка коду створює об'єкт Greal, який представляє
# передаточну функцію системи у форматі керованої бібліотеки (control library).
# control.TransferFunction() - це конструктор класу TransferFunction
# з бібліотеки control, який дозволяє створювати об'єкти, що представляють
# передаточні функції.
# У даному випадку передаточна функція Greal визначена за допомогою
# двох списків: [1, 2] як чисельник та [2, 3, 4, 1] як знаменник.
# Це означає, що передаточна функція має вигляд (s + 1) / (s^3 + 2s^2 + 3s + 4),
# де s - це змінна Лапласа.
# Отриманий об'єкт Greal можна використовувати для подальшого аналізу
# та моделювання системи з цією передаточною функцією.

ts, ys = control.step_response(Greal)
# Ця стрічка коду викликає функцію step_response() з бібліотеки control
# для обчислення часової відповіді системи з передаточною функцією Greal.
# Результат функції step_response() повертає два значення: ts і ys.
# ts - це масив, який містить часові моменти, на яких проводиться вимірювання
# часової відповіді системи.
# ys - це масив, який містить значення відповіді системи на кожен часовий момент t.
# Отримані значення t і y можна використовувати для подальшого аналізу та
# візуалізації часової відповіді системи.

# Пам’ятайте, що реальні дані не обов’язково починатимуться з нуля,
# тому ми додамо деяке значення для початкового результату. Ми також
# додамо деякий нормально розподілений шум, щоб представити похибку вимірювання.

yinitial = 10
# За допомогою цього рядка встановлюється початкове значення yinitial,
# яке використовується пізніше в обчисленнях
# значення yinitial використовується для зміщення часової відповіді
# y та відображення змішаної відповіді ym.

measurement_noise = np.random.randn(len(ys)) * 0.05
# Рядок коду measurement_noise = np.random.randn(len(y)) * 0.05
# генерує випадковий шум (measurement_noise) для додавання до часової відповіді y системи.
# Ось як працює цей рядок:
# np.random.randn(len(y)) генерує масив випадкових чисел,
# розподілених за нормальним законом, з розміром, що відповідає довжині масиву y.
# * 0.05 множить кожне випадкове число на 0.05, зменшуючи амплітуду шуму.
# Отриманий шум (measurement_noise) потім додається до часової відповіді y,
# щоб отримати змішану відповідь (ym), яка враховує початкове
# значення (yinitial) та шум вимірювання. Це допомагає змоделювати реальні
# умови зі змішаними вимірюваннями та початковим значенням.

ym = ys + yinitial + measurement_noise
# Рядок коду ym = y + yinitial + measurement_noise обчислює змішану
# відповідь системи ym, додавши до часової відповіді y початкове
# значення yinitial та шум вимірювання measurement_noise.
# Ось як працює цей рядок:
# y - це часова відповідь системи, отримана з попереднього обчислення.
# yinitial - це початкове значення, яке було встановлене раніше у коді.
# measurement_noise - це випадковий шум, який був згенерований для вимірювання.
# Результатом цього рядка коду є змішана відповідь ym, яка включає початкове
# значення та шум вимірювання, що додаються до часової відповіді системи.
# Це дозволяє моделювати реальні умови з початковим значенням та шумом
# вимірювання, що можуть впливати на отримані дані.


plt.scatter(ts, ym)
plt.plot(ts, ys + yinitial, color='red')

if __name__ == "__main__":
    plt.show()
