#------------------------------------Creating a Synthetic Point Cloud: -------------------------------------
import numpy as np
import open3d as o3d

# Create a random point cloud
points = np.random.rand(1000000, 3)  # 100 points in 3D space
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(points)

print(points)
o3d.visualization.draw_geometries([point_cloud])