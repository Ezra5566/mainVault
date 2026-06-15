import os

import cv2  # OpenCV for image processing
import pandas as pd
from sklearn.model_selection import train_test_split


# 1. Automating Data Cleaning (The "Dirty Work")
def preprocess_image_data(data_dir):
    valid_images = []
    valid_labels = []

    for filename in os.listdir(data_dir):
        if filename.endswith(".jpg"):
            # Read image
            img_path = os.path.join(data_dir, filename)
            img = cv2.imread(img_path)

            if img is None:
                continue  # Skip corrupted files

            # Resize and normalize (standard engineering task)
            img_resized = cv2.resize(img, (224, 224))
            img_normalized = img_resized / 255.0

            # Save processed version or store in memory
            # In real life, you'd save this to a secure bucket or database
            valid_images.append(img_normalized)
            # Assume filename contains label like "defect_001.jpg"
            valid_labels.append(0 if "normal" in filename else 1)

    return valid_images, valid_labels


# 2. Orchestrating Model Training
# You don't just run a script; you build pipelines
images, labels = preprocess_image_data("./raw_data")

# Split data properly (preventing data leakage)
X_train, X_test, y_train, y_test = train_test_split(
    images, labels, test_size=0.2, stratify=labels
)

print(f"Prepared {len(X_train)} training samples. Ready for model ingestion.")
