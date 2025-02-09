import open3d as o3d
import numpy as np

num_points = 1000000  # Ensure consistency

# ✅ Create a random point cloud
points = np.random.rand(num_points, 3)  # 1,000,000 points in 3D space
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(points)

# ✅ Visualize the raw point cloud
o3d.visualization.draw_geometries([point_cloud], window_name="Random Point Cloud")

# ✅ Assign colors based on the Z-axis (Gradient Effect)
colors = np.zeros((num_points, 3))  # Initialize colors
colors[:, 0] = (points[:, 2] - np.min(points[:, 2])) / (np.max(points[:, 2]) - np.min(points[:, 2]))  # Red intensity varies with Z

point_cloud.colors = o3d.utility.Vector3dVector(colors)  # Assign colors properly
o3d.visualization.draw_geometries([point_cloud], window_name="Gradient Color by Z-Axis")
