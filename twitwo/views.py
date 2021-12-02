from django.shortcuts import render

from .models import Twit

def index(request):
    twits = Twit.objects.all()
    return render(request, 'twitwo/index.html', {'twits': twits})
