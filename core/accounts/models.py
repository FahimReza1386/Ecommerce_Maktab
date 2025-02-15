from django.db import models
from django.contrib.auth.models import (BaseUserManager , AbstractBaseUser , PermissionsMixin )
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self , email , password , **extra_fields):
        '''
            Create and Save The User With The Given Email And Password or Extra_data .
        '''
        if not email:
            raise ValueError(_('Email Must Not Null .'))
        email = self.normalize_email(email)
        user = self.model(email=email , **extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self , email , password , **extra_fields):
        '''
            Create and Save The Super User With The Given Email And Password  or Extra_data .
        '''
        extra_fields.setdefault("is_staff" , True)
        extra_fields.setdefault("is_superuser" , True)
        extra_fields.setdefault("is_active" , True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('SuperUser Must Have is_staff == True .'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('SuperUser Must Have is_superuser == True .'))
        return self.create_user(email , password , **extra_fields)



    

class User(AbstractBaseUser,PermissionsMixin):

    '''
            Custom User Model for our app
    '''



    email = models.EmailField(max_length=400 , unique=True)


    is_superuser =models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False) 
    is_active= models.BooleanField(default=True)
    # is_verified = models.BooleanField(Define=False)

    first_name = models.CharField(max_length=20)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    craeted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    objects = UserManager()
    def __str__(self):
        return f'{self.email}'