13Dataontheweb.py
XML eXtensible Markup Language
works like html <>
<people> </people> = elements/nodes
XML Basics
-start tag, end tag, text content, attribute, self closing tag
XML Schema
validate or no validation = the act of verifing that the data is in the right
format.
XSD XML Schema
xs: elements
xs: sequence
xs: complexType
XSD Contraints
Parsing Example
import xlm.etree.ElementTree as eT
data = '''<person>
    <name>Chuck</name>
    <phone type = "intl">
        +1 734 303 4456
    </phone>
    <email hide = "yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:'), tree.find('email').get('hide'))

#xml2.py
