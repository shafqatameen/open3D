import open3d as o3d

# Load point cloud
pcd = o3d.io.read_point_cloud("datasets/online_bunny.ply")
print(pcd)
# Create voxel grid
voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd, voxel_size=0.001)
print(voxel_grid)
# Visualize
o3d.visualization.draw_geometries([pcd], "without downsampling applied")
o3d.visualization.draw_geometries([voxel_grid],"voxel downsamoling applied")
