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


# 3-4: Percentile Calculation
#
# Write a program that takes a list of numbers in a file as input and asks for a
#   percentile, then returns the item from the list at that percentile.

TEST_SCORES_FILE = 'exercises/data/testscores.txt'


def print_percentile():
    numbers = load_numbers()
    percentile = get_percentile_from_user()
    percentile_value = calculate_percentile(numbers, percentile)
    print('The value at %s percentile is %s' % (percentile, percentile_value))


def load_numbers():
    return [int(line.strip()) for line in open(TEST_SCORES_FILE)]


def get_percentile_from_user():
    percentile = int(input('What percentile value?: '))
    return percentile


def calculate_percentile(numbers, percentile):
    i = (len(numbers) * percentile) / 100 + 0.5
    if i.is_integer():
        return numbers[int(i)]
    else:
        k = int(i)
        f = i - k
        return (1 - f) * numbers[k] + f * numbers[k + 1]


# 3-5: Frequency Table
#
# Read in a list of numbers from a file.  Then, ask the user how many classes
#   they want the data in.  Split the data into the number of classes and display
#   it in a frequency table.

def frequency_table():
    numbers = load_numbers()
    num_classes = get_classes_from_user()
    ft = generate_frequency_table(numbers, num_classes)
    print_frequency_table(ft)


def get_classes_from_user():
    num_classes = int(input('How many classes?: '))
    return num_classes


def generate_frequency_table(numbers, num_classes):
    table = []
    interval_start = float(min(numbers))
    interval = (max(numbers) - min(numbers)) / num_classes
    interval_end = interval_start + interval
    for c in range(num_classes):
        count = 0
        for num in numbers:
            if num >= interval_start and num <= interval_end:
                count += 1
        table.append((interval_start, interval_end, count))
        interval_start, interval_end = interval_end, interval_end + interval
    return table


def print_frequency_table(table):
    print('Grade\tFrequency')
    for category in table:
        print('%s-%s\t%s' % (category[0], category[1], category[2]))


if __name__ == '__main__':
    frequency_table()
