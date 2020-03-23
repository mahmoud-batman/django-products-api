# Deployment :

_activate django env:_

- > pipenv shell

- > pip install gunicorn whitenoise

signup Heroku account .

- install Heroku-cli

- > heroku login

_to create project from cli :_

- > heroku create projectname

_to access the heroku project from cli :_

- > heroku git:remote -a porojectname

_to ensure which project we are in :_

- > git remote -v

- > heroku run python manage.py migrate

---

_create `requirements.txt` in root project_

- > pip freeze > requirements.txt

_create `runtime.txt`, see the available python versions in heroku docs_

- > python 3.8.1

_create `Procfile`_

- > web: gunicorn projectname.wsgi --log-file -

---

_setting.py :_
to allow tha app on local server and heroku server

```
DEBUG= False
ALLOWED_HOSTS = ['YOUR HEROKU APP URL', '127.0.0.1']
```

---

- _in heroku dashboard > settings add buildpack to python :_

---

_collect static error :_

add in setting.py

```
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

 STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
 STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


```

```
MIDDLEWARE = [
  # 'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
]
```

---

**heroku Git :**

- > git init

to show any modifications

- > git status

create .gitignore

- > git status
- > git add .
- > git commit -m "First Commit"
- > git push heroku master

**Github:**

- _create a git repo for your app_

# create postgres db :

- > heroku addons:create heroku-postgresql:hobby-dev

import a library to help us change from sqlite into postgres

- > pip install dj-database-url
- > pip install psycopg2==2.7.5

- > pip freeze > `requirements.txt`

- in `setting.py`:

  ```
  import dj_database_url
  DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
  ```

- > git status
- > git add .
- > git commit -m "postgres DB"
- > git push heroku master

- migrate the new database :
- > heroku run python manage.py migrate

---

NOTE : when you make changes you should enable the maintenance mode , to make the users not lose there data

> heroku mnaintenance:on

> heroku run python manage.py migrate

> heroku maintenance:off

---

Cloud file storage services Because Heroku has an “ephemeral” hard drive

EX:

- AWS
- MediaFire
- Google Drive

# 1 - AWS :

heroku dashboard > settings > config vars :

- NOTE :

DATABASE_URL = `postgres://USERNAME:PASSWORD@database url endpoint:PORT/DB NAME`

that what will do with AWS
