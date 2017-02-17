#In settings.py you can have play and plug around with the authentication system used in django
#AUTHENTICATION_BACKENDS: default ModelBackend is used to authenticate user with the username and password. 
#If we want to authenticate with some other values, Like phone number and pin in ai.core case, we can write our own class. Refer to this in base.py in ai-core. This particular class needs to ovveride 
#authentication method. 
# Please refer to djangobooks.com Custom Authentication section for more info

#DEFAULT_AUTHENTICATION_CLASSES: Please refer to http://www.django-rest-framework.org/api-guide/authentication/ for more info
# we can have various authentication systems, BasicAuthentication, TokenAuthentication, SessionAuthentication.
# We use token authentication, set in base.py. We also send 'Authorixation : Token asdshjdsin' in our headers. 
# TokenAuthentication used this token to authenticate the users. 

#To implement a custom authentication scheme, subclass BaseAuthentication and override the .authenticate(self, request) method. 
#The method should return a two-tuple of (user, auth) if authentication succeeds, or None otherwise. In our TokenAuthentication, we 
# have overriden the authenticate method.