from dataclasses import dataclass
@dataclass(frozen=True)
class Interval:
    start: int
    end: int

    def __post_init__(self):
        if self.start > self.end:
            raise ValueError("Start year is larger than end year.")
        #multe = safety: fail fast de cate ori poti, cat mai devreme
        #putin = mai reusable

    #pot si eu OOP: keep behavior close to data
    def intersects(self, other):
        return self.start <= other.end and other.start <= self.end


class CarSearchCriteria:
    def __init__(self, interval: Interval, make):
        self.make = make
        # if start_year > end_year:
        #     raise ValueError("Start year is larger than end year.")
        # self.start_year = start_year
        # self.end_year = end_year
        self.year_interval = interval

    def get_start_year(self):
        return self.start_year

    def get_end_year(self):
        return self.end_year

    def get_make(self):
        return self.make

    @property
    def year_interval(self):
        return Interval(self.start_year, self.end_year)


class CarModel:
    def __init__(self, make, model, interval: Interval):
        self.make = make
        self.model = model
        self.year_interval = interval

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


def filter_car_models(criteria: CarSearchCriteria, car_models: list[CarModel]):
    matches = [car_model for car_model in car_models
               if criteria.year_interval.intersects(car_model.year_interval)]
    print("More filtering logic ...")
    return matches


def apply_capacity_filter():
    print(Interval(2000, 1600).intersects(Interval(1250, 2000)))



class Alta:
    def apply_capacity_filter(self):
        interval_ = Interval(1000, 1600)
        interval_1 = Interval(1250, 2000)
        print(interval_.intersects(interval_1))


class CarModelMapper:
    def to_dto(self, car_model:CarModel):
        dto = CarModelDTO()
        dto.make = car_model.get_make()
        dto.model = car_model.get_model()
        # dto.start_year = car_model.get_start_year()
        dto.start_year = car_model.year_interval.start
        dto.end_year = car_model.get_end_year()
        return dto


class CarModelDTO:
    def __init__(self):
        self.make = None
        self.model = None
        self.start_year = None
        self.end_year = None
