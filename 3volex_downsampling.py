import open3d as o3d
#read
pcd=o3d.io.read_point_cloud('datasets/online_icp.pcd')
#voxel_downsampling 
downpcd=pcd.voxel_down_sample(voxel_size=0.001)

o3d.io.visualization.draw_geometries([downpcd],"voxel downsampling")