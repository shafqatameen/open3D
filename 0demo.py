import cv2
import torch
import numpy as np
import open3d as o3d
import torchvision.transforms as transforms
from torchvision.models.segmentation import deeplabv3_resnet50

# Load a pre-trained AI depth estimation model
model = deeplabv3_resnet50(pretrained=True)
model.eval()

# Define transformations for the input image
transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((480, 640)),
    transforms.ToTensor()
])

# Load video file
video_path = "data/dog.mp4"  # 🔴 Replace with your video path
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert BGR to RGB
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img_tensor = transform(img_rgb).unsqueeze(0)

    # Fake depth estimation using segmentation model
    with torch.no_grad():
        output = model(img_tensor)['out']
    depth_map = torch.sigmoid(output[0, 0]).numpy()

    # Normalize depth map
    depth_map = (depth_map - depth_map.min()) / (depth_map.max() - depth_map.min())

    # Convert to a 3D point cloud
    h, w = depth_map.shape
    fx, fy = w / 2, h / 2  # Fake focal lengths
    cx, cy = w / 2, h / 2  # Fake principal points

    points = []
    colors = []

    for i in range(h):
        for j in range(w):
            z = depth_map[i, j] * 2  # Scale depth
            x = (j - cx) * z / fx
            y = (i - cy) * z / fy

            points.append((x, y, z))
            colors.append(img_rgb[i, j] / 255.0)

    # Create Open3D point cloud
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(np.array(points))
    pcd.colors = o3d.utility.Vector3dVector(np.array(colors))

    # Visualize 3D scene
    o3d.visualization.draw_geometries([pcd], window_name="3D Video to Point Cloud")

    # Show depth map in OpenCV
    cv2.imshow("Depth Map", (depth_map * 255).astype(np.uint8))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
