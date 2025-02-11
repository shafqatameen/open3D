import open3d as o3d

print("Load a ply point cloud, print it, and render it")

sample_ply_data_xyz = o3d.data.PLYPointCloud()
pcd_xyz = o3d.io.read_point_cloud(sample_ply_data_xyz.path)

o3d.visualization.draw_geometries([pcd_xyz],"window name",1000,1000,
                                  zoom=0.41,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024])


# - sign decrease the size of point and + sign will increase the size in the window of o3d
#  

