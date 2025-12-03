# pip3 install lxml --break-system-packages

from lxml import etree

xml_doc = etree.parse("001 Curriculum.xml")
xsd_doc = etree.parse("002 Curriculum.xsd")

schema = etree.XMLSchema(xsd_doc)

print(schema.validate(xml_doc))