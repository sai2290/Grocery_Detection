import os

# Verify dataset paths
train_path = "C:/Users/kolah/OneDrive/Desktop/project/dataset/train"
val_path = "C:/Users/kolah/OneDrive/Desktop/project/dataset/val"

if os.path.exists(train_path) and os.path.exists(val_path):
    print("Dataset paths are correct!")
else:
    print("Check dataset paths.")
    # Optionally, print specific missing directories:
    if not os.path.exists(train_path):
        print(f"Train path does not exist: {train_path}")
    if not os.path.exists(val_path):
        print(f"Val path does not exist: {val_path}")
    exit()  # Exit if paths are incorrect

# Navigate to YOLOv5 directory
if not os.path.exists("yolov5"):
    os.system("git clone https://github.com/ultralytics/yolov5.git")
os.chdir("yolov5")

# Install dependencies
os.system("pip install -r requirements.txt")

# Train the YOLOv5 model
os.system("python train.py --img 640 --batch 16 --epochs 50 --data C:/Users/kolah/OneDrive/Desktop/project/data.yaml --weights yolov5s.pt")

print("Training complete. Model weights saved in 'runs/train/exp/weights/'.")
