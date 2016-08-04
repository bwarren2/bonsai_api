# Bonsai API

This is the API that powers Task Bonsai.

## Set up

    git clone git@github.com:bwarren2/bonsai_api.git
    cd bonsai_api
    mkvirtualenv bonsai_api
    setvirtualenv
    add2virtualenv bonsai
    pip install -r requirements/local.txt
    pip install -r requirements/base.txt

    export DJANGO_SETTINGS_MODULE='bonsai.settings'
    export PYTHONPATH={`manage.py` dir, ex /home/ben/Projects/bonsai_project/bonsai_api/bonsai}
    export PYTHONDONTWRITEBYTECODE=1
    export DJANGO_SECRET_KEY={a secret key}
    export DJANGO_DEBUG=True

    createdb bonsai
    python bonsai/manage.py migrate


## Test coverage

    py.test

## Deployment

    git push heroku master
