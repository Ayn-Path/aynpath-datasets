# aynpath-datasets

## Overview  
This repository contains the **image feature datasets (NPZ format)** used in the *Ayn-Path Indoor Navigation System*.  
The dataset was collected from indoor environments (eg: hallways, musolla, café, etc) and processed into feature descriptors for:  

* ORB feature matching  
* Location classification with CNN/MobileNetV2  
* Indoor navigation testing  

## Contents  
* `features_npz/` → Extracted ORB features (`.npz` files)  
* `raw_images/` (optional) → Original collected images  
* `labels.csv` → Location mapping and class labels  

## Notes  
* Dataset is **environment-specific** (IIUM hallways, musolla, café).  
* Accuracy may vary depending on lighting, camera quality, and angles.  
* Intended for **academic use only**.  
