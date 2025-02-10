import open3d as o3d

# Load point cloud
pcd = o3d.io.read_point_cloud("datasets/online_icp.ply")
print(pcd)
# Create voxel grid
voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd, voxel_size=0.005)
print(voxel_grid)
# Visualize
o3d.visualization.draw_geometries([pcd], "without downsampling applied")
o3d.visualization.draw_geometries([voxel_grid],"voxel downsamoling applied",                                 
                                  zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024])
