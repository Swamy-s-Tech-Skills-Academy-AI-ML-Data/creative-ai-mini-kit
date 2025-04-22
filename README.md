# Creative AI Mini Kit

A compact yet powerful toolkit leveraging OpenAI's GPT-3.5 and DALL-E 3 models to automate email responses, generate code from natural language, summarize text, and create images from descriptions. Designed for AI-driven creativity and efficiency.

## 1. Clone the Repository

```powershell
git clone https://github.com/Swamy-s-Tech-Skills-Academy-AI-ML-Data/creative-ai-mini-kit.git
cd creative-ai-mini-kit
```

## 2. Create & Activate a Virtual Environment

### For Windows 11 (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

### For Windows 11 (Command Prompt)

```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
python -m pip install --upgrade pip
```

### For macOS/Linux

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

## 3. Install Required Packages

Run the following command to install the required Python packages:

```powershell
pip install ipykernel openai pandas requests tiktoken pypdf matplotlib ipython jinja2
```

### 3.1 Required Packages for Notebook

> 1. openai: This package is used for accessing the OpenAI API.
> 2. pandas: This package is used for handling tabular data.
> 3. requests: This package is used for downloading files.
> 4. datetime from datetime: This module is required for getting the timestamp.
> 5. pprint from pprint: This module is required for pretty printing text in Python.
> 6. tiktoken: This package is required for counting the number of tokens in a string.
> 7. PdfReader from pypdf: This module is required for handling PDF files.
> 8. Markdown, and display from IPython.display: These modules are required for loading and displaying markdown content in the notebook.
> 9. os: This package is required to access operating system resources.
> 10. pyplot and image from matplotlib: These modules are required for displaying images in the notebook.

## 4. Web Application with Django, DRF, and Tailwind CSS

The Creative AI Mini Kit now includes a web application built with Django, Django REST Framework (DRF), and Tailwind CSS, offering a modern UI for all toolkit functionalities.

### 4.1 Features

- **Landing Page**: Introduction to the toolkit capabilities with interactive demos
- **Email Generation**: Generate professional response emails from customer reviews
- **Code Generation**: Create Python code from natural language descriptions
- **Modern UI**: Responsive design with Tailwind CSS
- **RESTful API**: Powerful backend API built with Django REST Framework
- **Custom Typography**: Integration with Google Fonts for beautiful typography
- **Modern Icons**: Font Awesome icons for enhanced user interface elements
- **Professional Branding**: Custom favicon for browser tab recognition

### 4.2 Prerequisites for Web Application (Windows 11)

