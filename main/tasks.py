from celery import shared_task
from main.spider import MySpider
from olx_report.celery import app
from django.core.mail import send_mail
from django.conf import settings
from main.models import Report, AdsDateTime


@app.task
def spider_run(url, email, current_site):
    spider = MySpider()
    spider.initial_urls.append(url)
    spider.run()

    report = Report.objects.create(
        url=url,
        email=email
    )      

    for date_time in spider.date_time:
        AdsDateTime.objects.create(
            report=report,
            date_time = date_time,
        )
    
    current_site = current_site
    mail_subject = 'Ссылка на график'
    message = 'http://{}/graph/{}/'.format(current_site, report.id)

    send_mail(
        mail_subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )

    return print('Success')