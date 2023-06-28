import unittest

from wapp.factory import create_app
from wapp.lib.models import db


class AppTestCase(unittest.TestCase):
    def __init__(self, methodName):
        self.app = create_app()
        super().__init__(methodName)

    def setUp(self):
        engine = self.app.extensions["sqlalchemy"].db.engine
        engine.dispose()


class TestClientMixin:
    def run(self, result=None):
        with self.app.test_client() as client:
            self.client = client
            super().run(result)


class DbMixin:
    def run(self, result=None):
        with self.app.app_context() as ctx:
            self.app_ctx = ctx
            super().run(result)

    def tearDown(self):
        super().tearDown()
        db.session.close()

    def setUp(self):
        super().setUp()
        meta = db.metadata
        for table in reversed(meta.sorted_tables):
            db.session.execute(table.delete())
        db.session.commit()
