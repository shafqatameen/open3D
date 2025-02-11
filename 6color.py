import open3d as o3d

# Load point cloud
pcd = o3d.io.read_point_cloud("datasets/online_bunny.ply")
print(pcd)
# Set color for each point
pcd.paint_uniform_color([1, 0.5, 0])

# Visualize
o3d.visualization.draw_geometries([pcd], "Point Cloud")