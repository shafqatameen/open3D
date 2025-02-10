import numpy as np
import open3d as o3d

num_points = 10000
points = np.random.rand(num_points, 3)  # Random points in [0,1] range

# ✅ Apply gradient to Z-axis
points[:, 2] = np.linspace(0, 1, num_points)

# ✅ Create Open3D point cloud
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)

# ✅ Color based on Z value
colors = np.zeros((num_points, 3))
colors[:, 2] = points[:, 2]  # Blue increases with Z

pcd.colors = o3d.utility.Vector3dVector(colors)

# ✅ Visualize the gradient effect
o3d.visualization.draw_geometries([pcd], window_name="Z-Gradient Point Cloud")
