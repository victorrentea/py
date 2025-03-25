RETIRED_AMOUNT = 2
DEAD_PAY_AMOUNT = 1
# TODO globala + unit tests + return intai + conditie simpla prima+ fara getteri

class Guards:

    def get_pay_amount(self, marine, bonus_package):
        # if not (marine is not None and (bonus_package.get_value() > 100 or bonus_package.get_value() < 10)):
        # if marine is None or not (bonus_package.get_value() > 100 or bonus_package.get_value() < 10):
        if marine is None:
            raise ValueError("Not applicable!") #early throw scoti erorile (validezi datele)
        if bonus_package.get_value() <= 100 and bonus_package.get_value() >= 10:
            raise ValueError("Not applicable!") #early throw scoti erorile (validezi datele)
        
        if marine.dead: #guard condition
            return DEAD_PAY_AMOUNT  #early return
    
        if  marine.is_retired():
            return self.retired_amount()
        
        if marine.get_years_service() is None:
            raise ValueError("Any marine should have the years of service set.")
        
        result = marine.get_years_service() * 100 + bonus_package.get_value()
        if len(marine.get_awards()) != 0:
            result += 1000
        if len(marine.get_awards()) >= 3:
            result += 2000
        return result
           

    def retired_amount(self):
        return RETIRED_AMOUNT


class Marine:
    def __init__(self, dead, is_retired, years_of_service, awards):
        self.dead = dead
        self.retired = is_retired
        self.years_service = years_of_service
        self.awards = awards

    def is_retired(self):
        return self.retired

    def get_years_service(self):
        return self.years_service

    def get_awards(self):
        return self.awards


class BonusPackage:
    def __init__(self, v):
        self.value = v

    def get_value(self):
        return self.value


class Award:
    pass


m = Marine(False, False, 10, [Award(), Award(), Award()])
b = BonusPackage(1)
print(Guards().get_pay_amount(m, b))
