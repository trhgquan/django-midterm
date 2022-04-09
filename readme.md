# Midterm dummy Django Project for Introduction to Software Engineering (CSC13002)

|SID|Name|
|---|----|
|19120338|Tran Hoang Quan|

Playlist link: https://www.youtube.com/watch?v=xv_bwpA_aEA&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO

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