import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Results_analysis.csv')
print(df)

OutputFolder = "./plots_analysis"

class MatData:
    def __init__(self, x_axis, y_axis = [], title = 'Matplot', x_label = 'x axis', y_label = 'y axis') -> None:
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.title = title
        self.x_label = x_label
        self.y_label = y_label

def plot_data(df, MatData = MatData, figure_number = '1', save = True):
    fig = plt.figure(figure_number)
    fig.set_size_inches(18, 9)
    plt.plot(df[MatData.x_axis], df[MatData.y_axis], marker='.', label=MatData.y_axis)
    plt.title(MatData.title)
    plt.xlabel(MatData.x_label)
    plt.ylabel(MatData.y_label)
    plt.grid(linestyle='--', alpha=0.7)
    plt.legend()
    if (save == True):
        plt.savefig(f"{OutputFolder}/Fig{figure_number}.png")

def subplot_data(df, d1 = MatData, d2 = MatData, n = '1'):
    fig = plt.figure(n)
    fig.set_size_inches(18, 9)
    plt.subplot(121)
    plot_data(df, d1, n, save=False)
    plt.subplot(122)
    plot_data(df, d2, n, save=False)
    fig.savefig(f"{OutputFolder}/Fig{n}.png")

# x axis initialization
x = 'Block Length'

# Time Analysis Graphs:
y = ['CCMP Encryption Time IEEE', 'CCMP Encryption Time Optimized']
d3 = MatData(x, y, 'Time Analysis', 'Block Length (Blocks)', 'Time (ms)')
# Blk vs (GCMP Enc, GCMP Dec)
y = ['GCMP Encryption Time IEEE', 'GCMP Encryption Time Optimized']
d4 = MatData(x, y, 'Time Analysis', 'Block Length (Blocks)', 'Time (ms)')
subplot_data(df, d3, d4, 1)

y = ['CCMP Decryption Time IEEE', 'CCMP Decryption Time Optimized']
d4 = MatData(x, y, 'Time Analysis', 'Block Length (Blocks)', 'Time (ms)')
# Blk vs (GCMP Enc, GCMP Dec)
y = ['GCMP Decryption Time IEEE', 'GCMP Decryption Time Optimized']
d5 = MatData(x, y, 'Time Analysis', 'Block Length (Blocks)', 'Time (ms)')
subplot_data(df, d4, d5, 2)

plt.show()