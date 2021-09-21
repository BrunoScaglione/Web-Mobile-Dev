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


class EntityTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.authy.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .entities.create(identity="identity", twilio_authy_sandbox_mode="twilio_authy_sandbox_mode")

        values = {'Identity': "identity", }

        headers = {'Twilio-Authy-Sandbox-Mode': "twilio_authy_sandbox_mode", }
        self.holodeck.assert_has_request(Request(
            'post',
            'https://authy.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Entities',
            headers=headers,
        ))
        self.holodeck.assert_has_request(Request(
            'post',
            'https://authy.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Entities',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "YEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "identity": "ff483d1ff591898a9942916050d2ca3f",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://authy.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities/ff483d1ff591898a9942916050d2ca3f",
                "links": {
                    "factors": "https://authy.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities/ff483d1ff591898a9942916050d2ca3f/Factors"
                }
            }
            '''
        ))

        actual = self.client.authy.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .entities.create(identity="identity")

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.authy.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .entities("identity").delete(twilio_authy_sandbox_mode="twilio_authy_sandbox_mode")

        headers = {'Twilio-Authy-Sandbox-Mode': "twilio_authy_sandbox_mode", }
        self.holodeck.assert_has_request(Request(
            'delete',
            'https://authy.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Entities/identity',
            headers=headers,
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.authy.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .entities("identity").delete()

        self.assertTrue(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.authy.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .entities("identity").fetch(twilio_authy_sandbox_mode="twilio_authy_sandbox_mode")

        headers = {'Twilio-Authy-Sandbox-Mode': "twilio_authy_sandbox_mode", }
        self.holodeck.assert_has_request(Request(
            'get',
            'https://authy.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Entities/identity',
            headers=headers,
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "YEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "identity": "ff483d1ff591898a9942916050d2ca3f",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://authy.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities/ff483d1ff591898a9942916050d2ca3f",
                "links": {
                    "factors": "https://authy.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities/ff483d1ff591898a9942916050d2ca3f/Factors"
                }
            }
            '''
        ))

        actual = self.client.authy.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .entities("identity").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.authy.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .entities.list(twilio_authy_sandbox_mode="twilio_authy_sandbox_mode")

        headers = {'Twilio-Authy-Sandbox-Mode': "twilio_authy_sandbox_mode", }
        self.holodeck.assert_has_request(Request(
            'get',
            'https://authy.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Entities',
            headers=headers,
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "entities": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://authy.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://authy.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "entities"
                }
            }
            '''
        ))

        actual = self.client.authy.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .entities.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "entities": [
                    {
                        "sid": "YEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "identity": "ff483d1ff591898a9942916050d2ca3f",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "url": "https://authy.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities/ff483d1ff591898a9942916050d2ca3f",
                        "links": {
                            "factors": "https://authy.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities/ff483d1ff591898a9942916050d2ca3f/Factors"
                        }
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://authy.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://authy.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "entities"
                }
            }
            '''
        ))

        actual = self.client.authy.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .entities.list()

        self.assertIsNotNone(actual)