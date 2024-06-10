import cv2
import torch

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Check if model.names is a dictionary or list and adjust accordingly
if isinstance(model.names, dict):
    class_names = list(model.names.values())
else:
    class_names = model.names

# Filter classes for 'dog' and 'cat'
cat_dog_class_ids = [class_names.index('dog'), class_names.index('cat')]

# Initialize video capture (0 for the default camera)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Perform inference
    results = model(frame)
    
    # Extract detections for 'dog' and 'cat'
    for *box, conf, cls in results.xyxy[0]:
        if int(cls) in cat_dog_class_ids:
            x1, y1, x2, y2 = map(int, box)
            label = f'{class_names[int(cls)]} {conf:.2f}'
            color = (0, 255, 0) if int(cls) == class_names.index('dog') else (255, 0, 0)
            
            # Draw bounding box and label
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    # Display the frame
    cv2.imshow('YOLOv5 Real-Time Detection', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture object and close display window
cap.release()
cv2.destroyAllWindows()