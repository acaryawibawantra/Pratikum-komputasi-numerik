import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sympy import sympify, symbols, lambdify

def main():
    print("PROGRAM METODE SECANT (PRAKTIKUM 2)")
    
    # 1. ui buat user input
    persamaan_str = input("Masukkan persamaan f(x) (contoh: x**3 - x - 1): ")
    x0 = float(input("Masukkan tebakan awal x0: "))
    x1 = float(input("Masukkan tebakan awal x1: "))
    tol = float(input("Masukkan toleransi error (contoh: 0.0001): "))
    max_iter = int(input("Masukkan maksimal iterasi: "))

    # Mengubah string menjadi fungsi matematika
    x_sym = symbols('x')
    expr = sympify(persamaan_str)
    f = lambdify(x_sym, expr)

    # 2. ALGORITMA SECANT
    data_log = []
    
    for i in range(1, max_iter + 1):
        fx0 = f(x0)
        fx1 = f(x1)
        
        # Cek pembagi nol
        if fx1 - fx0 == 0:
            print("Gagal: Pembagi nol dideteksi.")
            break
            
        # Rumus Secant
        x_baru = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        error = abs(f(x_baru))
        
        data_log.append([i, x0, x1, x_baru, f(x_baru), error])
        
        if error < tol:
            break
            
        # Update nilai untuk iterasi berikutnya
        x0 = x1
        x1 = x_baru

    # 3. OUTPUT TABEL
    df = pd.DataFrame(data_log, columns=['Iterasi', 'x(n-1)', 'x(n)', 'x(baru)', 'f(x_baru)', 'Error'])
    print("\n--- Hasil Proses Iteratif ---")
    print(df.to_string(index=False))
    
    akar_akhir = x1
    print(f"\nAkar ditemukan pada x = {akar_akhir:.6f}")

    x_vals = np.linspace(akar_akhir - 2, akar_akhir + 2, 400)
    y_vals = [f(val) for val in x_vals]

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label=f'f(x) = {persamaan_str}', color='green')
    plt.axhline(0, color='red', linestyle='--')
    plt.scatter([akar_akhir], [0], color='black', label=f'Akar ≈ {akar_akhir:.4f}')
    
    plt.title(f'Grafik Metode Secant: {persamaan_str}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()