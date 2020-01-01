import json
import time
import http.client
import urllib.parse

import dateutil.tz

from paste import config


def get(alias):
    # connect to API
    url = urllib.parse.urlparse(config.store)

    if url.scheme == 'https':
        conn = http.client.HTTPSConnection(url.netloc)
    else:
        conn = http.client.HTTPConnection(url.netloc)

    # request given alias
    conn.request('GET', url.path.rstrip('/') + '/store/paste/' + alias)

    # get response
    response = conn.getresponse()

    # check for 404
    if response.status == 404:
        raise KeyError(alias)

    # get metadata
    name = response.getheader('Content-Filename')
    date = datetime.datetime.strptime(response.getheader('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z').replace(tzinfo=datetime.timezone.utc).astimezone(dateutil.tz.gettz(config.timezone))
    expire = datetime.datetime.strptime(response.getheader('Expires'), '%a, %d %b %Y %H:%M:%S %Z').replace(tzinfo=datetime.timezone.utc).astimezone(dateutil.tz.gettz(config.timezone))
    language = response.getheader('Content-Type')

    # store the code
    code = response.read().decode('utf-8')

    return name, date, expire, language, code


def put(alias, name, language, code):
    if isinstance(code, str):
        code = code.encode('utf-8')

    # connect to API
    url = urllib.parse.urlparse(config.store)

    if url.scheme == 'https':
        conn = http.client.HTTPSConnection(url.netloc)
    else:
        conn = http.client.HTTPConnection(url.netloc)

    # determine if this is a put or a post
    if alias:
        method = 'PUT'
    else:
        method = 'POST'

    # make a metadata request
    conn.request(method, url.path.rstrip('/') + '/api/paste/' + alias, headers={'Content-Type': 'application/json'}, body=json.dumps({'filename': name, 'size': len(code), 'type': language, 'expire': time.time() + config.interval, 'locked': True}).encode('utf-8'))

    # get response
    response = conn.getresponse()

    # load data response
    data = json.loads(response.read().decode('utf-8'))

    # note bad requests - existing alias, bad name, and unknown error
    if response.status == 403:
        raise KeyError(alias)
    elif response.status == 404:
        raise NameError('alias ' + repr(alias) + ' invalid')
    elif response.status != 201:
        raise RuntimeError('failed to make alias: ' + repr(alias))

    # make a data request
    conn.request('PUT', url.path.rstrip('/') + '/store/paste/' + data['alias'], body=code)

    # get response
    response = conn.getresponse()
    response.read()

    # note bad requests
    if response.status != 204:
        raise RuntimeError('failed to make alias: ' + repr(alias))

    return data['alias']
