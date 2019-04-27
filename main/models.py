from django.db import models


class Report(models.Model):
    url = models.URLField(max_length=250)
    email = models.EmailField(max_length=250)

    def __str__(self):
        return '{}'.format(self.email)


class AdsDateTime(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='adsdatetimes')
    date_time = models.DateTimeField(null=True)
    
    def __str__(self):
        return ''