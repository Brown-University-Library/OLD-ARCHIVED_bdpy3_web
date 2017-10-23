# -*- coding: utf-8 -*-

import datetime, json, logging, os, pprint, time
import requests
from bdpy3 import BorrowDirect
from bdpy3_web_app import settings_app


log = logging.getLogger(__name__)


class V2RequestBibCaller( object ):
    """ Contains functions for bdpy3 bib-request call. """

    def __init__( self ):
        self.defaults = {
            'API_URL_ROOT': settings_app.BDPY3_API_URL_ROOT,
            'API_KEY': settings_app.BDPY3_API_KEY,
            'UNIVERSITY_CODE': settings_app.BDPY3_UNIVERSITY_CODE,
            'PARTNERSHIP_ID': settings_app.BDPY3_PARTNERSHIP_ID,
            'PICKUP_LOCATION': settings_app.BDPY3_PICKUP_LOCATION,
            }
        log.debug( 'self.defaults, ```%s```' % pprint.pformat(self.defaults) )

    def request_bib( self, params ):
        """ Runs lookup; returns bdpy3 request-bib dct output.
            Called by views.v2_bib_request() """
        log.debug( 'params, ```%s```' % pprint.pformat(params) )
        start = datetime.datetime.now()
        bd = BorrowDirect( self.defaults )
        ( patron_barcode, title, author, year ) = ( params['patron_barcode'], params['title'], params['author'], params['year'] )
        bd.run_request_bib_item( patron_barcode, title, [author], year )
        log.debug( 'bd_api result, ```%s```' % pprint.pformat(bd.request_result) )
        interpreted_response = self.interpret_response( bd.request_result )
        response_dct = self.prepare_response_dct( start, title, author, year, bd.request_result, interpreted_response )
        return response_dct

    def interpret_response( self, bd_api_result_dct ):
        """ Prepares easyBorrow convenience response.
            Called by request_bib() """
        if '''"ErrorMessage": "No result"''' in json.dumps( bd_api_result_dct ):
            interpreted_response = { 'result': 'not_found', 'bd_confirmation_code': None }
        log.debug( 'interpreted_response, ```%s```' % interpreted_response )
        return interpreted_response

    def prepare_response_dct( self, start, title, author, year, bd_api_result_dct, interpreted_response_dct ):
        """ Formats response (which will be json).
            Called by request_bib() """
        resp_dct = {
            'request': {
                'datetime_request': str( start ),
                'bib_query': { 'title': title, 'author': author, 'year': year }
            },
            'response': {
                'datetime_response': str( datetime.datetime.now() ),
                'bd_api_response': bd_api_result_dct,
                'interpreted_response': interpreted_response_dct
            }
        }
        log.debug( 'resp_dct, ```%s```' % pprint.pformat(resp_dct) )
        return resp_dct

    ## end class V2RequestBibCaller()
