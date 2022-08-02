import xml.etree.ElementTree as ET
data=ET.parse("simpleSample.xml")
root=data.getroot()
print(root.tag)

for x in root.iter("competition"):
    a=str(x.text)+"That was a very hard competition."
    x.text=str(a)
    x.set("updated","yes")
data.write("newSimpleSample.xml")

ET.SubElement(root[0],"medals")
for x in root.iter("medals"):
    b="This athlete has not previously won any medals."
    x.text=str(b)
data.write("newSimpleSample.xml")

#Now I just need to find out how I can iter over all to add the same subelement to all.