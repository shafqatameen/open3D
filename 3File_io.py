import open3d as o3d
#load image 
load_img=o3d.data.JuneauImage()
print(load_img.path)
#read  sample data
img=o3d.io.read_image(load_img.path)
print(img)
o3d.visualization.draw_geometries([img],"window name",width=1500,height=800)
#o3d.io.write_image()
o3d.io.write_image("datasets/img.png",img)