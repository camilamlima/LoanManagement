release: python manage.py makemigrations
release: python manage.py migrate

web: gunicorn TestSite.wsgi --log-file -