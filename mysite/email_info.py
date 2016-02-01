

# EMAIL_HOST = 'smtpout.secureserver.net'
# EMAIL_HOST_USER = 'email'
# EMAIL_HOST_PASSWORD = 'password'
# DEFAULT_FROM_EMAIL = 'email'
# SERVER_EMAIL = 'email'
# EMAIL_PORT = 80 
# EMAIL_USE_TLS = False

#ovo je za gmail

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'email'
DEFAULT_FROM_EMAIL = 'email'
SERVER_EMAIL = 'email'
EMAIL_HOST_PASSWORD = 'password'
