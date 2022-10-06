# Launching

Lines that contain [ ] and all caps are names created by you.
- Examples: [PROJECTNAME]/[APPNAME]
------------------------------------------------------

-Create new git branch

------------------------------------------------------
## Start Project

~~~
django-admin startproject [PROJECTNAME]
~~~  

- [PROJECTNAME] Should be unique and not interfere with internal Django workings.  
- Change Directory to use manage.py  

~~~	
py manage.py startapp [APPNAME]
~~~
- [APPNAME] Should be unique once again  

------------------------------------------------------
## Start View

in [APPNAME]/views.py:  
- Write your normal Python code for operations. Can also use HTTP methods provided by Django to manipulate your webpage  
- Views require (request)  
- Supporting functions do not require (request)  

### Simple View:

~~~python
from django.http import HttpResponse

def index(request):  
    return HttpResponse("Hello, world. You're at the [APPNAME] index.")  
~~~

------------------------------------------------------

create urls.py in [APPNAME] folder

------------------------------------------------------

in [APPNAME]/urls.py: (*1)

~~~python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
~~~

------------------------------------------------------

in [PROJECTNAME]/urls.py: (*2)

~~~python
from django.contrib import admin
from django.urls import include, path <-- add "include"

urlpatterns = [
    path('[APPNAME]/', include('[APPNAME].urls')), <-- don't forget the comma
    path('admin/', admin.site.urls),
]
~~~
------------------------------------------------------

in [APPNAME]/models.py: (*4)

- Create any necessary class for creating data utlizing Django models

------------------------------------------------------

in [PROJECTNAME]/settings.py:
- This is adding newly created apps to your overal Django project

~~~python
INSTALLED_APPS = [
    '[APPNAME].apps.[Appname]Config', <-- First letter capped for Config (AppnameConfig)
]
~~~
- Note that there are already lines in this list, just add to the top

------------------------------------------------------

~~~
py manage.py makemigrations [APPNAME] #### (*3.2)
~~~
- Numbers are optional. Name is too but not recommended


~~~
py manage.py migrate (*3.1)
~~~
------------------------------------------------------

## Create Superuser (admin)

~~~
py manage.py createsuperuser
~~~

------------------------------------------------------

in [APPNAME]/admin.py:

~~~python
from django.contrib import admin

from .models import [ModelName]

admin.site.register([ModelName])
~~~

- Remove [ ]'s around ModelName

------------------------------------------------------

## Add HTML

1. Add folders in the [APPNAME] folder:
	- .../templates/[APPNAME]
	- .../static/[APPNAME]
2. Add index.html to templates

3. Add style.css to static/[APPNAME]

3. add any images being used to static/[APPNAME]