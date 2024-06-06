# PetDetection
Kelompok 6 Praktikum Artificial Intelligence 2024
<p align="center">
  <h2 align="center">
    Cat and Dog Detection
  </h2>
</p>

<!-- Daftar Isi -->
<details open="open">
  <summary><h2 style="display: inline-block">Daftar Isi</h2></summary>
  <ol>
    <li><a href="#anggota-tim">Anggota Tim</a></li>
    <li><a href="#latar-belakang">Latar Belakang</a></li>
    <li><a href="#tujuan-dan-manfaat">Tujuan dan Manfaat</a></li>
    <li><a href="#penjelasan-aplikasi">Penjelasan Aplikasi</a></li>
    <li><a href="#rencana-pengerjaan-proyek">Rencana Pengerjaan Proyek</a></li>
    <li><a href="#lisensi">Lisensi</a></li>
  </ol>
</details>

<!-- Anggota Tim -->
## Anggota Tim
| NPM           | Name                        |
| ------------- |-----------------------------|
| 140810220001  | Nadia Mulyadi               |
| 140810220015  | Devi Humaira                |
| 140810220029  | Reghina Maisarah            |
| 140810220071  | Nabila Rahmanisa P. A.      |

<!-- Latar Belakang -->
## Latar Belakang
Perkembangan teknologi informasi dan komunikasi telah membawa banyak perubahan dalam berbagai aspek kehidupan manusia, termasuk dalam bidang kecerdasan buatan (Artificial Intelligence). AI kini mampu menyelesaikan berbagai masalah kompleks yang dulunya memerlukan keterlibatan manusia secara intensif. Salah satu bidang yang mengalami banyak kemajuan berkat AI adalah pengenalan gambar (image recognition), yang dapat diaplikasikan untuk berbagai keperluan, termasuk deteksi hewan peliharaan.

Deteksi objek menggunakan teknologi deep learning, khususnya dengan metode Convolutional Neural Network (CNN), telah menunjukkan performa yang sangat baik dalam beberapa tahun terakhir. Salah satu model yang terkenal dan banyak digunakan untuk ini adalah YOLO (You Only Look Once), yang kini telah mencapai versi kelima, yaitu YOLOv5. Model ini dikenal karena kecepatannya dalam melakukan deteksi secara real-time dan akurasi yang tinggi.

Di era digital ini, banyak orang yang memiliki hewan peliharaan dan memanfaatkan teknologi untuk merawat dan memantau hewan-hewan mereka. Namun, salah satu tantangan yang sering dihadapi adalah identifikasi dan pemantauan hewan peliharaan secara otomatis, terutama ketika hewan-hewan tersebut berada di luar pengawasan.

<!-- Tujuan dan Manfaat -->
## Tujuan dan Manfaat

Tujuan :
1. Mengembangkan program berbasis AI yang dapat mendeteksi dan mengenali hewan peliharaan seperti anjing, kucing, dan kelinci dari gambar menggunakan YOLOv5.
2. Output dari sistem ini akan berupa informasi hewan peliharaan yang terdeteksi dan ditampilkan dalam bentuk visual dan tekstual.
3. Membuat program yang mudah diimplementasikan dan digunakan oleh pengguna dengan berbagai tingkat keahlian teknis.

Manfaat Bagi Pembuat Program:
1. Meningkatkan pemahaman dan keterampilan dalam pengembangan aplikasi AI dan deep learning, khususnya dalam menggunakan model YOLOv5.
2. Mendorong inovasi dan kreativitas dalam menciptakan solusi baru untuk masalah yang ada, serta mengembangkan aplikasi praktis yang dapat digunakan dalam kehidupan sehari-hari.
3. Memperluas wawasan dan pengetahuan teknis melalui eksplorasi dan implementasi algoritma baru, serta mendorong pengembangan kode yang lebih efisien dan efektif untuk berbagai aplikasi.

<!-- Penjelasan Aplikasi -->
## Penjelasan Program
Sebagai anak kuliah, banyak yang memiliki hewan peliharaan atau minat terhadap hewan peliharaan. Dengan mengembangkan program deteksi kucing dan anjing dapat mengaplikasikan pengetahuan dan minat dalam dunia teknologi dan komputer untuk menciptakan sesuatu yang praktis dan bermanfaat dalam kehidupan sehari-hari. 

Program ini memanfaatkan teknologi machine learning, sebagai berikut.
1. Convolutional Neural Network (CNN):
   Digunakan untuk deteksi dan klasifikasi gambar objek hewan peliharaan.

2. OpenCV:
   Library untuk pemrosesan gambar dan video.

3. TensorFlow/Keras:
   Framework untuk membangun dan melatih model machine learning.

4. PyTorch:
   Framework untuk menggunakan YOLOv5

6. Python:
   Bahasa pemrograman utama yang digunakan untuk pengembangan aplikasi.

Proyek ini memberikan kesempatan untuk belajar dan meningkatkan keterampilan dalam bidang pemrosesan gambar, pembelajaran mendalam, dan visi komputer dan kecerdasan buatan. Dengan mengerjakan proyek ini, kita dapat mendapatkan pengalaman praktis yang berharga dan memperluas pemahaman tentang konsep-konsep penting dalam bidang AI.

Alasan menggunakan YOLOv5:

1. Kecepatan dan Efisiensi Real-time:
   YOLOv5 dirancang untuk kecepatan dan efisiensi, memungkinkan deteksi objek dalam gambar atau video secara real-time. Ini sangat penting untuk aplikasi yang membutuhkan respons cepat, seperti pengawasan video atau aplikasi interaktif yang memerlukan deteksi hewan peliharaan.
   
2. Akurasi Tinggi
   :YOLOv5 telah terbukti memberikan akurasi yang tinggi dalam mendeteksi berbagai objek, termasuk kucing dan anjing. Model ini mampu mendeteksi dan mengklasifikasikan objek dengan baik, bahkan dalam kondisi pencahayaan yang buruk atau latar belakang yang rumit.
   
3. Kemampuan Deteksi Multi-Objek:
   YOLOv5 dapat mendeteksi beberapa objek dalam satu gambar atau frame video, yang sangat berguna ketika terdapat lebih dari satu hewan peliharaan dalam gambar atau video. Model ini tidak hanya mengenali keberadaan kucing dan anjing tetapi juga mampu membedakan antara kedua jenis hewan tersebut.
   
4. Kemudahan Implementasi dan Penggunaan:
   YOLOv5 relatif mudah untuk diimplementasikan dibandingkan dengan beberapa model deteksi objek lainnya. Tersedia berbagai sumber daya, tutorial, dan komunitas pendukung yang besar, yang memudahkan proses pengembangan dan troubleshooting.

5. Dukungan untuk Berbagai Resolusi Gambar:
   YOLOv5 dapat bekerja dengan berbagai resolusi gambar tanpa kehilangan kinerja signifikan. Hal ini memungkinkan deteksi yang fleksibel pada berbagai kualitas gambar, dari resolusi rendah hingga tinggi.

<!-- Rencana Pengerjaan Proyek -->
## Rencana Pengerjaan Proyek

Untuk pelaksanaan proyek ini kami mempersiapkan beberapa rencana:

1. Membuat grup koordinasi di platform WhatsApp untuk saling mengabarkan progress

2. Membagi jobdesk tiap anggota

3. Melakukan meet di Discord/luring untuk mengerjakan bersama

<!-- Lisensi -->
## Lisensi

MIT License 2024
