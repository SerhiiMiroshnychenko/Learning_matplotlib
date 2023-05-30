import mysql.connector
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Підключення до бази даних
cnx = mysql.connector.connect(
    host='ваш хост',
    user='ваш користувач',
    password='ваш пароль',
    database='ваша база даних'
)

# Створення курсора для виконання запитів
cursor = cnx.cursor()

# Виконання запиту SELECT
query = "SELECT time FROM time_db ORDER BY time ASC"
cursor.execute(query)

# Отримання результатів запиту
results = cursor.fetchall()

# Закриття курсора та з'єднання з базою даних
cursor.close()
cnx.close()

# Створення списку об'єктів datetime з результатів запиту
times = [datetime.strptime(result[0], "%H:%M:%S") for result in results]

# Обчислення різниці в секундах між кожним часом і попереднім часом
differences = [(times[i] - times[i-1]).total_seconds()
               for i in range(1, len(times))]

# Побудова стовпчикової діаграми
x = range(len(differences))
plt.bar(x, differences)

# Налаштування міток осі X
labels = [time.strftime("%H:%M:%S") for time in times[1:]]
plt.xticks(x, labels, rotation='vertical')

# Налаштування заголовка та осі Y
plt.title("Різниця в секундах між часами")
plt.ylabel("Різниця (секунди)")

# Показ діаграми
plt.show()