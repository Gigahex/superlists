from django.test import TestCase

# Create your tests here.

class SmokeTest(TestCase):
    '''тест на токсичность'''

    def test_bad_maths(self):
        '''тест: неправильные математические расчёты'''
        self.assertEqual(1+1,3)