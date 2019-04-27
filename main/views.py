from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.sites.shortcuts import get_current_site
from main.models import Report
from main.charts import popular_time, popular_weekday
from main.tasks import spider_run


def index(request):
    return render(request, 'index.html', {})


class ReportView(View):
    def post(self, request):
        url = request.POST.get('url')
        email = request.POST.get('email')
        current_site = get_current_site(request).domain

        spider_run.delay(url, email, current_site)

        return redirect('/')


def graph(request, report_id):
    report = get_object_or_404(Report, id=int(report_id))
    date_time_list = [item.date_time for item in report.adsdatetimes.all()]

    chart1 = popular_time(date_time_list)
    chart2 = popular_weekday(date_time_list)

    context = {
        'chart1': chart1,
        'chart2': chart2,
    }

    return render(request, 'report.html', context)