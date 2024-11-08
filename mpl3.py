import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset and specify the separator
data = pd.read_csv(r'C:\Users\dimab\OneDrive\Desktop\students.csv', header=None, names=['Student', 'Group', 'Mark'], sep=';', dtype={'Student': str, 'Group': str, 'Mark': str})

# Convert the 'Mark' column to numeric, setting errors='coerce' to handle non-numeric values
data['Mark'] = pd.to_numeric(data['Mark'], errors='coerce')

# Drop any rows where 'Mark' could not be converted to a number
data.dropna(subset=['Mark'], inplace=True)
data['Mark'] = data['Mark'].astype(int)

# Create the first plot - distribution of marks per prep (student)
marks_per_prep = data.pivot_table(index='Student', columns='Mark', aggfunc='size', fill_value=0)
marks_per_prep.plot(kind='bar', stacked=True, colormap='tab20', figsize=(10, 6))
plt.title('Marks per prep')
plt.xlabel('Prep')
plt.ylabel('Count')
plt.legend(title='Marks')
plt.show()

# Create the second plot - distribution of marks per group
marks_per_group = data.pivot_table(index='Group', columns='Mark', aggfunc='size', fill_value=0)
marks_per_group.plot(kind='bar', stacked=True, colormap='tab20', figsize=(10, 6))
plt.title('Marks per group')
plt.xlabel('Group')
plt.ylabel('Count')
plt.legend(title='Marks')
plt.show()
