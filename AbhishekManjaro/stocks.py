import urllib2
from bs4 import BeautifulSoup
import re

adds = ['http://m.moneycontrol.com/sensex/bse/sensex-live']
for add in adds:
	page = urllib2.urlopen(add)
	soup = BeautifulSoup(page,'lxml')
	val_tag=str(soup.find("span", {"id":'ind_c_close'}))
	change_tag=str(soup.find("span", {"id":'ind_chg'}))
	re1='.*?'	# Non-greedy match on filler
	re2='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1
	re3='.*>(.*)<'			#For change in the value

	rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)
	val_str= rg.search(val_tag).group(1)
	
	rg = re.compile(re3)
	change_str = rg.search(change_tag).group(1)
	change_num = float(change_str.split(' ')[0])
	if(change_num>=0):
		icon = 'bull'
	else:
		icon = 'bear'
	
	
file = open('stocks.txt','w')
file.write(val_str+'\n')
file.write(change_str+'\n')
file.write(icon)
file.close()
	
	




