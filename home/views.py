from django.shortcuts import render
from django.contrib.auth.models import User
from event import models



def home(request):
    if request.user.is_authenticated and request.user.is_staff:
        user_count = User.objects.count()
        event_count = models.Event.objects.count()
        bookedTickets = models.BookedEvent.objects.count()
        return render(request, 'home.html', {'user_count': user_count, 'event_count': event_count, 'bookedTickets': bookedTickets})
    return render(request, 'home.html')
