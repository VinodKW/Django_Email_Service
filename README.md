# Django Email Service App

![alt text](https://github.com/VinodKW/Django_Email_Service/blob/master/image.png?raw=true)

**This Service is written with Django 2.0.7.**

## Email Services Used
* Gmail ( Please ensure that, the gmail accound is in less secure mode)
* SendGrid 

## Building

Clone the repository and hit the following commands:

```sh
$ cd Django_Email_Service/venv
$ source bin/activate
$ cd src/emailservice
$ python manage.py runserver
```

Then visit `http://localhost:8000` to view the app. 

## Logic for handling multiple Services

```
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

```
## Wanna Contribute? 

Master [git repository](https://github.com/VinodKW/Django_Email_Service.git):

* `git clone https://github.com/VinodKW/Django_Email_Service.git`

