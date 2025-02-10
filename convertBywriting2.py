import numpy as np
import open3d as o3d

# ---------------- READ ----------------
# Load a .bin point cloud (assuming it's in [x, y, z, intensity] format)
bin_pcdxyz = np.fromfile("data/000031.bin", dtype=np.float32).reshape(-1, 4)

# Extract XYZ
pointsxyz = bin_pcdxyz[:, :3]

# Create Open3D Point Cloud
pcdxyz = o3d.geometry.PointCloud()
pcdxyz.points = o3d.utility.Vector3dVector(pointsxyz)

# ---------------- WRITE ----------------
# Save the extracted XYZ points back to a .bin file
pointsxyz.tofile("data/output_saved.bin")

# ---------------- VERIFY ----------------
# Reload the saved file to check correctness
reloaded_pointsxyz = np.fromfile("data/output_saved.bin", dtype=np.float32).reshape(-1, 3)

# Print to compare
print("Original First 5 Points:\n", pointsxyz[:5])
print("Reloaded First 5 Points:\n", reloaded_pointsxyz[:5])

# ---------------- VISUALIZE ----------------
o3d.visualization.draw_geometries([pcdxyz], window_name="Point Cloud from .bin File")
