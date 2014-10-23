"""
Turns data from the OPA API into the relevant models.

Kind of a proxy/adapter for OPA data.

"""
import datetime
import logging
import re

import reversion

from .api import get_account_data, get_address_data
from .models import AccountOwner, BillingAccount
from ..owners.models import Owner
from ..utils import html_unescape


logger = logging.getLogger(__name__)

SALE_DATE_FORMAT = '%m/%d/%Y'

def json_date_as_datetime(json_date):
    """Parse date in .NET JSON format, eg /Date(1154970000000+0700)/"""
    # Get rid of annoying JSON date cruft
    json_date = re.sub('\/Date\(', '', json_date)
    json_date = re.sub('\)\/', '', json_date)

    # Watch for initial - sign
    negative = False
    if json_date[0] == '-':
        json_date = json_date[1:]
        negative = True

    # Grab timestamp, offset
    try:
        timestamp, offset = json_date.split('+')
        offset = int(offset)
    except ValueError:
        try:
            timestamp, offset = json_date.split('-')
            offset = -int(offset)
        except ValueError:
            timestamp = json_date
            offset = None

    ms = int(timestamp) * 1000
    if negative:
        ms = -ms
    if offset:
        # Convert offset to ms
        ms += offset * 60 * 60 * 10000

    # Return epoch + timestamp
    return datetime.datetime(1970, 1, 1) + datetime.timedelta(microseconds=ms)


def billing_account_kwargs(data):
    return {
        'external_id': data['account_number'],
    }


def get_assessment(valuation_history):
    if not valuation_history:
        return None
    most_recent = max(valuation_history, key=lambda entry: entry['certification_year'])
    return most_recent['market_value']


def billing_account_defaults(characteristics=None, sales_information=None,
                             valuation_history=None, defaults={}, **kwargs):
    defaults.update({
        'sale_date': json_date_as_datetime(sales_information['sales_date']),
        'land_area': characteristics['land_area'],

        # TODO NB: if 0, could indicate vacancy
        'improvement_area': characteristics['improvement_area'],

        # TODO NB: if starts with 'VAC LAND', could indicate vacancy
        'improvement_description': characteristics['improvement_description'],

        # TODO NB: if 0, could indicate publicly owned?
        'assessment': get_assessment(valuation_history),
    })
    return defaults


@reversion.create_revision()
def get_or_create_account_owner(ownership=None, **kwargs):
    # sorting owner names to keep internally consistent
    owner_name = ', '.join(sorted(ownership['owners']))
    owner_name = html_unescape(owner_name)

    account_owner, created = AccountOwner.objects.get_or_create(
        name=owner_name,
        defaults={ 'owner': Owner.objects.get_or_create(owner_name)[0], }
    )
    return account_owner


@reversion.create_revision()
def get_or_create_billing_account(data, account_owner):
    defaults = billing_account_defaults(defaults={'account_owner': account_owner,},
                                        **data)
    billing_account, created = BillingAccount.objects.get_or_create(
        defaults=defaults, **billing_account_kwargs(data))
    if not created:
        BillingAccount.objects.filter(pk=billing_account.pk).update(**defaults)
    return billing_account


def find_opa_details(address, brt_account=None):
    """Get or create a BillingAccount for the given address."""
    logger.debug('Getting OPA data for address "%s"' % address)

    # Attempt to get owner by address
    if address:
        data = get_address_data(address)

    # Attempt to get owner by BRT number
    if brt_account and not data:
        logger.debug('Getting OPA data for account "%s"' % brt_account)
        data = get_account_data(brt_account)

    if not data:
        raise Exception('Could not find OPA details for "%s"' % address)

    account_owner = get_or_create_account_owner(**data)
    return get_or_create_billing_account(data, account_owner)
