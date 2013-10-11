# Python 2.7

f = open('resolver.txt', 'r')

data = {}
for line in f:
	params = line.split(' ')
	data[params[1][:-1]] = params[0]
	# print params[0] + ' ' + params[1] # print line

for key in data:
	print key + ' ' + data[key]

new = '\n' + raw_input('Enter new ip-address: ')
new += ' ' + raw_input('Enter new domain: ')

f.close()

f = open('resolver.txt', 'a')
f.write(new)
f.close()
