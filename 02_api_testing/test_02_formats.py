import xml.etree.ElementTree as ET


def test_api_json(session, base_url):
    r = session.get(f'{base_url}/json')
    r_json = r.json()
    assert r_json['slideshow']['author'] == "Yours Truly"
    assert r_json['slideshow']['title'] == "Sample Slide Show"


def test_api_xml(session, base_url):
    r = session.get(f'{base_url}/xml')
    root = ET.fromstring(r.content)
    assert root.tag == "slideshow"
    assert root.attrib['author'] == "Yours Truly"
    assert root.attrib['title'] == "Sample Slide Show"
