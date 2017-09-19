import urllib,json
url = "http://api.fixer.io/latest?base=USD&symbols=INR"
response = urllib.urlopen(url)
data =json.loads(response.read())

file = open('forex.txt','w')
file.write(str(data['rates']['INR'])[:-1])
file.close()
