---
layout: post
title:  "Wagtail Web Deployment"
date:   2022-04-04 08:00:00 +0700
categories: deployment, web, working
author: ntnhaatj
---

# System overview
- wagtail/django (settings files, static root/dirs)
- db
- object storage
<figure>
    <img src="/images/20220404/system_overview.png" width="100%" height="100%">
</figure>

-----
# Dev deployment
- set `DJANGO_SETTINGS_MODULE=settings.dev`

## database
- sqlite

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

## static storage
- local storage

```python
# settings/dev.py

# where user's static file will be stored
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

# where collectstatic command output will be stored
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# relative URL to access static files, ie: http://domain.com/static/app.css
STATIC_URL = '/static/'
```

## media storage
- the same as `static`

## dev tools
- [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)

-----
# Staging deployment
- set `DJANGO_SETTINGS_MODULE=settings.staging`

## CI/CD pipeline
- versioning source code by github
- triggered `github actions` on every push to `main`, `feat/*`, `dev/*` branch and manually dispatch
- using github secrets to store secret keys for deployment
- example for github action workflow:

```yaml
name: CI/CD

on:
  push:
    branches: [ main, feat/* ]
  pull_request:
    branches: [ main ]
  workflow_dispatch:

jobs:
  deploy:

    runs-on: ubuntu-20.04
    strategy:
      max-parallel: 4
      matrix:
        python-version: [3.9]
        
    steps:
    - name: Checkout repo
      uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip pipenv
        pipenv install --system --dev --ignore-pipfile
    - name: Run Tests
      run: |
        python manage.py test
    - name: Deploy
      uses: akhileshns/heroku-deploy@v3.12.12 # This is the action
      with:
        heroku_api_key: ${{ secrets.HEROKU_API_KEY }}
        ...
      env:
        HD_DJANGO_SETTINGS_MODULE: "app.settings.staging" # env prefix is HD_ to be recognized by heroku deploy service
        ...
    - name: Slack Notification
      if: always()
      uses: rtCamp/action-slack-notify@v2
      env:
        SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK }}
        ...
```

## hosting
- heroku (using github actions `akhileshns/heroku-deploy@v3.12.12` as above to deploy, free pricing plan - `dyno` type)
- gunicorn (wsgi application)

```shell
# ./Procfile

web: gunicorn app.wsgi
release: python manage.py migrate
```

- collect static (this step is auto-executed by heroku). It will collect al static file (both `user's and django` static) into `STATIC_ROOT` dir

```shell
$ python manage.py collectstatic --noinput
```

## database
- heroku postgresql (free pricing plan)
- using github secrets to setup db credentials for deployment

## object storage (media, static files)
- cloudinary (media)

```python
# settings/staging.py

INSTALLED_APPS += [
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
]
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get("CLOUDINARY_NAME", "foo"),
    'API_KEY': os.environ.get("CLOUDINARY_API_KEY", "foo"),
    'API_SECRET': os.environ.get("CLOUDINARY_API_SECRET", "foo"),
    'STATICFILES_MANIFEST_ROOT': os.path.join(BASE_DIR, "static")
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

- whitenoise (static files)

```python
# settings/staging.py

MIDDLEWARE += [
    "whitenoise.middleware.WhiteNoiseMiddleware",
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
```

## other settings
```python
# settings/staging.py

ALLOWED_HOSTS = ["domain.com"]
# or easier
ALLOWED_HOSTS = ["*"]
```