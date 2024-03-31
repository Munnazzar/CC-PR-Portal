from django.contrib import admin
from .models import User


class UserView(admin.ModelAdmin):
    list_display = ["username", "email", "first_name", "last_name", "is_superuser"]


admin.site.register(User, UserView)
