import open3d as o3d
point_cloud=o3d.io.read_point_cloud("data/000031.pcd")

o3d.io.write_point_cloud('data/000031.ply',point_cloud)