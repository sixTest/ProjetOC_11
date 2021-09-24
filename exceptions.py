
class EmailNotFound(Exception):
    def __init__(self):
        self.msg = "Sorry, that email wasn't found."

    def __str__(self):
        return self.msg


class ClubNotEnoughPoints(Exception):
    def __init__(self):
        self.msg = "Sorry the club doesn't have enough points."

    def __str__(self):
        return self.msg


class CompetitionNotEnoughPlaces(Exception):
    def __init__(self):
        self.msg = "Sorry this competition doesn't have enough places."

    def __str__(self):
        return self.msg

