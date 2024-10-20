from base import *
DEBUG = False
ALLOWED_HOSTS = ['
Emiliano91.pythonanywhere.com']
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.sqlite3',
        'NAME':os.path.join(os.path.dirname(BASE_DIR),'db_sqlite3')
    }
}
