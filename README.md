## Under Development


### about

bdpy3_web is a lightweight python3 [django](https://www.djangoproject.com) wrapper around [bdpy3](https://github.com/birkin/bdpy3), a python3 library for the [BorrowDirect](http://www.borrowdirect.org) api.

('Lightweight' meaning no database, no sessions, no templates, no static-files.)

It and the underlying library are about to replace an [older deprecated code](https://github.com/Brown-University-Library/bdpyweb_code) in production.


### usage api-v1 for exact-item request

sample script...

    # -*- coding: utf-8 -*-

    import os
    import requests


    ## settings
    API_URL = 'https://127.0.0.1/bdpy3_web_project_name/v1/'
    API_IDENTITY = os.environ['expected_identity']
    API_KEY = os.environ['expected_key']

    params = {
        'api_identity': API_IDENTITY,
        'api_authorization_code': API_KEY,
        'user_barcode': 'the_patron_barcode',
        'isbn': 'the_isbn'
        }
    r = requests.post( API_URL, data=params )
    print r.content.decode( 'utf-8' )

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


### usage api-v2 for bib-item request

sample script...

    # -*- coding: utf-8 -*-

    import os
    import requests


    ## settings
    API_URL = 'https://127.0.0.1/bdpy3_web_project_name/v2/bib_request/'
    API_IDENTITY = os.environ['expected_identity']
    API_KEY = os.environ['expected_key']

    params = {
        'api_identity': API_IDENTITY,
        'api_authorization_code': API_KEY,
        'user_barcode': 'the_patron_barcode',
        'title': 'the_title',
        'author': 'the_author',
        'year': 'the_year',
        }
    r = requests.post( API_URL, data=params )
    print r.content.decode( 'utf-8' )

    # on success, the json response...
    # {
    #   "request": {
    #     "bib_query": {
    #       "author": "the_author",
    #       "title": "the_title",
    #       "year": "the_year"
    #     },
    #     "date_time": "2017-10-24 10:43:01.527551"
    #   },
    #   "response": {
    #     "bd_api_response": {
    #       "RequestNumber": "BRO-11801540"
    #     },
    #     "elapsed_time": "0:00:09.392543",
    #     "interpreted_response": {
    #       "bd_confirmation_code": "BRO-12345678",
    #       "result": "requested"
    #     }
    #   }
    # }

    # on failure, the json response...
    # {
    #   "request": {
    #     "bib_query": {
    #       "author": "the_author",
    #       "title": "the_title",
    #       "year": "the_year"
    #     },
    #     "date_time": "2017-10-24 10:46:24.409191"
    #   },
    #   "response": {
    #     "bd_api_response": {
    #       "Problem": {
    #         "ErrorCode": "PUBRI003",
    #         "ErrorMessage": "No result"
    #       }
    #     },
    #     "elapsed_time": "0:00:08.281432",
    #     "interpreted_response": {
    #       "bd_confirmation_code": null,
    #       "result": "not_found"
    #     }
    #   }
    # }




#### notes

- code contact: birkin_diana@brown.edu

---
