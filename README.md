# Tugas-Project--Data-Scientis-Phone-Sales-in-India-using-Kaggle-data-and-Streamlit


[![Pre-commit](https://img.shields.io/badge/pre--commit-passing-brightgreen?logo=github)](https://github.com/ilhamsaang/Tugas-Data/actions)   [![Tests](https://img.shields.io/badge/tests-passing-brightgreen?logo=github)](https://github.com/ilhamsaang/Tugas-Data/actions)    [![Documentation](https://img.shields.io/badge/Documentation-file-brightblue?logo=readthedocs)](https://docs.google.com/presentation/d/1YEaij5ZeBIOCvQnU78l52Ax7VHRz04ZD/edit?usp=sharing&ouid=106174243456610507450&rtpof=true&sd=true)   [![Dibimbing](https://img.shields.io/badge/Dibimbing-Online%20Bootcamp-Green?logo=bookstack&logoColor=white)](https://dibimbing.id/en) [![Deploy App](https://img.shields.io/badge/Dibimbing-Online%20Bootcamp-Green?logo=app&logoColor=white)]()

> Disusun untuk program pelatihan **Data Science Fundamental (DSF) : Data Scientis** di <img src="./asset/Dbimbing Logo.png" alt="Dbimbing" width="10"/> [DBimbing](https://dibimbing.id/en)

> __dibuat Oleh: Mohammad Ilham__

> __Tahun: 2025__

Terima kasih kepada:
<img src="./asset/Dbimbing Logo.png" alt="Dbimbing" width="10"/> [DBimbing](https://dibimbing.id/en)

## 🎯 Tujuan

Membangun **dashboard interaktif Streamlit** untuk menganalisis penjualan dan performa produk smartphone di india berdasarkan:
- Harga jual vs harga asli
- Diskon
- Rating pengguna
- Spesifikasi (RAM, storage, kamera)
- Brand-brand populer di pasar

---

## 📂 Struktur Data

| Kolom                 | Deskripsi                                  |
|----------------------|---------------------------------------------|
| `Brands`             | Merek HP (Samsung, Apple, dll)              |
| `Models`             | Model HP (Galaxy A14, iPhone 13, dll)       |
| `Memory`             | RAM (GB)                                    |
| `Storage`            | Internal storage (GB)                       |
| `Camera`             | Resolusi kamera atau hanya status ("Yes")   |
| `Rating`             | Rating pengguna (1.0 – 5.0)                 |
| `Selling Price`      | Harga jual saat ini                         |
| `Original Price`     | Harga awal sebelum diskon                   |
| `Mobile`             | Kombinasi Brand + Model                     |
| `Discount`           | Nilai diskon nominal                        |
| `discount percentage`| Persentase diskon (%)                       |

---

## 📈 Hasil Visualisasi

### 1️⃣ Korelasi Fitur Numerik & Performa Brand

![heatmap_and_performance](./heatmap fitur numerik dan performa brand berdasarkan harga vs rating.png)

- **Selling Price** & **Original Price** memiliki korelasi hampir sempurna (0.99)
- **Discount** dan **discount percentage** juga sangat berkorelasi (0.66)
- **Rating** hanya sedikit berkorelasi dengan harga → artinya kualitas tidak selalu tergantung harga

📌 Brand seperti **Apple** punya harga tinggi & rating tinggi, sedangkan brand lain seperti **realme** punya value-for-money bagus.

---

### 2️⃣ Korelasi Rating, Diskon & Rata-rata Diskon per Brand

![korelasi_rating_diskon](./Korelasi Rating vs Selling Price, Distribusi diskon, dan rata rata diskon perbrand.png)

- Scatter plot: hubungan rating vs harga jual menunjukkan tren lemah (r = 0.39)
- Histogram: mayoritas produk memiliki diskon sangat kecil atau tidak ada
- Barplot: brand seperti **Motorola, POCO** memberi diskon lebih besar dibanding Apple/Samsung

---

### 3️⃣ Rata-rata Harga Jual & Asli per Brand

![selling_vs_original](./Average Selling vs Original Price per Brand (Sorted by Selling Price).png)

- Apple tetap mendominasi dengan harga tertinggi, baik jual maupun asli
- Brand seperti **Infinix**, **Lenovo**, dan **GIONEE** ada di pasar low-end

---

### 4️⃣ Diskon: Distribusi & Hubungan dengan Harga

![diskon_4_plot](./distribusi persentase diskon, disribusi persentase diskon per brand, hubungan diskon dan harga jual, korelasi vs presentase diskon.png)

- Diskon >20% sangat jarang
- Beberapa brand tertentu cenderung memberi diskon besar (tapi bukan yang paling laku)
- Korelasi diskon nominal dan persentase cukup kuat → diskon besar = % besar juga

---

## 🧠 Insight Utama

- **Harga tidak menjamin kualitas** — rating rata-rata hampir merata di semua brand
- **Brand low-end lebih agresif diskon**, tapi tidak menjamin performa lebih baik
- **Apple & Samsung** tetap punya posisi kuat walau minim diskon
- **realme** dan **Redmi** jadi pesaing serius di kategori value-for-money

---

## 🛠️ Teknologi yang Digunakan

- Python (Pandas, Seaborn, Matplotlib)
- Streamlit
- Google Colab + pyngrok
- VS Code
- GitHub (untuk repo dan dokumentasi)


Ikuti dan dukung Dbimbing:
- 🌐 Website: [dbimbing.id](https://dibimbing.id/en)
- 📷 Instagram: [@dbimbing](https://www.instagram.com/dibimbing.id/)
- ▶️ YouTube: [Dbimbing Official](https://www.youtube.com/@dibimbingid)

> Dibuat dengan semangat belajar bersama komunitas Dbimbing 🚀
