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
You will be resulted with this
```bash
(todo_react) [whoami@swift backend]$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 23, 2019 - 18:14:33
Django version 2.2.5, using settings 'backend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Now logon to the address >> http://127.0.0.1:8000/
we should see an instance of a Django application running on this address

![django runnig successfully](https://miro.medium.com/max/3200/0*PvWdkGTFVcXMFOev)

