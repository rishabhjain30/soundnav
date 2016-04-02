from flask import Flask
from flask import render_template
from flask import send_from_directory

app = Flask(__name__)

@app.route('/home')
def hello_world():
    return render_template('search.html')

@app.route('/process')
def process_world():
	return render_template('process.html')

@app.route('/src/<path:filename>')
def send_js(filename):
	return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
