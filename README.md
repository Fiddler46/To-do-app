## Setting Backend
Creating directory for our project
```bash
mkdir todo_react
cd todo_react
```
Now we have to install Pipenv using pip to activate new vitual enviorment
```bash
pip install pipenv
##Give "sudo" before pip if it returns permission related errors 
pipenv shell
```
Now you will be enterd into vitual enviorment 

```bash
(todo_react) [whoami@swift todo_react]$
```
Now lets install Django using Pipenv and create a project called backend
```bash
pipenv install django
django-admin startproject backend
```
Now navigate into backend folder and start a new application called todo.
```bash
cd backend
python manage.py startapp todo
```
After that lets run migrations and start up server
```bash
python manage.py migrate
python manage.py runserver
```

