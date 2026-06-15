from flask import Flask, render_template, request
from romberg import romberg_integration

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/romberg', methods=['GET', 'POST'])
def halaman_romberg():
    hasil = None
    tabel = None
    error = None
    steps = 4
    persamaan = ""
    a_val = ""
    b_val = ""
    
    if request.method == 'POST':
        try:
            persamaan = request.form['persamaan']
            a_val = request.form['a']
            b_val = request.form['b']
            steps = int(request.form['steps'])
            
            a = float(a_val)
            b = float(b_val)
            
            hasil, tabel = romberg_integration(persamaan, a, b, steps)
        except ValueError as ve:
            error = str(ve)
        except Exception as e:
            error = f"Terjadi kesalahan komputasi: {str(e)}"
            
    return render_template(
        'romberg.html', 
        hasil=hasil, 
        tabel=tabel, 
        error=error, 
        steps=steps,
        persamaan=persamaan,
        a_val=a_val,
        b_val=b_val
    )

if __name__ == '__main__':
    app.run(debug=True)