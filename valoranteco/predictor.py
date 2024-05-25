"""
Assuming every player has 100% accuracy and are "dueling" who will come out on top based on valorant economies?

This model includes only gunplay and armor, which is a good approximation for the most part.
"""


class Gun:
    """
    Guns are listed as cost to dmg on a perfect shot
    """
    classic = (0, 78)
    shorty = (150, 150)
    frenzy = (450, 78)
    ghost = (500, 105)
    sheriff = (800, 159)
    stinger = (950, 67)
    spectre = (1600, 78)
    bucky = (850, 150)
    judge = (1850, 150)
    bulldog = (2050, 115)
    guardian = (2250, 195)
    phantom = (2900, 156)
    vandal = (2900, 160)
    marshal = (950, 202)
    operator = (4700, 255)
    ares = (1600, 72)
    odin = (3200, 95)


class Shield:
    """
    Class for shields which contribute to an agents overall health
    """
    none = 0
    light = 25
    heavy = 50


class Team:
    """
    Represents a valorant "team", consists of 5 players
    """


class Agent:
    """
    Represents a valorant "agent". These agents can have a maximum of 9000 credits
    """

    def __init__(self) -> None:
        """
        Init for an agent
        """
        self.creds = 800
        self.main_gun = Gun.classic
        self.shields = Shield.none
        self.health = 100

    def buy(self, gun: Gun, shield: Shield)

def calculateScore(attacker: Team, defender: Team) -> float:
    """
    Calculates the score of a team
    """