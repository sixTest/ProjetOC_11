import unittest
from server import getClubByEmail
from exceptions import EmailNotFound


class TestFormEmail(unittest.TestCase):

    def setUp(self):
        self.clubs = [{'name': 'club_1', 'email': 'email_club_1', 'points': 1},
                      {'name': 'club_2', 'email': 'email_club_2', 'points': 2}]

    def test_exception_is_raised_if_email_does_not_exist(self):
        wrong_email = 'email_club_3'
        with self.assertRaises(EmailNotFound):
            getClubByEmail(wrong_email, self.clubs)

    def test_returned_club_if_email_does_exist(self):
        club = getClubByEmail('email_club_1', self.clubs)
        self.assertEqual(club['name'], 'club_1')


if __name__ == '__main__':
    unittest.main()