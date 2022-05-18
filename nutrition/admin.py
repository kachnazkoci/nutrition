from django.contrib import admin


class HomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'food', 'contact', 'language')
    list_filter = ('language', )


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact_at', )
    list_filter = ('name',)
