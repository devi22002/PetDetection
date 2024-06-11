import cv2  # Mengimpor pustaka OpenCV
import torch  # Mengimpor pustaka PyTorch

# Memuat model YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Memeriksa apakah model.names adalah dictionary atau list dan menyesuaikan sesuai
if isinstance(model.names, dict):  # Jika model.names adalah dictionary
    class_names = list(model.names.values())  # Konversi nilai-nilai dictionary menjadi list
else:  # Jika model.names adalah list
    class_names = model.names  # Gunakan langsung list dari model.names

# Memfilter kelas untuk 'dog' dan 'cat'
cat_dog_class_ids = [class_names.index('dog'), class_names.index('cat')]  # Dapatkan indeks kelas 'dog' dan 'cat'

# Inisialisasi video capture (0 untuk kamera default)
cap = cv2.VideoCapture(0)  # Buka koneksi ke kamera default

while cap.isOpened():  # Loop berjalan selama kamera terbuka
    ret, frame = cap.read()  # Membaca frame dari kamera
    if not ret:  # Jika frame tidak berhasil dibaca, keluar dari loop
        break  # Keluar dari loop

    # Melakukan inferensi
    results = model(frame)  # Melakukan inferensi pada frame

    # Ekstrak deteksi untuk 'dog' dan 'cat'
    for *box, conf, cls in results.xyxy[0]:  # Iterasi melalui setiap deteksi
        if int(cls) in cat_dog_class_ids:  # Memeriksa apakah kelas adalah 'dog' atau 'cat'
            x1, y1, x2, y2 = map(int, box)  # Mengonversi koordinat kotak pembatas menjadi integer
            label = f'{class_names[int(cls)]} {conf:.2f}'  # Membuat label dengan nama kelas dan kepercayaan
            color = (0, 255, 0) if int(cls) == class_names.index('dog') else (255, 0, 0)  # Warna kotak (hijau untuk anjing, merah untuk kucing)

            # Menggambar kotak pembatas dan label
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)  # Menggambar kotak pembatas pada frame
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)  # Menambahkan label di atas kotak pembatas

    # Menampilkan frame
    cv2.imshow('YOLOv5 Real-Time Detection', frame)  # Menampilkan frame yang telah diproses

    # Hentikan loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Menunggu 1 ms untuk input kunci dan memeriksa apakah tombol 'q' ditekan
        break  # Keluar dari loop

# Melepaskan objek video capture dan menutup jendela tampilan
cap.release()  # Menutup koneksi ke kamera
cv2.destroyAllWindows()  # Menutup semua jendela yang dibuat oleh OpenCV
