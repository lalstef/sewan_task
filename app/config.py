import os

ADMIN_EMAIL = 'admin@example.com'
SMTP_HOST = os.environ.get('SMTP_HOST')
SMTP_PORT = os.environ.get('SMTP_PORT')
SMTP_USERNAME = os.environ.get('SMTP_USERNAME')
SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')

EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')
HTTP_BACKEND = os.environ.get('HTTP_BACKEND')
