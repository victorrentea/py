from gc import freeze


class CarSearchCriteria:  # = DTO vine ca JSON pe POST /search
    def __init__(self, start_year, end_year, make):
        self.make = make

        self.start_year = start_year
        self.end_year = end_year
        self.year_interval = Interval(start_year, end_year)


class CarModel:
    def __init__(self, make, model, year_interval: Interval):  # a propovaduit clasa noua altor tari
        self.make = make
        self.model = model
        if year_interval.start > year_interval.end:
            raise ValueError("Start year is larger than end year.")
        self.year_interval = year_interval

    def __str__(self):
        return f"CarModel{{make='{self.make}', model='{self.model}'}}"


def filter_car_models(criteria: CarSearchCriteria, car_models: list[CarModel]):
    matches = [car for car in car_models
               if criteria.year_interval.intersects(car.year_interval)]
    print("Pretend: more filtering logic ...")
    return matches


# list = [1, 2, 3]

# produs = reduce(mul, list, 1) 💖FP
#
# produs=1
# for e in list:
#     produs = produs * e

# TODO adding (*, to the signature makes params mandatory

# class Interval:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

# Value Object = obiect mic care reprezinta niste date cu sent impreuna
# Money(amount,currency)
# Target(hostname,port)
@dataclass(frozen=True)
class Interval:
    start: int
    end: int

    # def __init__(self, start, end):
    #     if start_year > end_year:
    #         raise ValueError("Start year is larger than end year.")

    # am facut OOP: am pus logica LANGA date, daca lucra doar cu datele claise asteia !
    def intersects(self: Interval, other: Interval):
        # self.start += 1 nu mai merge
        return self.start <= other.end and other.start <= self.end

    def length(self):
        return self.end - self.start


def apply_capacity_filter(i: Interval):
    print(i.intersects(Interval(1250, 2000)))


pr = [p for p in range(2, n + 1) if all(p % q for q in range(2, int(p ** 0.5) + 1))]


def f():
    x = 1
    print("halo")
    return 1
    print("halo")
    

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
