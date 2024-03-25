import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

    MAIL_SERVER = 'localhost' # 'smtp.googlemail.com'  or os.environ.get('MAIL_SERVER')
    MAIL_PORT = 8025 # 587 or int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['test@gmail.com']

    POSTS_PER_PAGE = 10
    LANGUAGES = ['en', 'es']
