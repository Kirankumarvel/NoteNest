from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.Config')
app.secret_key = 'your_secret_key'  # Add a secret key for session security

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True, index=True)
    password = db.Column(db.String(150), nullable=False)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        if User.query.filter_by(username=username).first():
            flash('Username already exists. Try another one.', 'danger')
            return redirect(url_for('signup'))

        try:
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Signup successful. Please login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            import logging
            logging.error(f"An error occurred during signup: {e}")
            flash('An error occurred. Please try again.', 'danger')
            return redirect(url_for('signup'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful.', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in first.', 'warning')
        return redirect(url_for('login'))

    user_id = session['user_id']
    user = User.query.get(user_id)
    notes = Note.query.filter_by(user_id=user_id).all()

    return render_template('dashboard.html', username=user.username, notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    if 'user_id' not in session:
        flash('Please log in first.', 'warning')
        return redirect(url_for('login'))

    content = request.form['content']
    user_id = session['user_id']

    try:
        new_note = Note(content=content, user_id=user_id)
        db.session.add(new_note)
        db.session.commit()
        flash('Note added successfully.', 'success')
    except Exception:
        flash('An error occurred. Please try again.', 'danger')

    return redirect(url_for('dashboard'))

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))


@app.route('/')
def home():
    return render_template('home.html')

migrate = Migrate(app, db)
    
with app.app_context():
        db.create_all()
    
if __name__ == '__main__':
    app.run(debug=True)
