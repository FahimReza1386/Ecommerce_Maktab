from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.


# class CustomUserAdmin(UserAdmin):
#     model=User
#     list_display = ('email' , 'is_superuser', 'is_active')
#     list_filter= ('email' , 'is_superuser', 'is_active')
#     searching_fields = ('email',)
#     ordering = ('email',)
#     fieldsets= (
#         (None , {
#             "fields": (
#                 'email' , 'password'
#             ),
#         })
#     )



# admin.site.register(User , CustomUserAdmin)