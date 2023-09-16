import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file into a Pandas DataFrame
file_path = 'clock.csv'
second_file = 'Lru.csv'# Replace with your CSV file path
third_file = "Rand.csv"
df = pd.read_csv(file_path)
df2 = pd.read_csv(second_file)
df3 = pd.read_csv(second_file)

# Assuming the first row contains data for one axis and the second row for another axis
x_data = df.iloc[:, 0].values
y_data = df.iloc[:, 4].values
lru_x_data = df2.iloc[:, 0].values
lry_y_data = df2.iloc[:, 4].values
rand_x_data = df3.iloc[:, 0].values
rand_y_data = df3.iloc[:, 4].values
# Create a Seaborn plot
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.scatterplot(x=x_data, y=y_data, marker='o', s=100)
sns.lineplot(x=x_data, y=y_data, marker='o')

sns.scatterplot(x=lru_x_data, y=lru_y_data, marker='o', s=100)
sns.lineplot(x=lru_x_data, y=lru_y_data, marker='o')
sns.scatterplot(x=rand_x_data, y=rand_y_data, marker='o', s=100)
sns.lineplot(x=rand_x_data, y=rand_y_data, marker='o')

plt.xlabel("Number of Frames")
plt.ylabel("Page fault rate")
plt.title("2D Scatter Plot")

# Show the plot
plt.show()
