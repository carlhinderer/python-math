# Chapter 2 Exercises

import matplotlib.pyplot as plt
import math

g = 9.8

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


# 2-3 Enhanced Projectile Trajectories
#
# Enhance the trajectory comparison program in a few ways:
#
#   1. Print the time of flight, maximum horizontal distance, and maximum vertical distance for each v0/theta pair.
#   2. Accept any number of v0/theta pairs, entered by the user.
#   3. Validate input and handle invalid input properly.


def enhanced_projectiles():
    us, thetas = get_projectiles_from_user()
    legend = []
    for i in range(len(us)):
        draw_trajectory(us[i], thetas[i])
        print_info(us[i], thetas[i])
        legend.append('u: %s, theta: %s' % (us[i], thetas[i]))
    show_graph(legend)


def get_projectiles_from_user():
    us = []
    thetas = []
    num_projectiles = int(input('How many trajectories?: '))
    for i in range(num_projectiles):
        u = float(input('Enter the initial velocity for trajectory %s (m/s): ' % i))
        theta = float(input('Enter the angle of projection for trajectory %s (degrees): ' % i))
        if valid_projectile(u, theta):
            us.append(u)
            theta = math.radians(theta)
            thetas.append(theta)
        else:
            print('The trajectory u: %s, theta: %s is not valid.' % (u, theta))
    return us, thetas


def valid_projectile(u, theta):
    return u > 0 and theta > 0 and theta < 90


def frange(start, final, interval):
    numbers = []
    while start < final:
        numbers.append(start)
        start += interval
    return numbers


def draw_trajectory(u, theta):
    intervals = frange(0, flight_time(u, theta), 0.001)
    x = []
    y = []
    for t in intervals:
        x.append(u * math.cos(theta) * t)
        y.append((u * math.sin(theta) * t) - (0.5 * g * t**2))
    plt.plot(x, y)


def print_info(u, theta):
    print('Results for u: %s, theta: %s' % (u, theta))
    print('Time of flight: %s s' % flight_time(u, theta))
    print('Max Height: %s m' % max_height(u, theta))
    print('Horizontal Range: %s m' % horizontal_range(u, theta))


def flight_time(u, theta):
    return 2 * u * math.sin(theta) / g


def max_height(u, theta):
    return u**2 * (math.sin(theta))**2 / (2 * g)


def horizontal_range(u, theta):
    return u**2 * math.sin(2 * theta) / g


def show_graph(legend):
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')
    plt.legend(legend)
    plt.show()


if __name__ == '__main__':
    enhanced_projectiles()
