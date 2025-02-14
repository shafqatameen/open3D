import open3d as o3d
import copy

# Create a cube mesh
cube = o3d.geometry.TriangleMesh.create_box(width=1.0, height=1.0, depth=1.0)
cube.compute_vertex_normals()
cube.paint_uniform_color([0.8, 0.2, 0.2])  # Red color for visualization

# Create deep copies and translate them
cube_tx = copy.deepcopy(cube)  # Copy for x-translation
cube_ty = copy.deepcopy(cube)  # Copy for y-translation

cube_tx.translate((1.3, 0, 0))  # Move in x-direction
cube_ty.translate((0, 1.3, 0))  # Move in y-direction

# Print center positions
print(f'Center of original cube: {cube.get_center()}')
print(f'Center of cube_tx: {cube_tx.get_center()}')
print(f'Center of cube_ty: {cube_ty.get_center()}')

# Visualize original and translated cubes
o3d.visualization.draw_geometries([cube, cube_tx, cube_ty])
