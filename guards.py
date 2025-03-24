RETIRED_AMOUNT = 2
DEAD_PAY_AMOUNT = 1

def get_pay_amount(self, marine, bonus_package):
    if marine is not None :
        if not marine.dead:
            if not marine.retired and (bonus_package.value < 100 or bonus_package.value > 10):
                if marine.years_service is not None:
                    result = marine.years_service * 100 + bonus_package.value
                    if len(marine.awards) != 0:
                        result += 1000
                    if len(marine.awards) >= 3:
                        result += 2000
                    return result
                else:
                    raise ValueError("Any marine should have the years of service set.")
            else:
                return RETIRED_AMOUNT
        else:
            return DEAD_PAY_AMOUNT
    else:
        raise ValueError("Not applicable!")


class Marine:
    def __init__(self, dead, is_retired, years_of_service, awards):
        self.dead = dead
        self.retired = is_retired
        self.years_service = years_of_service
        self.awards = awards

class BonusPackage:
    def __init__(self, v):
        self.value = v

class Award:
    pass


m = Marine(False, False, 10, [Award(), Award(), Award()])
b = BonusPackage(1)
print(Guards().get_pay_amount(m, b))
