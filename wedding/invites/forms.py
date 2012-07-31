from django import forms

from wedding.invites.models import RSVP


class RSVPForm(forms.ModelForm):
    
    class Meta:
        model = RSVP
        fields = ('name', 'attending', 'guests')

    def __init__(self, *args, **kwargs):
        super(RSVPForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Your name"
        self.fields['attending'].label = "Check if you will be attending"
        self.fields['guests'].label = "Number of guests, including yourself"