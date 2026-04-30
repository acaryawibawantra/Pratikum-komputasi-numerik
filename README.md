# Pratikum-komputasi-numerik

Library yang dibutuhkan:
- `numpy` (untuk komputasi array)
- `matplotlib` (untuk visualisasi grafik)
- `pandas` (untuk merapikan tabel iterasi)
- `sympy` (untuk memproses input persamaan string)

Buat dan aktifkan virtual environment, lalu install dependency:
```bash
python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows

pip install numpy matplotlib pandas sympy
```

## Cara Menjalankan

1. **Clone repositori ini:**
   ```bash
   git clone [https://github.com/acaryawibawantra/Pratikum-komputasi-numerik.git](https://github.com/acaryawibawantra/Pratikum-komputasi-numerik.git)
   cd Pratikum-komputasi-numerik

# Hasil Praktikum 1: Metode Regula Falsi

Mengimplementasikan metode tertutup Regula Falsi yang mampu menampilkan:

- Tabel iterasi numerik secara lengkap.

- Visualisasi grafik fungsi f(x) beserta posisi akar pada sumbu X.

Analisis Soal

- Persamaan: f(x) = x**3 - x - 1

- Batas awal: a = 1, b = 2

- Toleransi: 0.0001

Hasil Pengerjaan

### Hasil Pengerjaan

| Metrik           | Hasil        |
|------------------|-------------:|
| Akar ditemukan   | x ≈ 1.324704 |
| Jumlah iterasi   | 12 iterasi   |
| Status           | Konvergen    |


<img width="514" height="257" alt="Screenshot 2026-04-30 at 20 30 00" src="https://github.com/user-attachments/assets/cb4449fa-0a71-4a10-9262-d9834c92e4a5" />

Hasil Grafik : 
<img width="998" height="664" alt="Screenshot 2026-04-30 at 20 30 21" src="https://github.com/user-attachments/assets/e73664c9-1800-448e-a88c-19a94e6de8c9" />




# Hasil Praktikum 2: Metode Secant

Membangun program dengan User Interface terminal yang fleksibel untuk mempermudah pengguna dalam mengevaluasi berbagai persamaan matematika tanpa memodifikasi source code.

- Fleksibilitas Input: Menggunakan library ‎`SymPy` untuk melakukan parsing persamaan langsung dari input pengguna.

- Analisis Numerik: Menampilkan proses iterasi hingga mencapai toleransi error yang ditentukan.

Analisis Soal

- Persamaan: f(x) = x**3 - x - 1

- Tebakan awal: x₀ = 1, x₁ = 2

- Toleransi: 0.0001

| Metrik           | Hasil        |
|------------------|-------------:|
| Akar ditemukan   | x ≈ 1.324704 |
| Jumlah iterasi   | 5 iterasi   |
| Status           | Konvergen (lebih cepat dari Regula Falsi)    |

<img width="486" height="267" alt="Screenshot 2026-04-30 at 20 46 38" src="https://github.com/user-attachments/assets/0c1ee32e-1da3-414a-a4cc-38d3dcdc9dfa" />

Hasil Grafik
<img width="998" height="663" alt="Screenshot 2026-04-30 at 20 46 54" src="https://github.com/user-attachments/assets/b40ff311-ce22-4e9a-9e59-d3431e18e5d7" />



