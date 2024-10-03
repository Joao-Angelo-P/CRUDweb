from flask import Flask

app = Flask(__name__) # Initialize the application

lUser = list() # uma lista para guardar os numeros inseridos na url
# Montar uma view na 'root'
@app.route('/', methods=['GET'])
def index() -> str:
	return '<h1>Mensagem</h1>'

# Outra view com uma variavel na url
@app.route('/user/<string:id>', methods=['GET'])
def user(id) -> dict:
	lUser.append(id)
	print(lUser)
	return {"user": f"Ola user {id}°"}

if __name__ == '__main__': # Se rodar o programa pelo comando "python index.py", vai iniciar a aplicação
	app.run()

