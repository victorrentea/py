import unittest
from guards import Guards


class DummyMarine:
    def __init__(self, dead=False, retired=False, years_service=None, awards=None):
        self.dead = dead
        self._retired = retired
        self._years_service = years_service
        self._awards = awards or []

    def is_retired(self):
        return self._retired

    def get_years_service(self):
        return self._years_service

    def get_awards(self):
        return self._awards


class DummyBonusPackage:
    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value


DEAD_PAY_AMOUNT = 0
RETIRED_AMOUNT = 5000


@pytest.fixture
def guards_instance():
    return Guards()


def test_get_pay_amount_valid_marine_with_awards(guards_instance):
    marine = DummyMarine(dead=False, retired=False, years_service=5, awards=["award1", "award2", "award3"])
    bonus_package = DummyBonusPackage(value=50)
    result = guards_instance.get_pay_amount(marine, bonus_package)
    assert result == 5 * 100 + 50 + 1000 + 2000


def test_get_pay_amount_no_years_service_raises_error(guards_instance):
    marine = DummyMarine(dead=False, retired=False, years_service=None)
    bonus_package = DummyBonusPackage(value=50)
    with pytest.raises(ValueError, match="Any marine should have the years of service set."):
        guards_instance.get_pay_amount(marine, bonus_package)


def test_get_pay_amount_applicable_bonus_range_error(guards_instance):
    marine = DummyMarine(dead=False, retired=False, years_service=5)
    bonus_package = DummyBonusPackage(value=5)  # Out of range (less than 10)
    with pytest.raises(ValueError, match="Not applicable!"):
        guards_instance.get_pay_amount(marine, bonus_package)


def test_get_pay_amount_dead_marine_returns_dead_amount(guards_instance):
    marine = DummyMarine(dead=True)
    bonus_package = DummyBonusPackage(value=50)
    result = guards_instance.get_pay_amount(marine, bonus_package)
    assert result == DEAD_PAY_AMOUNT


def test_get_pay_amount_retired_marine_returns_retired_amount(guards_instance):
    marine = DummyMarine(dead=False, retired=True, years_service=10)
    bonus_package = DummyBonusPackage(value=50)
    result = guards_instance.get_pay_amount(marine, bonus_package)
    assert result == RETIRED_AMOUNT
