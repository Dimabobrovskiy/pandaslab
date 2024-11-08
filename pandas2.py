import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из файла
file_path = 'flights.csv'  # Замените на имя вашего файла
data = pd.read_csv(r"C:\Users\dimab\OneDrive\Desktop\flights.csv",encoding="utf-8")

# Группировка данных по авиакомпании и расчёт необходимых значений
summary = data.groupby('CARGO').agg(
    flights=('CARGO', 'size'),
    total_price=('PRICE', 'sum'),
    total_weight=('WEIGHT', 'sum')
).reset_index()

print("Сводная информация о рейсах для каждой авиакомпании:")
print(summary)

# Построение графиков
fig, ax1 = plt.subplots(1, 2, figsize=(14, 6))

# График количества рейсов
ax1[0].bar(summary['CARGO'], summary['flights'], color='skyblue')
ax1[0].set_title('Количество рейсов по авиакомпаниям')
ax1[0].set_xlabel('Авиакомпания')
ax1[0].set_ylabel('Количество рейсов')

# График общей стоимости и массы грузов
ax1[1].bar(summary['CARGO'], summary['total_price'], label='Стоимость', alpha=0.6, color='green')
ax1[1].bar(summary['CARGO'], summary['total_weight'], label='Масса', alpha=0.6, color='orange')
ax1[1].set_title('Общая стоимость и масса грузов по авиакомпаниям')
ax1[1].set_xlabel('Авиакомпания')
ax1[1].set_ylabel('Значение')
ax1[1].legend()

plt.tight_layout()
plt.show()
