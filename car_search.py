def intervals_intersect(start1, end1, start2, end2):
    return start1 <= end2 and start2 <= end1

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def intersects(self, other):
        return self.start <= other.end and other.start <= self.end

def intervals_intersect_elena(interval1:Interval, interval2):
    return interval1.start <= interval2.end and interval2.start <= interval1.end



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

    def filter_car_models(criteria, car_models):
        matches = []
        for car_model in car_models:
            criteria_interval = Interval(criteria.start_year, criteria.end_year)
            car_model_interval = Interval(car_model.get_start_year(), car_model.get_end_year())
            if criteria_interval.intersects(car_model_interval) :
                matches.append(car_model)

        print("More filtering logic ...")
        return matches

    def apply_capacity_filter():
        print(intervals_intersect(1000, 1600, 1250, 2000))


class Alta:
    def apply_capacity_filter(self):
        print(intervals_intersect(1000, 1600, 1250, 2000))


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
