import open3d as o3d
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.graphics import Ellipse, Color
import threading
import time

# Kivy App for 3D Point Cloud Cropping and Visualization
class PointCloudApp(App):
    def build(self):
        # Root Layout for Kivy UI
        self.layout = BoxLayout(orientation="vertical")

        # Load the demo data and setup the point cloud
        self.demo_crop_data = o3d.data.DemoCropPointCloud()
        self.pcd = o3d.io.read_point_cloud(self.demo_crop_data.point_cloud_path)
        self.vol = o3d.visualization.read_selection_polygon_volume(self.demo_crop_data.cropped_json_path)
        
        # Crop the point cloud (initial crop)
        self.chair = self.vol.crop_point_cloud(self.pcd)
        
        # Visualization Button
        self.visualize_btn = Button(text="Visualize Point Cloud")
        self.visualize_btn.bind(on_press=self.visualize_point_cloud)
        
        # Cropping Button
        self.crop_btn = Button(text="Crop Point Cloud")
        self.crop_btn.bind(on_press=self.crop_point_cloud)

        # Slider to adjust the zoom level
        self.zoom_slider = Slider(min=0.5, max=2.0, value=1.0)
        self.zoom_slider.bind(value=self.on_zoom_change)

        # Adding widgets to layout
        self.layout.add_widget(self.visualize_btn)
        self.layout.add_widget(self.crop_btn)
        self.layout.add_widget(Label(text="Adjust Zoom Level"))
        self.layout.add_widget(self.zoom_slider)

        return self.layout

    def visualize_point_cloud(self, instance):
        # Visualize the cropped point cloud in a new thread (to prevent UI blocking)
        threading.Thread(target=self.open3d_visualizer, args=(self.chair,)).start()

    def crop_point_cloud(self, instance):
        # Crop the point cloud again with the selected volume and update visualization
        self.chair = self.vol.crop_point_cloud(self.pcd)
        print("Point cloud cropped.")
        self.visualize_point_cloud(instance)

    def on_zoom_change(self, slider, value):
        # Adjust zoom level for visualization (this can be linked to the Open3D camera settings)
        print(f"Zoom Level: {value}")
        # In a real scenario, you would update Open3D's viewer settings here.
        
    def open3d_visualizer(self, chair):
        # Visualizer that runs in a separate thread (non-blocking)
        vis = o3d.visualization.Visualizer()
        vis.create_window()
        vis.add_geometry(chair)
        
        # Customize camera settings (optional)
        ctr = vis.get_view_control()
        ctr.set_zoom(self.zoom_slider.value)
        
        vis.run()
        vis.destroy_window()

if __name__ == "__main__":
    PointCloudApp().run()
