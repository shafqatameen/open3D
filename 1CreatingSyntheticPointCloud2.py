import open3d as o3d
import numpy as np

# Generate a synthetic point cloud (sphere)
num_points = 10000
radius = 1.0

# Random spherical coordinates
theta = np.random.uniform(0, 2 * np.pi, num_points)
phi = np.random.uniform(0, np.pi, num_points)

# Convert to Cartesian coordinates (x, y, z)
x = radius * np.sin(phi) * np.cos(theta)
y = radius * np.sin(phi) * np.sin(theta)
z = radius * np.cos(phi)

# Stack to form point cloud
points = np.vstack((x, y, z)).T

# Generate RGB colors (randomized)
colors = np.random.rand(num_points, 3)

# Create Open3D point cloud object
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
pcd.colors = o3d.utility.Vector3dVector(colors)
pcd.estimate_normals()

# Save to PLY file
o3d.io.write_point_cloud("datasets/synthetic_point_cloud.ply", pcd)

# Print a sample of the dataset (first 10 points)
print("Sample of Point Cloud Data:")
print("Index  |   X      |   Y      |   Z      |   R   |   G   |   B   ")
print("-" * 60)
for i in range(10):
    x, y, z = points[i]
    r, g, b = colors[i]
    print(f"{i:<6} | {x:.5f} | {y:.5f} | {z:.5f} | {r:.2f} | {g:.2f} | {b:.2f}")

print("\nPoint cloud saved as 'synthetic_point_cloud.ply'")

# **Visualize the Point Cloud in 3D**
o3d.visualization.draw_geometries([pcd])
