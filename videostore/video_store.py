from collections import OrderedDict

class Movie:
    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1
    def __init__(self, title, price_code):
        self._title = title
        self._price_code = price_code

    def get_price_code(self):
        return self._price_code

    def set_price_code(self, arg):
        self._price_code = arg

    def get_title(self):
        return self._title


class Customer:
    def __init__(self, name):
        self.name = name
        self.rentals = OrderedDict()

    def add_rental(self, m, d):
        self.rentals[m] = d

    def get_name(self):
        return self.name

    def statement(self):
        total_amount = 0
        frequent_rents_points = 0
        result = "Rental Record for " + self.get_name() + "\n"
        for each in self.rentals.keys():
            this_amount = 0
            dr = self.rentals[each]
            if each.get_price_code() == Movie.REGULAR:
                this_amount += 2
                if dr > 2:
                    this_amount += (dr - 2) * 1.5
                if dr > 5:
                    this_amount += (dr - 5) * 1.5
            elif each.get_price_code() == Movie.NEW_RELEASE:
                this_amount += dr * 3
            elif each.get_price_code() == Movie.CHILDRENS:
                this_amount += 1.5
                if dr > 3:
                    this_amount += (dr - 3) * 1.5
            frequent_rents_points += 1
            if (each.get_price_code() == Movie.NEW_RELEASE) and dr > 1:
                frequent_rents_points += 1
            result += "\t" + each.get_title() + "\t" + format(this_amount, '.1f')  + "\n"

            total_amount += this_amount
        result += "Amount owed is " + str(total_amount) + "\n"
        result += "You earned " + str(frequent_rents_points) + " frequent renter points"
        return result