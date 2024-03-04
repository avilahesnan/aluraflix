from django.test import TestCase
from apps.aluraflix.models import Program
from apps.aluraflix.serializer import ProgramSerializer


class ProgramSerializerTestCase(TestCase):

    def setUp(self):
        self.program = Program(
            title='Filme teste',
            type='S',
            release_date='2024-03-02',
            likes=3564,
            dislikes=4
        )

        self.serializer = ProgramSerializer(instance=self.program)

    def test_verifies_serialized_fields(self):
        '''
        Test that verifies the fields being serialized.
        '''

        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(['title', 'type', 'release_date', 'likes']))  # noqa: E501

    def test_checks_content_serialized_fields(self):
        '''
        Test that verifies the contents of the serialized fields.
        '''

        data = self.serializer.data

        self.assertEqual(data['title'], self.program.title)
        self.assertEqual(data['type'], self.program.type)
        self.assertEqual(data['release_date'], self.program.release_date)
        self.assertEqual(data['likes'], self.program.likes)
