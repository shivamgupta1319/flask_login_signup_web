from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return '<p>logout</p>'

@auth.route('/signup', methods=['GET','POST'])
def singup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstname) < 2:
            flash('Fistname must be greater than 2 characters.', category='error')
        elif password1 != password2:
            flash('passwords don\'t match.', category='error')
        else:
            flash('Account created', category='success')

    return render_template('signup.html')