import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('Results_optimized.csv')
OutputFolder = "./plots_optimized"
print(df)
    

# Avaliable parameter options:
# Block Length
# Entropy Plain Text
# Entropy Cipher Text
# CCMP Entropy MIC
# CCMP Encryption Time
# CCMP Encryption RAM
# CCMP Encryption CPU
# CCMP Decryption Time
# CCMP Decryption RAM
# CCMP Decryption CPU
# GCMP Entropy MIC
# GCMP Encryption Time
# GCMP Encryption RAM
# GCMP Encryption CPU
# GCMP Decryption Time
# GCMP Decryption RAM
# GCMP Decryption CPU

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

# Entropy Analysis Graphs:
# Blk vs (PT, CT)
y = ['Entropy Plain Text', 'Entropy Cipher Text']
d1 = MatData(x, y, 'Entropy Analysis', 'Block Length (Blocks)', 'Entropy')
plot_data(df, d1, 1)
# Blk vs (CCMP MIC, GCMP MIC)
y = ['Entropy Plain Text', 'CCMP Entropy MIC', 'GCMP Entropy MIC']
d2 = MatData(x, y, 'Entropy Analysis', 'Block Length (Blocks)', 'Entropy')
plot_data(df, d2, 2)

# Time Analysis Graphs:
# Blk vs (CCMP Enc, CCMP Dec)
y = ['CCMP Encryption Time', 'CCMP Decryption Time']
d3 = MatData(x, y, 'Time Analysis', 'Block Length (Blocks)', 'Time (ms)')
# Blk vs (GCMP Enc, GCMP Dec)
y = ['GCMP Encryption Time', 'GCMP Decryption Time']
d4 = MatData(x, y, 'Time Analysis', 'Block Length (Blocks)', 'Time (ms)')
subplot_data(df, d3, d4, 3)
# Blk vs (CCMP Enc, GCMP Enc)
y = ['CCMP Encryption Time', 'GCMP Encryption Time']
d5 = MatData(x, y, 'Time Analysis', 'Block Length (Blocks)', 'Time (ms)')
# Blk vs (CCMP Dec, GCMP Dec)
y = ['CCMP Decryption Time', 'GCMP Decryption Time']
d6 = MatData(x, y, 'Time Analysis', 'Block Length (Blocks)', 'Time (ms)')
subplot_data(df, d5, d6, 4)

# Resources Analysis Graphs: CPU ->
# Blk vs (CCMP Enc, CCMP Dec)
y = ['CCMP Encryption CPU', 'CCMP Decryption CPU']
d7 = MatData(x, y, 'CPU Analysis', 'Block Length (Blocks)', 'CPU Usage (Syscalls/sec)')
# Blk vs (GCMP Enc, GCMP Dec)
y = ['GCMP Encryption CPU', 'GCMP Decryption CPU']
d8 = MatData(x, y, 'CPU Analysis', 'Block Length (Blocks)', 'CPU Usage (Syscalls/sec)')
subplot_data(df, d7, d8, 5)
# Blk vs (CCMP Enc, GCMP Enc)
y = ['CCMP Encryption CPU', 'GCMP Encryption CPU']
d9 = MatData(x, y, 'CPU Analysis', 'Block Length (Blocks)', 'CPU Usage (Syscalls/sec)')
# Blk vs (CCMP Dec, GCMP Dec)
y = ['CCMP Decryption CPU', 'GCMP Decryption CPU']
d10 = MatData(x, y, 'CPU Analysis', 'Block Length (Blocks)', 'CPU Usage (Syscalls/sec)')
subplot_data(df, d9, d10, 6)

# Resources Analysis Graphs: RAM ->
# Blk vs (CCMP Enc, CCMP Dec)
y = ['CCMP Encryption RAM', 'CCMP Decryption RAM']
d11 = MatData(x, y, 'RAM Analysis', 'Block Length (Blocks)', 'RAM Usage (MiB)')
# Blk vs (GCMP Enc, GCMP Dec)
y = ['GCMP Encryption RAM', 'GCMP Decryption RAM']
d12 = MatData(x, y, 'RAM Analysis', 'Block Length (Blocks)', 'RAM Usage (MiB)')
subplot_data(df, d11, d12, 7)
# Blk vs (CCMP Enc, GCMP Enc)
y = ['CCMP Encryption RAM', 'GCMP Encryption RAM']
d13 = MatData(x, y, 'RAM Analysis', 'Block Length (Blocks)', 'RAM Usage (MiB)')
# Blk vs (CCMP Dec, GCMP Dec)
y = ['CCMP Decryption RAM', 'GCMP Decryption RAM']
d14 = MatData(x, y, 'RAM Analysis', 'Block Length (Blocks)', 'RAM Usage (MiB)')
subplot_data(df, d13, d14, 8)

plt.show()