# Remington Williams Portfolio Website

A dynamic, secure portfolio website built with Flask, featuring photography galleries, technical projects, and professional achievements.

## 🌟 Features

- **Secure Authentication**: Login system to protect sensitive content
- **Dynamic Content**: Multiple portfolio sections including:
  - Photography Gallery (35mm, Polaroid, Cookbook)
  - Fashion Photography
  - Technical Projects
  - Professional Experience
  - Skills & Certifications
- **Responsive Design**: Mobile-first approach with modern CSS
- **Interactive UI**: Smooth transitions and hover effects
- **Modular Architecture**: Well-organized Flask routes and templates

## 🛠️ Technology Stack

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Authentication**: Flask-Login
- **Security**: Session management, CSRF protection
- **Database**: File-based for simplicity (can be upgraded to SQLite/MySQL)

## 📋 Prerequisites

- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rwilly1/PythonFinalCode.git
   cd PythonFinalCode
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up media files**
   - Create directories:
     ```bash
     mkdir -p static/Images/photography
     mkdir -p static/Images/fashion
     mkdir -p static/video
     ```
   - Add your images to the respective directories

5. **Run the application**
   ```bash
   python app.py
   ```
   The site will be available at `http://localhost:5005`

## 🗂️ Project Structure

```
portfolio/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── static/
│   ├── css/           # Stylesheets
│   ├── Images/        # Image assets
│   └── video/         # Video content
├── templates/         # HTML templates
│   ├── about.html
│   ├── contact.html
│   ├── fashion.html
│   ├── index.html
│   ├── login.html
│   ├── photography.html
│   ├── tech_stack.html
│   └── template.html
└── README.md
```

## 🔐 Security Features

- Session-based authentication
- Password protection for sensitive content
- CSRF token protection
- Secure file handling
- Error handling and logging

## 🎨 Customization

1. **Change Login Credentials**
   - Update `SITE_PASSWORD` in `app.py`

2. **Modify Styles**
   - Edit `static/css/styles.css`
   - Color scheme uses variables for easy updates

3. **Update Content**
   - Modify HTML templates in the `templates/` directory
   - Add new routes in `app.py` as needed

## 📱 Responsive Design

- Mobile-first approach
- Breakpoints for tablets and desktops
- Flexible grid layouts
- Optimized images for different screen sizes

## 🔄 Future Improvements

- [ ] Database integration for dynamic content management
- [ ] Admin dashboard for content updates
- [ ] Contact form with email integration
- [ ] Image optimization and lazy loading
- [ ] Analytics integration
- [ ] API endpoints for headless CMS integration

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👩‍💻 Author

**Remington Williams**
- Portfolio: [View Live Site]
- GitHub: [@Rwilly1](https://github.com/Rwilly1)
- LinkedIn: [Remington Williams](https://www.linkedin.com/in/remington-williams/)

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 💫 Acknowledgments

- Flask documentation and community
- Python web development community
- Modern web design inspiration and resources
