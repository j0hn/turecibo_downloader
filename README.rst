===================
TuRecibo Downloader
===================


.. image:: https://img.shields.io/pypi/v/turecibo_downloader.svg
        :target: https://pypi.python.org/pypi/turecibo_downloader

.. image:: https://img.shields.io/travis/gbourdin/turecibo_downloader.svg
        :target: https://travis-ci.org/gbourdin/turecibo_downloader

.. image:: https://readthedocs.org/projects/turecibo-downloader/badge/?version=latest
        :target: https://turecibo-downloader.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Downloads documents from turecibo.com as PDF
This has only been tested for Argentina.


* Free software: MIT license
* Documentation: https://turecibo-downloader.readthedocs.io.


Usage
--------
Install:
    pip install this folder

Run:
    ``$ turecibo_downloader by-hash HASH``
    ``$ turecibo_downloader by-inbox FOLDER COOKIE``

How to get the hashes:

1. Using chrome with DevTools open (F12 or Ctrl + J), log in to "turecibo.com"
2. Open the the document you want to download
3. Go to the network tab in DevTools and put "thumbnail" in the filters
4. You'll see a bunch or requests getting thumbnails for different pages, the format is similar to this
    ``https://api.nosconecta.com.ar/eform/thumbnail/b72b7a6053e0212e9f6d1707041acaddb72b7a6053e0212e9f6d1707041acadd?page=1``
5. From that url, you want everything after the last / and before the ?, so, this: ``b72b7a6053e0212e9f6d1707041acaddb72b7a6053e0212e9f6d1707041acadd``
6. That's your hash, now use it with the downloader
    ``$ turecibo_downloader by-hash b72b7a6053e0212e9f6d1707041acaddb72b7a6053e0212e9f6d1707041acadd``

How to cookie and folder:

1. Using chrome with DevTools open (F12 or Ctrl + J), log in to "turecibo.com"
2. Open any request and copy the cookie header. That's what you'll use as cookie parameter
3. Change the page on your inbox and you'll see a request to something like
    ``https://ar.turecibo.com/bandeja.php?apiendpoint=/folders/827/documents/available``
    your folder parameter is the number 827 in this case. Use that.
4. You have all you need, now use it with the downloader
    ``$ turecibo_downloader by-inbox 827 "PHPSESSID=cu03g93rhe9lk....``
5. ???
6. Profit.

Features
--------

* TODO

To Do
-----
* Release on pypi
* Add support for more countries
* Add tests, documentation, etc.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
