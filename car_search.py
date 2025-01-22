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


def years_match(car_model, criteria):
    interval1 = Interval(criteria.start_year, criteria.end_year)
    interval2 = Interval(car_model.start_year, car_model.end_year)
    return interval1.intersects(interval2)

def intervals_intersect(interval1, interval2):
    return interval1.start <= interval2.end and interval2.start <= interval1.end  # copiata cu grije din StackOverflow

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def length(self):
        return self.end - self.start

    def intersects(self, other):
        return self.start <= other.end and other.start <= self.end


def filter_car_models(criteria: CarSearchCriteria, car_models: list[CarModel]):
    matches = [car_model for car_model in car_models if years_match(car_model, criteria)]
    print("More filtering logic ...")
    return matches


def apply_capacity_filter():
    print(intervals_intersect({start:1000, end:1600},{start: 1250, end: 2000}))



class CarModelMapper:
    def to_dto(self, car_model):
        dto = CarModelDTO()
        dto.make = car_model.get_make()
        dto.model = car_model.get_model()
        dto.start_year = car_model.get_start_year()
        dto.end_year = car_model.get_end_year()
        return dto


class CarModelDTO:
    def __init__(self):
        self.make = None
        self.model = None
        self.start_year = None
        self.end_year = None
