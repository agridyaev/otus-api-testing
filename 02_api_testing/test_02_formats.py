import xml.etree.ElementTree as ET


def test_api_json(session):
    r = session.get('https://httpbin.org/json')
    r_json = r.json()
    assert r_json['slideshow']['author'] == "Yours Truly"
    assert r_json['slideshow']['title'] == "Sample Slide Show"


def test_api_xml(session):
    r = session.get('https://httpbin.org/xml')
    root = ET.fromstring(r.content)
    assert root.tag == "slideshow"
    assert root.attrib['author'] == "Yours Truly"
    assert root.attrib['title'] == "Sample Slide Show"
