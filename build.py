import os
import shutil
from jinja2 import Environment, FileSystemLoader

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def url_for(endpoint, filename=None):
    """Custom url_for function to replace Flask's url_for"""
    if endpoint == 'static' and filename:
        return f'/static/{filename}'
    
    # Map endpoints to their static HTML files
    endpoint_map = {
        'index': 'index.html',
        'about': 'about.html',
        'tech_stack': 'tech_stack.html',
        'algorithmic_crafting': 'algorithmic_crafting.html',
        'software_development': 'software_development.html',
        'streamlit_applications': 'streamlit_applications.html',
        'design_tools': 'design_tools.html',
        'photography': 'photography.html',
        'polaroid': 'polaroid.html',
        'cookbook': 'cookbook.html',
        'thirtyfive_mm': '35mm.html',
        'fashion': 'fashion.html',
        'contact': 'contact.html',
        'login': 'login.html',
        'logout': 'login.html'
    }
    
    return f'/{endpoint_map.get(endpoint, endpoint)}'

def main():
    # Create dist directory
    dist_dir = 'dist'
    ensure_dir(dist_dir)

    # Set up Jinja environment
    env = Environment(loader=FileSystemLoader('templates'))
    env.globals['url_for'] = url_for

    # Copy static files
    static_src = 'static'
    static_dest = os.path.join(dist_dir, 'static')
    if os.path.exists(static_dest):
        shutil.rmtree(static_dest)
    shutil.copytree(static_src, static_dest)

    # List of pages to render
    pages = [
        ('index.html', {}),
        ('about.html', {}),
        ('tech_stack.html', {}),
        ('tech_stack.html', {'section': 'algorithmic', 'output_file': 'algorithmic_crafting.html'}),
        ('tech_stack.html', {'section': 'software', 'output_file': 'software_development.html'}),
        ('tech_stack.html', {'section': 'streamlit', 'output_file': 'streamlit_applications.html'}),
        ('tech_stack.html', {'section': 'design', 'output_file': 'design_tools.html'}),
        ('photography.html', {}),
        ('photography.html', {'section': 'polaroid', 'output_file': 'polaroid.html'}),
        ('photography.html', {'section': 'cookbook', 'output_file': 'cookbook.html'}),
        ('photography.html', {'section': '35mm', 'output_file': '35mm.html'}),
        ('fashion.html', {}),
        ('contact.html', {}),
    ]

    # Render all pages
    for template_name, template_vars in pages:
        template = env.get_template(template_name)
        output = template.render(**template_vars)

        output_file = template_vars.get('output_file', template_name)
        output_path = os.path.join(dist_dir, output_file)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as f:
            f.write(output)

    print("Build completed successfully!")

if __name__ == '__main__':
    main()
