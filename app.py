from flask import Flask, request, render_template
#from flask_script import Manager

app = Flask(__name__) # Initialize the application
#manager = Manager(app)

lUser = list() # uma lista para guardar os numeros inseridos na url
# Montar uma view na 'root'
"""
@app.route('/', methods=['GET'])
def index() -> str:
	user_agent = request.headers.get('User-Agent')
	return '<h1>Mensagem</h1>' + '<br>' + '<p>Your browser is %s </p>' % user_agent

@app.route('/user/<string:id>', methods=['GET'])
def user(id) -> dict:
	lUser.append(id)
	print(lUser)
	return {"user": f"Ola user {id}°"}
# Outra view com uma variavel na url
"""
@app.route('/index')
def index():
	# Vai renderizar a página inicial (Index) com o template que está na pasta: /templates/index.html
	return render_template('index.html'), 200


@app.route('/user/<name>')
def user(name):
	# Vai passar uma variável na url e renderizar o template na pasta: /templates/user.html
	return render_template('user.html', name=name), 200





if __name__ == '__main__': # Se rodar o programa pelo comando "python index.py", vai iniciar a aplicação
	app.run()

