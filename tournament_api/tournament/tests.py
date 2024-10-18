from django.test import TestCase

# Create your tests here.
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from tournament.models import Tournament, Team, Match
# from tournament.serializers import TournamentSerializer, TeamSerializer, MatchSerializer

# class TournamentTests(APITestCase):
#     def test_create_tournament(self):
#         """
#         Ensure we can create a new tournament object.
#         """
#         url = reverse('tournament-list')
#         data = {'name': 'Test Tournament'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Tournament.objects.count(), 1)
#         self.assertEqual(Tournament.objects.get().name, 'Test Tournament')
