import unittest
import os
import sys

# Ensure project root is on sys.path when tests are run from repository root or elsewhere
CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from pure_functions import Pure, Product, Coupon


class FakeProduct(Product):
    def __init__(self, pid, name=None):
        super().__init__()
        self.id = pid
        self.name = name or f"P{pid}"


class FakeCoupon(Coupon):
    def __init__(self, name, auto_apply=True, predicate=None, transform=None):
        super().__init__()
        self.name = name
        self.auto_apply = auto_apply
        # predicate: (product) -> bool
        # transform: (price, product) -> price
        self._predicate = predicate or (lambda p: True)
        self._transform = transform or (lambda price, p: price)

    def __repr__(self):
        return f"FakeCoupon({self.name})"

    def is_applicable_for(self, product):
        return self._predicate(product)

    def apply(self, price, product):
        return self._transform(price, product)


class TestApplyCoupons(unittest.TestCase):
    def setUp(self):
        # We don't use other dependencies for apply_coupons tests
        self.pure = Pure(customer_repo=None, third_party_prices_api=None, coupon_repo=None, product_repo=None)

    def test_applies_single_coupon_when_applicable_and_auto(self):
        # Given
        p1 = FakeProduct(1)
        p2 = FakeProduct(2)
        initial_prices = {1: 100.0, 2: 200.0}
        # 10% off only for product id 1
        c1 = FakeCoupon(
            name="10% off P1",
            auto_apply=True,
            predicate=lambda prod: prod.id == 1,
            transform=lambda price, prod: round(price * 0.9, 2),
        )

        # When
        final_prices, used = self.pure.apply_coupons([c1], initial_prices, [p1, p2])

        # Then
        self.assertEqual(final_prices[1], 90.0)
        self.assertEqual(final_prices[2], 200.0)
        self.assertEqual(used, [c1])

    def test_coupon_used_at_most_once_even_if_applicable_to_multiple_products(self):
        # Given
        p1 = FakeProduct(1)
        p2 = FakeProduct(2)
        initial_prices = {1: 50.0, 2: 80.0}
        # Flat 5 off for any product, but should be applied only once overall
        c1 = FakeCoupon(
            name="-5 once",
            auto_apply=True,
            predicate=lambda prod: True,
            transform=lambda price, prod: price - 5,
        )

        # When
        final_prices, used = self.pure.apply_coupons([c1], initial_prices, [p1, p2])

        # Then: applied to first product in iteration order, not to second
        self.assertEqual(final_prices[1], 45.0)
        self.assertEqual(final_prices[2], 80.0)
        self.assertEqual(used, [c1])

    def test_multiple_coupons_chain_if_applicable_and_not_used_before(self):
        # Given
        p1 = FakeProduct(1)
        initial_prices = {1: 100.0}
        c_percent = FakeCoupon(
            name="-10%",
            auto_apply=True,
            predicate=lambda prod: True,
            transform=lambda price, prod: round(price * 0.9, 2),
        )
        c_fixed = FakeCoupon(
            name="-7",
            auto_apply=True,
            predicate=lambda prod: True,
            transform=lambda price, prod: price - 7,
        )

        # When
        final_prices, used = self.pure.apply_coupons([c_percent, c_fixed], initial_prices, [p1])

        # Then: first 10% off => 90, then -7 => 83
        self.assertEqual(final_prices[1], 83.0)
        self.assertEqual(used, [c_percent, c_fixed])

    def test_not_auto_apply_coupons_are_ignored(self):
        # Given
        p1 = FakeProduct(1)
        initial_prices = {1: 100.0}
        c1 = FakeCoupon(
            name="ignored",
            auto_apply=False,
            predicate=lambda prod: True,
            transform=lambda price, prod: 0.0,  # would zero price, but should not be applied
        )

        # When
        final_prices, used = self.pure.apply_coupons([c1], initial_prices, [p1])

        # Then
        self.assertEqual(final_prices[1], 100.0)
        self.assertEqual(used, [])


if __name__ == "__main__":
    unittest.main()
