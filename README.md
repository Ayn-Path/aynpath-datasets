# aynpath-server_datasets

## Overview  
This repository contains the **image feature datasets (NPZ format)** used in the *Ayn-Path Indoor Navigation System*. 
The dataset was collected from indoor environments at the Kulliyyah of Information and Communication Technology (KICT), IIUM (e.g., hallways, musolla, café, etc) and processed into feature descriptors for:  

* ORB feature matching (Location Prediction)
* Indoor navigation testing  

## Contents  
| Item | Description |
|---|-------------|
| `features_npz` | `.npz` files storing extracted feature descriptors (ORB) |
| `extract_frames.py` | Script to extract image frames (if starting from video / larger image collections) |
| `extract_features.py` | Script to compute feature descriptors from images and save as NPZ |

## Notes/Limitations 
* Dataset is **environment-specific** at Block A, Level 1 of KICT, IIUM
* Accuracy may vary depending on lighting, camera quality, and angles.  
* Intended for **academic use only**.  
