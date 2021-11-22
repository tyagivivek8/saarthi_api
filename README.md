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

The API for Ice and Fire is working on /api/external-books/?name=<variable>
  You can query it with the name of the books.
  
The CRUD API is live on /api/v1/books/
  GET, POST, PATCH, DELETE methods are enabled.
# GET Request
  GET /api/v1/books/
You may also search using 
  /api/v1/books?name=<name>&country=<var>&publisher=<var>&year=<var>
  
  You may use any combination of parameters
  
# POST Request
  POST /api/v1/books/
  
  JSON Body Format:
  
```  
  {
    "name": "A Game of Thrones",
    "isbn": "978-0553103540",
    "authors": [
      "George R. R. Martin"
    ],
    "number_of_pages": 694,
    "publisher": "Bantam Books",
    "country": "United States",
    "release_date": "1996-08-01"
  }
```
# UPDATE Request
  PATCH /api/v1/books/<bookid>
  Body with Same format as POST

# DELETE Request
  DELETE /api/v1/books/<bookid>

# To deploy on Heroku
  
  Create a Heroku account and install the Heroku CLI

  Now you may create a Heroku app with
  >heroku create <app_name>

  Set the SECRET_KEY and DEBUG_VALUE as environment variables in Heroku app
  >heroku config:set SECRET_KEY=<your secret key>
  >heroku config:set DEBUG_VALUE=False

  To generate a secret key, open Python shell
  >import secrets
  >secrets.token_hex(24)

  Use the generated secret key for production
  Add "<app_name>.herokuapp.com" to ALLOWED_HOSTS

  Now deploy the app to heroku
  >git add -A
  >git commit -m "message"
  >git push heroku master

  To create database and admin user on server
  >heroku run python manage.py migrate
  >heroku run bash

  In the heroku bash use
  >python manage.py createsuperuser

  and create an admin account for the application
  The admin panel is available at /admin route

The app is now live at <app_name>.herokuapp.com
  
The API is also live at https://saarthiapi.herokuapp.com/api/v1/books/ (CRUD) and https://saarthiapi.herokuapp.com/api/external-books/ (IceandFire)
Thank you for using the API!
