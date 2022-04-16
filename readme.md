# Dummy Django Project, Introduction to Software Engineering (CSC13002)
A dummy Django Project for Introduction to Software Engineering (CSC13002) midterm personal lab.

|SID|Name|
|---|----|
|19120338|Tran Hoang Quan|

Tutorial playlist: https://www.youtube.com/watch?v=xv_bwpA_aEA&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO

## Installation
```
pip install -r requirements.txt
```

Run `python manage.py shell` to enter shell interface, then
```python3
from django.core.management.utils import get_random_secret_key  
get_random_secret_key()
```

Paste that newly-generated key to `crm1/.env`:
```
SECRET_KEY = 'your newly created key'
```

## Notes
### 1. Authentication for administrator
```
python manage.py createsuperuser
```

By this far, I configurated these fields as default admin credential:
```
Username: quan
Password: tranluixuong
```

### 2. Model creation and migration
To generate migration scripts (after creating a new model):
```
python manage.py makemigrations
```

To apply (aka generate table):
```
python manage.py migrate
```