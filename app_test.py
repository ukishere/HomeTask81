import unittest
from unittest.mock import patch
import app

class AppTest(unittest.TestCase):

    def setUp(self):
        self.dirs, self.docs = app.update_date()
        with patch('app.input', return_value='q'):
            with patch('app.update_date') as mock:
                mock.return_value = self.dirs, self.docs
                app.secretary_program_start()

    def test_get_doc_owner_name(self):
        with patch('app.input', return_value='10006'):
            self.assertEqual(app.get_doc_owner_name(), 'Аристарх Павлов')

    def test_get_doc_shelf(self):
        with patch('app.input', return_value='10006'):
            self.assertIs(app.get_doc_shelf(), '2')

    def test_add_new_doc(self):
        user_input = ['11-3', 'new_type', 'Alex', '3']
        with patch('app.input', side_effect=user_input):
            app.add_new_doc()
            self.assertIn('11-3', self.dirs['3'])
            self.assertIn({"type": "new_type", "number": "11-3", "name": "Alex"}, self.docs)

    def test_delete(self):
        with patch('app.input', return_value='10006'):
            app.delete_doc()
            self.assertNotIn('10006', self.dirs['2'])

    def test_move_doc_to_shelf(self):
        user_input = ['11-2', '3']
        with patch('app.input', side_effect=user_input):
            app.move_doc_to_shelf()
            self.assertIn('11-2', self.dirs['3'])

    def test_add_new_shelf(self):
        with patch('app.input', return_value='4'):
            app.add_new_shelf()
            self.assertIn('4', self.dirs.keys())

if __name__ == '__main__':

    unittest.main()