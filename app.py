from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "super-secret-key"

@app.route('/')
def home():
    if 'user' in session:
        return render_template("home.html")
    
    return render_template('signup.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_type = request.form['user_type']
        username = request.form['username']
        password = request.form['password']
        if username == password:
            session['user'] = username
            return redirect(url_for('home'))
        else:
            return render_template('signup.html', error='Invalid login details !')
    return render_template('signup.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_type = request.form['user_type']
        email = request.form['email']
        password = request.form['password']
        return redirect(url_for('home'))
    
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)