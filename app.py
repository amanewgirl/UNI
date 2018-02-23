from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
	return 'Yo, it is working!'

@app.route('/form')
def form():
	return render_template ('argumentform.html')

@app.route('/shuffle')
def puzzle():
	return render_template ('puzzle.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0')
