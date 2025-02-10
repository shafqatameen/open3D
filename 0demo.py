import open3d as o3d

# Load Mesh
data = o3d.data.BunnyMesh()
mesh = o3d.io.read_triangle_mesh(data.path)

# Compute Vertex Normals for Better Lighting
mesh.compute_vertex_normals()

# Convert Mesh to Point Cloud with More Points
pcd = mesh.sample_points_uniformly(number_of_points=10000)

# Paint the Mesh and Point Cloud for Clarity
mesh.paint_uniform_color([1, 0.7, 0.2])  # Orange mesh
pcd.paint_uniform_color([0, 0.5, 1])  # Blue point cloud

# Scale Point Cloud (if needed)
pcd.scale(10, center=pcd.get_center())

# Improve visualization settings
o3d.visualization.draw_geometries(
    [mesh, pcd],
    window_name="Improved Visualization",
    mesh_show_back_face=True  # Ensures back faces are visible
)
