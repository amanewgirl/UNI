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
def puz():
	return render_template ('argSign.html')

@app.route('/shuffle<stage>')
def puzzle(stage):
	if stage == '2':
		return render_template ('argAnalogy.html')
	elif stage == '3':
		return render_template ('argExpert.html')


@app.route('/debate')
def debate():
	return render_template ('lvl 2Gameboardtest.html')

#if __name__ == "__main__":
#	app.run(host='0.0.0.0')

port = int(os.environ.get("PORT", 5000))
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=port)
