# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%mif%4x#o9!6t&vje3l3$_h1erhzuh4il483a$cl15e%x$!rce'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Password'
    }
}