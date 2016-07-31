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
    createdb bonsai
    python bonsai/manage.py migrate

## Test coverage

    py.test

## Deployment

    git push heroku master
