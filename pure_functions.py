class Pure:
    def __init__(self, customer_repo, third_party_prices_api, coupon_repo, product_repo):
        self.customer_repo = customer_repo
        self.third_party_prices_api = third_party_prices_api
        self.coupon_repo = coupon_repo
        self.product_repo = product_repo

    def compute_prices(self, customer_id, product_ids, internal_prices):
        customer = self.customer_repo.find_by_id(customer_id)
        # n = customer.name.upper() if customer.name else "Default Name"
        products = self.product_repo.find_all_by_id(product_ids) # fetch many products at once BUN
        # products = [self.product_repo.find_by_id(id) for id in product_ids] #PROST = N+1 query problem
        # uzual apare cand un framework/cod necunoscut le face fara sa te prinzi (Hibernate/ORM)

        product_prices = self.resolve_prices(internal_prices, products)

        # in general e dubios sa returnezi mai multe valori dintr-o functie. poti incalca principiul single responsibility
        final_prices, used_coupons = self.apply_coupons(products, customer.coupons, product_prices)

        self.coupon_repo.mark_used_coupons(customer_id, used_coupons)
        return final_prices

    def resolve_prices(self, internal_prices, products):
        return [internal_prices.get(product.id) or self.third_party_prices_api.fetch_price(product.id)
                for product in products]

    # class {}

    # functie pura, usor de testat (fara mockuri) si de inteles (fara legaturi externe, fara changeuri de stare)
    def apply_coupons(self, products, coupons, product_prices):
        used_coupons = []
        final_prices = {}
        for product in products:
            price = product_prices[product.id]
            for coupon in coupons:
                if coupon.auto_apply and coupon.is_applicable_for(product) and coupon not in used_coupons:
                    price = coupon.apply(price, product)
                    used_coupons.append(coupon)
            final_prices[product.id] = price
        return final_prices, used_coupons


# vom extrage complexitatea principala a codului intr-o fucntie pura, usor de testat si inteles.


class Repository:
    def find_by_id(self, id):
        pass

    def find_all_by_id(self, ids):
        pass

    def mark_used_coupons(self, customer_id, used_coupons):
        pass

class CustomerRepo(Repository):
    pass


class ProductRepo(Repository):
    pass


class CouponRepo(Repository):
    pass


class Customer:
    coupons: list
    name: str
    def __init__(self):
        self.coupons = []


class Product:
    def __init__(self):
        self.id = 0


class Coupon:
    def __init__(self):
        self.auto_apply = False

    def is_applicable_for(self, product):
        pass

    def apply(self, price, product):
        pass


class ThirdPartyPricesAPI:
    def fetch_price(self, id):
        pass