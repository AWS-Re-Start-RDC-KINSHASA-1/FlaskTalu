from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to the API"

@app.route('/test')
def index():
    return render_template('index.html')

@app.route('/okay')
def okay():
    data = {
        "http_code": 200,
        "message": "OK"
    }

    return jsonify(data)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/handle_connection', methods=['GET', 'POST'])
def handle_connection():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f"Vous êtes connecté en tant que {username}"
        return render_template('login.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)