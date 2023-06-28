
from unittest.mock import MagicMock, patch
from truth.truth import AssertThat

from tests import AppTestCase, DbMixin, TestClientMixin


class TestSession(TestClientMixin, DbMixin, AppTestCase):
    
    @patch("wapp.lib.session.db")
    def test_session_creates_session_in_db(self, db_mock):
        from wapp.lib.session import create_session
        
        create_session(123)
        
        AssertThat(db_mock.session.add).WasCalled()
        AssertThat(db_mock.session.commit).WasCalled()
