# Hybrid YOLO-MF-MLSN TB Detection

## Features
- Lung segmentation using U-Net
- TB lesion detection using YOLOv8
- Multi-frequency enhancement
- Statistical normalization
- Evaluation metrics

## Run Steps

1. Install dependencies
pip install -r requirements.txt

2. Train U-Net
python train_unet.py

3. Run YOLO detection
python detect_yolo.py

4. Enhance image
python enhance.py

5. Evaluate
python evaluate.py
