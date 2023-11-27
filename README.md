# **Api_YaMDb**

the project was carried out in collaboration with 

https://github.com/DanikKravets

https://github.com/ownslv

https://github.com/Astaforkin

---

## Technologies
- Python 3.7
- Django 3.2
- DjangoRestFramework 3.12.4
- SQLite
- Pytest

## Project description
The YaMDb project collects user reviews on works. The works themselves are not stored in YaMDb, so it is not possible to watch a movie or listen to music here. Works are divided into categories such as "Books", "Movies", and "Music". For example, in the "Books" category, there may be works such as "Winnie-the-Pooh" and "The Martian Chronicles", while in the "Music" category there may be a song "Davacha" by the band "Zhuki" and Bach's second suite. The list of categories can be expanded (for example, you can add a category of "Fine Arts" or "Jewelry"). Grateful or outraged users leave text reviews on the works and rate the work on a scale of one to ten (whole number); the user ratings form an average rating of the work - a rating (whole number). A user can leave only one review per work.<br/>

## How to launch a project in dev mode

* Clone the repository and go to it on the command line:
``
git clone git@github.com:DanikKravets/api_yamdb.git

`` ``
cd api_yamdb
``
* Create and activate a virtual environment

for Linux or macOS:
```
python3 -m venv venv
```
```
source venv/bin/activate
``
for Windows:
``
python -m venv venv
```
```
source venv/Script/activate
``
* Install dependencies from a file requirements.txt :
``
pip install -r requirements.txt
``
* Go to the api_yamdb folder, and perform migrations:
``
cd api_yamdb

````
python3 manage.py migrate
``
* Start the project:
``
python3 manage.py runserver
``
_* in Windows, use "python" instead of the "python3" command_

---
after launching the project, at http://127.0.0.1:8000/redoc / documentation for the Yatube API will be available.It describes possible API requests and the structure of expected responses. For each request, the levels of access rights are specified: user roles that are allowed to request.

---
fill in the test data:
``
python manage.py load_data
```

## Registering a new user
- POST
```
http://127.0.0.1:8000/api/v1/auth/signup/
{
  "email": "user@example.com",
  "username": "string"
}
``
## Request examples:
**Getting a JWT token:**
- POST
```
http://127.0.0.1:8000/api/v1/auth/create/
```
**Get a list of all publications:**
- GET
```
http://127.0.0.1:8000/api/v1/posts/
{
  "username": "string",
  "confirmation_code": "string"
}
```
**Adding a new work (administrator):**
- POST
```
http://127.0.0.1:8000/api/v1/titles/
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```
**Getting a list of all reviews:**
- GET
```
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
```
**Getting all comments on a review:**
- GET
```
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
```
**Detailed documentation for the project is available at:**
```
http://127.0.0.1:8000/redoc/