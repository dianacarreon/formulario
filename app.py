from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/submit', methods=['POST'])
def submit():
    nombre = request.form.get('nombre')
    return f"¡Hola, {nombre}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
