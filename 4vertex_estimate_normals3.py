import open3d as o3d
import numpy as np
# Load point cloud
pcd = o3d.io.read_point_cloud("datasets/online_bunny.ply")
print(pcd)

# Estimate normals
#pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParam(radius=0.1, max_nn=30))
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamKNN(30))

#access estimated vertex normal (single point)
print(pcd.normals[0])
#access estimated vertex normal (under the range)
print()







'''# **1st Method: Orient normals to align with a given direction (e.g., [0, 0, 1])**
pcd.orient_normals_to_align_with_direction(orientation_reference=[0, 0, 1])

# Visualize the first orientation result
print("Displaying normals aligned to direction [0, 0, 1]")
o3d.visualization.draw_geometries([pcd], point_show_normal=True)

# **2nd Method: Orient normals to face the camera (e.g., at origin [0, 0, 0])**
pcd.orient_normals_towards_camera_location(camera_location=[0, 0, 0])

# Visualize the second orientation result
print("Displaying normals facing camera at [0, 0, 0]")
o3d.visualization.draw_geometries([pcd], point_show_normal=True)'''


