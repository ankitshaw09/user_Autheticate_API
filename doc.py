#   step 1 : create virtual env 
# 2> create app and project 
#   user_authenticate_API is project 
#   user is app 
# connect app with your project in settings.py
# then go to drf website and install restframework 
#   " pip install djangorestframework "

# INSTALLED_APPS = [
#     ...
#     'rest_framework',
# ]
#
# MIDDLEWARE = [
    
# ]
#
""" install simple jwt
'pip install djangorestframework-simplejwt'
add this code in setting.py file
REST_FRAMEWORK = {
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
        
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
   
}
note : jwt kya hota hai


INSTALLED_APPS = [
    ...
    'rest_framework_simplejwt',
    ...
]

jwt setting from simple jwt website 

from datetime import timedelta
...

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
   
}

install pip install django-cors-headers
  
  INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
]
  MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...,
]
  
  CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]


then create models.py

and 
python manage.py makemigrations
python manage.py migrate


create superuser
python manage.py createsuperuser

# now amake urls.py in both app and project 

# then make views.py in views make a class  userRegistrations
 

/////   postman  testing     ////
# 1> register user
http://127.0.0.1:8000/api/user/register/
{
    "email":""
    "name":""
    "password":""
    "password2":""
    "tc":true
    }

    hume dekhne milega jab hum send karenge  
    {
    "token": {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNjQ0MzgxOSwiaWF0IjoxNzA2MzU3NDE5LCJqdGkiOiI0ZDczOGIyNGQxODE0OTU3YWU2YTQ0NTNlNmU2M2NkYyIsInVzZXJfaWQiOjJ9.i12emBQMYhrc2DMqJdtYIeOLoekOtHZlqo_REN8jWRY",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2MzU4NjE5LCJpYXQiOjE3MDYzNTc0MTksImp0aSI6IjNmYTdiNDUzZDJkMjQ2OTA4ZjkwMWNjNWQ1OTUxOTAwIiwidXNlcl9pZCI6Mn0.sa5ILUuyJSRU2qp1up0uVyH6fvy4tu3RqeVwlEMcRko"
    },
    "msg": "Registration Successful"
}
# 2> login user

http://127.0.0.1:8000/api/user/login/
{
    "email":""
    "password":""

}

or dekhne milega {
    "token": {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNjQ0MzgxOSwiaWF0IjoxNzA2MzU3NDE5LCJqdGkiOiI0ZDczOGIyNGQxODE0OTU3YWU2YTQ0NTNlNmU2M2NkYyIsInVzZXJfaWQiOjJ9.i12emBQMYhrc2DMqJdtYIeOLoekOtHZlqo_REN8jWRY",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2MzU4NjE5LCJpYXQiOjE3MDYzNTc0MTksImp0aSI6IjNmYTdiNDUzZDJkMjQ2OTA4ZjkwMWNjNWQ1OTUxOTAwIiwidXNlcl9pZCI6Mn0.sa5ILUuyJSRU2qp1up0uVyH6fvy4tu3RqeVwlEMcRko"
    },
     "msg": "Login Success"
}
# 3> profile user

http://127.0.0.1:8000/api/user/profile/

go to header
Key - Accept    Value - application/json
Key - Authorization    Value - Bearer token here  (access token)  ye >>> "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2MzU4NjE5LCJpYXQiOjE3MDYzNTc0MTksImp0aSI6IjNmYTdiNDUzZDJkMjQ2OTA4ZjkwMWNjNWQ1OTUxOTAwIiwidXNlcl9pZCI6Mn0.sa5ILUuyJSRU2qp1up0uVyH6fvy4tu3RqeVwlEMcRko"
   access token kaha milega  jab hum login karenge tab 


# 4> change password user

http://127.0.0.1:8000/api/user/changepassword/

{
    "old_password": "",
    "new_password": "",
    "confirm_password": ""
}

# 5> send reset password email user
http://127.0.0.1:8000/api/user/send-reset-password-email/

{
    "email": " "


}

# 6> reset password user
http://127.0.0.1:8000/api/user/reset-password/<uid>/<token>
{
    "new_password": "", 
    "confirm_password": ""
    




  """