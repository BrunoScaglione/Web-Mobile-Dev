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


class OutgoingCallerIdTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .outgoing_caller_ids("PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/OutgoingCallerIds/PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "Fri, 21 Aug 2009 00:11:24 +0000",
                "date_updated": "Fri, 21 Aug 2009 00:11:24 +0000",
                "friendly_name": "(415) 867-5309",
                "phone_number": "+141586753096",
                "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .outgoing_caller_ids("PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .outgoing_caller_ids("PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/OutgoingCallerIds/PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "Fri, 21 Aug 2009 00:11:24 +0000",
                "date_updated": "Fri, 21 Aug 2009 00:11:24 +0000",
                "friendly_name": "(415) 867-5309",
                "phone_number": "+141586753096",
                "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .outgoing_caller_ids("PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .outgoing_caller_ids("PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/OutgoingCallerIds/PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .outgoing_caller_ids("PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .outgoing_caller_ids.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/OutgoingCallerIds.json',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json?Page=0&PageSize=50",
                "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json?Page=0&PageSize=50",
                "next_page_uri": null,
                "num_pages": 1,
                "outgoing_caller_ids": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "Fri, 21 Aug 2009 00:11:24 +0000",
                        "date_updated": "Fri, 21 Aug 2009 00:11:24 +0000",
                        "friendly_name": "(415) 867-5309",
                        "phone_number": "+141586753096",
                        "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                    }
                ],
                "page": 0,
                "page_size": 50,
                "previous_page_uri": null,
                "start": 0,
                "total": 1,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .outgoing_caller_ids.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json?Page=0&PageSize=50",
                "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json?Page=0&PageSize=50",
                "next_page_uri": null,
                "num_pages": 1,
                "outgoing_caller_ids": [],
                "page": 0,
                "page_size": 50,
                "previous_page_uri": null,
                "start": 0,
                "total": 1,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .outgoing_caller_ids.list()

        self.assertIsNotNone(actual)
