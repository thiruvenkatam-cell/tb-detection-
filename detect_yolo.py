from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # or your trained model

results = model("data/images/sample.png", save=True)

for r in results:
    print(r.boxes)
