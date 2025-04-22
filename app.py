from flask import Flask, render_template, url_for, redirect, request, flash, send_from_directory, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a secure secret key
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Configure static folders
app.static_folder = 'static'
app.static_url_path = '/static'

# Move static files to appropriate directories
@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('static/css', filename)

@app.route('/Images/<path:filename>')
def serve_images(filename):
    return send_from_directory('static/Images', filename)

# Simple user class
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Create a single user
user = User(1)

# Password hash - you should change this to your desired password
SITE_PASSWORD = "remi"

@login_manager.user_loader
def load_user(user_id):
    if int(user_id) == 1:
        return user
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Clear any existing flashed messages
    session.clear()
    if request.method == 'POST':
        password = request.form.get('password')
        if password == SITE_PASSWORD:
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
        else:
            flash('Invalid password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Route handlers for each page
@app.route('/')
@app.route('/index.html')
@login_required
def index():
    return render_template('index.html')

@app.route('/about.html')
@login_required
def about():
    return render_template('about.html')

@app.route('/tech_stack.html')
@login_required
def tech_stack():
    return render_template('tech_stack.html')

@app.route('/algorithmic_crafting.html')
@login_required
def algorithmic_crafting():
    return render_template('tech_stack.html', section='algorithmic')

@app.route('/design_tools.html')
@login_required
def design_tools():
    return render_template('tech_stack.html', section='design')

@app.route('/software_development.html')
@login_required
def software_development():
    return render_template('tech_stack.html', section='software')

@app.route('/streamlit_applications.html')
@login_required
def streamlit_applications():
    return render_template('tech_stack.html', section='streamlit')

@app.route('/photography')
@login_required
def photography():
    return render_template('photography.html')

@app.route('/polaroid')
@login_required
def polaroid():
    return render_template('photography.html', section='polaroid')

@app.route('/cookbook')
@login_required
def cookbook():
    return render_template('photography.html', section='cookbook')

@app.route('/35mm')
@login_required
def thirtyfive_mm():
    return render_template('photography.html', section='35mm')

@app.route('/fashion.html')
@login_required
def fashion():
    return render_template('fashion.html')

@app.route('/contact.html')
@login_required
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    # Create static directories if they don't exist
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/Images', exist_ok=True)
    os.makedirs('static/Images/photography', exist_ok=True)
    
    app.run(debug=True, port=5005)
