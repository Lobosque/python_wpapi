#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_python_wpapi
----------------------------------

Tests for `python_wpapi` module.
"""

import pytest

from mock import patch
from mock import Mock
from python_wpapi import python_wpapi
from python_wpapi import errors


@pytest.fixture
def api():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')
    return python_wpapi.WpApi('http://base.url')


def test_strip_slash():
    """Verifies that the same base_url is generated if
    a trailing slash is added or not.
    """
    api1 = python_wpapi.WpApi('http://base.url')
    api2 = python_wpapi.WpApi('http://base.url/')
    assert api1.base_url == api2.base_url

def test_auth():
    """Check the possible self.auth combinations.
    """
    api1 = python_wpapi.WpApi('http://base.url')
    api2 = python_wpapi.WpApi('http://base.url', user='User')
    api3 = python_wpapi.WpApi('http://base.url', user='User', password='Password')
    assert api1.auth == None
    assert api2.auth == ('User', None)
    assert api3.auth == ('User', 'Password')

@patch.object(python_wpapi.WpApi, '_request')
def test_get_posts(mock, api):
    api.get_posts()
    mock.assert_called_with('http://base.url/wp-json/wp/v2/posts')

@patch.object(python_wpapi.WpApi, '_request')
def test_get_post(mock, api):
    api.get_post(3)
    mock.assert_called_with('http://base.url/wp-json/wp/v2/posts/3',
        context='view')

@patch.object(python_wpapi.WpApi, '_request')
def test_create_post(mock, api):
    api.create_post(title='Title Here', content='Content Here')
    mock.assert_called_with('http://base.url/wp-json/wp/v2/posts',
        method='POST', title='Title Here', content='Content Here')

@patch.object(python_wpapi.WpApi, '_request')
def test_update_post(mock, api):
    api.update_post(id=5, title='Updated')
    mock.assert_called_with('http://base.url/wp-json/wp/v2/posts/5',
        method='POST', title='Updated')

@patch.object(python_wpapi.WpApi, '_request')
def test_delete_post(mock, api):
    api.delete_post(28)
    mock.assert_called_with('http://base.url/wp-json/wp/v2/posts/28',
        force=False,
        method='DELETE')

@patch.object(python_wpapi.WpApi, '_request')
def test_get_medias(mock, api):
    api.get_medias()
    mock.assert_called_with('http://base.url/wp-json/wp/v2/media')

@patch.object(python_wpapi.WpApi, '_request')
def test_get_media(mock, api):
    api.get_media(5)
    mock.assert_called_with('http://base.url/wp-json/wp/v2/media/5',
        context='view')

@patch.object(python_wpapi.WpApi, '_request')
def test_create_media(mock, api):
    api.create_media(filename='file.png',
        content_type='image/png',
        file_data=b'123')
    expected_headers = {'Content-Disposition': 'attachment; filename="file.png"'}
    expected_files = {'file': ('file.png', b'123', 'image/png',
        {'Expires': '0'})}
    mock.assert_called_with('http://base.url/wp-json/wp/v2/media',
        method='POST',
        headers=expected_headers,
        files=expected_files)

@patch.object(python_wpapi.WpApi, '_request')
def test_update_media(mock, api):
    api.update_media(6, email='john@smith')
    mock.assert_called_with('http://base.url/wp-json/wp/v2/media/6',
        method='POST',
        email='john@smith')

@patch.object(python_wpapi.WpApi, '_request')
def test_delete_media(mock, api):
    api.delete_media(7)
    mock.assert_called_with('http://base.url/wp-json/wp/v2/media/7',
        force=False,
        method='DELETE')

@patch.object(python_wpapi.WpApi, '_request')
def test_get_users(mock, api):
    api.get_users()
    mock.assert_called_with('http://base.url/wp-json/wp/v2/users')

@patch.object(python_wpapi.WpApi, '_request')
def test_get_user(mock, api):
    res = api.get_user(1)
    mock.assert_called_with('http://base.url/wp-json/wp/v2/users/1',
        context='view')

@patch.object(python_wpapi.WpApi, '_request')
def test_create_user(mock, api):
    api.create_user(username='johndoe', email='john@doe', password='123')
    mock.assert_called_with('http://base.url/wp-json/wp/v2/users',
        method='POST',
        username='johndoe',
        email='john@doe',
        password='123')

@patch.object(python_wpapi.WpApi, '_request')
def test_update_user(mock, api):
    api.update_user(2, email='john@smith')
    mock.assert_called_with('http://base.url/wp-json/wp/v2/users/2',
        method='POST',
        email='john@smith')

@patch.object(python_wpapi.WpApi, '_request')
def test_delete_user(mock, api):
    api.delete_user(3)
    mock.assert_called_with('http://base.url/wp-json/wp/v2/users/3',
        force=True,
        method='DELETE')

@patch.object(python_wpapi.WpApi, '_request')
def test_get_taxonomies(mock, api):
    api.get_taxonomies()
    mock.assert_called_with('http://base.url/wp-json/wp/v2/taxonomies', type=None)

    api.get_taxonomies(type='slug')
    mock.assert_called_with('http://base.url/wp-json/wp/v2/taxonomies', type='slug')

@patch.object(python_wpapi.WpApi, '_request')
def test_get_taxonomy(mock, api):
    api.get_taxonomy('slug')
    mock.assert_called_with('http://base.url/wp-json/wp/v2/taxonomies/slug')

@patch.object(python_wpapi.WpApi, '_request')
def test_get_categories(mock, api):
    api.get_categories()
    mock.assert_called_with('http://base.url/wp-json/wp/v2/categories')

@patch.object(python_wpapi.WpApi, '_request')
def test_get_category(mock, api):
    api.get_category(43)
    mock.assert_called_with('http://base.url/wp-json/wp/v2/categories/43',
        context='view')

@patch.object(python_wpapi.WpApi, '_request')
def test_create_category(mock, api):
    api.create_category(name='Category Name')
    mock.assert_called_with('http://base.url/wp-json/wp/v2/categories',
        method='POST',
        name='Category Name')

@patch.object(python_wpapi.WpApi, '_request')
def test_update_category(mock, api):
    api.update_category(44, description='desc')
    mock.assert_called_with('http://base.url/wp-json/wp/v2/categories/44',
        method='POST',
        description='desc')

@patch.object(python_wpapi.WpApi, '_request')
def test_delete_category(mock, api):
    api.delete_category(45)
    mock.assert_called_with('http://base.url/wp-json/wp/v2/categories/45',
        force=True,
        method='DELETE')

@patch.object(python_wpapi.WpApi, '_request')
def test_get_tags(mock, api):
    api.get_tags()
    mock.assert_called_with('http://base.url/wp-json/wp/v2/tags')

@patch.object(python_wpapi.WpApi, '_request')
def test_get_tag(mock, api):
    api.get_tag(19)
    mock.assert_called_with('http://base.url/wp-json/wp/v2/tags/19',
        context='view')

@patch.object(python_wpapi.WpApi, '_request')
def test_create_tag(mock, api):
    api.create_tag(name='Category Name')
    mock.assert_called_with('http://base.url/wp-json/wp/v2/tags',
        method='POST',
        name='Category Name')

@patch.object(python_wpapi.WpApi, '_request')
def test_update_tag(mock, api):
    api.update_tag(20, description='desc')
    mock.assert_called_with('http://base.url/wp-json/wp/v2/tags/20',
        method='POST',
        description='desc')

@patch.object(python_wpapi.WpApi, '_request')
def test_delete_tag(mock, api):
    api.delete_tag(21)
    mock.assert_called_with('http://base.url/wp-json/wp/v2/tags/21',
        force=True,
        method='DELETE')

@patch.object(python_wpapi.requests, 'request')
def test__request_get(mock, api):
    mock.return_value.json.return_value = {}
    mock.return_value.status_code = 200

    api._request('endpoint', arg1='value')
    mock.assert_called_with('GET',
        'endpoint',
        auth=api.auth,
        params={'arg1': 'value'},
        json=None,
        files=None,
        headers={'Content-Length': '0'}
    )

@patch.object(python_wpapi.requests, 'request')
def test__request_post(mock, api):
    mock.return_value.json.return_value = {}
    mock.return_value.status_code = 200

    api._request('endpoint', method='POST', arg1='value',
        headers={'header1': 'header2'})
    mock.assert_called_with('POST',
        'endpoint',
        auth=api.auth,
        params={},
        json={'arg1': 'value'},
        files=None,
        headers={'header1': 'header2'}
    )

@patch.object(python_wpapi.requests, 'request')
def test__request_400(mock, api):
    mock.return_value.json.return_value = {}
    mock.return_value.status_code = 400
    with pytest.raises(errors.BadRequestWpApiError) as e:
        api._request('endpoint')
        assert e.status_code == 400

@patch.object(python_wpapi.requests, 'request')
def test__request_401(mock, api):
    mock.return_value.json.return_value = {}
    mock.return_value.status_code = 401
    with pytest.raises(errors.UnauthorizedWpApiError) as e:
        api._request('endpoint2')
        assert e.status_code == 401

@patch.object(python_wpapi.requests, 'request')
def test__request_403(mock, api):
    mock.return_value.json.return_value = {}
    mock.return_value.status_code = 403
    with pytest.raises(errors.ForbiddenWpApiError) as e:
        api._request('endpoint3')
        assert e.status_code == 403

@patch.object(python_wpapi.requests, 'request')
def test__request_404(mock, api):
    mock.return_value.json.return_value = {}
    mock.return_value.status_code = 404
    with pytest.raises(errors.NotFoundWpApiError) as e:
        api._request('endpoint4')
        assert e.status_code == 404

@patch.object(python_wpapi.requests, 'request')
def test__request_500(mock, api):
    mock.return_value.json.return_value = {}
    mock.return_value.status_code = 500
    with pytest.raises(errors.InternalErrorWpApiError) as e:
        api._request('endpoint4')
        assert e.status_code == 500

@patch.object(python_wpapi.requests, 'request')
def test__request_generic(mock, api):
    mock.return_value.json.return_value = {}
    mock.return_value.status_code = 561
    with pytest.raises(errors.WpApiError) as e:
        api._request('endpoint4')
        assert e.status_code == 561
