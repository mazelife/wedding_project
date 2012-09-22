from django.contrib import admin

from wedding.invites.models import RSVP


class RSVPAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_attending', 'is_coming')

    def total_attending(self):
        return self.model.objects.total_attending()
        
admin.site.register(RSVP, RSVPAdmin)