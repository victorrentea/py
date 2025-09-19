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
            return parcel.tobacco_value / 2 + parcel.regular_value
        case "CN":
            return parcel.tobacco_value + parcel.regular_value
        case "FR" | "ES" | "RO":
            return parcel.tobacco_value / 3
        case _:
            raise ValueError(f"Not a valid country ISO2 code: {parcel.origin_country}")


if __name__ == "__main__":
    print("Tax for (RO,100,100) =",
          calculate_customs_tax(Parcel("RO", 100, 100, date.today())))
    print("Tax for (CN,100,100) =",
          calculate_customs_tax(Parcel("CN", 100, 100, date.today())))
    print("Tax for (UK,100,100) =",
          calculate_customs_tax(Parcel("UK", 100, 100, date.today())))
