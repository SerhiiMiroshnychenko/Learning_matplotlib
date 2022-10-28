from random import choice


class RandomWalk:
    """Клас, що генерує випадкове блукання"""

    def __init__(self, num_points=5000):
        """Ініціалізувати атрибути блукання"""
        self.num_points = num_points
        # Всі блукання починаються з (0, 0)
        self.x_values = 0
        self.y_values = 0

    def fill_walk(self):
        """Обчислити всі точки блукання"""
        # Продовжити робити кроки, поки блукання не досягне необхідної довжини
        while len(self.x_values) < self.num_points:

            # Вирішити, в якому напрямку рухатися та як довго
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Відкинути кроки, що нікуди не просувається
            if x_step == 0 and y_step == 0:
                continue

            # Розрахувати нову позицію
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

