import os
import cv2

# Paths
image_path = "C:/Users/kolah/OneDrive/Desktop/project/dataset/val"
weights_path = "C:/Users/kolah/OneDrive/Desktop/project/runs/train/exp/weights/best.pt"
output_path = "C:/Users/kolah/OneDrive/Desktop/project/yolov5/runs/results"

# Ensure results folder exists
if not os.path.exists(output_path):
    os.makedirs(output_path)
    print(f"Created missing output folder: {output_path}")

# Run YOLOv5 detection with correct project directory
os.system(f"python detect.py --weights {weights_path} --img 640 --conf 0.4 --source {image_path} --project {output_path} --name results --exist-ok")

# Wait for YOLOv5 to finish running and save output images to 'results' folder

# Verify the output folder
results_folder = os.path.join(output_path, "results")  # Results will be saved in subfolder 'results'

# Visualize detection results
if os.path.exists(results_folder):
    print(f"Detection completed. Results saved in: {results_folder}")
    # Iterate through results and display each image
    for image_file in os.listdir(results_folder):
        file_path = os.path.join(results_folder, image_file)
        if os.path.isfile(file_path) and image_file.lower().endswith((".jpg", ".png")):
            image = cv2.imread(file_path)
            cv2.imshow("Detection Result", image)
            cv2.waitKey(0)  # Press any key to close the image window
    cv2.destroyAllWindows()
else:
    print(f"Output directory '{results_folder}' does not exist. Ensure detection was successful.")
