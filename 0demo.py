import open3d as o3d

# Load the demo data
demo_crop_data = o3d.data.DemoCropPointCloud()

# Read the point cloud
pcd = o3d.io.read_point_cloud(demo_crop_data.point_cloud_path)

# Visualize the point cloud
o3d.visualization.draw_geometries([pcd],
                                  zoom=0.7,
                                  front=[0.5439, -0.2333, -0.8060],
                                  lookat=[2.4615, 2.1331, 1.338],
                                  up=[-0.1781, -0.9708, 0.1608])
