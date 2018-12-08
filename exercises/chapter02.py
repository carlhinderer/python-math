# Chapter 2 Exercises

import matplotlib.pyplot as plt

# 2-1: Temperature Varying During The Day
#
# Pick 3 cities, and plot their daily hourly temperatures.


def plot_hourly_temperatures():
    hours = range(24)
    nyc_temps = [29, 29, 28, 28, 27, 27, 27, 28, 28, 30, 32, 34, 35, 36, 37, 36, 35, 34, 34, 33, 33, 33, 32, 32]
    chicago_temps = [21, 21, 20, 20, 20, 20, 20, 20, 21, 23, 25, 27, 28, 29, 29, 29, 29, 28, 27, 26, 26, 26, 24, 24]
    la_temps = [54, 54, 54, 53, 53, 52, 52, 52, 55, 59, 63, 65, 68, 68, 69, 68, 66, 62, 60, 59, 58, 57, 56, 56]

    plt.plot(hours, nyc_temps, hours, chicago_temps, hours, la_temps, marker='o')
    plt.title('Hourly Temperatures on December 8, 2018')
    plt.legend(['NYC', 'Chicago', 'LA'])
    plt.xlabel('Hours After Midnight')
    plt.ylabel('Temperature in Degrees Farenheit')
    plt.show()


# 2-2: Visualizing Quadratic Functions
#
# Write a function to plot a quadratic function for x values -5 to 5.


def visualize_quadratic_function(a, b, c):
    x_vals = range(-5, 6)
    y_vals = []
    for xval in x_vals:
        y = (a * xval**2) + (b * xval) + c
        y_vals.append(y)

    plt.plot(x_vals, y_vals)
    plt.title('Quadratic Function Plotted')
    plt.show()


if __name__ == '__main__':
    visualize_quadratic_function(1, 2, 1)
