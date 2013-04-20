from xml.dom import XHTML_NAMESPACE

from xml.sax.saxutils import XMLGenerator
from xml.sax.xmlreader import AttributesImpl
from StringIO import StringIO

def create_testdoc(_title, _content, _data_count):
    xml_doc = StringIO()
    try:
        xml_generator = XMLGenerator(xml_doc, 'UTF-8')
        start_element = lambda name, attrs: xml_generator.startElement(name, attrs)
        end_element =  lambda name: xml_generator.endElement(name)
        text = lambda value: xml_generator.characters(value)
        attrs = lambda values: AttributesImpl(values)
        empty_attrs = attrs({})
        xml_generator.startDocument()
        #xml_generator.notationDecl('html', '', '')
        start_element('html', attrs({'xmlns': XHTML_NAMESPACE}))
        start_element('head', empty_attrs)
        start_element('title', empty_attrs)
        text(_title)
        end_element('title')
        end_element('head')
        start_element('body', empty_attrs)
        start_element('h1', empty_attrs)
        text(_title)
        end_element('h1')
        start_element('p', empty_attrs)
        text(_content)
        end_element('p')
        for i in range(_data_count):
            start_element('p', {'data-i': unicode(_data_count)})
            text(unicode(_data_count))
            end_element('p')
        end_element('body')
        end_element('html')
        xml_generator.endDocument()
        return xml_doc.getvalue()
    finally:
        xml_doc.close()

