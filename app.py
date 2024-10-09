from flask import Flask, request, render_template, url_for, redirect, session
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired # WTForms > 3.x, from wtforms.validators import DataRequired, less version from wtforms.validators import Required
#from flask_script import Manager

app = Flask(__name__) # Initialize the application
app.config['SECRET_KEY'] = 'difcil_para_descobrir' # pode ser salva como variavel do ambiente

bootstrap = Bootstrap(app) # Use a Bootstrap module with Jinja2 engine
moment = Moment(app)
# manager = Manager(app)

lUser = list() # uma lista para guardar os numeros inseridos na url

class NameForm(FlaskForm):
	name = StringField('Qual é seu nome?', validators=[DataRequired()])
	submit = SubmitField('Submit')

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
@app.route('/', methods=['GET', 'POST'])
def index():
	# name = None -> não vai mais precisar. Usa-se session para armazenar o nome inserido no formulario
	form = NameForm()
	if form.validate_on_submit():
		# name = form.name.data
		# form.name.data = ''
		# POST REDIRECT / GET Pattern
		session['name'] = form.name.data
		print(session.get('name'))
		return redirect(url_for('index'))
	# Vai renderizar a página inicial (Index) com o template que está na pasta: /templates/index.html
	return render_template('index.html', current_time=datetime.utcnow(), form=form, name=session.get('name')), 200


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

