# Arklis
Web application written with Python + Django

This application was written on 3 course learning in the Daugavpils Tehnical School.
The application was written for practical purposes.

# Installation
Arklis application requires Python 3.8, PostgreSQL.

## Documentaion
> git clone https://github.com/DenisOstr/Arklis

1. Open CMD in project directory and enter following command:
    - ` python -m pip install -r requirements.txt `
2. Open pgAdmin and create database with name 'arklisdb'
3. Run the following commands (in cmd):
    - ` python manage.py makemigrations `
    - ` python manage.py migrate `
4. Run following command for start server
    - ` python manage.py runserver `
5. Open in browser: http://localhost:8000/

# Demo
> Demo application on heroku: http://arklisweb.herokuapp.com

# Author
> © Denis Ostrovsky

# License
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/DenisOstr/Arklis/blob/master/LICENSE)