#------------------------------------Creating a Synthetic Point Cloud: -------------------------------------
import numpy as np
import open3d as o3d

# Create a random point cloud
points = np.random.rand(100000, 3)  # 10000 points in 3D space
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(points)
o3d.io.write_point_cloud("datasets/syntheticCubicPcd.pcd",point_cloud)
print(points)
print(point_cloud)
o3d.visualization.draw_geometries([point_cloud])