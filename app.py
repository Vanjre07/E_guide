from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from pymongo import MongoClient
from flask_babel import Babel
from datetime import datetime
import os
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this to a secure secret key
babel = Babel(app)

# MongoDB configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['entrepreneurship_guide']

# Flask-Login configuration
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, user_data):
        self.id = str(user_data['_id'])
        self.email = user_data['email']
        self.is_admin = user_data.get('is_admin', False)

@login_manager.user_loader
def load_user(user_id):
    user_data = db.users.find_one({'_id': ObjectId(user_id)})
    if user_data:
        return User(user_data)
    return None

# Language configuration
@babel.localeselector
def get_locale():
    return session.get('language', 'en')

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user_data = db.users.find_one({'email': email})
        if user_data and check_password_hash(user_data['password'], password):
            user = User(user_data)
            login_user(user)
            if user.is_admin:
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('dashboard'))
        
        flash('Invalid email or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if password != confirm_password:
            flash('Passwords do not match')
            return redirect(url_for('register'))
        
        if db.users.find_one({'email': email}):
            flash('Email already registered')
            return redirect(url_for('register'))
        
        user_data = {
            'email': email,
            'password': generate_password_hash(password),
            'is_admin': False,
            'created_at': datetime.utcnow()
        }
        
        db.users.insert_one(user_data)
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    resources = list(db.resources.find())
    questions = list(db.questions.find({'user_id': current_user.id}))
    return render_template('dashboard.html', resources=resources, questions=questions)

@app.route('/admin')
@login_required
def admin():
    if not current_user.is_admin:
        return redirect(url_for('dashboard'))
    
    users = list(db.users.find())
    questions = list(db.questions.find())
    return render_template('admin.html', users=users, questions=questions)

@app.route('/change_language/<language>')
def change_language(language):
    session['language'] = language
    return redirect(request.referrer or url_for('index'))

@app.route('/post_question', methods=['POST'])
@login_required
def post_question():
    question = request.form.get('question')
    db.questions.insert_one({
        'user_id': current_user.id,
        'user_email': current_user.email,
        'question': question,
        'created_at': datetime.utcnow(),
        'answered': False
    })
    flash('Question posted successfully!')
    return redirect(url_for('dashboard'))

@app.route('/answer_question', methods=['POST'])
@login_required
def answer_question():
    if not current_user.is_admin:
        return redirect(url_for('dashboard'))
    
    question_id = request.form.get('question_id')
    answer = request.form.get('answer')
    
    db.questions.update_one(
        {'_id': ObjectId(question_id)},
        {'$set': {'answer': answer, 'answered': True}}
    )
    
    flash('Answer posted successfully!')
    return redirect(url_for('admin'))

@app.route('/forum')
@login_required
def forum():
    # Get all questions for display
    all_questions = list(db.questions.find().sort('created_at', -1))
    
    # If user is admin, get unanswered questions separately
    unanswered_questions = []
    if current_user.is_admin:
        unanswered_questions = list(db.questions.find({'answered': False}).sort('created_at', -1))
    
    return render_template('forum.html', 
                         all_questions=all_questions,
                         unanswered_questions=unanswered_questions)

@app.route('/learning-resources')
@login_required
def learning_resources():
    return render_template('learning_resources.html')

if __name__ == '__main__':
    # Create admin user if not exists
    admin_user = db.users.find_one({'email': 'admin@example.com'})
    if not admin_user:
        admin_data = {
            'email': 'admin@example.com',
            'password': generate_password_hash('admin123'),
            'is_admin': True,
            'created_at': datetime.utcnow()
        }
        db.users.insert_one(admin_data)
        print("Admin user created successfully!")
    
    app.run(debug=True) 