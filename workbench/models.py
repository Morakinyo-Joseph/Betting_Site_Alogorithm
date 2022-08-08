from calendar import c
from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()


class Game(models.Model):
    GAME_CHOICES = (
        ("Football", "Football"),
        ("Basketball", "Basketball"),
    )

    name = models.CharField(max_length=250, choices=GAME_CHOICES)

    gameID = models.CharField(max_length=50) #this means game's unique identity key.

    player1 = models.CharField(max_length=250)
    player2 = models.CharField(max_length=250)
    
    player1_odd = models.FloatField()
    player2_odd = models.FloatField()
    draw_odds = models.FloatField()

    created_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name + ": " + self.player1 + " VS " + self.player2


class GameResult(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE)

    PREDICTION_CHOICES = (
        ("1x", "1x"),
        ("x2", "x2"),
        ("Draw", "Draw"),
    )

    game_result = models.CharField(max_length=25, choices=PREDICTION_CHOICES)

    def __str__(self):
        return self.game.name + ": " + self.game.player1 + " VS " + self.game.player2 + " (" + self.game_result + ")"



class Slip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picked_game = models.ForeignKey(Game, on_delete=models.CASCADE)

    USER_PREDICTIONS = (
        ("1x", "1x"),
        ("x2", "x2"),
        ("Draw", "Draw"),
    )

    predict = models.CharField(max_length=25, choices=USER_PREDICTIONS)
    slip_creation = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.username + ": " + self.picked_game.name + " -- " + self.picked_game.player1 + " VS " + self.picked_game.player2 + " (" + self.predict + ")" 



class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game_slip = models.ForeignKey(Slip, on_delete=models.CASCADE)
    ticket_code = models.CharField(max_length=10)

    TICKET_OPTIONS = (
        ("Won", "Won"),
        ("Lost", "Lost"),
        ("Void", "Void"),
    )

    ticket_option = models.CharField(max_length=10, choices=TICKET_OPTIONS)
    ticket_date = models.DateTimeField(default=datetime.now)


