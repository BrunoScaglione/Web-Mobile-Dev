# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class TerminatingSipDomainTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks("TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                   .terminating_sip_domains("SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://trunking.twilio.com/v1/Trunks/TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/TerminatingSipDomains/SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2010-04-01",
                "auth_type": "IP_ACL",
                "date_created": "2015-07-20T17:27:10Z",
                "date_updated": "2015-10-09T11:36:32Z",
                "domain_name": "dunder-mifflin-scranton.sip.twilio.com",
                "friendly_name": "Scranton Office",
                "sip_registration": true,
                "sid": "SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TerminatingSipDomains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "voice_fallback_method": "POST",
                "voice_fallback_url": null,
                "voice_method": "POST",
                "voice_status_callback_method": "POST",
                "voice_status_callback_url": null,
                "voice_url": "https://demo.twilio.com/welcome/voice/",
                "trunk_sid": "TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "sip_domain": "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            }
            '''
        ))

        actual = self.client.trunking.v1.trunks("TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .terminating_sip_domains("SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks("TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                   .terminating_sip_domains("SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://trunking.twilio.com/v1/Trunks/TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/TerminatingSipDomains/SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.trunking.v1.trunks("TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .terminating_sip_domains("SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks("TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                   .terminating_sip_domains.create(sip_domain_sid="SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        values = {'SipDomainSid': "SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://trunking.twilio.com/v1/Trunks/TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/TerminatingSipDomains',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2010-04-01",
                "auth_type": "IP_ACL",
                "date_created": "2015-07-20T17:27:10Z",
                "date_updated": "2015-10-09T11:36:32Z",
                "domain_name": "dunder-mifflin-scranton.sip.twilio.com",
                "friendly_name": "Scranton Office",
                "sip_registration": true,
                "sid": "SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TerminatingSipDomains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "voice_fallback_method": "POST",
                "voice_fallback_url": null,
                "voice_method": "POST",
                "voice_status_callback_method": "POST",
                "voice_status_callback_url": null,
                "voice_url": "https://demo.twilio.com/welcome/voice/",
                "trunk_sid": "TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "sip_domain": "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            }
            '''
        ))

        actual = self.client.trunking.v1.trunks("TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .terminating_sip_domains.create(sip_domain_sid="SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks("TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                   .terminating_sip_domains.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://trunking.twilio.com/v1/Trunks/TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/TerminatingSipDomains',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TerminatingSipDomains?PageSize=50&Page=0",
                    "key": "sip_domains",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TerminatingSipDomains?PageSize=50&Page=0"
                },
                "sip_domains": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "api_version": "2010-04-01",
                        "auth_type": "IP_ACL",
                        "date_created": "2015-07-20T17:27:10Z",
                        "date_updated": "2015-10-09T11:36:32Z",
                        "domain_name": "dunder-mifflin-scranton.sip.twilio.com",
                        "friendly_name": "Scranton Office",
                        "sip_registration": true,
                        "sid": "SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TerminatingSipDomains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "voice_fallback_method": "POST",
                        "voice_fallback_url": null,
                        "voice_method": "POST",
                        "voice_status_callback_method": "POST",
                        "voice_status_callback_url": null,
                        "voice_url": "https://demo.twilio.com/welcome/voice/",
                        "trunk_sid": "TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "links": {
                            "sip_domain": "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                        }
                    }
                ]
            }
            '''
        ))

        actual = self.client.trunking.v1.trunks("TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .terminating_sip_domains.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TerminatingSipDomains?PageSize=50&Page=0",
                    "key": "sip_domains",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TerminatingSipDomains?PageSize=50&Page=0"
                },
                "sip_domains": []
            }
            '''
        ))

        actual = self.client.trunking.v1.trunks("TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .terminating_sip_domains.list()

        self.assertIsNotNone(actual)
