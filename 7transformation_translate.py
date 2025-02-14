import open3d as o3d
import copy

# Create a coordinate frame mesh
mesh = o3d.geometry.TriangleMesh.create_coordinate_frame()

# Create deep copies and translate
mesh_tx = copy.deepcopy(mesh)
mesh_ty = copy.deepcopy(mesh)
mesh_tz = copy.deepcopy(mesh)

mesh_tx.translate((1.3, 0, 0))  # Move in x-direction
mesh_ty.translate((0, 1.3, 0))  # Move in y-direction
mesh_tz.translate((0, 0, 1.3))  # Move in z-direction

# Print centers
print(f'Center of mesh: {mesh.get_center()}')
print(f'Center of mesh tx: {mesh_tx.get_center()}')
print(f'Center of mesh ty: {mesh_ty.get_center()}')
print(f"Center of mesh tz{mesh_tz.get_center()}")

# Visualize the original and translated meshes
o3d.visualization.draw_geometries([mesh, mesh_tx, mesh_ty,mesh_tz])
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
