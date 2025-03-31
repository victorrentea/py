RETIRED_AMOUNT = 2
DEAD_PAY_AMOUNT = 1

def get_pay_amount(self, marine, bonus_package):
    if marine is None: #guard
        raise ValueError("Not applicable!") # early throw
    if marine.dead: 
        return DEAD_PAY_AMOUNT #early return
    # if not (not marine.retired and (bonus_package.value < 100 or bonus_package.value > 10)):
    # if marine.retired or not (bonus_package.value < 100 or bonus_package.value > 10):
    # if marine.retired or (bonus_package.value >= 100 and bonus_package.value <= 10):
    if marine.retired: # suna Produsu
        return RETIRED_AMOUNT
    if marine.years_service is None:
        raise ValueError("Any marine should have the years of service set.")

    result = marine.years_service * 100 + bonus_package.value
    if len(marine.awards) != 0:
        result += 1000
    if len(marine.awards) >= 3:
        result += 2000

    return result

    # if len(marine.awards) >= 3:
    #     result += 3000
    # elif len(marine.awards) != 0:
    #     result += 1000
        
#    if len(marine.awards) != 0 and len(marine.awards) < 3:
#         result += 1000
#     if len(marine.awards) >= 3:
#         result += 3000
    
        
   


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
