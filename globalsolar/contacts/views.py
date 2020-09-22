from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        work_title = request.POST["work_title"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        message = request.POST["message"]
        work_id = request.POST["work_id"]

        if request.user.is_authenticated:
            user_id = request.user.id
            contact = Contact.objects.all().filter(
                work_id=work_id, user_id=user_id
            )
            if contact:
                print("contact added")
                return redirect('/portfolio/' + work_id)
        contact = Contact(title=work_title, work_id=work_id, name=name, email=email,
                          phone=phone, message=message, address=address, user_id=request.user.id)
        contact.save()

        send_mail(
            "New connect",
            "Станція:" + " " + work_title + " " + "контакт з новим клієнтом" +
            message + " " + name + " " + email + " " + phone,
            'sup2a1nn@gmail.com',
            ['sup2a1nn@gmail.com'],# Теж ваша електронка - куди буде лист відправлятися
            fail_silently=False
        )

        return redirect('/portfolio/' + work_id)
