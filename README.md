Installation

```sh
>> python3 -m venv myTidyVEnv
>> source myTidyVEnv/bin/activate
>> pip3 install django djangorestframework requests
>> python -m pip install django-cors-headers
```
Download your library

```sh
>> cd books
>> python books.py
```

Load your database

```sh
>> python manage.py makemigrations
>> python manage.py migrate
>> python manage.py populateDB
```