# !/bin/bash
mkdir -p ./run
pip install -r ./requirements.txt
python manage.py makemigrations
python manage.py migrate
#python manage.py runserver 0.0.0.0:8000
uwsgi --ini uwsgi.ini
tail -f /dev/null