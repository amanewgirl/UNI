from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)
@app.route('/')
def index():
	return 'Yo, it is working!'

@app.route('/form')
def form():
	return render_template ('workingargumentform.html')

@app.route('/formtest')
def formtest():
	return render_template ('argumentformtest.html')


@app.route('/data', methods=['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['blob']
      f.save('static/upload.jpg')
      return 'file uploaded successfully'

@app.route('/shuffle')
def puzzle():
	return render_template ('puzzle.html')

@app.route('/debate')
def debate():
	return render_template ('lvl 2Gameboardtest.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0')
