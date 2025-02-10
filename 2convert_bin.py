import numpy as np
import open3d as o3d

# Load a .bin point cloud (assuming it's in [x, y, z, intensity] format)
bin_pcd = np.fromfile("data/000031.bin", dtype=np.float32).reshape(-1, 4)

# Extract only XYZ coordinates (ignore intensity)
points = bin_pcd[:, :3]

# Create Open3D point cloud
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)

# Visualize
o3d.visualization.draw_geometries([pcd])
