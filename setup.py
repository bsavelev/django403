# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
 
long_description = ""
 
setup(
    name='django403',
    version='0.0.1',
    description='Middleware for handle 403 HTTP',
    long_description=long_description,
    author='Ludwik Trammer',
    author_email='ludwik@gmail.com',
    url='http://code.google.com/p/django-tagging-autocomplete/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    #package_data={},
    #test_suite='tagging_autocomplete.tests.runtests.runtests'
) 
