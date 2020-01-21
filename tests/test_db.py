from unittest import TestCase
from unittest.mock import patch
from src.db_helper import DbHelper
from io import StringIO

class TestDbHelper(TestCase):
    def setUp(self):
        pass

    def test_db(self):
        expected = '62000.0\n12000.0\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            DbHelper().print_sal()
            self.assertEqual(fake_out.getvalue(), expected)