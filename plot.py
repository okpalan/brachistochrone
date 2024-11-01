import numpy as np
import matplotlib.pyplot as plt

# Define the start and end points for the Brachistochrone problem
start = np.array([50, 50])
end = np.array([750, 550])

# Midpoint weighted average - midpoint of the start and end points
mid = (start + end) / 2

# Function to calculate the right-angled triangle approximation
def draw_triangle_approximation(start, end, mid):
    plt.plot([start[0], mid[0], end[0]], [start[1], end[1], end[1]], 'b--', label="Triangle Approximation")
    plt.scatter(*start, color="green", label="Start Point")
    plt.scatter(*end, color="red", label="End Point")

# Function to calculate the approximate curve trajectory using a quadratic spline
def draw_quadratic_spline(start, end, mid):
    t_values = np.linspace(0, 1, 100)
    curve_x = (1 - t_values) * ((1 - t_values) * start[0] + t_values * mid[0]) + t_values * ((1 - t_values) * mid[0] + t_values * end[0])
    curve_y = (1 - t_values) * ((1 - t_values) * start[1] + t_values * mid[1]) + t_values * ((1 - t_values) * mid[1] + t_values * end[1])
    
    plt.plot(curve_x, curve_y, 'r-', label="Quadratic Spline Approximation")
    plt.legend()

# Plot the triangle approximation and spline approximation on the same graph
plt.figure(figsize=(10, 8))
draw_triangle_approximation(start, end, mid)
draw_quadratic_spline(start, end, mid)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Brachistochrone Problem - Optimized Triangle and Spline Approximations")
plt.grid(True)
plt.show()
