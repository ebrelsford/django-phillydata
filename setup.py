from setuptools import setup, find_packages
import os

import phillydata


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
]

setup(
    author="Eric Brelsford",
    author_email="eric@596acres.org",
    name='django-phillydata',
    version=phillydata.__version__,
    description=('A set of Django apps for loading and storing data regarding '
                 'the city of Philadelphia.'),
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='https://github.com/ebrelsford/django-phillydata/',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.3.1',
        'pyproj==1.9.3',
        'django-reversion==1.6.6',
        'django-reversion-compare==0.3.5',
    ],
    packages=find_packages(),
    include_package_data=True,
)
