from flask import Flask, make_response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index() -> object:
	response = make_response('<h1>Esta é uma mensagem</h1>')
	response.set_cookie('awser', '42')
	# response.server('nao interessa')
	return response

if __name__ == '__main__':
	app.run()

