import xml.etree.ElementTree as ET
mytree = ET.parse("Sample.xml")
myroot=mytree.getroot()
text=myroot[1]
body=text[0]
div=body[0]
div2=div[1]
p=div2[1]

print(p.text)

#Ich weiß nicht, warum das nicht funktioniert. Es funktioniert für head, das erste child element von div2.
#Ich weiß außerdem nicht, ob das wirklich nützlich ist, wenn man die genaue Struktur der Daten schon kennen
#muss, um irgendetwas ansteuern zu können.