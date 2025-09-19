import abc
from dataclasses import dataclass
from datetime import date
from enum import Enum

class Country(Enum):
    UK = "UK"
    CN = "CN"
    FR = "FR"
    ES = "ES"
    RO = "RO"

@dataclass(frozen=True)
class Parcel:
    origin_country: Country
    tobacco_value: float
    regular_value: float
    date: date


# Strategy = o interfata care defineste o problema de rezolvat
# cu multe implementari ca moduri diferite de a rezolva acea problema
class TaxCalculator:
    def calculate(self, parcel: Parcel) -> float:
        raise NotImplementedError


class EUCustomsTaxCalculator(TaxCalculator):
    def calculate(self, parcel: Parcel) -> float:
        return parcel.tobacco_value / 3


class ChinaCustomsTaxCalculator(TaxCalculator):
    def calculate(self, parcel: Parcel) -> float:
        # +50 linie
        return parcel.tobacco_value + parcel.regular_value


class UKCustomsTaxCalculator(TaxCalculator):
    def calculate(self, parcel: Parcel) -> float:
        # 100+ linii in 7 metode
        return parcel.tobacco_value / 2 + parcel.regular_value

def calculate_customs_tax(parcel: Parcel) -> float:
    calculator = select_tax_calculator(parcel.origin_country)
    return calculator.calculate(parcel)


# factory method care-ti intoarce o subclasa oarecare in fct de country
def select_tax_calculator(country: Country) -> TaxCalculator:
    match country:
        case Country.UK:
            return UKCustomsTaxCalculator()
        case Country.CN:
            return ChinaCustomsTaxCalculator()
        case Country.FR | Country.ES | Country.RO:
            return EUCustomsTaxCalculator()
        case _:
            raise ValueError(f"Not a valid country ISO2 code: {parcel.origin_country}")


if __name__ == "__main__":
    print("Tax for (RO,100,100) =",
          calculate_customs_tax(Parcel(Country.RO, 100, 100, date.today())))
    print("Tax for (CN,100,100) =",
          calculate_customs_tax(Parcel(Country.CN, 100, 100, date.today())))
    print("Tax for (UK,100,100) =",
          calculate_customs_tax(Parcel(Country.UK, 100, 100, date.today())))
