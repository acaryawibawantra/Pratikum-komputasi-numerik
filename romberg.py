import sympy as sp
import numpy as np

def trapezoid_rule(f_expr, x_sym, a, b, n):
    """Menghitung integrasi menggunakan metode Trapezoida dengan n pias"""
    if n <= 0:
        return 0
    
    h = (b - a) / n
    f_a = float(f_expr.subs(x_sym, a))
    f_b = float(f_expr.subs(x_sym, b))
    
    total_sum = 0.5 * (f_a + f_b)
    for i in range(1, n):
        xi = a + i * h
        total_sum += float(f_expr.subs(x_sym, xi))
        
    return h * total_sum

def romberg_integration(func_str, a, b, steps=4):
    """
    Menghitung integrasi Romberg dari sebuah fungsi string.
    steps: jumlah baris/iterasi tabel Romberg.
    """
    x = sp.symbols('x')
    try:
        func_str = func_str.replace('e**', 'sp.exp').replace('e^', 'sp.exp')
        f_expr = sp.sympify(func_str)
    except Exception as e:
        raise ValueError(f"Format fungsi matematika tidak valid: {e}")

    R = np.zeros((steps, steps))
    
    # Baris pertama (R[0,0]) dengan 1 pias
    R[0, 0] = trapezoid_rule(f_expr, x, a, b, 1)
    
    for i in range(1, steps):
        n = 2**i 
        R[i, 0] = trapezoid_rule(f_expr, x, a, b, n)
        
        for j in range(1, i + 1):
            R[i, j] = R[i, j-1] + (R[i, j-1] - R[i-1, j-1]) / (4**j - 1)
            
    return R[steps-1, steps-1], R.tolist()