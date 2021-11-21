# saarthi_api
Backend Developer profile task - API based on DRF

To install the required files use:
>pip3 install -r requirements.txt

The application is meant to run on a server. If you wish to run on your system then set **DEBUG = True** and **SECRET_KEY as the old key in comments**. All the changes to be done in settings.py

To make database,
>python manage.py migrate

To make admin user
>python manage.py createsuperuser

Now run the app using
>python manage.py runserver



