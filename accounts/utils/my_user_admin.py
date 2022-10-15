from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


class MyUserAdmin(UserAdmin):
    fieldsets = (
        # (None, {"fields": ("username", "password")}),
        (None, {
            "fields": ("email", "password")
        }),
        # (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (_("Personal info"), {
            "fields": ("first_name", "last_name")
        }),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {
            "fields": ("last_login", "date_joined")
        }),
    )

    # docs.djangoproject.com/en/4.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.get_fieldsets
    def get_fieldsets(self, request, obj=None):
        if not request.user.is_superuser:
            fieldsets = (
                (None, {
                    "fields": ("email", "password")
                }),
                (_("Personal info"), {
                    "fields": ("first_name", "last_name")
                }),
                (
                    _("Permissions"),
                    {
                        "fields": (
                            "is_active",
                            "is_staff",
                            # "is_superuser",
                            "groups",
                            # "user_permissions",
                        ),
                    },
                ),
                (_("Important dates"), {
                    "fields": ("last_login", "date_joined")
                }),
            )
            return fieldsets
        return self.fieldsets

    readonly_fields = ('last_login', 'date_joined',)  # add

    # docs.djangoproject.com/en/4.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.get_readonly_fields
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return self.readonly_fields + ('is_active', )
        return self.readonly_fields

    # The add_fieldsets variable is used to define the fields
    # that will be displayed on the create user page.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide", ),
                # "fields": ("username", "password1", "password2"),
                "fields": ("email", "password1", "password2"),
            },
        ), )

    # list_display = ("username", "email", "first_name", "last_name", "is_staff")
    list_display = ("email", "first_name", "last_name", "is_staff")
    # search_fields = ("username", "first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")

    # ordering = ("username",)
    ordering = ("email", )
