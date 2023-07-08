# Pinterest-django



### server start 

서버 시작전

 1. 명령어 실행
    
 pip install django
 
 pip install django-environ

3. git에 없는 .env 파일 만들기
   
(manage.py와 같은 경로에)

.env(settings.py와 관련됨)

-----------------------------

SECRET_KEY=[secret-key 값]

DEBUG=True

-----------------------------

manage.py와 같은 경로에서 -> python manage.py runserver [ip]:[port]
