'''
This script stores the bitcoin value in bitcoin.txt
This script uses coindesk api.
CoinDesk provides a simple API to make its Bitcoin Price Index (BPI) data programmatically available to others. 
You are free to use this API to include our data in any application or website as you see fit, 
as long as each page or app that uses it includes the text Powered by CoinDesk, linking to our price page
'''

import urllib,json
from datetime import datetime
from dateutil import tz
#If you don't have these dependencies you will have to get them
#sudo pip2 install python-dateutil
#sudo pip2 install datetime

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = urllib.urlopen(url)
data =json.loads(response.read())
utc_time_str =str(data['time']['updated'][:-4]).strip()
from_zone = tz.gettz('UTC')
to_zone = tz.tzlocal()

utc = datetime.strptime(utc_time_str, '%b %d, %Y %H:%M:%S')
utc = utc.replace(tzinfo=from_zone)
localtime = str(utc.astimezone(to_zone))
timestring = localtime.split(' ')[1].split('+')[0]

usdval=data['bpi']['USD']['rate'][:-2]

file = open('bitcoin.txt','w')
file.write("Time:"+timestring+'\n')
file.write('$'+usdval)
file.close()
