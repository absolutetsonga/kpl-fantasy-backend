from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm

#     model = CustomUser

#     list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined')
#     list_filter = ('is_active', 'is_superuser', 'is_staff')
    
#     fieldsets = (None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name')}), 
#     ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
#     ('Dates', {'fields': ('last_login', 'date_joined')})

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_active')}
#          ),
#     )    

#     search_fields = ('email',)
#     ordering = ('email',)

# admin.site.register(CustomUser, CustomUserAdmin)