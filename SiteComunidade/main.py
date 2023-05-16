from flask import Flask, render_template, url_for

app = Flask(__name__)

lista_usuario = ['Thiarly', 'Luca', 'Laila', 'Clara']

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/contato")
def contato():
    return render_template('contato.html')


@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html', lista_usuario=lista_usuario)

if __name__ == '__main__':
    app.run(debug=True)

