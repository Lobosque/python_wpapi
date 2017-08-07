# -*- coding: utf-8 -*-
import requests
from python_wpapi.errors import WpApiError


class WpApi():

    def __init__(self, base_url, user=None, password=None):
        self.auth = None
        if user:
            self.auth = (user, password)
        self.base_url = base_url.strip('/') + '/wp-json/wp/v2'

    def _request(self, endpoint, method='GET', files=None, headers={}, **kwargs):
        params = {}
        if method == 'GET':
            params = kwargs
            data = None
            headers = {'Content-Length': '0'}
        else:
            data = kwargs

        response = requests.request(method,
            endpoint,
            auth=self.auth,
            params=params,
            json=data,
            headers=headers,
            files=files
        )
        if not response.status_code // 100 == 2:
            error = WpApiError.factory(response)
            raise error
        return response.json()

    def get_posts(self):
        endpoint = '{}/posts'.format(self.base_url)
        return self._request(endpoint)

    def get_post(self, id, context='view'):
        endpoint = '{}/posts/{}'.format(self.base_url, id)
        return self._request(endpoint, context=context)
    
    def create_post(self, **data):
        endpoint = '{}/posts'.format(self.base_url)
        return self._request(endpoint, method='POST', **data)

    def update_post(self, id, **data):
        endpoint = '{}/posts/{}'.format(self.base_url, id)
        return self._request(endpoint, method='POST', **data)

    def delete_post(self, id, force=False):
        endpoint = '{}/posts/{}'.format(self.base_url, id)
        return self._request(endpoint, method='DELETE', force=force)

    def get_medias(self):
        endpoint = '{}/media'.format(self.base_url)
        return self._request(endpoint)

    def get_media(self, id, context='view'):
        endpoint = '{}/media/{}'.format(self.base_url, id)
        return self._request(endpoint, context=context)

    def create_media(self, filename, content_type, file_data, **data):
        headers = {'Content-Disposition': 'attachment; filename="{}"'.format(filename)}
        files = {'file': (filename, file_data, content_type, {'Expires': '0'})}
        endpoint = '{}/media'.format(self.base_url)
        return self._request(endpoint, method='POST',
            headers=headers, files=files, **data)

    def update_media(self, id, **data):
        endpoint = '{}/media/{}'.format(self.base_url, id)
        return self._request(endpoint, method='POST', **data)

    def delete_media(self, id, force=False):
        endpoint = '{}/media/{}'.format(self.base_url, id)
        return self._request(endpoint, method='DELETE', force=force)

    def get_users(self):
        endpoint = '{}/users'.format(self.base_url)
        return self._request(endpoint)

    def get_user(self, id, context='view'):
        endpoint = '{}/users/{}'.format(self.base_url, id)
        return self._request(endpoint, context=context)

    def create_user(self, username, email, password, **data):
        endpoint = '{}/users'.format(self.base_url)
        return self._request(endpoint, method='POST',
            username=username, email=email, password=password, **data)

    def update_user(self, id, **data):
        endpoint = '{}/users/{}'.format(self.base_url, id)
        return self._request(endpoint, method='POST', **data)

    def delete_user(self, id):
        endpoint = '{}/users/{}'.format(self.base_url, id)
        return self._request(endpoint, method='DELETE', force=True)

    def get_taxonomies(self, type=None):
        endpoint = '{}/taxonomies'.format(self.base_url)
        return self._request(endpoint, type=type)

    def get_taxonomy(self, slug):
        endpoint = '{}/taxonomies/{}'.format(self.base_url, slug)
        return self._request(endpoint)

    def get_categories(self):
        endpoint = '{}/categories'.format(self.base_url)
        return self._request(endpoint)

    def get_category(self, id, context='view'):
        endpoint = '{}/categories/{}'.format(self.base_url, id)
        return self._request(endpoint, context=context)

    def create_category(self, name, **data):
        endpoint = '{}/categories'.format(self.base_url)
        return self._request(endpoint, method='POST', name=name, **data)

    def update_category(self, id, **data):
        endpoint = '{}/categories/{}'.format(self.base_url, id)
        return self._request(endpoint, method='POST', **data)

    def delete_category(self, id):
        endpoint = '{}/categories/{}'.format(self.base_url, id)
        return self._request(endpoint, method='DELETE', force=True)

    def get_tags(self):
        endpoint = '{}/tags'.format(self.base_url)
        return self._request(endpoint)

    def get_tag(self, id, context='view'):
        endpoint = '{}/tags/{}'.format(self.base_url, id)
        return self._request(endpoint, context=context)

    def create_tag(self, name, **data):
        endpoint = '{}/tags'.format(self.base_url)
        return self._request(endpoint, method='POST', name=name, **data)

    def update_tag(self, id, **data):
        endpoint = '{}/tags/{}'.format(self.base_url, id)
        return self._request(endpoint, method='POST', **data)

    def delete_tag(self, id):
        endpoint = '{}/tags/{}'.format(self.base_url, id)
        return self._request(endpoint, method='DELETE', force=True)
