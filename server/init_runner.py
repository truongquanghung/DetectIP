import requests
from django.conf import settings
import time
def run():
    d = 0
    while True:
        try:
            r = requests.get('https://api.ipify.org')
            if settings.IP != r.text:
                settings.IP = r.text
                update = requests.get('https://qhung.pythonanywhere.com/update/'+r.text)
        except:
            print('Error!')
        d+=1
        print('Load '+str(d)+' time')
        time.sleep(30)