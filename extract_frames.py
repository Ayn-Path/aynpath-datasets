import os
import cv2

# Input and output directories
VIDEO_DIR = "C:/Users/mhmda/Downloads/dataset_opencv/videos"
OUTPUT_DIR = "C:/Users/mhmda/Downloads/dataset_opencv/databases"

# Loop through each subfolder in VIDEO_DIR
for location in os.listdir(VIDEO_DIR):
    location_path = os.path.join(VIDEO_DIR, location)

    # Skip if not a folder
    if not os.path.isdir(location_path):
        continue

    # Create matching output folder
    output_location_path = os.path.join(OUTPUT_DIR, location)
    os.makedirs(output_location_path, exist_ok=True)

    print(f"Processing location: {location}")

    # Loop through videos in this location
    for video_file in os.listdir(location_path):
        if not video_file.lower().endswith((".mp4", ".avi", ".mov", ".mkv")):
            continue

        video_path = os.path.join(location_path, video_file)
        cap = cv2.VideoCapture(video_path)

        frame_count = 0
        success = True

        while success:
            success, frame = cap.read()
            if not success:
                break

            # Save frames with video name prefix
            frame_filename = os.path.join(
                output_location_path,
                f"{os.path.splitext(video_file)[0]}_frame_{frame_count:04d}.jpg"
            )
            cv2.imwrite(frame_filename, frame)
            frame_count += 1

        cap.release()
        print(f"  Extracted {frame_count} frames from {video_file}")
=======
import os
import cv2

# Input and output directories
VIDEO_DIR = "C:/Users/mhmda/Downloads/dataset_opencv/videos"
OUTPUT_DIR = "C:/Users/mhmda/Downloads/dataset_opencv/databases"

# Loop through each subfolder in VIDEO_DIR
for location in os.listdir(VIDEO_DIR):
    location_path = os.path.join(VIDEO_DIR, location)

    # Skip if not a folder
    if not os.path.isdir(location_path):
        continue

    # Create matching output folder
    output_location_path = os.path.join(OUTPUT_DIR, location)
    os.makedirs(output_location_path, exist_ok=True)

    print(f"Processing location: {location}")

    # Loop through videos in this location
    for video_file in os.listdir(location_path):
        if not video_file.lower().endswith((".mp4", ".avi", ".mov", ".mkv")):
            continue

        video_path = os.path.join(location_path, video_file)
        cap = cv2.VideoCapture(video_path)

        frame_count = 0
        success = True

        while success:
            success, frame = cap.read()
            if not success:
                break

            # Save frames with video name prefix
            frame_filename = os.path.join(
                output_location_path,
                f"{os.path.splitext(video_file)[0]}_frame_{frame_count:04d}.jpg"
            )
            cv2.imwrite(frame_filename, frame)
            frame_count += 1

        cap.release()
        print(f"  Extracted {frame_count} frames from {video_file}")
