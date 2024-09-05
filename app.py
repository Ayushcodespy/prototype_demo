from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "super-secret-key"

@app.route('/')
def home():
    # Check if 'user' key exists in the session
    if 'user' in session:
        if session['user'] == 'admin':
            return redirect(url_for('admin_page'))
        
        if session['user'] == 'alumni':
            return redirect(url_for('alumni_page'))
        
        if session['user'] == 'student':
            return redirect(url_for('student_page'))
    
    # Default redirect if 'user' key is not present or does not match any condition
    return redirect(url_for('login'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['user_id']
        password = request.form['passwd']
        user_type = request.form['user_type']

        if user_type == 'administration':
            if username == 'admin' and password == 'admin':
                session['user'] = username
                return redirect(url_for('admin_page'))
            else:
                return render_template("login.html", error='Incorrect login details!')

        if user_type == 'alumini':
            if username == 'alumni' and password == 'alumni':
                session['user'] = username
                return redirect(url_for('alumni_page'))
            else:
                return render_template("login.html", error='Incorrect login details!')

        if user_type == 'student':
            if username == 'student' and password == 'student':
                session['user'] = username
                return redirect(url_for('student_page'))
            else:
                return render_template("login.html", error='Incorrect login details!')

    return render_template('login.html')



@app.route("/admin_page")
def admin_page():
    return render_template('admin_page.html')

@app.route("/alumni_page")
def alumni_page():
    return render_template('alumni_page.html')

@app.route("/student_page")
def student_page():
    return render_template('student_page.html')


@app.route("/logout", methods=['GET','POST'])
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)