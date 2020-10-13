import json
import xml.etree.ElementTree as ET


def test_file_json():
    with open('01_data_formats/example.json') as f:
        content = json.load(f)
    assert len(content) == 2
    for r in content:
        assert r["country"] == "Turkey"
        assert r["alpha_two_code"] == "TR"


def test_file_xml():
    tree = ET.parse('01_data_formats/example.xml')
    root = tree.getroot()
    assert root.tag == "bookstore"
    for child in root:
        assert child.tag == "book"
