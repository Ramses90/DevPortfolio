from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
def index(request):
    user = User.objects.all()
    portfolios = Portfolio.objects.all()
    contact = Contact.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name,email, message, subject)
        comment = '%s %s %s %s' % (email, name, subject, message)
        send_mail(subject, comment, email, ['mobeenarchi@gmail.com'])
        print(send_mail)
        messages.success(request, 'Your message has been sent. Thank you!')
        return redirect('index')

    context = {'user': user[0], 'portfolios': portfolios, 'contact':contact[0],}
    return render(request, 'index.html', context)