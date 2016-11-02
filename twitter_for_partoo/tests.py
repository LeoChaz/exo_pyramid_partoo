import unittest
import mock

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from .views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['project'], 'twitter_for_partoo')

    def test_newtweet(self):
        from .views import newtweet, api
        from pyramid.httpexceptions import HTTPSeeOther

        with mock.patch.object(api, "request") as mock_api_request:
            request = testing.DummyRequest()

            with self.assertRaises(HTTPSeeOther):
                _ = newtweet(request)
                mock_api_request.assert_called_with('statuses/update', {'status': mock.ANY})


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from twitter_for_partoo import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'Pyramid' in res.body)

    def test_newtweet(self):
        from .views import api
        with mock.patch.object(api, "request") as mock_api_request:
            res = self.testapp.post('/newtweet', status=303)
            mock_api_request.assert_called_with('statuses/update', {'status': mock.ANY})
            self.assertTrue(res.status_code, 303)
