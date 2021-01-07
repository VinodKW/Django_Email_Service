from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def sendmail(request):
    if request.method == "POST":
        to = request.POST.get('toemail')
        content = request.POST.get('content')
        print("-------------REQUEST----------------")
        print(send_mail(
            "testing", 
            content, 
            settings.EMAIL_HOST, 
            [to]
        ))
        print("------------------")
        print(HttpResponse.status_code)
        print("------------------")
        return render(
            request, 
            'email.html', 
            {
                'title':'send and email'
            }
        )
    else:
        return render(
            request, 
            'email.html', 
            {
                'title':'send and email'
            }
        )