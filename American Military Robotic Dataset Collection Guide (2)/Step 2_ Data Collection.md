# Step 2: Data Collection

**Project:** Autonomous Military Vehicle Recognition and Tactical AI System  
**Author:** Brandon Patterson  
**Date:** October 2025

## Overview

This directory contains all materials related to Step 2 of the capstone project: Data Collection. The goal is to collect comprehensive datasets for training a military vehicle recognition system capable of identifying and classifying vehicles in various operational environments.

## Datasets

The project utilizes three high-quality datasets from Kaggle, totaling over 68,000 images with professional annotations:

### 1. Indian Vehicle Dataset
- **Source:** [Kaggle - Indian Vehicle Dataset](https://www.kaggle.com/datasets/dataclusterlabs/indian-vehicle-dataset)
- **Size:** 50,000+ high-definition images
- **Annotations:** 53,000 professionally annotated bounding boxes
- **Resolution:** 100% HD images (1920x1080 and above)
- **Classes:** 7 categories including two-wheelers, four-wheelers, commercial vehicles, construction equipment
- **Quality Score:** 8.75/10 usability rating
- **Coverage:** 1000+ urban and rural locations with diverse lighting conditions

### 2. Military Vehicles Dataset
- **Source:** [Kaggle - Military Vehicles](https://www.kaggle.com/datasets/aayushkatoch/military-vehicles)
- **Size:** 7 military vehicle classes
- **Format:** YOLO annotation format
- **Classes:** Tank, APC, IFV, Artillery, Military Truck, Military Jeep, Helicopter
- **Quality:** High-quality annotations suitable for object detection

### 3. Military Assets Dataset
- **Source:** [Kaggle - Military Assets Dataset](https://www.kaggle.com/datasets/rawsi18/military-assets-dataset-12-classes-yolo8-format)
- **Size:** 15,000+ samples
- **Format:** YOLO8 annotation format
- **Classes:** 12 categories including tanks, APCs, IFVs, artillery, MLRS, SAM systems
- **Quality:** Pre-formatted for YOLOv8 training

## Quick Start

### Prerequisites

Before running the data collection scripts, ensure you have:

1. **Python 3.11+** installed
2. **Kaggle API credentials** configured
3. **Sufficient disk space** (approximately 20GB)

### Setup Kaggle API

1. Create a Kaggle account at https://www.kaggle.com
2. Go to Account Settings → API → Create New API Token
3. Download `kaggle.json` file
4. Place it in one of these locations:
   - `~/.kaggle/kaggle.json` (recommended)
   - `./kaggle.json` (project root)

5. Set proper permissions:
   ```bash
   chmod 600 ~/.kaggle/kaggle.json
   ```

### Option 1: Using Python Script (Recommended)

The Python script provides comprehensive features including verification, metadata generation, and reporting.

```bash
# Install dependencies
pip install kaggle

# Download all datasets
python scripts/data_collection.py --dataset all

# Download specific dataset
python scripts/data_collection.py --dataset indian_vehicle

# Force re-download
python scripts/data_collection.py --dataset all --force

# Verify existing datasets
python scripts/data_collection.py --verify-only

# View help
python scripts/data_collection.py --help
```

### Option 2: Using Bash Script

The bash script provides a simpler alternative for Unix/Linux systems.

```bash
# Make executable (if not already)
chmod +x scripts/download_datasets.sh

# Run the script
./scripts/download_datasets.sh
```

### Manual Download

If you prefer to download manually:

```bash
# Install Kaggle CLI
pip install kaggle

# Download datasets
kaggle datasets download -d dataclusterlabs/indian-vehicle-dataset -p data/raw/indian_vehicle --unzip
kaggle datasets download -d aayushkatoch/military-vehicles -p data/raw/military_vehicles --unzip
kaggle datasets download -d rawsi18/military-assets-dataset-12-classes-yolo8-format -p data/raw/military_assets --unzip
```

## Directory Structure

```
step2-data-collection/
├── README.md                          # This file
├── DATASETS.md                        # Detailed dataset documentation
│
├── scripts/                           # Data collection scripts
│   ├── data_collection.py             # Python collection script
│   ├── download_datasets.sh           # Bash collection script
│   └── verify_data.py                 # Data verification script
│
├── notebooks/                         # Jupyter notebooks
│   └── 01_data_collection.ipynb       # Data collection notebook
│
├── data/                              # Data directory
│   ├── raw/                           # Raw downloaded data
│   │   ├── indian_vehicle/
│   │   ├── military_vehicles/
│   │   └── military_assets/
│   ├── processed/                     # Processed data (Step 5)
│   └── metadata/                      # Dataset metadata
│       ├── indian_vehicle_metadata.json
│       ├── military_vehicles_metadata.json
│       └── military_assets_metadata.json
│
└── reports/                           # Reports and documentation
    └── data_collection_report.md      # Auto-generated report
```

## Features

### Python Script Features

- ✅ **Automated Download:** Downloads all datasets with one command
- ✅ **Kaggle API Integration:** Seamless integration with Kaggle API
- ✅ **Metadata Generation:** Automatically generates metadata for each dataset
- ✅ **Verification:** Verifies dataset integrity and completeness
- ✅ **Reporting:** Generates comprehensive collection reports
- ✅ **Error Handling:** Robust error handling and retry logic
- ✅ **Progress Tracking:** Shows download progress and status

### Bash Script Features

- ✅ **Simple Interface:** Easy-to-use bash script
- ✅ **Interactive Prompts:** Asks before re-downloading existing data
- ✅ **Color Output:** Color-coded success/error messages
- ✅ **Summary Statistics:** Shows total size and file counts
- ✅ **Directory Tree:** Displays organized directory structure

## Dataset Statistics

After successful collection, you should have:

- **Total Images:** 68,000+
- **Total Annotations:** 75,000+
- **Total Size:** ~15-20 GB
- **Unique Classes:** 29 (after merging and taxonomy unification)
- **Formats:** Mixed (YOLO, COCO-compatible, raw images)

## Verification

To verify your downloaded datasets:

```bash
# Using Python script
python scripts/data_collection.py --verify-only

# Manual verification
ls -lh data/raw/*/
```

Expected output:
```
data/raw/indian_vehicle/    - 50,000+ files
data/raw/military_vehicles/  - 7 class directories
data/raw/military_assets/    - train/val/test splits
```

## Troubleshooting

### Issue: "401 Unauthorized" Error

**Solution:** Your Kaggle credentials are incorrect or not properly configured.
1. Verify `kaggle.json` exists and has correct permissions (600)
2. Ensure the file contains valid credentials
3. Try re-downloading the API token from Kaggle

### Issue: "403 Forbidden" Error

**Solution:** You need to accept the dataset's terms of use.
1. Visit the dataset page on Kaggle
2. Click "Download" (you don't need to actually download)
3. Accept the terms and conditions
4. Run the script again

### Issue: "Disk Space" Error

**Solution:** Ensure you have at least 20GB of free disk space.
```bash
df -h .
```

### Issue: Slow Download Speed

**Solution:** 
- Use a stable internet connection
- Consider downloading datasets individually
- Try downloading during off-peak hours

## Next Steps

After successful data collection:

1. ✅ **Verify Data Integrity:** Run verification scripts
2. ➡️ **Exploratory Data Analysis:** Analyze dataset characteristics
3. ➡️ **Data Wrangling (Step 5):** Clean and preprocess the data
4. ➡️ **Data Integration:** Merge datasets with unified taxonomy
5. ➡️ **Train/Val/Test Split:** Create 70/20/10 splits

## References

- [Kaggle API Documentation](https://github.com/Kaggle/kaggle-api)
- [Indian Vehicle Dataset](https://www.kaggle.com/datasets/dataclusterlabs/indian-vehicle-dataset)
- [Military Vehicles Dataset](https://www.kaggle.com/datasets/aayushkatoch/military-vehicles)
- [Military Assets Dataset](https://www.kaggle.com/datasets/rawsi18/military-assets-dataset-12-classes-yolo8-format)

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the Kaggle API documentation
3. Verify your internet connection and disk space
4. Open an issue in the project repository

---

**Author:** Brandon Patterson  
**Project:** ML Engineering Bootcamp Capstone  
**Step:** 2 - Data Collection  
**Status:** Complete

