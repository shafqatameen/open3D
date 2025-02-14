import open3d as o3d
import copy

# Create a coordinate frame mesh
mesh = o3d.geometry.TriangleMesh.create_coordinate_frame()

# Translate with relative=False (places center at (2,2,2))
mesh_mv_absolute = copy.deepcopy(mesh).translate((2, 2, 2), relative=False)

# Translate with relative=True (shifts by (2,2,2))
mesh_mv_relative = copy.deepcopy(mesh).translate((2, 2, 2), relative=True)

# Print centers
print(f'Center of original mesh: {mesh.get_center()}')
print(f'Center of mesh_mv_absolute: {mesh_mv_absolute.get_center()}')  # Moves to (2,2,2)
print(f'Center of mesh_mv_relative: {mesh_mv_relative.get_center()}')  # Moves by (2,2,2)

# Visualize all meshes
o3d.visualization.draw_geometries([mesh, mesh_mv_absolute, mesh_mv_relative])
