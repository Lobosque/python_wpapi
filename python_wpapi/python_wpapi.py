# -*- coding: utf-8 -*-
import requests
from python_wpapi.errors import WpApiError


class WpApi():

    def __init__(self, base_url, user=None, password=None):
        self.auth = None
        if user:
            self.auth = (user, password)
        self.base_url = base_url.strip('/') + '/wp-json/wp/v2'

    def _request(self, endpoint, method='GET', headers={}, **kwargs):
        data = {}
        params = {}
        if method == 'GET':
            params = kwargs
        else:
            data = kwargs

        response = requests.request(method,
            endpoint,
            auth=self.auth,
            params=params,
            json=data,
            headers=headers
        )
        if not response.status_code // 100 == 2:
            error = WpApiError.factory(response)
            raise error
        return response.json()

    def get_posts(self):
        endpoint = '{}/posts'.format(self.base_url)
        return self._request(endpoint)

    def get_post(self, id):
        endpoint = '{}/posts/{}'.format(self.base_url, id)
        return self._request(endpoint)
    
    def create_post(self, **data):
        endpoint = '{}/posts'.format(self.base_url)
        return self._request(endpoint, method='POST', **data)

    def update_post(self, id, **data):
        endpoint = '{}/posts/{}'.format(self.base_url, id)
        return self._request(endpoint, method='POST', **data)

    def get_medias(self):
        endpoint = '{}/media'.format(self.base_url)
        return self._request(endpoint)

    def get_media(self, id):
        endpoint = '{}/media/{}'.format(self.base_url, id)
        return self._request(endpoint)
    
    def get_users(self):
        endpoint = '{}/users'.format(self.base_url)
        return self._request(endpoint)

    def get_user(self, id):
        endpoint = '{}/users/{}'.format(self.base_url, id)
        return self._request(endpoint)

    def get_taxonomies(self, type=None):
        endpoint = '{}/taxonomies'.format(self.base_url)
        return self._request(endpoint, type=type)

    def get_taxonomy(self, slug):
        endpoint = '{}/taxonomies/{}'.format(self.base_url, slug)
        return self._request(endpoint)
