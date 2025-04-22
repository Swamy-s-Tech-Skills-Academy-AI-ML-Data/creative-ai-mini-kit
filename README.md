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
pip install django-tailwind==3.4.0
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
python manage.py startapp theme

# Create static files directories
mkdir -p frontend/static/css
mkdir -p frontend/static/js
mkdir -p frontend/static/images
mkdir -p frontend/static/icons
```

### 4.5 Setup Tailwind CSS

Tailwind CSS provides a utility-first CSS framework that will help us create a modern, responsive interface without writing custom CSS. We'll set it up using django-tailwind:

To find the path of npm `Get-Command npm | Format-List`

```powershell
# Navigate to the src directory if you're not already there
cd src

# Initialize django-tailwind with a theme app
python manage.py tailwind init theme

# Install Tailwind CSS dependencies (requires Node.js)
python manage.py tailwind install

# Build Tailwind CSS
python manage.py tailwind build
```

What happens in these steps:

1. We create a new Django app called "theme" that will handle Tailwind CSS
2. We install Tailwind's dependencies using npm (Node.js package manager)
3. We compile the CSS from Tailwind's utility classes

### 4.6 Configure Project Settings

After creating the apps and setting up Tailwind, we need to update the Django settings file to include our apps and configure various settings:

1. Update `caimk_web/settings.py` to:
   - Register all created apps
   - Configure Tailwind CSS
   - Set up static files location
   - Configure templates directory
   - Set up environment variables

The key settings we'll update include:

```python
# Add to INSTALLED_APPS
INSTALLED_APPS = [
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    # ...

    # Third-party apps
    'rest_framework',
    'tailwind',

    # Tailwind theme app
    'theme',

    # Project apps
    'api',
    'email_generator',
    'code_generator',
    'frontend',
]

# Tailwind configuration
TAILWIND_APP_NAME = 'theme'

# Templates configuration to use our frontend app's templates
TEMPLATES = [
    {
        # ...
        'DIRS': [os.path.join(BASE_DIR, 'frontend/templates')],
        # ...
    }
]

# Static files configuration
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/static'),
]
```

### 4.7 Create Base Template with Navbar and Footer

Now we'll create the foundation of our UI - a base template with a consistent navbar and footer that will be used across all pages.

1. Create template directories structure:

```
src/frontend/templates/
├── base.html
├── components/
│   ├── navbar.html
│   └── footer.html
├── pages/
│   ├── home.html
│   ├── email_generator.html
│   └── code_generator.html
```

2. In `base.html`, we'll create the main layout that includes:

   - HTML5 doctype and responsive viewport
   - Google Fonts integration
   - Navbar component
   - Content block where page-specific content will be inserted
   - Footer component
   - JavaScript for interactive elements

3. In the navbar component, we'll include:

   - Logo/Project name
   - Navigation links to all sections
   - Mobile-responsive menu

4. In the footer component, we'll include:
   - Copyright information
   - Links to GitHub or other resources
   - Brief description of the project

### 4.8 Implement URL Routing

Next, we'll set up the URL routing to connect our views to specific URL paths:

1. Update `caimk_web/urls.py` to include our app URLs
2. Create URLs files for each app if needed
3. Define URL patterns for each view

The main URL configuration will look like:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),  # For frontend pages
    path('api/', include('api.urls')),   # For API endpoints
    # You can add more URL includes for other apps as needed
]
```

### 4.9 Create Homepage View

Now we'll implement the homepage view in the frontend app:

1. Update `frontend/views.py` to create a view for the homepage
2. Create a template for the homepage with:
   - Hero section introducing the toolkit
   - Feature cards explaining main functionality
   - Example or demo section
   - Call-to-action buttons to try features

The view will be simple:

```python
from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')
```

### 4.10 Implement Email Generator Feature

Next, we'll implement the email generation feature:

1. Create a form for submitting customer reviews
2. Create a view to handle the form submission
3. Use the OpenAI API to generate responses
4. Display the generated email to the user

The implementation will involve:

- Creating a form class in `email_generator/forms.py`
- Setting up the view logic in `email_generator/views.py`
- Creating templates for the form and results
- Creating a service to handle the OpenAI API communication

### 4.11 Implement Code Generator Feature

Similarly, we'll implement the code generation feature:

1. Create a form for describing the code to generate
2. Create a view to handle form submission
3. Use OpenAI API to generate Python code
4. Display the generated code with syntax highlighting
5. Add a feature to download the generated code

These implementations will follow a similar pattern to the email generator but with different form fields and API prompts.

### 4.12 Create API Endpoints

Finally, we'll create API endpoints using Django REST Framework:

1. Define serializers for our data models
2. Create ViewSets or API views
3. Configure URL routing for the API

This will allow:

- Frontend to make AJAX requests to our backend
- Other applications to integrate with our toolkit
- Separation of concerns between frontend and backend logic

### 4.13 Run and Test the Application

Once all components are implemented, we'll run and test the application:

```powershell
# Make sure you're in the src directory
cd src

# Run the development server
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to see your application in action!

## 5. Project Structure

After implementation, your project structure should look like this:

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
    ├── caimk_web/
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── code_generator/
    │   ├── forms.py
    │   ├── services.py
    │   ├── urls.py
    │   ├── views.py
    │   └── templates/
    │       └── code_generator/
    │           ├── form.html
    │           └── result.html
    ├── email_generator/
    │   ├── forms.py
    │   ├── services.py
    │   ├── urls.py
    │   ├── views.py
    │   └── templates/
    │       └── email_generator/
    │           ├── form.html
    │           └── result.html
    ├── frontend/
    │   ├── static/
    │   │   ├── css/
    │   │   ├── images/
    │   │   │   └── favicon.ico
    │   │   └── js/
    │   ├── templates/
    │   │   ├── base.html
    │   │   ├── components/
    │   │   │   ├── navbar.html
    │   │   │   └── footer.html
    │   │   └── pages/
    │   │       ├── home.html
    │   │       ├── email_generator.html
    │   │       └── code_generator.html
    │   ├── urls.py
    │   └── views.py
    ├── theme/
    │   └── static_src/
    │       ├── src/
    │       │   └── styles.css
    │       └── tailwind.config.js
    ├── manage.py
    └── requirements.txt
```
