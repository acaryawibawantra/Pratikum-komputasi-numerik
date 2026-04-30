import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 1. Definisikan fungsi f(x)
def f(x):
    # Contoh fungsi: x^3 - x - 1
    return x**3 - x - 1

def regula_falsi(a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        print("Error: Batas [a, b] tidak mengurung akar. Tanda f(a) dan f(b) harus berbeda.")
        return None, None

    data_iterasi = []
    
    print("-" * 60)
    print(f"{'Iter':<5} {'a':<10} {'b':<10} {'c':<10} {'f(c)':<10}")
    print("-" * 60)

    for i in range(1, max_iter + 1):
        # Rumus Regula Falsi
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        fc = f(c)
        
        # Simpan data untuk tabel dan grafik
        data_iterasi.append([i, a, b, c, fc])
        print(f"{i:<5} {a:<10.6f} {b:<10.6f} {c:<10.6f} {fc:<10.6f}")

        # Cek toleransi (konvergensi)
        if abs(fc) < tol:
            break
            
        # Update interval
        if f(a) * fc < 0:
            b = c
        else:
            a = c
            
    return data_iterasi, c

batas_bawah = 1.0
batas_atas = 2.0
target_toleransi = 0.0001
maksimal_loop = 20

hasil_iterasi, akar = regula_falsi(batas_bawah, batas_atas, target_toleransi, maksimal_loop)

if akar is not None:
    print("-" * 60)
    print(f"Akar ditemukan di x = {akar:.6f}")

    x_range = np.linspace(batas_bawah - 0.5, batas_atas + 0.5, 500)
    y_range = f(x_range)

    plt.figure(figsize=(10, 6))
    plt.plot(x_range, y_range, label='f(x) = x^3 - x - 1', color='blue', linewidth=2)
    plt.axhline(0, color='black', linestyle='--', linewidth=1) # Sumbu X
    plt.axvline(0, color='black', linestyle='--', linewidth=1) # Sumbu Y
    
    plt.scatter([akar], [0], color='red', s=100, label=f'Akar ≈ {akar:.4f}', zorder=5)
    
    plt.title('Grafik Metode Regula Falsi (Praktikum 1)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()