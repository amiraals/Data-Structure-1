import matplotlib.pyplot as plt
import pandas as pd

data = {
    "n": [0, 20, 50, 100, 200, 300, 400],
    "Iterative": [0.000002, 0.000008, 0.000012, 0.000021, 0.000038, 0.000052, 0.000075],
    "Recursive": [0.00, 0.000009, 0.000016, 0.000047, 0.000103, 0.000169, 0.000243],
    "Sort by Weight": [0.00, 0.000041, 0.000107, 0.000261, 0.000496, 0.000828, 0.001010],
    "Sort by Price": [0.00, 0.000035, 0.000097, 0.000244, 0.000496, 0.000854, 0.000981],
}

# Creating DataFrame from the data
df = pd.DataFrame(data)
methods = df.columns[1:]

# Defining the plot function
def plot_method_performance(df, method_name):
    plt.figure(figsize=(10, 5))
    plt.plot(df['n'], df[method_name], 'o-', label=method_name)
    plt.xlabel('Number of Students (n)')
    plt.ylabel('Time (seconds)')
    plt.title(f'Time Complexity of {method_name} Method')
    plt.legend()
    plt.grid(True)
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.show()

# Iterating over each method and ploting it using the defined function
for method in methods:
    plot_method_performance(df, method)