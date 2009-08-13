from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name='django-writeboards',
    version=version,
    description="Manage 123.writeboard.com hosted writeboards in one place. Allows easier team collaboration on multiple writeboardsself.",
    long_description=read('README'),
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords='writeboards,django'
    author='Thomas Schreiber',
    author_email='tom@insatsu.us',
    url='http://github.com/rizumu/django-writeboards',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)