import cv2  
import torch  

# Memuat model YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Memeriksa apakah model.names adalah dictionary atau list dan menyesuaikan sesuai
if isinstance(model.names, dict):  
    class_names = list(model.names.values())  
else:  
    class_names = model.names  

# Memfilter kelas untuk 'dog' dan 'cat'
cat_dog_class_ids = [class_names.index('dog'), class_names.index('cat')]  

# Inisialisasi video capture (0 untuk kamera default)
cap = cv2.VideoCapture(0)  

while cap.isOpened():  
    ret, frame = cap.read()  
    if not ret: 
        break  

    # Melakukan inferensi
    results = model(frame) 

    # Ekstrak deteksi untuk 'dog' dan 'cat'
    for *box, conf, cls in results.xyxy[0]:  
        if int(cls) in cat_dog_class_ids:  
            x1, y1, x2, y2 = map(int, box)  
            label = f'{class_names[int(cls)]} {conf:.2f}'  
            color = (0, 255, 0) if int(cls) == class_names.index('dog') else (255, 0, 0)  

            # Menggambar kotak pembatas dan label
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)  
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2) 
            
    # Menampilkan frame
    cv2.imshow('YOLOv5 Real-Time Detection', frame) 

    # Hentikan loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break  

# Melepaskan objek video capture dan menutup jendela tampilan
cap.release()  
cv2.destroyAllWindows()  
