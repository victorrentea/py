import unittest

from video_store import Customer, Movie, PriceCode, Rental


class CustomerTest(unittest.TestCase):
    def test_something(self):
        customer = Customer("John Doe")
        customer.add_rental(Rental(Movie("Star Wars", PriceCode.NEW_RELEASE), 6))
        customer.add_rental(Rental(Movie("Sofia", PriceCode.CHILDREN), 7))
        customer.add_rental(Rental(Movie("Inception", PriceCode.REGULAR), 5))

        expected = "Rental Record for John Doe\n" \
                   + "\tStar Wars\t18.0\n" \
                   + "\tSofia\t7.5\n" \
                   + "\tInception\t6.5\n" \
                   + "Amount owed is 32.0\n" \
                   + "You earned 4 frequent renter points"

        self.assertEqual(expected, customer.statement())


if __name__ == '__main__':
    unittest.main()