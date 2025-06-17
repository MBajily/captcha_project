# Django reCAPTCHA Contact Form

A Django web application demonstrating the integration of Google reCAPTCHA v2 with a contact form. This project provides a secure contact form with spam protection using reCAPTCHA verification.

## Features

- **Contact Form**: Clean, responsive contact form with name, email, subject, and message fields
- **reCAPTCHA v2 Integration**: "I'm not a robot" checkbox verification
- **Bootstrap UI**: Modern, responsive design using Bootstrap 5
- **Message Storage**: Contact messages are saved to SQLite database
- **Admin Interface**: Django admin panel for viewing submitted messages
- **Form Validation**: Server-side validation with user-friendly error messages
- **Success/Error Feedback**: Clear user feedback with Django messages framework

## Technology Stack

- **Backend**: Django 4.2+
- **Frontend**: HTML5, Bootstrap 5, CSS3
- **Database**: SQLite (default, easily configurable)
- **Security**: Google reCAPTCHA v2
- **Configuration**: python-decouple for environment variables

## Project Structure

```
recaptcha_project/
├── recaptcha_project/
│   ├── __init__.py
│   ├── settings.py          # Main settings file
│   ├── urls.py              # Root URL configuration
│   └── wsgi.py
├── recaptcha_test/          # Main app
│   ├── __init__.py
│   ├── admin.py             # Admin configuration
│   ├── apps.py
│   ├── forms.py             # Contact form with reCAPTCHA
│   ├── models.py            # ContactMessage model
│   ├── urls.py              # App URL patterns
│   └── views.py             # View functions
├── templates/
│   ├── base.html            # Base template
│   └── recaptcha_test/
│       ├── contact_form.html # Contact form template
│       └── success.html     # Success page template
├── static/                  # Static files directory
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (create this)
└── manage.py
```

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning)

### Step 1: Clone or Download the Project

```bash
# Option 1: Clone with git
git clone <your-repository-url>
cd recaptcha_project

# Option 2: Create new project and copy files
django-admin startproject recaptcha_project
cd recaptcha_project
python manage.py startapp recaptcha_test
# Then copy the provided files to their respective locations
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the project root directory:

```env
SECRET_KEY=your-django-secret-key-here
DEBUG=True
RECAPTCHA_PUBLIC_KEY=your-recaptcha-public-key
RECAPTCHA_PRIVATE_KEY=your-recaptcha-private-key
```

### Step 5: Get reCAPTCHA Keys

1. Visit [Google reCAPTCHA Admin Console](https://www.google.com/recaptcha/admin/create)
2. Click "Create" to register a new site
3. Choose **reCAPTCHA v2** → **"I'm not a robot" Checkbox**
4. Add your domain:
   - For local development: `localhost` and `127.0.0.1`
   - For production: your actual domain
5. Copy the **Site Key** and **Secret Key** to your `.env` file

#### Testing Keys (for development only)

For testing purposes, you can use Google's test keys:

```env
RECAPTCHA_PUBLIC_KEY=6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI
RECAPTCHA_PRIVATE_KEY=6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe
```

**Note**: Test keys will always pass validation but won't provide real spam protection.

### Step 6: Setup Database

```bash
# Create and apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional, for admin access)
python manage.py createsuperuser
```

### Step 7: Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see the contact form in action!

## Usage

### Contact Form

1. Navigate to the home page (`http://127.0.0.1:8000/`)
2. Fill out the contact form with:
   - Name
   - Email address
   - Subject
   - Message
3. Complete the reCAPTCHA verification
4. Click "Send Message"
5. Upon successful submission, you'll be redirected to a success page

### Admin Interface

1. Navigate to `http://127.0.0.1:8000/admin/`
2. Log in with your superuser credentials
3. Click on "Contact messages" to view submitted forms
4. You can search, filter, and view all contact submissions

## Configuration Options

### reCAPTCHA Settings

In `settings.py`, you can adjust:

```python
# Minimum score required for reCAPTCHA v3 (not used in this v2 implementation)
RECAPTCHA_REQUIRED_SCORE = 0.85

# Test mode (bypasses actual reCAPTCHA verification)
RECAPTCHA_PUBLIC_KEY = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'  # Test key
RECAPTCHA_PRIVATE_KEY = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'  # Test key
```

### Database Configuration

The project uses SQLite by default. To use PostgreSQL or MySQL, update the `DATABASES` setting in `settings.py`:

```python
# PostgreSQL example
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Customization

### Styling

- The project uses Bootstrap 5 for styling
- Custom CSS can be added to the `static/css/` directory
- Update `base.html` to include custom stylesheets

### Form Fields

To add more fields to the contact form:

1. Update the `ContactMessage` model in `models.py`
2. Add fields to the `ContactForm` in `forms.py`
3. Update the template in `templates/recaptcha_test/contact_form.html`
4. Run migrations: `python manage.py makemigrations && python manage.py migrate`

### reCAPTCHA Version

To switch to reCAPTCHA v3 (invisible):

```python
# In forms.py
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    # ... rest of the form
```

## Deployment

### Production Checklist

1. Set `DEBUG = False` in production
2. Update `ALLOWED_HOSTS` with your domain
3. Use a production database (PostgreSQL recommended)
4. Collect static files: `python manage.py collectstatic`
5. Use environment variables for sensitive settings
6. Configure HTTPS for your domain
7. Update reCAPTCHA keys for your production domain

### Environment Variables for Production

```env
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=your-database-url
RECAPTCHA_PUBLIC_KEY=your-production-public-key
RECAPTCHA_PRIVATE_KEY=your-production-private-key
```

## Troubleshooting

### Common Issues

1. **reCAPTCHA not loading**
   - Check your public key is correct
   - Ensure your domain is registered with reCAPTCHA
   - Check browser console for JavaScript errors

2. **Form not submitting**
   - Verify private key is correct
   - Check Django logs for validation errors
   - Ensure reCAPTCHA is completed

3. **Bootstrap styles not loading**
   - Check internet connection (CDN links)
   - Verify template extends `base.html`

### Debug Mode

Enable Django debug mode to see detailed error messages:

```python
# settings.py
DEBUG = True
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For issues and questions:

1. Check the [Django documentation](https://docs.djangoproject.com/)
2. Review [django-recaptcha documentation](https://github.com/torchbox/django-recaptcha)
3. Check [Google reCAPTCHA documentation](https://developers.google.com/recaptcha)
4. Open an issue in this repository

## Acknowledgments

- [Django](https://www.djangoproject.com/) - The web framework
- [django-recaptcha](https://github.com/torchbox/django-recaptcha) - reCAPTCHA integration
- [Bootstrap](https://getbootstrap.com/) - Frontend framework
- [Google reCAPTCHA](https://www.google.com/recaptcha/) - Spam protection service