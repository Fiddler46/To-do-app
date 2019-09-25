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

### Adding 'todo' app to Django app list

Now we have to open up ```backend/settings.py``` file. By adding todo app inside Django  ```INSTALLED_APPS``` list django can recoginize our todo app.

```python
# backend/settings.py
.
.
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo' #adding todo app to the list
]
```

### To-do Model defining 

Creating a model for our app, to define how todo item should be stored in database.</BR>
Open ```todo/models.py``` and update it with following code
```python
#add this to todo/models.py
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextFeild()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
```
Above code explain the 3 models which we have introduced for our todo app

- Title
- Description
- Completed 

Complete property will act as status of the task(completed/not completed).</br>
To apply chnages that we have given we have to migrate the app.</br>
For that
```shell
python manage.py makemigrations todo
python manage.py migrate todo
```
Now lets configure admin interface that provided by django out-of-the box.</br>
Update ```todo/admin.py``` like this
```python
from django.contrib import admin
from .models import Todo #add this , importing todo model that we created 
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
# Register your models here
admin.site.register(Todo, TodoAdmin)
```
