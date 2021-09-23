
class EmailNotFound(Exception):
    def __init__(self):
        self.msg = "Sorry, that email wasn't found."

    def __str__(self):
        return self.msg
