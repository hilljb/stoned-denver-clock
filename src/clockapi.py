#!/usr/bin/python

from __future__ import print_function

import requests
from requests_oauthlib import OAuth1

from urlparse import urlparse, urlunparse
from urllib import urlencode
from urllib import __version__ as urllib_version 

import messages

# keys are in a dict in credentials.py, included in .gitignore
import credentials


def post(msg=None):
    """
    Post a status update.
    """
    user_agent = 'Python-urllib/%s' % urllib_version
    url = 'https://api.twitter.com/1.1/statuses/update.json'
    oauth = OAuth1(
        credentials.credentials['consumer_key'],
        credentials.credentials['consumer_secret'],
        credentials.credentials['access_token_key'],
        credentials.credentials['access_token_secret'])
    parameters = {
        'lat': '39.748114',
        'long': '-104.995639'
    }

    # Form the status
    if msg:
        parameters['status'] = msg
    else:
        parameters['status'] = messages.make_message()

    # Set up the request components
    (scheme, netloc, path, params, query, fragment) = urlparse(url)

    # Encode the parameters
    encoded_params = urlencode(
        dict(
            [(k, str(v).encode('utf-8')) for k, v in list(parameters.items())]
        )
    )

    # Form the URL
    url = urlunparse((scheme, netloc, path, params, encoded_params, fragment))

    # Make the request
    resp = requests.post(url, auth=oauth)

