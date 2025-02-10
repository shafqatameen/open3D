import open3d as o3d
#read  sample data
img=o3d.io.read_image("data/cat.jpg")
#o3d.io.write_image()
o3d.io.write_image("datasets/cat.png",img)
o3d.visualization.draw_geometries([img],"window name",width=1500,height=800)
