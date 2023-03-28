import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Variables
ax = plt.axes(projection="3d")
x_data = np.arange(-5, 5, 0.1)
y_data = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x_data, y_data)
Z = np.sin(3.14 * X) * np.cos(3.14 * Y)

ax.plot_surface(X, Y, Z, cmap="viridis")
plt.show()