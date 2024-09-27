from flask import Flask, request, make_response, jsonify
import random

app = Flask(__name__, instance_relative_config=True)

@app.route('/add')
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        return make_response(jsonify(s=a+b), 200)  # HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400)  # HTTP 400 BAD REQUEST

@app.route('/sub')
def sub():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        return make_response(jsonify(s=a-b), 200)  # HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400)  # HTTP 400 BAD REQUEST

@app.route('/mul')
def mul():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        return make_response(jsonify(s=a*b), 200)  # HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400)  # HTTP 400 BAD REQUEST

@app.route('/div')
def div():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        if b == 0:
            return make_response('Division by zero\n', 400)  # HTTP 400 BAD REQUEST
        return make_response(jsonify(s=a/b), 200)  # HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400)  # HTTP 400 BAD REQUEST

@app.route('/mod')
def mod():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        if b == 0:
            return make_response('Division by zero\n', 400)  # HTTP 400 BAD REQUEST
        return make_response(jsonify(s=a % b), 200)  # HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400)  # HTTP 400 BAD REQUEST

@app.route('/random')
def random_number():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if a is not None and b is not None:
        if a > b:
            return make_response('Invalid input: a should not be greater than b\n', 400)  # HTTP 400 BAD REQUEST
        random_num = random.randint(a, b)
        return make_response(jsonify(random=random_num), 200)  # HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400)  # HTTP 400 BAD REQUEST

if __name__ == '__main__':
    app.run(debug=True)