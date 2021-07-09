DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'highlightvideo',
        'USER': 'highlighter',
        'PASSWORD': 'highlighter12',
        'HOST': 'highlighter-mysql.cpt0ctnfatu9.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306', 
    }
}

import settings 

SECRET_KEY = settings.SECRET_KEY