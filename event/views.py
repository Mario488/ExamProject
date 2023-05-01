from django.shortcuts import render, redirect
from . import models
from django.contrib import messages


def events(request):
    if request.method == "POST" and request.POST['post'] == "POST1":
        event = request.POST['search_input']
        Event = models.Event.objects.filter(Name__contains=event)
        if Event.exists():
            return render(request, 'events.html', {'event': Event})
        else:
            return render(request, 'events.html')   

    if request.method == "POST" and request.POST['post'] == "POST2":
        if not request.user.is_authenticated:
            messages.success(request, 'Моля, влезте в профила си или се регистрирайте, за да направите резервация.')
            return redirect('login')
        else:
            username = request.user.username
            eventName = request.POST['eventName']
            checkExist = models.BookedEvent.objects.filter(User=username, Name=eventName)
            if checkExist.exists():
                messages.success(request, 'Вече имате резервация за този билет. Моля, изберете друг събитие или анулирайте съществуващата резервация.')
                return redirect('reserve')

            bookedEvent = models.BookedEvent(User=username, Name=eventName)
            messages.success(request, 'Успешно направена резервация')
            bookedEvent.save()
            return redirect('reserve')

    event = models.Event.objects.all()
    return render(request, 'events.html', {"event": event})


