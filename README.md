# Pratikum Komputasi Numerik

Library yang dibutuhkan:

- `numpy` (untuk komputasi array)
- `matplotlib` (untuk visualisasi grafik)
- `pandas` (untuk merapikan tabel iterasi)
- `sympy` (untuk memproses input persamaan string)
- `flask` (untuk web interface)

Buat dan aktifkan virtual environment, lalu install dependency:

```bash
python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows

pip install numpy matplotlib pandas sympy flask
```

## Cara Menjalankan

1. **Clone repositori ini:**
```
git clone https://github.com/acaryawibawantra/Pratikum-komputasi-numerik.git

cd Pratikum-komputasi-numerik
```
2. Jalankan web app:
```
python app.py
```

Buka browser di `http://127.0.0.1:5000`

---

# Hasil Praktikum 1 (ppt2): Metode Regula Falsi

Mengimplementasikan metode tertutup Regula Falsi yang mampu menampilkan:

- Tabel iterasi numerik secara lengkap.
- Visualisasi grafik fungsi f(x) beserta posisi akar pada sumbu X.

### Analisis Soal

- Persamaan: f(x) = x**3 - x - 1
- Batas awal: a = 1, b = 2
- Toleransi: 0.0001

### Hasil Pengerjaan

| Metrik | Hasil |
| --- | --- |
| Akar ditemukan | x ≈ 1.324704 |
| Jumlah iterasi | 12 iterasi |
| Status | Konvergen |

---

# Hasil Tugas Pratikum #1 (ppt3): Metode Secant

Membangun program dengan User Interface terminal yang fleksibel untuk mempermudah pengguna dalam mengevaluasi berbagai persamaan matematika tanpa memodifikasi source code.

- Fleksibilitas Input: Menggunakan library `SymPy` untuk melakukan parsing persamaan langsung dari input pengguna.
- Analisis Numerik: Menampilkan proses iterasi hingga mencapai toleransi error yang ditentukan.

### Analisis Soal

- Persamaan: f(x) = x**3 - x - 1
- Tebakan awal: x₀ = 1, x₁ = 2
- Toleransi: 0.0001

### Hasil Pengerjaan

| Metrik | Hasil |
| --- | --- |
| Akar ditemukan | x ≈ 1.324704 |
| Jumlah iterasi | 5 iterasi |
| Status | Konvergen (lebih cepat dari Regula Falsi) |

---

# Hasil Tugas Pratikum #3 (ppt6): Integrasi Romberg

Membangun program web-based menggunakan Flask yang mengimplementasikan metode Integrasi Romberg untuk mengatasi kelemahan metode Trapezoidal yang membutuhkan jumlah interval besar untuk mencapai akurasi tinggi.

- **Web Interface**: Pengguna dapat menginput persamaan/fungsi melalui browser tanpa menjalankan terminal.
- **Romberg Integration**: Menggunakan Richardson Extrapolation pada hasil Trapezoidal untuk mempercepat konvergensi.
- **Matriks Romberg**: Menampilkan matriks segitiga R[i][j] lengkap dengan orde akurasi O(H²), O(H⁴), O(H⁶), O(H⁸).

### Analisis Soal

- Persamaan: f(x) = x**2
- Batas bawah: a = 0, Batas atas: b = 4
- Baris matriks: 4 iterasi

### Hasil Pengerjaan

| Metrik | Hasil |
| --- | --- |
| Hasil Integral | 21.333333333333332 |
| Status | Konvergen Sempurna |

### Matriks Segitiga Romberg

| Iterasi | O(H²) | O(H⁴) | O(H⁶) | O(H⁸) |
| --- | --- | --- | --- | --- |
| 1 | 32.00000000 | - | - | - |
| 2 | 24.00000000 | 21.33333333 | - | - |
| 3 | 22.00000000 | 21.33333333 | 21.33333333 | - |
| 4 | 21.50000000 | 21.33333333 | 21.33333333 | 21.33333333 |

Kolom pertama (O(H²)) adalah hasil Trapezoidal biasa — membutuhkan banyak interval dan masih error. Kolom berikutnya menggunakan ekstrapolasi Richardson yang langsung konvergen ke nilai exact 64/3 ≈ 21.3333.

<img width="1423" height="914" alt="Screenshot 2026-06-15 at 15 29 01" src="https://github.com/user-attachments/assets/ff515ea9-7b7d-427d-a0c3-89c05a302bc3" />

