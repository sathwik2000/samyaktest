from flask import Flask, request
import ast
from rt import clear, clear1
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/", methods=['get'])
def index():
	return "Hello welcome"

@app.route('/register', methods=['post'])
def register():
	# print(dir(request.data))
	data = request.data.decode()
	data = ast.literal_eval(data)
	t=clear(data['name'], data['mail'], data['college'], data['amount'])
	if(t=='done'):
		return "success"
	elif t=='faileMail':
		return "Mail failed"
	else:
		return "register failed"
@app.route('/search', methods=['post'])
def search():
	# print(dir(request.data))
	data = request.data.decode()
	data = ast.literal_eval(data)
	t1=clear1(data['id'])
	if(t1):
		return "Found"
	else:
		return "Not Found"
if __name__ == '__main__':
   app.run(debug = True)