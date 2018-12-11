# Chapter 3 Exercises

import matplotlib.pyplot as plt
import csv
import statistics

# 3-3: World Population
#
# Download a csv file containing the historical United States population data.
#   Find the mean, median, variance, and standard deviation of the differences
#   between the years.  Then, create a graph showing these differences.

POP_DATA_FILE = 'exercises/data/WPP2017_TotalPopulationBySex.csv'


def world_population():
    years, populations = read_csv()
    print_stats(years, populations)
    draw_graph(years, populations)


def read_csv():
    years, populations = [], []
    with open(POP_DATA_FILE) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[1] == 'United States of America' and row[3] == 'Medium':
                years.append(int(row[4]))
                populations.append(int(float(row[8])))
    return years, populations


def print_stats(years, populations):
    differences = yearly_differences(populations)
    print('Mean of differences: %s' % statistics.mean(differences))
    print('Median of differences: %s' % statistics.median(differences))
    print('Variance of differences: %s' % statistics.pvariance(differences))
    print('Standard Deviation of differences: %s' % statistics.pstdev(differences))


def draw_graph(years, populations):
    plt.plot(years[1:], yearly_differences(populations))
    plt.title('Yearly Population Change In The United States, 1951-2100')
    plt.xlabel('Year')
    plt.ylabel('Yearly Population Change (In Millions)')
    plt.show()


def yearly_differences(populations):
    differences = []
    for i in range(1, len(populations)):
        differences.append(populations[i] - populations[i - 1])
    return differences


if __name__ == '__main__':
    world_population()
