from dataclasses import dataclass
from typing import List

# Value Object: grupezi date care au sens impreuna (se misca impreuna)`
#  intr-un obiect imutabil (readonly)
@dataclass(frozen=True)
class Interval:
    start: int
    end: int

    def intersects(self, other:Interval):
        return self.start <= other.end and other.start <= self.end

# def intervals_intersect(interval1: Interval, interval2: Interval):
#     return interval1.start <= interval2.end and interval2.start <= interval1.end #copiata cu grije de pe SO 

class CarSearchCriteria:
    def __init__(self, start_year, end_year, make):
        self.make = make
        if start_year > end_year:
            raise ValueError("Start year is larger than end year.")
        self.start_year = start_year
        self.end_year = end_year

    def get_start_year(self):
        return self.start_year

    def get_end_year(self):
        return self.end_year

    def get_make(self):
        return self.make


class CarModel:
    def __init__(self, make, model, start_year, end_year):
        self.make = make
        self.model = model
        if start_year > end_year:
            raise ValueError("Start year is larger than end year.")
        self.start_year = start_year
        self.end_year = end_year


    def get_year_interval(self):
        return Interval(self.start_year, self.end_year)
    @property
    def year_interval(self):
        return Interval(self.start_year, self.end_year)
    
    def get_end_year(self):
        self.make = 2
        return self.end_year

    def get_start_year(self):
        return self.start_year

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def __str__(self):
        return f"CarModel{{make='{self.make}', model='{self.model}'}}"
    def apply_capacity_filter():
        print(Interval(1000, 1600).intersects(Interval(1250, 2000)))






def filter_car_models(criteria:CarSearchCriteria, car_models:List[CarModel]):
    # matches = [car_model for car_model in car_models
    #             if intervals_intersect(
    #                 criteria.start_year, criteria.end_year,
    #                 car_model.start_year, car_model.end_year)]
    criteria_years = Interval(criteria.start_year, criteria.end_year)
    # criteria_years.end=2
    matches = []
    for car_model in car_models:
        if criteria_years.intersects(car_model.year_interval):
            matches.append(car_model)

    print("More filtering logic ...")
    return matches




class Alta:
    def apply_capacity_filter(self):
        print(Interval(1000, 1600).intersects(Interval(1250, 2000)))


class CarModelMapper:
    def to_dto(self, car_model):
        dto = CarModelDTO()
        dto.make = car_model.get_make()
        dto.model = car_model.get_model()
        dto.start_year = car_model.get_start_year()
        dto.end_year = car_model.get_end_year()
        return dto

    def from_dto(self, dto):
        return CarModel(dto.make, dto.model, dto.start_year, dto.end_year)


class CarModelDTO:
    def __init__(self):
        self.make = None
        self.model = None
        self.start_year = None
        self.end_year = None
