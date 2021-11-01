from django.contrib import admin
from users.models import User


# @admin.register(User)

class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ("last_name", "first_name", "role")
    list_filter = ("role", )
    fields = (("first_name", "last_name"), "email", "role", "password", "is_active", "is_staff", "is_admin")

admin.site.register(User, UserAdmin)
