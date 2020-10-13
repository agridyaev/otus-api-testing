import pytest

POSTS_MAX = 100


@pytest.mark.parametrize('post_id', [1, POSTS_MAX])
def test_get_positive(session, base_url, post_id):
    res = session.get(url=f'{base_url}/{post_id}')

    assert res.status_code == 200
    assert res.json()['id'] == post_id


@pytest.mark.parametrize('post_id', [-1, 0, POSTS_MAX + 1])
def test_get_negative(session, base_url, post_id):
    res = session.get(url=f'{base_url}/{post_id}')

    assert res.status_code == 404
    assert not res.json()


def test_create(session, base_url):
    title = 'foo'
    body = 'bar'
    payload = {'title': title, 'body': body, 'userId': 1}
    res = session.post(url=base_url, json=payload)

    assert res.status_code == 201
    j = res.json()
    assert j['id'] == POSTS_MAX + 1
    assert j['userId'] == 1
    assert j['title'] == title
    assert j['body'] == body


def test_update(session, base_url):
    post_id = 1
    title = 'foo'
    body = 'bar'
    payload = {'title': title, 'body': body, 'id': post_id, 'userId': 1}
    res = session.put(url=f'{base_url}/{post_id}', json=payload)

    assert res.status_code == 200
    res_json = res.json()
    assert res_json['title'] == title
    assert res_json['body'] == body


def test_delete(session, base_url):
    res = session.delete(url=f'{base_url}/1')

    assert res.status_code == 200
    assert not res.json()
