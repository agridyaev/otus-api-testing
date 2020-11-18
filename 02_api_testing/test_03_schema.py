import json
from jsonschema import validate


def assert_valid_schema(data, schema_file):
    with open(schema_file) as f:
        schema = json.load(f)
    return validate(instance=data, schema=schema)


def test_get_post(session, base_url):
    res = session.get(url=f'{base_url}/1')
    assert_valid_schema(res.json(), 'schemas/post_schema.json')


def test_get_posts(session, base_url):
    res = session.get(url=base_url)
    assert_valid_schema(res.json(), 'schemas/posts_schema.json')
