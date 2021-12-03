
class EmailNotFound(Exception):
    def __init__(self):
        self.msg = "Sorry, this email is incorrect."


class ClubNotEnoughPoints(Exception):
    def __init__(self):
        self.msg = "Sorry the club have not enough points."


class CompetitionNotEnoughPlaces(Exception):
    def __init__(self):
        self.msg = "Sorry this competition have not enough places."


class BookingLimitPlaces(Exception):
    def __init__(self):
        self.msg = "Sorry a club can only book a maximum of 12 places."


class CompetitionIsClosed(Exception):
    def __init__(self):
        self.msg = "Sorry the competition is closed."
