class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = (
        'mysql://fernandoh41500:'
        'Password41500'
        '@fernandoh41500.mysql.pythonanywhere-services.com/'
        'fernandoh41500$mysitedb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'nano'
