import unittest
import server
import exceptions
from bs4 import BeautifulSoup

class TestRenderHtml(unittest.TestCase):

    def setUp(self):
        self.app = server.app.test_client()
        self.competitions = server.loadCompetitions()
        self.clubs = server.loadClubs()

    def test_club_and_competition_appears_correctly_in_summary(self):
        rv = self.app.post('/showSummary', data={'email': 'club@test.com'})
        self.assertEqual(rv.status_code, 200)
        self.assertIn(self.clubs[0]['email'], str(rv.data))
        for comp in self.competitions:
            self.assertIn(comp['name'], str(rv.data))
            self.assertIn(f"Number of Places: {comp['numberOfPlaces']}", str(rv.data))
            self.assertIn(comp['date'], str(rv.data))

    def test_board_appear_correctly(self):
        rv = self.app.get('/Board')
        self.assertEqual(rv.status_code, 200)
        soup = BeautifulSoup(rv.data, 'html.parser')
        ltd = [ str(td) for td in soup.findAll('td') ]
        self.assertIn('club_test', ''.join(ltd))
        self.assertIn('1000', ''.join(ltd))

    def test_valid_club_and_competition_appear_on_booking_place(self):
        rv = self.app.get('/book/competition_valid_test/club_test')
        soup = BeautifulSoup(rv.data, 'html.parser')
        linput = [ str(input) for input in soup.findAll('input')]
        self.assertIn('club_test', ''.join(linput))
        self.assertIn('competition_valid_test', ''.join(linput))

    def test_login_error_appear_if_incorrect_email(self):
        rv = self.app.post('/showSummary', data={'email': 'bad_email'})
        self.assertEqual(rv.status_code, 200)
        self.assertIn(exceptions.EmailNotFound().msg, str(rv.data))

    def test_booking_error_appear_if_competition_is_closed(self):
        rv = self.app.post('/purchasePlaces', data={'club': 'club_test', 'competition':'competition_closed_test',
                                                    'places':1})
        self.assertEqual(rv.status_code, 200)
        self.assertIn(exceptions.CompetitionIsClosed().msg, str(rv.data))

    def test_booking_error_appear_if_competition_have_not_enough_places(self):
        rv = self.app.post('/purchasePlaces', data={'club': 'club_test', 'competition':'competition_not_enough_places_test',
                                                    'places':2})
        self.assertEqual(rv.status_code, 200)
        self.assertIn(exceptions.CompetitionNotEnoughPlaces().msg, str(rv.data))

    def test_booking_error_appear_if_club_have_not_enough_points(self):
        rv = self.app.post('/purchasePlaces', data={'club': 'club_test', 'competition':'competition_club_not_enough_points_test',
                                                    'places':1001})
        self.assertEqual(rv.status_code, 200)
        self.assertIn(exceptions.ClubNotEnoughPoints().msg, str(rv.data))

    def test_booking_error_appear_if_number_of_places_required_are_greater_than_booking_limit_places(self):
        rv = self.app.post('/purchasePlaces', data={'club': 'club_test', 'competition':'competition_booking_limit_places_test',
                                                    'places':13})
        self.assertEqual(rv.status_code, 200)
        self.assertIn(exceptions.BookingLimitPlaces().msg, str(rv.data))

    def test_error_not_appear_if_all_parameters_are_valid(self):
        rv = self.app.post('/purchasePlaces', data={'club': 'club_test', 'competition':'competition_valid_test',
                                                    'places':1})
        self.assertEqual(rv.status_code, 200)


if __name__ == '__main__':
    unittest.main()