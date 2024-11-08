import pandas as pd

# Чтение данных из файла
file_path = 'transactoins.csv'  # Замените на имя вашего файла
data = pd.read_csv(r"C:\Users\dimab\OneDrive\Desktop\transactions.csv",encoding="utf-8")

# Задача 1: Найти 3 самых крупных платежа со статусом "OK"
top_3_payments = data[data['STATUS'] == 'OK'].nlargest(3, 'SUM')
print("Три самых крупных платежа со статусом OK:")
print(top_3_payments)

# Задача 2: Определить полную сумму платежей со статусом "OK" для компании "Umbrella, Inc"
umbrella_sum_ok = data[(data['CONTRACTOR'] == 'Umbrella, Inc') & (data['STATUS'] == 'OK')]['SUM'].sum()
print("\nПолная сумма реально проведённых платежей в адрес Umbrella, Inc:", umbrella_sum_ok)
