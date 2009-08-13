from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name='django-writeboards',
    version=version,
    description="Manage 123.writeboard.com hosted writeboards in one place. Allows easier team collaboration on multiple writeboardsself.",
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
    keywords='writeboards,django'
    packages=[
        'writeboards',
    ],
    package_dir={'writeboards': 'writeboards'},
    zip_safe=False,
)