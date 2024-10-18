from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Match(models.Model):
    player1 = models.ForeignKey(Player, related_name='matches_as_player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, related_name='matches_as_player2', on_delete=models.CASCADE)
    winner = models.ForeignKey(Player, related_name='matches_won', null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player1} vs {self.player2}"


# Path: tournament_api/tournament/models.py : game model


class Game(models.Model):
    player1 = models.ForeignKey(Player, related_name='player1_games', on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, related_name='player2_games', on_delete=models.CASCADE)
    winner = models.ForeignKey(Player, related_name='won_games', null=True, blank=True, on_delete=models.SET_NULL)
    score_player1 = models.IntegerField(default=0)
    score_player2 = models.IntegerField(default=0)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.player1} vs {self.player2}"
