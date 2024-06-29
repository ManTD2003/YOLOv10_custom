from ultralytics import YOLOv10

# Load model
model = YOLOv10('yolov10m.pt')

# Train model
model.train(
    data = 'data.yaml', 
    epochs = 100, 
    batch = 64, 
    imgsz = 640, 
    project = "/mnt/man/",
    name = "Polyp", 
    exist_ok = True,
    optimizer = "Adam",
    lr0 = 1e-3,
    device = "0",
)
