# Heroku :

- signup :
  - email : mahmoud148043@gmail.com
  - password : mahmoud_batman123123

* installation inside the enviroment:
  - > pipenv shell
  - > npm install -g heroku

- **Create a file named `Procfile` in the project root :**
  - add th following Note: change `eStore` with the name of your Django project.
  ```
  web: gunicorn eStore.wsgi --log-file -
  ```
- **Create a file requirements.txt:**

  ```
  pip freeze > requirements.txt
  ```

- **Create a file runtime.txt in the project root:**

  - and put the specific Python version , python --version

  ```
  Python 3.6.6
  ```

- **Configure the STATIC-related parameters on settings.py:**

PROJECT_ROOT = os.path.dirname(os.path.abspath(**file**))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
os.path.join(PROJECT_ROOT, 'static'),
)

- **Install the Whitenoise,**

  > pip install whitenoise

- **Add the Whitenoise to your Django application in the wsgi.py file:**

```
import os
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bootcamp.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
```

- **Update the settings.py**

```
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
```

# Deployment

- > heroku login
- > heroku create demo-bootcamp

- open heruko dashboard > deploy

- open heruko dashboard > settings > add vars SECRET_KEY

Push to deploy:

- > git push heroku master
