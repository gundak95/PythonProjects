#This is my first actually really useful Python file for changing stuff in xml with Regex.
import xml.etree.cElementTree as ET
mytree = ET.parse("Sample.xml")
myroot=mytree.getroot()
print(myroot[1].attrib)
for x in myroot[1]:
    print(x.tag)
body=myroot[1]
for x in body[0]:
    print(x.tag)
div=body[0]
for x in div[0]:    
    print(x.tag)
p=div[1]
for x in p:
    print(x.text)
#doesn't work because it is still deeper nested: there is another div with another head and paragraph.
