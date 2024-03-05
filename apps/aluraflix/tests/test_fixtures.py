from django.test import TestCase
from apps.aluraflix.models import Program


class FixtureDataTestCase(TestCase):

    fixtures = ['programs_initial']

    def test_checks_loading_fixture(self):
        '''
        Test verifying fixture loading.
        '''

        program = Program.objects.get(pk=1)
        all_programs = Program.objects.all()

        self.assertEqual(program.title, 'Coisas bizarras')
        self.assertEqual(len(all_programs), 9)
