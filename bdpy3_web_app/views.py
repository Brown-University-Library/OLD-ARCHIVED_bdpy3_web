# -*- coding: utf-8 -*-

import datetime, json, logging, os, pprint
from bdpy3_web_app import settings_app
from bdpy3_web_app.lib.app_helper import Validator, LibCaller
from django.conf import settings
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


log = logging.getLogger(__name__)
validator = Validator()
caller = LibCaller()


def info( request ):
    """ Returns simplest response. """
    return HttpResponseRedirect( settings_app.README_URL )


def v1( request ):
    """ Handles post from easyborrow & returns json results. """
    # log.debug( 'request, ```%s```' % pprint.pformat(request.__dict__) )
    log.debug( '\n\nstarting request...' )
    if validator.validate_request( request.method, request.META.get('REMOTE_ADDR', ''), request.POST ) is False:
        log.info( 'request invalid, returning 400' )
        return HttpResponseBadRequest( '400 / Bad Request' )
    result_data = caller.do_lookup( request.POST )
    interpreted_response_dct = caller.interpret_result( result_data )
    logger.debug( 'returning response' )
    return flask.jsonify( interpreted_response_dct )

    return HttpResponse( 'v1 handling coming' )


def access_test( request ):
    """ Returns simplest response. """
    log.debug( 'request, ```%s```' % pprint.pformat(request.__dict__) )
    now = datetime.datetime.now()
    return HttpResponse( '<p>hi</p> <p>( %s )</p>' % now )
