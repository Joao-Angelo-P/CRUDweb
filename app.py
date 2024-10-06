from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
#from flask_script import Manager

app = Flask(__name__) # Initialize the application
bootstrap = Bootstrap(app) # Use a Bootstrap module with Jinja2 engine
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
@app.route('/')
def index():
	# Vai renderizar a página inicial (Index) com o template que está na pasta: /templates/index.html
	return render_template('index.html'), 200


@app.route('/user/<name>')
def user(name):
	# Vai passar uma variável na url e renderizar o template na pasta: /templates/user.html
	return render_template('user.html', name=name), 200

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def server_internal_error(e):
	return render_template('500.html'), 500

if __name__ == '__main__': # Se rodar o programa pelo comando "python index.py", vai iniciar a aplicação
	app.run()

