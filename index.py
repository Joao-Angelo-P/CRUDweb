from flask import Flask

app = Flask(__name__) # Initialize the application

# Montar uma view na 'root'
@app.route('/', methods=['GET'])
def index():
	return {'user': 'mensagem'}

if __name__ == '__main__': # Se rodar o programa pelo comando "python index.py", vai iniciar a aplicação
	app.run()

