from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from . import models



def index(request):
    if models.SavedUser.objects.exists():
        return render(request, 'index.html', {'subscribed': True})
    else:
        return render(request, 'index.html')


def mail(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        user = models.SavedUser(name=name, email=email)
        user.save()
        try:
            send_mail(
            "Welcome to D4Devs",
            f"Hi {name},\nWelcome to D4Devs! 🎉\nThank you for subscribing to our newsletter. You're now part of a community that stays ahead with the latest in software development, industry insights, and exclusive updates from our team.\nIn the meantime, feel free to check out our [website link] or follow us on [social media links] for more exciting updates!\n\nStay tuned",
            "786alidev@gmail.com",
            [f"{email}"],
            fail_silently=False,
            )
            return redirect('index')
        except Exception as e:
            print(e)
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')
    

def unsubscribed(request):
    user = models.SavedUser.objects.all()
    name = user[0].name
    email = user[0].email
    print(f"{name}, {email}")
    try:
        send_mail(
        "",
        f"Hi {name},\nYou have successfully unsubscribed from the D4Devs Newsletter",
        "786alidev@gmail.com",
        [f"{email}"],
        fail_silently=False,
        )
        user.delete()
        return redirect('index')
    except Exception as e:
        print(e)
        return redirect('index')
