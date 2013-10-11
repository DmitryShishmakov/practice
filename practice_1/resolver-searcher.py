# Python 2.7

f = open('resolver.txt', 'r')

data = {}
for line in f:
	params = line.split(' ')
	data[params[1][:-1]] = params[0]

query = raw_input('Enter ip-address or domain for search: ')

if(data.has_key(query)):
	print 'Found: ' + data[query] + ' ' + query
else:
	notFound = True

	for key in data:
		if(query == data[key]):
			notFound = False
			print 'Found: ' + key + ' ' + data[key]

	if(notFound):
		print 'Error: data not found!'

f.close()
