## Under Development


#### about

bdpy3_web is a lightweight python3 [django](https://www.djangoproject.com) wrapper around [bdpy3](https://github.com/birkin/bdpy3), a python3 library for the [BorrowDirect](http://www.borrowdirect.org) api.

('Lightweight' meaning no database, no sessions, no templates, no static-files.)

It's still under development. It and the underlying library are about to replace older versions of the code in production.


#### usage

sample script...

    # -*- coding: utf-8 -*-

    import os
    import requests


    ## settings
    URL = os.environ['bdpyweb_flask_api_url']
    API_IDENTITY = os.environ['bdpyweb_flask_api_identity']
    API_KEY = os.environ['bdpyweb_flask_api_auth_key']

    params = {
        'api_identity': API_IDENTITY,
        'api_authorization_code': API_KEY,
        'user_barcode': 'the_patron_barcode',
        'isbn': 'the_isbn'
        }
    r = requests.post( URL, data=params )
    print r.content

    # on success, the json response...
    # {
    #   "bd_confirmation_code": "BRO-12345678",
    #   "found": true,
    #   "requestable": true,
    #   "search_result": "SUCCESS"
    # }

    # on failure, the json response...
    # {
    #   "bd_confirmation_code": null,
    #   "found": false,
    #   "requestable": false,
    #   "search_result": "FAILURE"
    # }


#### notes

- code contact: birkin_diana@brown.edu

---
