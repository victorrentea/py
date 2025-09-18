from dataclasses import dataclass
from typing import List

class CarSearchCriteria:
    def __init__(self, start_year, end_year, make):
        self.make = make
        if start_year > end_year:
            raise ValueError("Start year is larger than end year.")
        self.start_year = start_year
        self.end_year = end_year


class CarModel:
    def __init__(self, make, model, start_year, end_year):
        self.make = make
        self.model = model
        if start_year > end_year:
            raise ValueError("Start year is larger than end year.")
        self.year_range = Range(self.start_year, self.end_year)

    def __str__(self):
        return f"CarModel{{make='{self.make}', model='{self.model}'}}"

def to_dto(car_model):
    dto = CarModelDTO()
    dto.make = car_model.make
    dto.model = car_model.model
    dto.start_year = car_model.start_year
    dto.end_year = car_model.end_year
    return dto

def from_dto(dto):
    return CarModel(dto.make, dto.model, dto.start_year, dto.end_year)


class CarModelDTO:
    def __init__(self):
        self.make = None
        self.model = None
        self.start_year = None
        self.end_year = None


def filter_car_models(criteria:CarSearchCriteria, car_models:List[CarModel]):
    matches = [car_model for car_model in car_models if __matches_years(car_model, criteria)]
    print("Pretend: more filtering logic ...")
    return matches


def __matches_years(car_model:CarModel, criteria:CarSearchCriteria):
    criteria_range = Range(criteria.start_year, criteria.end_year)
    return criteria_range.intersects_with(car_model.year_range)


@dataclass(frozen=True) #immutable object, cannot change after instantiation
class Range:
    start:int
    end:int

    def intersects_with(self, other:'Range')->bool:
        return self.start <= other.end and other.start <= self.end


r1 = Range(1000, 1600)
r2 = Range(1250, 2000)
# r2.start = 1000
print(r1.intersects_with(r2))
print(f"r1 = {r1}")
