import csv
import matplotlib.pyplot as plt
import numpy as np

def get_data() -> list | list | list | float | float:
    ls = []
    n = 0 

    with open('Stats.csv', 'r', encoding='utf-8-sig') as data:

        for value in data:
            value = value.strip()
            ls.append(float(value))
            n += 1

    sqrt_n = 10.0
    ls = np.array(ls)
    bin_edges = []
    heights = []

    max = np.max(ls)
    min = np.min(ls)
    cur_int = min
    interval = (max - min)/sqrt_n
    
    while cur_int < max: 
        bin_edges.append(round(cur_int, 5))
        counter = 0
        for value in ls: 
            if cur_int <= value and value < (cur_int + interval): 
                counter += 1
        heights.append(round(float(counter)/n, 5))
        counter = 0
        cur_int += interval
    
    return ls, bin_edges, heights, max, min, n

def graph_rel_freq(bin_edges, heights, n):

    plt.figure(figsize=[15, 8])

    plt.bar(bin_edges, heights, width = 0.015, color='#0504aa',alpha=0.7, align="center")
    plt.xlim(min - 0.02, max + 0.02)
    plt.xticks(bin_edges, fontsize=15)
    plt.legend([f'Num data points: {n}', f'minimum: {min}', f'maximum: {max}'])
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Value (KOhms)',fontsize=15)
    plt.ylabel('Relative Frequency',fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.title('Relative Frequency of 20 KOhm Resistors',fontsize=15)
    plt.savefig('./out/freq_histo')

def graph_normal_dist(mean, std_dev, max, min, bin_edges, heights):

    x = np.linspace(min, max, 1000)
    y = ( 1 / ( ((2 * np.pi)** 1/2) * std_dev)) * (np.exp(-1 * (((x - mean)** 2) / (2 * (std_dev ** 2)))))
    plt.figure(figsize=[15, 8])
    plt.plot(x, y)
    plt.bar(bin_edges, heights, width = 0.015, color='#0504aa',alpha=0.7, align="center")
    plt.xlim(min - 0.02, max + 0.02)
    plt.xticks(bin_edges, fontsize=15)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Value (KOhms)',fontsize=15)
    plt.ylabel('Relative Frequency',fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.title('Relative Frequency of 20 KOhm Resistors',fontsize=15)
    plt.savefig('./out/std_distro')

def main():

    sqrt_n = 10.0

    ls, bin_edges, heights, max, min, n = get_data()

    sample_mean = np.sum(ls)/n
    sample_variance = np.sum((ls - sample_mean)**2)/(n-1)
    sample_standard_deviation = sample_variance ** (1/2)

    print(sample_mean, sample_standard_deviation)
    graph_normal_dist(sample_mean, sample_standard_deviation, max, min, bin_edges, heights)

if __name__ == '__main__':
    main()