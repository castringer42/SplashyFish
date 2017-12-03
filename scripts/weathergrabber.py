# -*- coding: utf-8 -*-
import datetime
import time
import sys

from bs4 import BeautifulSoup
import requests

class WeatherGrabber():
    
   def GetData(self, date):
        
       date = datetime.date(*time.strptime(date, '%Y-%m-%d')[:3])
       
       year, month, day = date.timetuple()[:3]
    
       base_url = "http://www.wunderground.com/history/airport/BNA/{year}/{month}/{day}/DailyHistory.html"
    
       url = base_url.format(year=year, month=month, day=day)
    
       response = requests.get(url)
       if response.status_code != 200:
           print("An error occurred while getting data for {day}/{month}/{year}".format(
               year=year, month=month, day=day))
       else:
           html = response.content
    
           soup = BeautifulSoup(html, "html.parser")
           table = soup.find_all(attrs={'id': 'historyTable'})[0]      
           #print (table.tbody('tr')[17]('span')[5].text)
           avg_precip = float(table.tbody('tr')[17]('span')[5].text)
    
           #sys.stdout.write("{}-{}-{},{}\n".format(year, month, day, avg_precip))
           #sys.stdout.flush()
       return avg_precip


"""
if len(sys.argv) < 2:
   print("You need to provide a date in the format YYYY-MM-DD")
   sys.exit(1)

start_date = datetime.date(*time.strptime(sys.argv[1], '%Y-%m-%d')[:3])

if len(sys.argv) > 2:
   end_date = datetime.date(*time.strptime(sys.argv[2], '%Y-%m-%d')[:3])
else:
   # end yesterday
   end_date = datetime.date.today() - datetime.timedelta(1)


date = start_date
while date <= end_date:
   year, month, day = date.timetuple()[:3]

   base_url = "http://www.wunderground.com/history/airport/BNA/{year}/{month}/{day}/DailyHistory.html"

   url = base_url.format(year=year, month=month, day=day)

   response = requests.get(url)
   if response.status_code != 200:
       print("An error occurred while getting data for {day}/{month}/{year}".format(
           year=year, month=month, day=day))
       sys.exit(1)
   else:
       html = response.content

       soup = BeautifulSoup(html, "html.parser")
       table = soup.find_all(attrs={'id': 'historyTable'})[0]      
       #print (table.tbody('tr')[17]('span')[5].text)
       avg_precip = float(table.tbody('tr')[17]('span')[5].text)

       sys.stdout.write("{}-{}-{},{}\n".format(year, month, day, avg_precip))
       sys.stdout.flush()

   date = date + datetime.timedelta(1)
"""