#This is my first actually really useful Python file for changing stuff in xml with Regex.

import xml.etree.ElementTree as ET
mytree=ET.parse("sample.xml")
myroot=mytree.getroot()
print(myroot)