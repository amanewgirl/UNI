import os
from flask import Flask, render_template, request, url_for, abort,render_template, send_from_directory
from werkzeug import secure_filename
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

number=0

#socketio code to handle messages
@socketio.on('my event')
def tryn(int):
   global number
   print(number)
   number=number+1
   emit('my response',number)
   return number
   

#socketio code to handle messages
@socketio.on('message')
def stuff(msg):
    print('Message:' +msg)
    send(msg, broadcast=True)

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

#debate game instructions
@app.route('/instruct')
def instructions():
	return render_template('debateInstructions.html')

#debate game
@app.route('/debate')
@app.route('/debate/<player>')
def debate(player=None):
	return render_template ('boardFinal.html', player=player)

@app.route('/debatetest')
def deb():
	return render_template ('lvl 2Gameboardtest.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0')

#port = int(os.environ.get("PORT", 5000))
#if __name__ == "__main__":
#	app.run(host='0.0.0.0', port=port)
