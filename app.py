from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

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

# Route handlers for each page
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/tech_stack.html')
def tech_stack():
    return render_template('tech_stack.html')

@app.route('/algorithmic_crafting.html')
def algorithmic_crafting():
    return render_template('tech_stack.html', section='algorithmic')

@app.route('/design_tools.html')
def design_tools():
    return render_template('tech_stack.html', section='design')

@app.route('/software_development.html')
def software_development():
    return render_template('tech_stack.html', section='software')

@app.route('/streamlit_applications.html')
def streamlit_applications():
    return render_template('tech_stack.html', section='streamlit')

@app.route('/photography')
def photography():
    return render_template('photography.html')

@app.route('/polaroid')
def polaroid():
    return render_template('photography.html', section='polaroid')

@app.route('/cookbook')
def cookbook():
    return render_template('photography.html', section='cookbook')

@app.route('/35mm')
def thirtyfive_mm():
    return render_template('photography.html', section='35mm')

@app.route('/fashion.html')
def fashion():
    return render_template('fashion.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    # Create static directories if they don't exist
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/Images', exist_ok=True)
    os.makedirs('static/Images/photography', exist_ok=True)
    
    app.run(debug=True, port=5006)