1. **Install Node.js and npm**:

   - Download and install Node.js from [nodejs.org](https://nodejs.org/)
   - Verify installation with `node -v` and `npm -v` in a new terminal window

2. **Install Git (if not already installed)**:
   - Download and install Git from [git-scm.com](https://git-scm.com/download/win)

### 4.3 Installation for Web Application

```powershell
# Install required packages for the web application
pip install django djangorestframework django-tailwind django-compressor python-dotenv pillow gunicorn whitenoise dj-database-url

pip install django djangorestframework django-tailwind python-dotenv
```

### 4.4 Create Django Project Structure in src Directory

```powershell
# Navigate to the src directory
cd src

# Start a new Django project
django-admin startproject caimk_web .

# Create necessary apps
python manage.py startapp api
python manage.py startapp email_generator
python manage.py startapp code_generator
python manage.py startapp frontend
```

### 4.5 Setup Tailwind CSS

```powershell
# Install django-tailwind app
python manage.py tailwind init theme

# Install Tailwind CSS dependencies (requires Node.js)
python manage.py tailwind install

# Build Tailwind CSS
python manage.py tailwind build
```

### 4.6 Configure Environment Variables

Create a `.env` file in the src directory with the following variables:

```
DEBUG=True
SECRET_KEY=your_secret_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

To generate a secure Django secret key, you can use Python:

```powershell
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

### 4.7 Run Migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 4.8 Create Superuser (Optional)

```powershell
python manage.py createsuperuser
```

### 4.9 Run Development Server

```powershell
python manage.py runserver
```

Access the web application at http://127.0.0.1:8000/

### 4.10 Enhance UI with Google Fonts, Font Awesome, and Favicon

#### 4.10.1 Add Google Fonts

1. Choose fonts from [Google Fonts](https://fonts.google.com/)
2. Add the font links to your base template:

```html
<!-- In your base.html template -->
<head>
    <!-- ... other head elements ... -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
    <!-- ... other head elements ... -->
</head>
```

3. Configure the fonts in your Tailwind CSS configuration:

```javascript
// In theme/static_src/tailwind.config.js
module.exports = {
    theme: {
        extend: {
            fontFamily: {
                sans: ['Inter', 'sans-serif'],
                heading: ['Poppins', 'sans-serif'],
            },
        },
    },
    // ... other configuration options
}
```

#### 4.10.2 Add Font Awesome Icons

1. Install Font Awesome using npm (within the theme directory):

```powershell
cd theme
npm install @fortawesome/fontawesome-free
```

2. Import Font Awesome in your CSS:

```css
/* In theme/static_src/src/styles.css */
@import '@fortawesome/fontawesome-free/css/all.min.css';
```

3. Use icons in your templates:

```html
<!-- Example usage -->
<i class="fas fa-envelope"></i> <!-- Email icon -->
<i class="fas fa-code"></i> <!-- Code icon -->
<i class="fas fa-home"></i> <!-- Home icon -->
```

#### 4.10.3 Add Custom Favicon

1. Create or obtain your favicon file (favicon.ico)
2. Place it in the `frontend/static/images/` directory
3. Link to the favicon in your base template:

```html
<!-- In your base.html template -->
<head>
    <!-- ... other head elements ... -->
    <link rel="icon" type="image/x-icon" href="{% static 'images/favicon.ico' %}">
    <!-- ... other head elements ... -->
</head>
```

4. Ensure your template loads the static files:

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <!-- ... head content ... -->
</head>
<body>
    <!-- ... body content ... -->
</body>
</html>
```

## 5. Project Structure

```
creative-ai-mini-kit/
├── LICENSE
├── README.md
├── docs/
│   └── images/
├── notebooks/
│   ├── CreativeAIMiniKit.ipynb
│   ├── emails/
│   ├── generatedcode/
│   │   └── python/
│   └── reviews/
└── src/
    ├── api/
    │   ├── migrations/
    │   ├── models.py
    │   ├── serializers.py
    │   ├── urls.py
    │   └── views.py
    ├── code_generator/
    │   ├── forms.py
    │   ├── services.py
    │   ├── urls.py
    │   └── views.py
    ├── caimk_web/
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── email_generator/
    │   ├── forms.py
    │   ├── services.py
    │   ├── urls.py
    │   └── views.py
    ├── frontend/
    │   ├── static/
    │   │   ├── css/
    │   │   ├── images/
    │   │   │   └── favicon.ico
    │   │   └── js/
    │   └── templates/
    ├── theme/
    │   └── static_src/
    │       └── tailwind/
    ├── manage.py
    └── requirements.txt
```

## 6. Architecture

The web application follows a clean architecture pattern with separation of concerns:

1. **Presentation Layer**: Django templates with Tailwind CSS
2. **API Layer**: Django REST Framework endpoints for service consumption
3. **Service Layer**: Business logic encapsulated in service modules
4. **Data Layer**: Django ORM models for database interactions

### 6.1 Best Practices Implemented

- **Environment Variable Management**: Using python-dotenv for secure configuration
- **API Documentation**: Automatic API documentation with DRF's built-in tools
- **Responsive Design**: Mobile-first approach with Tailwind CSS
- **Caching**: Performance optimization with Django's caching framework
- **Error Handling**: Comprehensive error management
- **Testing**: Unit and integration tests for all components
- **Security**: CSRF protection, input validation, and data sanitization
- **Code Organization**: Clear separation between API, business logic, and templates
- **Version Control**: Proper gitignore settings for sensitive files

## 7. Development Workflow

1. **Frontend Development**: Edit Tailwind CSS styles in the theme app
2. **Backend Development**: Implement business logic in service modules
3. **API Integration**: Connect frontend to backend via the DRF endpoints
4. **Testing**: Run tests to ensure functionality works as expected
5. **Deployment**: Use gunicorn and whitenoise for production deployment

## 8. Troubleshooting (Windows 11)

### Common Issues and Solutions

1. **Permission Errors**: Run your terminal (PowerShell or Command Prompt) as Administrator if you encounter permission issues.

2. **Virtual Environment Not Activating**: If you see an error about execution policies in PowerShell, try:

   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

3. **Node.js/npm Issues**: If Tailwind installation fails, ensure Node.js is in your PATH and restart your terminal.

4. **Django Command Not Found**: Ensure you've activated your virtual environment before running Django commands.

5. **Tailwind Build Errors**: Check if Node.js is installed correctly with `node -v`. If problems persist, try the standalone installation method for Tailwind CSS.
