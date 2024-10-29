from rest_framework import status
from rest_framework.test import APITestCase
from .models import User  # Assurez-vous que le chemin d'importation est correct
from .serializers import UserSerializer  # Assurez-vous que le chemin d'importation est correct

class UserAPITestCase(APITestCase):
    def setUp(self):
        self.utilisateur1=User.objects.create(username='Alice',first_name='Alicia',last_name='Jean',email='alice@example.com')
        self.url = '/api/utilisateur/'  # Assurez-vous que cette URL est correcte

    def test_list_utilisateurs(self):
        response = self.client.get(self.url)
        utilisateurs = User.objects.all()
        serializer = UserSerializer(utilisateurs, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_utilisateur(self):
        initial_count = User.objects.count()
        data = {'username': 'Charlie', 'first_name': 'Charly', 'email': 'charlie@example.com', 'last_name': 'Jean'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), initial_count + 1)  # Vérifie que le nombre a augmenté de 1

    def test_update_utilisateur(self):
        data = {'username': 'Charlie1', 'first_name': 'Charly1', 'email': 'charlie1@example.com', 'last_name': 'Jean1'}
        response = self.client.put(f'{self.url}{self.utilisateur1.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.utilisateur1.refresh_from_db()
        self.assertEqual(self.utilisateur1.username,'Charlie1')  # Vérifiez le nom mis à jour

    def test_delete_utilisateur(self):
        utilisateur2 = User.objects.create(username='Bob',first_name='Bobby',email='bob@example.com',last_name='Smith')
        response = self.client.delete(f'{self.url}{utilisateur2.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(),1)# Vérifie que seul Alice reste       