from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '080bd08ca3fdc729e1e4a4ece3109b39'

posts = [
        {'author': 'George RR Martin',
        'title': 'A Storm of Swords',
        'content': 'Story of 7 Kingdoms',
        'date_released': 'August 8, 2000',
        },
        {
        'author': 'JRR Tolkien',
        'title': 'Lord of the Rings',
        'content': 'Story of Shire',
        'date_released': 'July 29, 1954',
        }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if(form.validate_on_submit()):
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if(form.validate_on_submit()):
        if(form.email.data == 'admin@blog.com' and form.password.data == 'password'):
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title = 'Login', form = form)

if __name__ == '__main__':
    app.run(debug=True)