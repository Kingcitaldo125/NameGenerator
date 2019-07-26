import urllib.request
import urllib.parse

def randRange(amount,min,max):
	"""
	Return a list of random numbers with length of 'amount' and
	between the range of 'min' and 'max'
	"""
	data = {}
	data['num'] = str(amount)
	data['min'] = str(min)
	data['max'] = str(max % 10000)
	data['col'] = "1"
	data['base'] = "10"
	data['format'] = "plain"
	data['rnd'] = "new"

	vals = urllib.parse.urlencode(data)
	url = "https://www.random.org/integers/"
	furl = url + '?' + vals

	#print("Opening...")
	data = ''
	dataList = []
	with urllib.request.urlopen(furl) as dat:
		data = str(dat.read().decode("utf-8"))
		for d in data.split("\n"):
			if d != "":
				dataList.append(d)
	
	return dataList

