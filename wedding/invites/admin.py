from django.contrib import admin

from invites.models import RSVP

class RSVPAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_attending', 'is_coming')

admin.site.register(RSVP, RSVPAdmin)