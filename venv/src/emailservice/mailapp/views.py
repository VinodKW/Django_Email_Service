from django.shortcuts import render
from django.core.mail import send_mail, get_connection
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail.message import EmailMessage
from smtplib import SMTPException

# View for sending the emails
def sendmail(request):

    # condition to check whether the incoming request is of type post or not
    if request.method == "POST":

        # variable "to" for taking the receivers email id.
        to = request.POST.get('toemail') 
        # variable "content" for taking the desired text content.
        content = request.POST.get('content')

        # Try block to send the mail using SendGrid service. 
        try:
            send_mail(
                "SENDGRID MAIL SERVICE", 
                content, 
                settings.EMAIL_HOST, 
                [to]
            )
       
            return render(
                request, 
                'success.html', 
                {
                        'title':'Success'
                }
            )

        # Catching the SMTPException in case Sendgrid service is down. 
        # After Catching the exception we will provide an another service to the user. 
        except SMTPException as e: 

            try:
            
                host = ''
                username = ''
                password = ''

                # Sending the mail with an alternative mail Service, in our case its Gmail.
                with get_connection(
                    host=settings.EMAIL_HOST_GMAIL, 
                    port=settings.EMAIL_PORT, 
                    username=settings.EMAIL_HOST_USER_GMAIL, 
                    password=settings.EMAIL_HOST_PASSWORD_GMAIL, 
                    use_tls=True
                ) as connection:
                    EmailMessage("GMAIL MAIL SERVICE", 
                        content, 
                        host, 
                        [to],
                        connection=connection).send(fail_silently=True)

                
                return render(
                    request, 
                    'success.html', 
                    {
                        'title':'Success'
                    }
                )

            except SMTPException as e:
                print("Both the Services are down", e)
                return render(
                    request, 
                    'error.html', 
                    {
                        'title':'Error'
                    }
                )
    
    
    # If the request is not of type POST, we are render the following template. 
    else:
        return render(
            request, 
            'email.html', 
            {
                'title':'Send an Email'
            }
        )