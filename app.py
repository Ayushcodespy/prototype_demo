from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "super-secret-key"

@app.route('/')
def home():
    return render_template('signup.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == password:
            return 'Welcome logged in'
        else:
            return render_template('signup.html', error='Invalid login details !')
    return render_template('signup.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return redirect(url_for('home'))
    
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)