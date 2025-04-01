from collections import OrderedDict
from dataclasses import dataclass
from enum import Enum
from typing import List

class PriceCode(Enum):
    CHILDREN = 2
    NEW_RELEASE = 1
    REGULAR = 0

class Movie:
    def __init__(self, title:str, price_code:PriceCode):
        self.title = title
        self.price_code = price_code
@dataclass
class Rental:
    movie:Movie
    days_rented:int
    
    def compute_amount(self):
        this_amount = 0
        if self.movie.price_code == PriceCode.REGULAR:
            this_amount += 2
            if self.days_rented > 2:
                this_amount += (self.days_rented - 2) * 1.5
        elif self.movie.price_code == PriceCode.NEW_RELEASE:
            this_amount += self.days_rented * 3
        elif self.movie.price_code == PriceCode.CHILDREN:
            this_amount += 1.5
            if self.days_rented > 3:
                this_amount += (self.days_rented - 3) * 1.5
        return this_amount
    
    def compute_points(self):
        frequent_rents_points = 1
        if (self.movie.price_code == PriceCode.NEW_RELEASE) and self.days_rented > 1:
            frequent_rents_points += 1
        return frequent_rents_points

class Customer:
    def __init__(self, name):
        self.name = name
        self.rentals_list:List[Rental]=[] # contine Rental

    def add_rental(self, rental:Rental):
        self.rentals_list.append(rental)

    def statement(self):
        # header
        result = "Rental Record for " + self.name + "\n"

        # body
        for rental in self.rentals_list:
            result += "\t" + rental.movie.title + "\t" + format(rental.compute_amount(), '.1f')  + "\n"

        # footer
        result += f"Amount owed is {self.compute_total_amount()}\n"
        result += f"You earned {self.compute_total_points()} frequent renter points"
        return result

    def compute_total_points(self):
        # frequent_rents_points = 0
        # for rental in self.rentals_list:
        #     frequent_rents_points += rental.compute_points()
        # return frequent_rents_points

        return sum(rental.compute_points() for rental in self.rentals_list)

    def compute_total_amount(self):
        # total_amount = 0
        # for rental in self.rentals_list:
        #     total_amount += rental.compute_amount()
        # return total_amount
        
        return sum(rental.compute_amount() for rental in self.rentals_list)



   