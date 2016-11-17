# Python Wordpress API

[![Pypi][pypi-image]][pypi-url]
[![Updates][pyup-image]][pyup-url]


Simple python wrapper around the Wordpress REST API. Supports authentication using Basic Auth.

All endpoints for the following resources are available:

* Posts
* Media
* Post Types
* Taxonomies
* Categories
* Tags
* Users

These endpoints will be implemented soon:

* Post Revisions
* Pages
* Post Types
* Post Statuses
* Comments

Use the [official api documentation](http://v2.wp-api.org/reference) as reference for what is possible.

## Installation

```
pip install python_wpapi
```

## Usage

```
from python_wpapi import WpApi

api1 = WpApi('http://example.com') # No authentication. Public endpoints only
api2 = WpApi('http://example.com', user='User', password='pwd') # Basic Auth

posts = api1.get_posts()
new_post = api2.create_post(title='Foo', content='Bar')
```

## TODO

* Documentation
* OAuth authentication

## Tests

```
make test
```

* Free software: MIT licensea

[pypi-image]: https://img.shields.io/pypi/v/python_wpapi.svg 
[pypi-url]: https://pypi.python.org/pypi/python_wpapi
[pyup-image]: https://pyup.io/repos/github/Lobosque/python_wpapi/shield.svg 
[pyup-url]: https://pyup.io/repos/github/Lobosque/python_wpapi/ 
