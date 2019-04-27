import re
import locale
from grab.spider import Spider, Task
from datetime import datetime


class MySpider(Spider):

    initial_urls = []

    def prepare(self):
        locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

        self.date_time = []

    def task_initial(self, grab, task):        
        pages_nmb = grab.doc.select('//a[@class="block br3 brc8 large tdnone lheight24"]')[-1].text()

        for i in range(int(pages_nmb)):
        # for i in range(2):
            url = '{}?page={}'.format(self.initial_urls[0], i+1)
            yield Task('page', url=url)

    def task_page(self, grab, task):
        ads_list = grab.doc.select('//a[@class="marginright5 link linkWithHash detailsLink"]')

        for elem in ads_list:
            yield Task('ad', url=elem.attr('href'))
    
    def task_ad(self, grab, task):
        date_time_info = grab.doc.select('//div[@class="offer-titlebox__details"]/em')

        for elem in date_time_info:
            text = elem.text()

            time = re.search(r'\d{2}:\d{2}', text)[0]
            date = re.search(r'\d{1,2} [а-я]+ \d{4}', text)[0]
            date_time = '{} {}'.format(date, time)

            self.date_time.append(datetime.strptime(date_time, '%d %B %Y %H:%M'))
