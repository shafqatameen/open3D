import cv2
import torch
import numpy as np
import open3d as o3d
import torchvision.transforms as transforms
from torchvision.models.segmentation import deeplabv3_resnet50

# Load a pre-trained depth estimation model (using semantic segmentation)
model = deeplabv3_resnet50(pretrained=True)
model.eval()

# Define image transform
transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((480, 640)),
    transforms.ToTensor()
])

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert BGR to RGB
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img_tensor = transform(img_rgb).unsqueeze(0)

    # Fake depth estimation using segmentation output
    with torch.no_grad():
        output = model(img_tensor)['out']
    depth_map = torch.sigmoid(output[0, 0]).numpy()

    # Normalize depth map
    depth_map = (depth_map - depth_map.min()) / (depth_map.max() - depth_map.min())

    # Convert to a 3D point cloud
    h, w = depth_map.shape
    fx, fy = w / 2, h / 2  # Focal lengths (fake values)
    cx, cy = w / 2, h / 2  # Principal points

    points = []
    colors = []

    for i in range(h):
        for j in range(w):
            z = depth_map[i, j] * 1  # Scale depth
            x = (j - cx) * z / fx
            y = (i - cy) * z / fy

            points.append((x, y, z))
            colors.append(img_rgb[i, j] / 200.0)

    # Create Open3D point cloud
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(np.array(points))
    pcd.colors = o3d.utility.Vector3dVector(np.array(colors))

    # Visualize the point cloud
    o3d.visualization.draw_geometries([pcd], window_name="AI Depth Estimation")

    # Show depth map in OpenCV
    cv2.imshow("Depth Map", (depth_map * 200).astype(np.uint8))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
