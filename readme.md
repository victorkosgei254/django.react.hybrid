This is a Django react project

Backend:- Contains Django source code with react production build in the frontend folder 

Frontend :- Holds the frontend code 

Steps 

```
cd backend
pip install requirements.txt
./manage.py makemigrations 
./manage.py createsuperuser
./manage.py runserver
```

You can navigate to admin console and add blogs in via the admin interface

using postman go to `http://localhost:8000/blog/api/v1/blog` to get  a list of blogs 

Open `http://localhost:8000/blog` to get a blank REACT app, on the developers tab, view the console

Console should log all the updated blogs

This simple demo shows how to integrate  django with react.

