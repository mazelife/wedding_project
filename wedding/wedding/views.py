from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, TemplateView

from invites import forms, models


class Home(TemplateView):
    template_name = "home.html"


class RSVP(CreateView):
    model = models.RSVP
    form_class = forms.RSVPForm
    success_url = "/"
    template_name = "rsvp.html"

    def form_valid(self, form):
        redirect_response = super(RSVP, self).form_valid(form)
        return redirect_response
    