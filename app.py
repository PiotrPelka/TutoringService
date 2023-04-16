from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # code to authenticate user
        return render_template('dashboard.html', username=username)
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # code to create user account
        return render_template('login.html')
    else:
        return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    username = request.args.get('username')
    # code to retrieve user information and display on dashboard
    return render_template('dashboard.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)