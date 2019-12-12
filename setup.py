"""
Flask-SSPI
--------------

Provides SSPI authentication support for Flask applications

Links
`````

* `documentation <https://flask-sspi.readthedocs.org/en/latest/>`_
* `development version
  <http://github.com/mkomitee/flask-sspi/zipball/master#egg=Flask-SSPI-dev>`_

"""

from setuptools import setup

setup(name='Flask-SSPI',
      version='1.0.0',
      url='http://github.com/mkomitee/flask-sspi',
      license='BSD',
      author='Michael Komitee',
      author_email='mkomitee@gmail.com',
      description='SSPI authentication support for Flask',
      long_description=__doc__,
      py_modules=['flask_sspi'],
      zip_safe=False,
      include_package_data=True,
      package_data={'': ['LICENSE', 'AUTHORS']},
      platforms='any',
      install_requires=['Flask', 'sspi'],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Internet :: WWW/HTTP',
                   'Topic :: Software Development :: Libraries :: Python Modules'],
      test_suite='test_flask_sspi',
      tests_require=['mock'])
