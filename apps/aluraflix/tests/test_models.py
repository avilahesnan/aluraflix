from django.test import TestCase
from apps.aluraflix.models import Program


class ProgramModelTestCase(TestCase):

    def setUp(self):
        self.program = Program(
            title='Filme teste',
            release_date='2024-03-02'
        )

    def test_verify_attributes_program(self):
        '''
        Test that verifies the attributes of a program with default values.
        '''

        self.assertEqual(self.program.title, 'Filme teste')
        self.assertEqual(self.program.type, 'F')
        self.assertEqual(self.program.release_date, '2024-03-02')
        self.assertEqual(self.program.likes, 0)
        self.assertEqual(self.program.dislikes, 0)
