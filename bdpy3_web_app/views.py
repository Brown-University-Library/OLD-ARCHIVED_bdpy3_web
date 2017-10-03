# -*- coding: utf-8 -*-

import datetime, json, logging, os, pprint
from bdpy3_web_app import settings_app
from bdpy3_web_app.lib.app_helper import Validator
from django.conf import settings
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


log = logging.getLogger(__name__)
validator = Validator()


def info( request ):
    """ Returns simplest response. """
    return HttpResponseRedirect( settings_app.README_URL )


def v1( request ):
    """ Handles post from easyborrow & returns json results. """
    # log.debug( 'request, ```%s```' % pprint.pformat(request.__dict__) )
    log.debug( '\n\nstarting request...' )
    if validator.validate_request( request.method, request.META.get('REMOTE_ADDR', ''), request.GET ) is False:  # for dev; will be POST
        log.info( 'request invalid, returning 400' )
        return HttpResponseBadRequest( '400 / Bad Request' )
    result_data = ezb_helper.do_lookup( flask.request.form )
    interpreted_response_dct = ezb_helper.interpret_result( result_data )
    logger.debug( 'returning response' )
    return flask.jsonify( interpreted_response_dct )

    return HttpResponse( 'v1 handling coming' )


def access_test( request ):
    """ Returns simplest response. """
    log.debug( 'request, ```%s```' % pprint.pformat(request.__dict__) )
    now = datetime.datetime.now()
    return HttpResponse( '<p>hi</p> <p>( %s )</p>' % now )
