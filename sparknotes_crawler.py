from bs4 import BeautifulSoup
import urllib2, textwrap

number_of_sections=input('Please enter a value:')

output_text = open('out.txt','a')

for x in xrange(1,number_of_sections+1):
	print x

	url = "http://www.sparknotes.com/lit/pride/section%d.rhtml" % x
	 
	content = urllib2.urlopen(url).read()
	 
	soup = BeautifulSoup(content)
	 
	pretty = soup.prettify()

	studyGuideText = soup.find('div', {'class':'studyGuideText'})

	text = studyGuideText.get_text().encode('utf-8')
	
	output_text.write(text)


	# On Windows, utf-8-sig will allow the file to be read by Notepad.
	#with open('out.txt','w',encoding='utf-8-sig') as f:
	# f.write(soup.prettify())

output_text.close()
