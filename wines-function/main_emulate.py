from flask import Flask, request
from main import wines

app = Flask('functions')
methods = ['GET', 'POST', 'PUT', 'DELETE']

@app.route('/wines', methods=methods)
@app.route('/wines/<timestamp>', methods=methods)
#@app.route('/wines/points', methods=methods)
#@app.route('/wines/province', methods=methods)

def catch_all(timestamp=''):
	request.path = '/' + timestamp
	return wines(request)

if __name__ == '__main__':
	app.run(port=5001)