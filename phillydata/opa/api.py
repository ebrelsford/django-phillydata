import json
import logging
from urllib import urlencode
from urllib2 import quote, urlopen, URLError

logger = logging.getLogger(__name__)


BASE_URL = 'http://api.phila.gov/opa/v1.0/'
ADDRESS_ENDPOINT = 'address/'
ACCOUNT_ENDPOINT = 'account/'

params = {
    'format': 'json',
}

def get_address_data(address):
    if not address:
        raise ValueError('address must not be None')
    try:
        url = BASE_URL + ADDRESS_ENDPOINT + quote(address) + '/?' + urlencode(params)
        data = json.load(urlopen(url, None, 30))['data']
        return data['property']
    except KeyError:
        logger.debug(('Could not find unique property in response for %s. '
                      'Trying by account number') % address)

        # Try to find a matching property in the response's properties
        if 'properties' in data:
            for prop in data['properties']:
                if prop['full_address'].lower() == address.lower():
                    return prop

        logger.debug('Could not find property by account number, either.')
        return None
    except URLError:
        logger.exception('Exception while querying OPA API with URL "%s"' %
                         url)


def get_account_data(account):
    try:
        url = BASE_URL + ACCOUNT_ENDPOINT + account + '?' + urlencode(params)
        data = json.load(urlopen(url))['data']
        return data['property']
    except Exception:
        logger.exception('Exception while getting OPA data for account %s'
                         % str(account))
        return None
