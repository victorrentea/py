import unittest

from video_store import Customer, Movie

class CustomerTest(unittest.TestCase):
    def test_something(self):
        customer = Customer("John Doe")
        customer.add_rental(Movie("Star Wars", Movie.NEW_RELEASE), 6)
        customer.add_rental(Movie("Sofia", Movie.CHILDRENS), 7)
        customer.add_rental(Movie("Inception", Movie.REGULAR), 5)

        expected = "Rental Record for John Doe\n" \
                   + "\tStar Wars\t18.0\n" \
                   + "\tSofia\t7.5\n" \
                   + "\tInception\t6.5\n" \
                   + "Amount owed is 32.0\n" \
                   + "You earned 4 frequent renter points"

        self.assertEqual(expected, customer.statement())


if __name__ == '__main__':
    unittest.main()