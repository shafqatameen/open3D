import open3d as o3d
#load point cloud and  to get volume
demo_crop_data=o3d.data.DemoCropPointCloud()
#read thse point cloud 
pcd=o3d.io.read_point_cloud(demo_crop_data.point_cloud_path)
#read the croped json file to get the volume
vol=o3d.visualization.read_selection_polygon_volume(demo_crop_data.cropped_json_path)
#crop the point cloud
chair=vol.crop_point_cloud(pcd)

#visualization 
o3d.visualization.draw_geometries([chair],zoom=0.7,front=[0.5439,-0.2333,-0.8060],lookat=[2.4615,2.1331,1.338],up=[-0.1781,-0.9708,0.1608])