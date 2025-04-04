
def filter_car_models(criteria, car_models):
    matches = [car_model for car_model in car_models
               if intervals_intersect(
            criteria.start_year, criteria.end_year,
            car_model.start_year, car_model.end_year)]
    print("Pretend: more filtering logic ...")
    return matches

# TODO adding (*, to the signature makes params mandatory
def intervals_intersect(start1, end1, start2, end2):
    return start1 <= end2 and start2 <= end1

def apply_capacity_filter():
    print(intervals_intersect(1000, 1600, 1250, 2000))


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
        self.start_year = start_year
        self.end_year = end_year

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
