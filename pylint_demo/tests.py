from django.test import TestCase
from exemple.tests import UserAPITestCase  # Assurez-vous que le chemin est correct
import unittest

class CombinedTests(TestCase):
    def test_user_app_tests(self):
        # Créez une suite de tests et ajoutez-y les tests de UtilisateurAPIViewTests
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(UserAPITestCase))

        # Exécutez la suite de tests
        result = unittest.TextTestRunner().run(suite)

        # Vérifiez si tous les tests ont réussi
        self.assertTrue(result.wasSuccessful(), "Les tests  ont échoué.")