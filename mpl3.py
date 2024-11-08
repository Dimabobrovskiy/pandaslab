import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\dimab\OneDrive\Desktop\students.csv', header=None, names=['Student', 'Group', 'Mark'], sep=';', dtype={'Student': str, 'Group': str, 'Mark': str})


data['Mark'] = pd.to_numeric(data['Mark'], errors='coerce')

data.dropna(subset=['Mark'], inplace=True)
data['Mark'] = data['Mark'].astype(int)


marks_per_prep = data.pivot_table(index='Student', columns='Mark', aggfunc='size', fill_value=0)
marks_per_prep.plot(kind='bar', stacked=True, colormap='tab20', figsize=(10, 6))
plt.title('Marks per prep')
plt.xlabel('Prep')
plt.ylabel('Count')
plt.legend(title='Marks')
plt.show()

marks_per_group = data.pivot_table(index='Group', columns='Mark', aggfunc='size', fill_value=0)
marks_per_group.plot(kind='bar', stacked=True, colormap='tab20', figsize=(10, 6))
plt.title('Marks per group')
plt.xlabel('Group')
plt.ylabel('Count')
plt.legend(title='Marks')
plt.show()
