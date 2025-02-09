import open3d as o3d

# Load the point cloud file
pcd = o3d.io.read_point_cloud("data\000031.bin")  # Replace with your file path

# Print basic info
print(pcd)  # Shows number of points, format, etc.
print("Point Cloud has", len(pcd.points), "points.")

# Visualize the point cloud
o3d.visualization.draw_geometries([pcd], window_name="Point Cloud Viewer")
import open3d as o3d

# Load the point cloud file
pcd = o3d.io.read_point_cloud("data\000031.pcd")  # Replace with your file path

# Print basic info
print(pcd)  # Shows number of points, format, etc.
print("Point Cloud has", len(pcd.points), "points.")

# Visualize the point cloud
o3d.visualization.draw_geometries([pcd], window_name="Point Cloud Viewer")
