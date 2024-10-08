from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Player, Match
from .serializers import PlayerSerializer, MatchSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    @action(detail=False, methods=['post'])
    def schedule(self, request):
        player1_id = request.data.get('player1_id')
        player2_id = request.data.get('player2_id')

        player1 = Player.objects.get(id=player1_id)
        player2 = Player.objects.get(id=player2_id)

        match = Match.objects.create(player1=player1, player2=player2)

        return Response(MatchSerializer(match).data)

    @action(detail=True, methods=['post'])
    def set_winner(self, request, pk=None):
        match = self.get_object()
        winner_id = request.data.get('winner_id')
        winner = Player.objects.get(id=winner_id)

        match.winner = winner
        match.save()

        return Response(MatchSerializer(match).data)

