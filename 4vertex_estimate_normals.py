import open3d as o3d
# load read and visualize then voxel_down_sample and finally do the estimate the normals
loaded_data=o3d.data.PLYPointCloud()
pcd=o3d.io.read_point_cloud(loaded_data.path)
#o3d.visualization.draw_geometries([pcd],window_name="vertex normal estimation",front=[0.4257, -0.2125, -0.8795])
# Visualize the point cloud with custom camera parameters
o3d.visualization.draw_geometries(
    [pcd],
    window_name="before Vertex Normal Estimation and voxel downsampling"
    )

#voxel down_sampling
downpcd=pcd.voxel_down_sample(voxel_size=0.05)
#visualize it
o3d.visualization.draw_geometries([downpcd],"before Vertex Normal Estimation and  after voxel downsampling")

#vertex estimat_normal on downpcd
downpcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1,max_nn=30))
#visualize it
o3d.visualization.draw_geometries([downpcd],"vertex estimat_normal on downpcd",point_show_normal=True)
#vertex estimat_normal on pcd
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1,max_nn=30))
#visualize it
o3d.visualization.draw_geometries([pcd],"vertex estimat_normal on pcd",point_show_normal=True)

