import csv
import matplotlib.pyplot as plt
import numpy

def main():

    ls = []

    with open('Stats.csv', encoding='utf8', newline='') as data:
        for value in data: 
            ls.append(float(value))
    
    sqrt_n = 10
    n = 92
            

if __name__ == '__main__':
    main()