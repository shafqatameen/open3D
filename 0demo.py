import open3d as o3d
import numpy as np

# Set up a simple camera intrinsic model
width, height = 640, 480  # Image dimensions
fx, fy = 600, 600  # Focal length
cx, cy = width / 2, height / 2  # Principal point (center of image)

# Create camera intrinsics
intrinsic = o3d.camera.PinholeCameraIntrinsic(width, height, fx, fy, cx, cy)

# Create a coordinate frame to visualize the world axes
world_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.5)

# Create a simple camera frustum visualization
frustum = o3d.geometry.LineSet.create_camera_visualization(width, height, intrinsic.intrinsic_matrix, np.eye(4))

# Visualize
o3d.visualization.draw_geometries([world_frame, frustum], window_name="Pinhole Camera Intrinsics")
