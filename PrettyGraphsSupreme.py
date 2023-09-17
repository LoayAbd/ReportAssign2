import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file into a Pandas DataFrame
file_path = 'BzipLowEndClock.csv'
second_file = 'BzipLowEndLru.csv'# Replace with your CSV file path
third_file = "BzipLowEndRand.csv"
high_end_one = "BzipHighEndClock.csv"
high_end_two = "BzipHighEndLru.csv"
high_end_three = "BzipHighEndRand.csv"
df = pd.read_csv(file_path)
df2 = pd.read_csv(second_file)
df3 = pd.read_csv(third_file)
df4 = pd.read_csv(high_end_one)
df5 = pd.read_csv(high_end_two)
df6 = pd.read_csv(high_end_three)

# Assuming the first row contains data for one axis and the second row for another axis
x_data = df.iloc[:, 0].values
y_data = df.iloc[:, 4].values
lru_x_data = df2.iloc[:, 0].values
lru_y_data = df2.iloc[:, 4].values
rand_x_data = df3.iloc[:, 0].values
rand_y_data = df3.iloc[:, 4].values
high_clock_x_data = df4.iloc[:,0].values
high_clock_y_data = df4.iloc[:,4].values
high_lru_x_data = df5.iloc[:,0].values
high_lru_y_data = df5.iloc[:,4].values
high_rand_x_data = df6.iloc[:,0].values
high_rand_y_data = df6.iloc[:,4].values

# Create a Seaborn plot
sns.set(style="whitegrid")
plt.figure(figsize=(50, 25))
sns.scatterplot(x=x_data, y=y_data, marker='o', s=100)
sns.lineplot(x=x_data, y=y_data , marker='o')
sns.scatterplot(x=lru_x_data, y=lru_y_data, marker='o', s=100)
sns.lineplot(x=lru_x_data, y=lru_y_data, marker='o')
sns.scatterplot(x=rand_x_data, y=rand_y_data, marker='o', s=100)
sns.lineplot(x=rand_x_data, y=rand_y_data, marker='o')
sns.scatterplot(x=high_clock_x_data, y=high_clock_y_data, marker='o', s=100)
sns.lineplot(x=high_clock_x_data, y=high_clock_y_data, marker='o')
sns.scatterplot(x=high_lru_x_data, y=high_lru_y_data, marker='o', s=100)
sns.lineplot(x=high_lru_x_data, y=high_lru_y_data, marker='o')
sns.scatterplot(x=high_rand_x_data, y=high_rand_y_data, marker='o', s=100)
sns.lineplot(x=high_rand_x_data, y=high_rand_y_data, marker='o')
plt.xlabel("Number of Frames")
plt.ylabel("Page fault rate")
plt.title("Fault rate comparison to frame number Plot")
plt.legend(labels = [None , 'Low end clock' , None , None, 'Low end lru',None,None,'Low end rand' , None , None , 'High end clock', None , None , 'High End Lru' , None , None , 'High end rand'])

# save plot as svg file.
plt.savefig("pretty_plot_Bzip.svg", format="svg")

# Show the plot
plt.show()
