from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(get_user_model())
class UserAdmin(BaseUserAdmin):
	ordering = ('-id',)

	list_display = ('id', 'email', 'is_active')

	search_fields = ['email', 'mobile_no', 'first_name', 'middle_name',
					 'last_name']

	list_filter = ()

	fieldsets = (
		(None, {
			'fields': (('email', 'mobile_no'),)
		}),
		('Personal details', {
			'fields': (('first_name', 'middle_name', 'last_name'), 'date_of_birth'),
			'classes': ('wide',)
		}),
		('Account status', {
			'fields': (
				('is_active', 'is_staff', 'is_superuser'),
			)
		}),
	)


admin.site.disable_action('delete_selected')
