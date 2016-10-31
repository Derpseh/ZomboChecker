# Whee, lots of imports!
import xml.etree.ElementTree as ET
import time
import urllib2

# Gotta set my headers
Region = str(raw_input('Region Name: '))
headers = { 'User-Agent' : 'Zombie-Checker: Devved by valkynora@gmail.com'}
try:
	testReq = urllib2.Request('http://www.nationstates.net/cgi-bin/api.cgi?region=' + Region.replace(' ', '_') + '&q=nations', None, headers)
	html = urllib2.urlopen(testReq).read()
except:
	print "Region not found. Be sure to input the name of a region that actually exists"
	quit()

# Sanitize our founderless regions list a wee bit, 'cause at the moment, it's xml, and xml is gross.
print "Processing data..."
root = ET.fromstring(html)
for EVENT in root.iter('NATIONS'):
	NationString = EVENT.text
ZomboList = []
NationList = NationString.split(':')
counter = 1
for Nation in NationList:
	time.sleep(0.7)
	print 'Checking ' + str(counter) + ' of ' + str(len(NationList)) + '...'
	counter = counter + 1
	Req = urllib2.Request('http://www.nationstates.net/cgi-bin/api.cgi?nation=' + Nation + '&q=zombie', None, headers)
	html2 = urllib2.urlopen(Req).read()
	root2 = ET.fromstring(html2)
	for EVENT in root2.iter('ZACTION'):
		if EVENT.text == 'export':
			ZomboList = ZomboList + [Nation.replace('_', ' ')]
print ZomboList
with open('Zombos.txt', 'w') as myfile:
	for Nation in ZomboList:
		myfile.write(Nation + '\n')
