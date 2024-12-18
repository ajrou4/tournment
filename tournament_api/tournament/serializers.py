from rest_framework import serializers
from .models import Player, Match, Game

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    player1 = serializers.StringRelatedField()
    player2 = serializers.StringRelatedField()
    winner = serializers.StringRelatedField()

    class Meta:
        model = Match
        fields = '__all__'

#serializer for game model
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'