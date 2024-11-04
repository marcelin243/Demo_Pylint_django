"""
Module de tests combinés pour l'application.
"""

import unittest  # Import standard

from django.test import TestCase
from exemple.tests import UserAPITestCase  # Import tiers

class CombinedTests(TestCase):
    """
    Classe de tests combinés pour exécuter les tests de UserAPITestCase.
    """

    def test_user_app_tests(self):
        """
        Exécute les tests de UserAPITestCase et vérifie si tous les tests ont réussi.
        """
        # Créez une suite de tests et ajoutez-y les tests de UserAPITestCase
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(UserAPITestCase))

        # Exécutez la suite de tests
        result = unittest.TextTestRunner().run(suite)

        # Vérifiez si tous les tests ont réussi
        self.assertTrue(result.wasSuccessful(), "Les tests ont échoué.")

# Assurez-vous d'avoir une nouvelle ligne ici