import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Variables
ax = plt.axes(projection="3d")
x_data = np.arange(-5, 5, 0.1)
y_data = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x_data, y_data) # Compute meshes
Z = np.sin(X) * np.cos(Y)

# Plot mesh
ax.plot_surface(X, Y, Z, cmap="viridis")
plt.show()
