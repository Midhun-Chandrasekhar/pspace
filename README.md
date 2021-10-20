# P SPACE
Auther: Midhun Chandrasekhar
<br>
Software Architect / Engineer

Date: Oct 20, 2021
<br>
Place: Kerala, In

## B2B Data Repository

Builld: Passed

PSPACE is Web Application Target to track the details of Partners and members under them. Application Help the users to store the information required about the Partners and Members so that they can retrive information int he future for neccisity. 

Architecture: MVT

## Features

- Store Partner Information
- Edit Partner Information
- Retrieve Partner information

## Tech Stacks

- Django: Full Stack Web Framework
- SQLITE: DataBase (Use PSQL in ALL env)
- Bootstrap 5: UI boilerplate for modern web apps
- Django-REST: REST Framework

## Installation

PSPACE requires python >= 3.8 to run.

Install the dependencies and devDependencies and start the server.

```sh
cd pspace
pip3 install -r requirements.txt (better use environments)
Update pspace/settings.py configurations
Python manage.py migrate
Python manage.py createsuperuser
python manage.py runserver
```

Browse: http://localhost:8000/
<br>
API: http://localhost:8000/api/
<br>
Admin: http://localhost:8000/admin/

## TO DO

- Environment Configurations
- Member Features
- Custom Response Classes
- AJAX
- API Documentation Tools
- Logger
