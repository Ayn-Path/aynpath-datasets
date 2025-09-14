import os
import cv2
import numpy as np

# CONFIGURATION
VIDEO_DIR = r"C:/Users/mhmda/Downloads/dataset_opencv/videos" # dir to retrieve the videos
FEATURES_DIR = r"C:/Users/mhmda/Downloads/dataset_opencv/features_npz" # dir to save the extracted features
os.makedirs(FEATURES_DIR, exist_ok=True)

MAX_FRAMES_PER_LOCATION = 5000  # limit total frames to prevent memory issues
FRAME_SKIP = 5  # keep every 5th frame
RESIZE_DIM = (640, 360)  # resize frames to width x height

# ORB detector
orb = cv2.ORB_create(nfeatures=2000)

# Helper Function
def extract_orb_descriptors(frame):
    """Convert frame to grayscale and compute ORB descriptors."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kp, des = orb.detectAndCompute(gray, None)
    return des

# Processing for each location
for location in os.listdir(VIDEO_DIR):
    location_path = os.path.join(VIDEO_DIR, location)
    if not os.path.isdir(location_path):
        continue

    all_descriptors = []
    frame_count = 0

    print(f"\nProcessing location: {location}")

    for video_file in os.listdir(location_path):
        if not video_file.lower().endswith((".mp4", ".avi", ".mov", ".mkv")):
            continue

        video_path = os.path.join(location_path, video_file)
        cap = cv2.VideoCapture(video_path)
        success = True
        frame_idx = 0

        while success:
            success, frame = cap.read()
            if not success:
                break

            # Skip frames
            if frame_idx % FRAME_SKIP != 0:
                frame_idx += 1
                continue

            # Resize frame
            frame = cv2.resize(frame, RESIZE_DIM)

            # Extract ORB descriptors
            des = extract_orb_descriptors(frame)
            if des is not None:
                all_descriptors.append(des)

            frame_idx += 1
            frame_count += 1

            # Stop if max frames reached
            if frame_count >= MAX_FRAMES_PER_LOCATION:
                break

        cap.release()
        if frame_count >= MAX_FRAMES_PER_LOCATION:
            break

    # Combine all descriptors into one array
    if all_descriptors:
        all_descriptors = np.vstack(all_descriptors)
        output_file = os.path.join(FEATURES_DIR, f"{location}_features.npz")
        np.savez_compressed(output_file, descriptors=all_descriptors)
        print(f"Saved {output_file} with {all_descriptors.shape[0]} descriptors")
    else:
        print(f"No descriptors extracted for {location}")
=======
import os
import cv2
import numpy as np

# CONFIGURATION
VIDEO_DIR = r"C:/Users/mhmda/Downloads/dataset_opencv/videos" # dir to retrieve the videos
FEATURES_DIR = r"C:/Users/mhmda/Downloads/dataset_opencv/features_npz" # dir to save the extracted features
os.makedirs(FEATURES_DIR, exist_ok=True)

MAX_FRAMES_PER_LOCATION = 5000  # limit total frames to prevent memory issues
FRAME_SKIP = 5  # keep every 5th frame
RESIZE_DIM = (640, 360)  # resize frames to width x height

# ORB detector
orb = cv2.ORB_create(nfeatures=2000)

# Helper Function
def extract_orb_descriptors(frame):
    """Convert frame to grayscale and compute ORB descriptors."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kp, des = orb.detectAndCompute(gray, None)
    return des

# Processing for each location
for location in os.listdir(VIDEO_DIR):
    location_path = os.path.join(VIDEO_DIR, location)
    if not os.path.isdir(location_path):
        continue

    all_descriptors = []
    frame_count = 0

    print(f"\nProcessing location: {location}")

    for video_file in os.listdir(location_path):
        if not video_file.lower().endswith((".mp4", ".avi", ".mov", ".mkv")):
            continue

        video_path = os.path.join(location_path, video_file)
        cap = cv2.VideoCapture(video_path)
        success = True
        frame_idx = 0

        while success:
            success, frame = cap.read()
            if not success:
                break

            # Skip frames
            if frame_idx % FRAME_SKIP != 0:
                frame_idx += 1
                continue

            # Resize frame
            frame = cv2.resize(frame, RESIZE_DIM)

            # Extract ORB descriptors
            des = extract_orb_descriptors(frame)
            if des is not None:
                all_descriptors.append(des)

            frame_idx += 1
            frame_count += 1

            # Stop if max frames reached
            if frame_count >= MAX_FRAMES_PER_LOCATION:
                break

        cap.release()
        if frame_count >= MAX_FRAMES_PER_LOCATION:
            break

    # Combine all descriptors into one array
    if all_descriptors:
        all_descriptors = np.vstack(all_descriptors)
        output_file = os.path.join(FEATURES_DIR, f"{location}_features.npz")
        np.savez_compressed(output_file, descriptors=all_descriptors)
        print(f"Saved {output_file} with {all_descriptors.shape[0]} descriptors")
    else:
        print(f"No descriptors extracted for {location}")
