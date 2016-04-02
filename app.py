from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/home')
def hello_world():
    return render_template('search.html')

@app.route('/process')
def process_world():
	return render_template('process.html')

if __name__ == '__main__':
    app.run(debug=True)
