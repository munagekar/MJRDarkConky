import urllib,json
url = "https://query.yahooapis.com/v1/public/yql?format=json&q=select+title%2C+units.temperature%2C+item.forecast%0Afrom+weather.forecast%0Awhere+woeid+in+%28select+woeid+from+geo.places+where+text%3D%22Katraj%2C+India%22%29%0Aand+u+%3D+%27C%27%0Alimit+5%0A%7C%0Asort%28field%3D%22item.forecast.date%22%2C+descending%3D%22false%22%29%0A%3B"
response = urllib.urlopen(url)
data =json.loads(response.read())

file = open('conkyweather.txt','w')
for entryitem in ["day","code","high","low"]: 
	for i in range(4):
		file.write(data["query"]["results"]["channel"][i]['item']['forecast'][entryitem]+"\n")	
file.close()
