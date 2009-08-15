import os
from setuptools import setup, find_packages

version = '0.1.0'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-paste-organizer',
    version=version,
    description="Manage 3rd party hosted pastes in one place. Allows easier team collaboration on multiple pastes by condensing them in one place.",
    long_description=read('README'),
    author='Thomas Schreiber',
    author_email='tom@insatsu.us',
    url='http://github.com/rizumu/django-writeboards/',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    keywords='django,writeboard,gist,dpaste,pastebins',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)