import xm.etree.ElementTree as ET

def parsefile(xml_file):
	tree=ET.parse(xml_file)
	root=tree.getroot()

	for person in root.findall('person'):
		name = person.find('name').text
		age = person.find('age').text
		city = person.find('city').text

		print("Name:", name)
		print("Age:", age)
		print("City:", city)


parsefile('file.xml')
