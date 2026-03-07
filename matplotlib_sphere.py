import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D # This import registers the 3D projection

# --- 1. Generate Data (Points on a sphere surface) ---
# We can use spherical coordinates to generate points
n_points = 500
radius = 1.0

# Generate random points using spherical coordinates
# Theta (azimuth) from 0 to 2*pi
# Phi (inclination) from 0 to pi
theta = 2 * np.pi * np.random.rand(n_points)
phi = np.pi * np.random.rand(n_points)

# Convert spherical to Cartesian coordinates
x = radius * np.sin(phi) * np.cos(theta)
y = radius * np.sin(phi) * np.sin(theta)
z = radius * np.cos(phi)

# --- 2. Create the 3D plot ---
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d') # Use "projection='3d'"

# --- 3. Scatter plot the data ---
ax.scatter(x, y, z, marker='o', color='b', s=20) # s is marker size

# --- 4. Customize the plot (optional) ---
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Scatter Plot of Points Forming a Sphere')

# Optional: Set equal aspect ratio so the sphere looks like a sphere
# This is a bit tricky with matplotlib 3D, we can manually set limits
# max_range = np.array([x.max()-x.min(), y.max()-y.min(), z.max()-z.min()]).max() / 2.0
# mid_x = (x.max()+x.min()) * 0.5
# mid_y = (y.max()+y.min()) * 0.5
# mid_z = (z.max()+z.min()) * 0.5
# ax.set_xlim(mid_x - max_range, mid_x + max_range)
# ax.set_ylim(mid_y - max_range, mid_y + max_range)
# ax.set_zlim(mid_z - max_range, mid_z + max_range)

# Show the plot
plt.show()
