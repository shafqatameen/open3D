import open3d as o3d
import numpy as np
import copy

# Create a coordinate frame mesh
mesh = o3d.geometry.TriangleMesh.create_coordinate_frame()

# Translate the mesh in the x-direction
mesh_t = copy.deepcopy(mesh).translate((2, 0, 0))

# Apply rotation (90° around X, 45° around Z) with center at (0,0,0)
mesh_r = copy.deepcopy(mesh_t).rotate(mesh_t.get_rotation_matrix_from_xyz((np.pi / 2, 0, np.pi / 4)),
              center=(0, 0, 0))

# Visualize original and rotated meshes
o3d.visualization.draw_geometries([mesh,mesh_t, mesh_r])
