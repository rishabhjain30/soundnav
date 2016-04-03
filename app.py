from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask import request
from untitled import search
import requests

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

@app.route('/searchterm')
def googlesearch():
	argument = request.args.get('query')
	return search(argument)


@app.route('/url')
def geturl():
    url = 'http://'+request.args.get('query')
    print url
    http_proxy = 'http://HITN042:69183421@172.31.1.6:8080/'    
    proxyDict = { 
              "http"  : http_proxy, 
              "https" : http_proxy
            }
    headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36",
    'accept-encoding': "gzip, deflate, sdch",
    'accept-language': "en-US,en;q=0.8",
    }

    response = requests.request("GET", url, headers=headers)
    print response.text
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
