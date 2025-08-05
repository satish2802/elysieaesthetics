from django.http import HttpResponse
from django.shortcuts import render, redirect
from skincare.models import Appointment
from django.core.mail import send_mail
from django.conf import settings



def homepage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        service = request.POST.get('service')

        # Save to DB
        Appointment.objects.create(
            name=name,
            email=email,
            date=date,
            time=time,
            service=service
        )
        # Send email
        subject = 'New Appointment Booking'
        message = f'''
        Name: {name}
        Email: {email}
        Date: {date}
        Time: {time}
        Service: {service}
        '''
        recipient = settings.EMAIL_HOST_USER  # Replace with the email you want to receive appointments at

        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])

        return redirect('/?success=true')
    
    success = request.GET.get('success') == 'true'
    
    return render(request, 'index.html', {'success': success})
            


def aboutUs(request):
    return render(request,"about.html")
def products(request):
    return render(request,"products.html")
def price(request):
    return render(request,"price.html")
def contacts(request):
    return render(request,"contact.html")


