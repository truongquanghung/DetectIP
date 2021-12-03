from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import requests
from django.conf import settings
# Create your views here.

class home(View):

    def get(self, request):
        r = requests.get('https://api.ipify.org')
        print(r.text)
        if settings.IP != r.text:
            settings.IP = r.text
            update = requests.get('https://qhung.pythonanywhere.com/update/'+r.text)
        return HttpResponse("This is current Server's IP: "+r.text)
