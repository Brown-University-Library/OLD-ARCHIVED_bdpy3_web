# -*- coding: utf-8 -*-

import logging
from django.test import SimpleTestCase    ## TestCase requires db
from bdpy3_web_app import settings_app
from bdpy3_web_app.lib.app_helper import LibCaller


log = logging.getLogger(__name__)
SimpleTestCase.maxDiff = None


## disables test because it would really submit a request
# class Bdpy3LibTest( SimpleTestCase ):
#     """ Checks call to bdpy3 library. """

#     def setUp(self):
#         self.libcaller = LibCaller()

#     def test_do_lookup( self):
#         """ Checks good params. """
#         params = { 'user_barcode': settings_app.TEST_PATRON_BARCODE, 'isbn': settings_app.TEST_ISBN }
#         result = self.libcaller.do_lookup( params )
#         self.assertEqual(
#             dict,
#             type(result) )
#         self.assertEqual(
#             ['Available', 'OrigNumberOfRecords', 'PickupLocation', 'RequestLink'],
#             sorted(result.keys()) )
#         self.assertEqual(
#             'foo',
#             result['Available'] )
#         self.assertEqual(
#             'foo',
#             result['RequestLink']['RequestMessage'] )


class RootUrlTest( SimpleTestCase ):
    """ Checks root urls. """

    def test_root_url_no_slash(self):
        """ Checks '/root_url'. """
        response = self.client.get( '' )  # project root part of url is assumed
        self.assertEqual( 302, response.status_code )  # permanent redirect
        redirect_url = response._headers['location'][1]
        self.assertEqual(  '/info/', redirect_url )

    def test_root_url_slash(self):
        """ Checks '/root_url/'. """
        response = self.client.get( '/' )  # project root part of url is assumed
        self.assertEqual( 302, response.status_code )  # permanent redirect
        redirect_url = response._headers['location'][1]
        self.assertEqual(  '/info/', redirect_url )

    # end class RootUrlTest()
