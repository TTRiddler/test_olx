from highcharts import Highchart
from collections import Counter


def popular_time(date_time):
    times = []
    for item in date_time:
        time = round((int(item.strftime('%H')) * 60 + int(item.strftime('%M'))) / 60) #%H:%M в целое число с округлением
        times.append(time)
        
    times.sort()
    times_counters = dict(Counter(times))

    times_counters = [[key, value] for key, value in times_counters.items()]

    chart = Highchart()

    options = {
        'chart': {
            'renderTo': 'container1',
            'type': 'spline',
        },
        'title': {
            'text': 'Популярное время размещения'
        },
        'xAxis': {
            'title': {
                'text': 'Часы'
            },
            'min': 0,
            'max': 23,
            'categories': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        },
        'yAxis': {
            'title': {
                'text': 'Количество объявлений'
            },
        },
    }

    chart.set_dict_options(options)
    chart.add_data_set(times_counters, series_type='spline', name='Количество объявлений')

    return chart


def popular_weekday(date_time):
    weekdays = []
    for item in date_time:
        weekday = item.weekday()
        weekdays.append(weekday)
        
    weekdays.sort()
    weekdays_counters = dict(Counter(weekdays))

    weekdays_counters = [[key, value] for key, value in weekdays_counters.items()]

    chart = Highchart()

    options = {
        'chart': {
            'renderTo': 'container2',
            'type': 'spline',
        },
        'title': {
            'text': 'Популярный день недели'
        },
        'xAxis': {
            'title': {
                'text': 'День недели'
            },
            'min': 0,
            'max': 6,
            'categories': ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']
        },
        'yAxis': {
            'title': {
                'text': 'Количество объявлений'
            },
        },
    }

    chart.set_dict_options(options)
    chart.add_data_set(weekdays_counters, series_type='spline', name='Количество объявлений')

    return chart