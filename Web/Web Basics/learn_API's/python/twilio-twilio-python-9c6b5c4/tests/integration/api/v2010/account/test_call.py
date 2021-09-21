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


class CallTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .calls.create(to="+15558675310", from_="+15017122661")

        values = {'To': "+15558675310", 'From': "+15017122661", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Calls.json',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "annotation": null,
                "answered_by": null,
                "api_version": "2010-04-01",
                "caller_name": null,
                "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",
                "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",
                "direction": "inbound",
                "duration": "15",
                "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",
                "forwarded_from": "+141586753093",
                "from": "+14158675308",
                "from_formatted": "(415) 867-5308",
                "group_sid": null,
                "parent_call_sid": null,
                "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "price": "-0.03000",
                "price_unit": "USD",
                "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",
                "status": "completed",
                "subresource_uris": {
                    "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                    "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",
                    "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Feedback.json",
                    "feedback_summaries": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/FeedbackSummary.json",
                    "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json"
                },
                "to": "+14158675309",
                "to_formatted": "(415) 867-5309",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls.create(to="+15558675310", from_="+15017122661")

        self.assertIsNotNone(actual)

    def test_create_with_twiml_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "annotation": null,
                "answered_by": null,
                "api_version": "2010-04-01",
                "caller_name": null,
                "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",
                "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",
                "direction": "inbound",
                "duration": "15",
                "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",
                "forwarded_from": "+141586753093",
                "from": "+14158675308",
                "from_formatted": "(415) 867-5308",
                "group_sid": null,
                "parent_call_sid": null,
                "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "price": "-0.03000",
                "price_unit": "USD",
                "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",
                "status": "completed",
                "subresource_uris": {
                    "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                    "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",
                    "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Feedback.json",
                    "feedback_summaries": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/FeedbackSummary.json",
                    "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json"
                },
                "to": "+14158675309",
                "to_formatted": "(415) 867-5309",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls.create(to="+15558675310", from_="+15017122661")

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Calls/CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Calls/CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "annotation": "billingreferencetag",
                "answered_by": "machine_start",
                "api_version": "2010-04-01",
                "caller_name": "callerid",
                "date_created": "Fri, 18 Oct 2019 17:00:00 +0000",
                "date_updated": "Fri, 18 Oct 2019 17:01:00 +0000",
                "direction": "outbound-api",
                "duration": "4",
                "end_time": "Fri, 18 Oct 2019 17:03:00 +0000",
                "forwarded_from": "calledvia",
                "from": "+13051416799",
                "from_formatted": "(305) 141-6799",
                "group_sid": "GPdeadbeefdeadbeefdeadbeefdeadbeef",
                "parent_call_sid": "CAdeadbeefdeadbeefdeadbeefdeadbeef",
                "phone_number_sid": "PNdeadbeefdeadbeefdeadbeefdeadbeef",
                "price": "-0.200",
                "price_unit": "USD",
                "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "start_time": "Fri, 18 Oct 2019 17:02:00 +0000",
                "status": "completed",
                "subresource_uris": {
                    "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                    "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",
                    "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Feedback.json",
                    "feedback_summaries": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/FeedbackSummary.json",
                    "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json"
                },
                "to": "+13051913581",
                "to_formatted": "(305) 191-3581",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .calls.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Calls.json',
        ))

    def test_read_full_page1_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "calls": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "annotation": "billingreferencetag1",
                        "answered_by": "machine_start",
                        "api_version": "2010-04-01",
                        "caller_name": "callerid1",
                        "date_created": "Fri, 18 Oct 2019 17:00:00 +0000",
                        "date_updated": "Fri, 18 Oct 2019 17:01:00 +0000",
                        "direction": "outbound-api",
                        "duration": "4",
                        "end_time": "Fri, 18 Oct 2019 17:03:00 +0000",
                        "forwarded_from": "calledvia1",
                        "from": "+13051416799",
                        "from_formatted": "(305) 141-6799",
                        "group_sid": "GPdeadbeefdeadbeefdeadbeefdeadbeef",
                        "parent_call_sid": "CAdeadbeefdeadbeefdeadbeefdeadbeef",
                        "phone_number_sid": "PNdeadbeefdeadbeefdeadbeefdeadbeef",
                        "price": "-0.200",
                        "price_unit": "USD",
                        "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "start_time": "Fri, 18 Oct 2019 17:02:00 +0000",
                        "status": "completed",
                        "subresource_uris": {
                            "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Feedback.json",
                            "feedback_summaries": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/FeedbackSummary.json",
                            "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",
                            "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json"
                        },
                        "to": "+13051913581",
                        "to_formatted": "(305) 191-3581",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                    },
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "annotation": "billingreferencetag2",
                        "answered_by": "human",
                        "api_version": "2010-04-01",
                        "caller_name": "callerid2",
                        "date_created": "Fri, 18 Oct 2019 16:00:00 +0000",
                        "date_updated": "Fri, 18 Oct 2019 16:01:00 +0000",
                        "direction": "inbound",
                        "duration": "3",
                        "end_time": "Fri, 18 Oct 2019 16:03:00 +0000",
                        "forwarded_from": "calledvia2",
                        "from": "+13051416798",
                        "from_formatted": "(305) 141-6798",
                        "group_sid": "GPdeadbeefdeadbeefdeadbeefdeadbeee",
                        "parent_call_sid": "CAdeadbeefdeadbeefdeadbeefdeadbeee",
                        "phone_number_sid": "PNdeadbeefdeadbeefdeadbeefdeadbeee",
                        "price": "-0.100",
                        "price_unit": "JPY",
                        "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0",
                        "start_time": "Fri, 18 Oct 2019 16:02:00 +0000",
                        "status": "completed",
                        "subresource_uris": {
                            "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Feedback.json",
                            "feedback_summaries": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/FeedbackSummary.json",
                            "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Notifications.json",
                            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Recordings.json",
                            "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Payments.json"
                        },
                        "to": "+13051913580",
                        "to_formatted": "(305) 191-3580",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0.json"
                    }
                ],
                "end": 1,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&To=%2B123456789&From=%2B987654321&StartTime=2008-01-02&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&EndTime=2009-01-02&PageSize=2&Page=0",
                "next_page_uri": null,
                "page": 0,
                "page_size": 2,
                "previous_page_uri": null,
                "start": 0,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&To=%2B123456789&From=%2B987654321&StartTime=2008-01-02&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&EndTime=2009-01-02&PageSize=2&Page=0"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls.list()

        self.assertIsNotNone(actual)

    def test_read_full_page2_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "calls": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "annotation": "billingreferencetag1",
                        "answered_by": "machine_start",
                        "api_version": "2010-04-01",
                        "caller_name": "callerid1",
                        "date_created": "Fri, 18 Oct 2019 17:00:00 +0000",
                        "date_updated": "Fri, 18 Oct 2019 17:01:00 +0000",
                        "direction": "outbound-api",
                        "duration": "4",
                        "end_time": "Fri, 18 Oct 2019 17:03:00 +0000",
                        "forwarded_from": "calledvia1",
                        "from": "+13051416799",
                        "from_formatted": "(305) 141-6799",
                        "group_sid": "GPdeadbeefdeadbeefdeadbeefdeadbeef",
                        "parent_call_sid": "CAdeadbeefdeadbeefdeadbeefdeadbeef",
                        "phone_number_sid": "PNdeadbeefdeadbeefdeadbeefdeadbeef",
                        "price": "-0.200",
                        "price_unit": "USD",
                        "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "start_time": "Fri, 18 Oct 2019 17:02:00 +0000",
                        "status": "completed",
                        "subresource_uris": {
                            "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Feedback.json",
                            "feedback_summaries": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/FeedbackSummary.json",
                            "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",
                            "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json"
                        },
                        "to": "+13051913581",
                        "to_formatted": "(305) 191-3581",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                    },
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "annotation": "billingreferencetag2",
                        "answered_by": "human",
                        "api_version": "2010-04-01",
                        "caller_name": "callerid2",
                        "date_created": "Fri, 18 Oct 2019 16:00:00 +0000",
                        "date_updated": "Fri, 18 Oct 2019 16:01:00 +0000",
                        "direction": "inbound",
                        "duration": "3",
                        "end_time": "Fri, 18 Oct 2019 16:03:00 +0000",
                        "forwarded_from": "calledvia2",
                        "from": "+13051416798",
                        "from_formatted": "(305) 141-6798",
                        "group_sid": "GPdeadbeefdeadbeefdeadbeefdeadbeee",
                        "parent_call_sid": "CAdeadbeefdeadbeefdeadbeefdeadbeee",
                        "phone_number_sid": "PNdeadbeefdeadbeefdeadbeefdeadbeee",
                        "price": "-0.100",
                        "price_unit": "JPY",
                        "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0",
                        "start_time": "Fri, 18 Oct 2019 16:02:00 +0000",
                        "status": "completed",
                        "subresource_uris": {
                            "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Feedback.json",
                            "feedback_summaries": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/FeedbackSummary.json",
                            "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Notifications.json",
                            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Recordings.json",
                            "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Payments.json"
                        },
                        "to": "+13051913580",
                        "to_formatted": "(305) 191-3580",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0.json"
                    }
                ],
                "end": 3,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&From=%2B987654321&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&To=%2B123456789&StartTime=2008-01-02&EndTime=2009-01-02&PageSize=2&Page=0",
                "next_page_uri": null,
                "page": 1,
                "page_size": 2,
                "previous_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&From=%2B987654321&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&To=%2B123456789&StartTime=2008-01-02&EndTime=2009-01-02&PageSize=2&Page=0&PageToken=PBCAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "start": 2,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&From=%2B987654321&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&To=%2B123456789&StartTime=2008-01-02&EndTime=2009-01-02&PageSize=2&Page=1&PageToken=PACAdeadbeefdeadbeefdeadbeefdeadbeef"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls.list()

        self.assertIsNotNone(actual)

    def test_read_empty_dates_greater_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "calls": [],
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&To=%2B123456789&EndTime%3E=2009-01-02&From=%2B987654321&StartTime%3E=2008-01-02&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&PageSize=2&Page=0",
                "next_page_uri": null,
                "page": 0,
                "page_size": 2,
                "previous_page_uri": null,
                "start": 0,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&To=%2B123456789&EndTime%3E=2009-01-02&From=%2B987654321&StartTime%3E=2008-01-02&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&PageSize=2&Page=0"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls.list()

        self.assertIsNotNone(actual)

    def test_read_empty_dates_less_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "calls": [],
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?EndTime%3C=2009-01-02&Status=completed&From=%2B987654321&To=%2B123456789&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&StartTime%3C=2008-01-02&PageSize=2&Page=0",
                "next_page_uri": null,
                "page": 0,
                "page_size": 2,
                "previous_page_uri": null,
                "start": 0,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?EndTime%3C=2009-01-02&Status=completed&From=%2B987654321&To=%2B123456789&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&StartTime%3C=2008-01-02&PageSize=2&Page=0"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls.list()

        self.assertIsNotNone(actual)

    def test_read_empty_date_fun_date_formats_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "calls": [],
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?EndTime%3C=2019-06-11+22%3A05%3A25.000&Status=completed&From=%2B987654321&To=%2B123456789&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&StartTime%3C=06%2F11%2F2019+22%3A05%3A25+MST&PageSize=2&Page=0",
                "next_page_uri": null,
                "page": 0,
                "page_size": 2,
                "previous_page_uri": null,
                "start": 0,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?EndTime%3C=2019-06-11+22%3A05%3A25.000&Status=completed&From=%2B987654321&To=%2B123456789&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&StartTime%3C=06%2F11%2F2019+22%3A05%3A25+MST&PageSize=2&Page=0"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Calls/CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "annotation": null,
                "answered_by": null,
                "api_version": "2010-04-01",
                "caller_name": null,
                "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",
                "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",
                "direction": "inbound",
                "duration": "15",
                "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",
                "forwarded_from": "+141586753093",
                "from": "+14158675308",
                "from_formatted": "(415) 867-5308",
                "group_sid": null,
                "parent_call_sid": null,
                "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "price": "-0.03000",
                "price_unit": "USD",
                "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",
                "status": "completed",
                "subresource_uris": {
                    "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                    "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",
                    "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Feedback.json",
                    "feedback_summaries": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/FeedbackSummary.json",
                    "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json"
                },
                "to": "+14158675309",
                "to_formatted": "(415) 867-5309",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_cancel_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "annotation": null,
                "answered_by": null,
                "api_version": "2010-04-01",
                "caller_name": null,
                "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",
                "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",
                "direction": "inbound",
                "duration": "15",
                "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",
                "forwarded_from": "+141586753093",
                "from": "+14158675308",
                "from_formatted": "(415) 867-5308",
                "group_sid": null,
                "parent_call_sid": null,
                "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "price": "-0.03000",
                "price_unit": "USD",
                "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",
                "status": "canceled",
                "subresource_uris": {
                    "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                    "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",
                    "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Feedback.json",
                    "feedback_summaries": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/FeedbackSummary.json",
                    "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json"
                },
                "to": "+14158675309",
                "to_formatted": "(415) 867-5309",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_posttwiml_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "annotation": null,
                "answered_by": null,
                "api_version": "2010-04-01",
                "caller_name": null,
                "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",
                "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",
                "direction": "inbound",
                "duration": "15",
                "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",
                "forwarded_from": "+141586753093",
                "from": "+14158675308",
                "from_formatted": "(415) 867-5308",
                "group_sid": null,
                "parent_call_sid": null,
                "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "price": "-0.03000",
                "price_unit": "USD",
                "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",
                "status": "canceled",
                "subresource_uris": {
                    "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                    "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",
                    "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Feedback.json",
                    "feedback_summaries": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/FeedbackSummary.json",
                    "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json"
                },
                "to": "+14158675309",
                "to_formatted": "(415) 867-5309",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)