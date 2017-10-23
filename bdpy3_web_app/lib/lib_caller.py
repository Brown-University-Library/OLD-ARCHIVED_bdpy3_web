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
        # log.debug( 'self.defaults, ```%s```' % pprint.pformat(self.defaults) )
        start = datetime.datetime.now()
        bd = BorrowDirect( self.defaults )
        ( patron_barcode, title, author, year ) = ( params['patron_barcode'], params['title'], params['author'], params['year'] )
        bd.run_request_bib_item( patron_barcode, title, [author], year )
        log.debug( 'bd_api result, ```%s```' % pprint.pformat(bd.request_result) )
        response_dct = self.prepare_response_dct( start, title, author, year, bd.request_result )
        return response_dct

    def prepare_response_dct( self, start, title, author, year, bd_api_result_dct ):
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
                'interpreted_response': 'coming'
            }
        }
        log.debug( 'resp_dct, ```%s```' % pprint.pformat(resp_dct) )
        return resp_dct

    ## end class LibCaller()


class FormHelper( object ):
    """ Not currently in-use. """

    def __init__( self, logger ):
        """ Helper functions for app->handle_form() """
        log.debug( 'form_helper initialized' )
        self.defaults = {
            'API_URL_ROOT': settings_app.BDPY3_API_URL_ROOT,
            'API_KEY': settings_app.BDPY3_API_KEY,
            'UNIVERSITY_CODE': settings_app.BDPY3_UNIVERSITY_CODE,
            'PARTNERSHIP_ID': settings_app.BDPY3_PARTNERSHIP_ID,
            'PICKUP_LOCATION': settings_app.BDPY3_PICKUP_LOCATION,
            }

    ## main functions

    def run_search( self, isbn ):
        """ Hits test-server with search & returns output.
            Called by bdpyweb_app.handle_form_post() """
        bd = BorrowDirect( self.defaults )
        bd.run_search( self.defaults['PATRON_BARCODE'], 'ISBN', isbn )
        bdpy3_result = bd.search_result
        if bdpy3_result.get( 'Item', None ) and bdpy3_result['Item'].get( 'AuthorizationId', None ):
            bdpy3_result['Item']['AuthorizationId'] = '(hidden)'
        return bdpy3_result

    def run_request( self, isbn ):
        """ Hits test-server with request & returns output.
            Called by bdpyweb_app.handle_form_post() """
        time.sleep( 1 )
        bd = BorrowDirect( self.defaults )
        bd.run_request_item( self.defaults['PATRON_BARCODE'], 'ISBN', isbn )
        bdpy3_result = bd.request_result
        return bdpy3_result

    def hit_availability_api( self, isbn ):
        """ Hits hit_availability_api for holdings data.
            Called by bdpyweb_app.handle_form_post() """
        url = '%s/%s/' % ( self.defaults['AVAILABILITY_API_URL_ROOT'], isbn )
        r = requests.get( url )
        dct = r.json()
        items = dct['items']
        for item in items:
            for key in ['is_available', 'requestable', 'barcode', 'callnumber']:
                del item[key]
        return_dct = {
            'title': dct.get( 'title', None ),
            'items': items }
        return return_dct

    def build_response_jsn( self, isbn, search_result, request_result, availability_api_data, start_time ):
        """ Prepares response data.
            Called by bdpyweb_app.handle_form_post() """
        end_time = datetime.datetime.now()
        response_dct = {
            'request': { 'datetime': unicode(start_time), 'isbn': isbn },
            'response': {
                'availability_api_data': availability_api_data,
                'bd_api_testserver_search_result': search_result,
                'bd_api_testserver_request_result': request_result,
                'time_taken': unicode( end_time - start_time ) }
                }
        log.debug( 'response_dct, `%s`' % pprint.pformat(response_dct) )
        return json.dumps( response_dct, sort_keys=True, indent=4 )

    # end class FormHelper
