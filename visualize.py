import cv2
import os

# Visualize detection results
output_path = "C:/Users/kolah/OneDrive/Desktop/project/runs/detect"
"""
if not os.path.exists(output_path):
    print(f"Output path '{output_path}' not found. Ensure detection has been run.")
else:
    for image_file in os.listdir(output_path):
        image = cv2.imread(os.path.join(output_path, image_file))
        cv2.imshow("Detection Result", image)
        cv2.waitKey(0)  # Press any key to close the image window
    cv2.destroyAllWindows()
"""
if not os.path.exists(output_path):
    print(f"Output path '{output_path}' not found. Ensure detection has been run.")
else:
    # List all files in the directory
    image_files = os.listdir(output_path)
    if not image_files:
        print(f"No images found in the directory '{output_path}'.")
    else:
        for image_file in image_files:
            # Check if the file is an image (you can extend this with more image file formats)
            if image_file.endswith(('.jpg', '.png', '.jpeg')):
                image_path = os.path.join(output_path, image_file)
                image = cv2.imread(image_path)
                
                if image is None:
                    print(f"Failed to read image: {image_path}")
                else:
                    # Show the image
                    cv2.imshow("Detection Result", image)
                    cv2.waitKey(0)  # Wait for a key press to close the image
            else:
                print(f"Skipping non-image file: {image_file}")

        # Destroy all OpenCV windows after the loop
        cv2.destroyAllWindows()