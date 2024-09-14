from django.contrib import admin
from .models import Book

admin.site.register(Book)
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')

admin.site.register(Book, BookAdmin)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author__name')  # Use double underscores for related fields

admin.site.register(Book, BookAdmin)
   # users/admin.py

   from django.contrib import admin
   from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
   from .models import CustomUser

   class CustomUserAdmin(BaseUserAdmin):
       model = CustomUser
       list_display = ('username', 'email', 'date_of_birth', 'profile_photo', 'is_staff')
       fieldsets = (
           (None, {'fields': ('username', 'password')}),
           ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
           ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')}),
           ('Important dates', {'fields': ('last_login', 'date_joined')}),
       )
       add_fieldsets = (
           (None, {
               'classes': ('wide',),
               'fields': ('username', 'password1', 'password2', 'date_of_birth', 'profile_photo')}
           ),
       )
       search_fields = ('username',)
       ordering = ('username',)

   admin.site.register(CustomUser, CustomUserAdmin)
   
