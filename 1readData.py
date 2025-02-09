import open3d as o3d
data=o3d.data.BunnyMesh()
print(data.path)

pcd=o3d.io.read_point_cloud(data.path)
o3d.io.write_point_cloud("open3d/datasets/bunny.pcd",pcd)
o3d.visualization.draw_geometries([pcd],"window name is Bunny Mesh")



