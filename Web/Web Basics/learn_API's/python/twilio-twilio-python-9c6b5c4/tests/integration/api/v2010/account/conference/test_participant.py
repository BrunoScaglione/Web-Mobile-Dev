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


class ParticipantTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .participants("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Conferences/CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Participants/CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "Fri, 18 Feb 2011 21:07:19 +0000",
                "date_updated": "Fri, 18 Feb 2011 21:07:19 +0000",
                "end_conference_on_exit": false,
                "muted": false,
                "hold": false,
                "status": "complete",
                "start_conference_on_enter": true,
                "coaching": true,
                "call_sid_to_coach": "CAbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .participants("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .participants("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Conferences/CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Participants/CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
        ))

    def test_mute_participant_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "Fri, 18 Feb 2011 21:07:19 +0000",
                "date_updated": "Fri, 18 Feb 2011 21:07:19 +0000",
                "end_conference_on_exit": false,
                "muted": true,
                "hold": false,
                "status": "complete",
                "start_conference_on_enter": true,
                "coaching": false,
                "call_sid_to_coach": null,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .participants("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_modify_participant_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "Fri, 18 Feb 2011 21:07:19 +0000",
                "date_updated": "Fri, 18 Feb 2011 21:07:19 +0000",
                "end_conference_on_exit": false,
                "muted": false,
                "hold": false,
                "status": "complete",
                "start_conference_on_enter": true,
                "coaching": true,
                "call_sid_to_coach": "CAbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .participants("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .participants.create(from_="+15017122661", to="+15558675310")

        values = {'From': "+15017122661", 'To': "+15558675310", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Conferences/CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Participants.json',
            data=values,
        ))

    def test_create_with_sid_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "Fri, 18 Feb 2011 21:07:19 +0000",
                "date_updated": "Fri, 18 Feb 2011 21:07:19 +0000",
                "end_conference_on_exit": false,
                "muted": false,
                "hold": false,
                "status": "complete",
                "start_conference_on_enter": true,
                "coaching": false,
                "call_sid_to_coach": null,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .participants.create(from_="+15017122661", to="+15558675310")

        self.assertIsNotNone(actual)

    def test_create_with_friendly_name_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "Fri, 18 Feb 2011 21:07:19 +0000",
                "date_updated": "Fri, 18 Feb 2011 21:07:19 +0000",
                "end_conference_on_exit": false,
                "muted": false,
                "hold": false,
                "status": "complete",
                "start_conference_on_enter": true,
                "coaching": false,
                "call_sid_to_coach": null,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .participants.create(from_="+15017122661", to="+15558675310")

        self.assertIsNotNone(actual)

    def test_create_with_sid_as_coach_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "Fri, 18 Feb 2011 21:07:19 +0000",
                "date_updated": "Fri, 18 Feb 2011 21:07:19 +0000",
                "end_conference_on_exit": false,
                "muted": false,
                "hold": false,
                "status": "queued",
                "start_conference_on_enter": true,
                "coaching": false,
                "call_sid_to_coach": null,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .participants.create(from_="+15017122661", to="+15558675310")

        self.assertIsNotNone(actual)

    def test_create_with_non_e164_number_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "Fri, 18 Feb 2011 21:07:19 +0000",
                "date_updated": "Fri, 18 Feb 2011 21:07:19 +0000",
                "end_conference_on_exit": false,
                "muted": false,
                "hold": false,
                "status": "complete",
                "start_conference_on_enter": true,
                "coaching": false,
                "call_sid_to_coach": null,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .participants.create(from_="+15017122661", to="+15558675310")

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .participants("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Conferences/CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Participants/CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .participants("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .participants.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Conferences/CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Participants.json',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "participants": [],
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json?Hold=True&PageSize=50&Page=0",
                "next_page_uri": null,
                "previous_page_uri": null,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json?Hold=True&PageSize=50&Page=0",
                "page": 0,
                "page_size": 50,
                "end": 0,
                "start": 0
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .participants.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "participants": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "Sat, 19 Feb 2011 21:07:19 +0000",
                        "date_updated": "Sat, 19 Feb 2011 21:07:19 +0000",
                        "end_conference_on_exit": false,
                        "muted": true,
                        "hold": false,
                        "status": "connected",
                        "start_conference_on_enter": true,
                        "coaching": true,
                        "call_sid_to_coach": "CAbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                    },
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "call_sid": "CAbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                        "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "Fri, 18 Feb 2011 21:07:19 +0000",
                        "date_updated": "Fri, 18 Feb 2011 21:07:19 +0000",
                        "end_conference_on_exit": false,
                        "muted": true,
                        "hold": false,
                        "status": "connected",
                        "start_conference_on_enter": true,
                        "coaching": false,
                        "call_sid_to_coach": null,
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.json"
                    }
                ],
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json?Muted=true&PageSize=2&Page=0",
                "next_page_uri": null,
                "previous_page_uri": null,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json?Muted=true&PageSize=2&Page=0",
                "page": 0,
                "page_size": 2,
                "start": 0,
                "end": 1
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .participants.list()

        self.assertIsNotNone(actual)

    def test_read_next_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "participants": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "call_sid": "CAcccccccccccccccccccccccccccccccc",
                        "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "Thu, 17 Feb 2011 21:07:19 +0000",
                        "date_updated": "Thu, 17 Feb 2011 21:07:19 +0000",
                        "end_conference_on_exit": false,
                        "muted": true,
                        "hold": false,
                        "status": "connected",
                        "start_conference_on_enter": true,
                        "coaching": false,
                        "call_sid_to_coach": null,
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAcccccccccccccccccccccccccccccccc.json"
                    },
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "call_sid": "CAdddddddddddddddddddddddddddddddd",
                        "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "Wed, 16 Feb 2011 21:07:19 +0000",
                        "date_updated": "Wed, 16 Feb 2011 21:07:19 +0000",
                        "end_conference_on_exit": false,
                        "muted": true,
                        "hold": false,
                        "status": "connected",
                        "start_conference_on_enter": true,
                        "coaching": false,
                        "call_sid_to_coach": null,
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAdddddddddddddddddddddddddddddddd.json"
                    }
                ],
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json?Muted=true&PageSize=2&Page=0",
                "next_page_uri": null,
                "previous_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json?Muted=true&PageSize=2&Page=0&PageToken=PBCPcccccccccccccccccccccccccccccccc",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json?Muted=true&PageSize=2&Page=1&PageToken=PACPbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                "page": 1,
                "page_size": 2,
                "start": 2,
                "end": 3
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .participants.list()

        self.assertIsNotNone(actual)

    def test_read_previous_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "participants": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "Sat, 19 Feb 2011 21:07:19 +0000",
                        "date_updated": "Sat, 19 Feb 2011 21:07:19 +0000",
                        "end_conference_on_exit": false,
                        "muted": true,
                        "hold": false,
                        "status": "connected",
                        "start_conference_on_enter": true,
                        "coaching": true,
                        "call_sid_to_coach": "CAbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                    },
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "call_sid": "CAbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                        "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "Fri, 18 Feb 2011 21:07:19 +0000",
                        "date_updated": "Fri, 18 Feb 2011 21:07:19 +0000",
                        "end_conference_on_exit": false,
                        "muted": true,
                        "hold": false,
                        "status": "connected",
                        "start_conference_on_enter": true,
                        "coaching": false,
                        "call_sid_to_coach": null,
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.json"
                    }
                ],
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json?Muted=true&PageSize=2&Page=0",
                "next_page_uri": null,
                "previous_page_uri": null,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json?Muted=true&PageSize=2&Page=0&PageToken=PBCPcccccccccccccccccccccccccccccccc",
                "page": 0,
                "page_size": 2,
                "start": 0,
                "end": 1
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .participants.list()

        self.assertIsNotNone(actual)
