from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Parcel:
    origin_country: str
    tobacco_value: float
    regular_value: float
    date: date


def calculate_customs_tax(parcel: Parcel) -> float:
    match parcel.origin_country:
        case "UK":
            return UKCustomsTaxCalculator.calculate(parcel)
        case "CN":
            return ChinaCustomsTaxCalculator.calculate(parcel)
        case "FR" | "ES" | "RO":
            return EUCustomsTaxCalculator.calculate(parcel)
        case _:
            raise ValueError(f"Not a valid country ISO2 code: {parcel.origin_country}")


class EUCustomsTaxCalculator:
    @staticmethod
    def calculate(parcel: Parcel) -> float:
        return parcel.tobacco_value / 3


class ChinaCustomsTaxCalculator:
    @staticmethod
    def calculate(parcel: Parcel) -> float:
        # +50 linie
        return parcel.tobacco_value + parcel.regular_value


class UKCustomsTaxCalculator:
    @staticmethod
    def calculate(parcel: Parcel) -> float:
        # 100+ linii in 7 metode
        return parcel.tobacco_value / 2 + parcel.regular_value


if __name__ == "__main__":
    print("Tax for (RO,100,100) =",
          calculate_customs_tax(Parcel("RO", 100, 100, date.today())))
    print("Tax for (CN,100,100) =",
          calculate_customs_tax(Parcel("CN", 100, 100, date.today())))
    print("Tax for (UK,100,100) =",
          calculate_customs_tax(Parcel("UK", 100, 100, date.today())))
