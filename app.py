from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "super-secret-key"

@app.route('/')
def home():
    if 'user' in session:
        return render_template("index.html")

    else:
        return redirect(url_for('login'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('home'))

    if request.method == "POST":
        username = request.form['user_id']
        password = request.form['passwd']
        user_type = request.form['user_type']

        if user_type == 'administration':
            if username == 'admin'and password == 'admin':
                session['user'] = username  # Store user in session
                return redirect(url_for('home'))
            else:
                return render_template("login.html", error='Incorrect login details!')

        if user_type == 'alumini':
            if username == 'alumini'and password == 'alumini':
                session['user'] = username  # Store user in session
                return redirect(url_for('home'))
            else:
                return render_template("login.html", error='Incorrect login details!')

        if user_type == 'student':
            if username == 'student'and password == 'student':
                session['user'] = username  # Store user in session
                return redirect(url_for('home'))
            else:
                return render_template("login.html", error='Incorrect login details!')

    return render_template('login.html')


@app.route("/logout", methods=['GET','POST'])
def logout():
    session.pop('user')
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)