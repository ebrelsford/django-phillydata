django-phillydata
==============

A set of Django apps for loading and storing data provided by or related to the
city of Philadelphia.


Usage
-----

Install using `pip <https://pypi.python.org/pypi/pip/1.4>`_, which should get 
any requirements, eg:

::

    pip install git+git://github.com/ebrelsford/django-phillydata@master

Change your Django settings to at least include phillydata:

::

    INSTALLED_APPS += (
        'phillydata',
    )

include any of the following that you will be using:

::

    INSTALLED_APPS += (
        'phillydata.availableproperties',
        'phillydata.citycouncil',
        'phillydata.landuse',
        'phillydata.li',
        'phillydata.licenses',
        'phillydata.opa',
        'phillydata.owners',
        'phillydata.parcels',
        'phillydata.taxaccounts',
        'phillydata.violations',
        'phillydata.waterdept',
        'phillydata.zoning',
    )

Then migrate using `South <http://south.readthedocs.org/en/latest/>`_.

For more details, see `v2v <https://github.com/ebrelsford/v2v>`_, the 
repository behind `Grounded in Philly <http://groundedinphilly.org/>`_.


Contributing
------------

Your pull requests are very welcome! Please follow the established code style.


License
-------

django-phillydata is released under the GNU `Affero General Public License, 
version 3 <http://www.gnu.org/licenses/agpl.html>`_.
