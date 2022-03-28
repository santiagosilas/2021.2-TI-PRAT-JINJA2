
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

######
class Pessoa:
    def __init__(self):
        self.nome = 'Fulano de Tal'
        self.telefone = '85 9876-5432'
admin = Pessoa()
######

class GerenciarUsuario:
    def adicionar(self):
        return True
gerenciar_usuario = GerenciarUsuario()

@app.route('/contact')
def view_contact():
    usuario = {
        'nome': 'Fulano de tal',
        'email': 'fulano@gmail.com',
        'telefone':'85 99876 - 9876',
        'telefones': ['88 99876 - 9876', '85 99876 - 9876', '84 99877 - 9878']
    }
    return render_template('contact.html', usuario = usuario, admin = admin)

@app.route('/')
@app.route('/home')
def view_home():
    mensagem = 'Seja bem vindo!'
    return render_template('home.html', saudacao = mensagem)



@app.route('/about')
def view_about():
    return render_template('about.html')

@app.route('/ex1')
def view_jinja2_ex1():
    status_add_db = False
    return render_template('exemplo-jinja2-001.html', status_registro = status_add_db)

@app.route('/ex2')
def view_jinja2_ex2():
    status_operation = 2
    return render_template('exemplo-jinja2-002.html', status_op = status_operation)



