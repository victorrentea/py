class Pure:
    def __init__(self, customer_repo, third_party_prices_api, coupon_repo, product_repo):
        self.customer_repo = customer_repo
        self.third_party_prices_api = third_party_prices_api
        self.coupon_repo = coupon_repo
        self.product_repo = product_repo

    def compute_prices(self, customer_id, product_ids, internal_prices):
        customer = self.customer_repo.find_by_id(customer_id) # WHERE ID = ?
        products = self.product_repo.find_all_by_id(product_ids) # WHERE ID IN (?,?...)

        initial_prices = self.resolve_initial_prices(internal_prices, products)

        # for i in range(len(products)):
            # product = products[i]
        # for product, i in products, initial_prices:

        final_prices, used_coupons = self.apply_coupons(customer, products, initial_prices)

        self.coupon_repo.mark_used_coupons(customer_id, used_coupons)
        return final_prices

    def resolve_initial_prices(self, internal_prices, products):
        initial_prices = {}
        for product in products:
            price = internal_prices.get(product.id)
            if price is None:
                price = self.third_party_prices_api.fetch_price(product.id)
            initial_prices[product.id]=price
        return initial_prices

    def apply_coupons(self, customer, products, initial_prices):
        used_coupons = []
        final_prices = {}
        for product in products:
            price = initial_prices[product.id]
            final_price = self.apply_coupons(customer.coupons, used_coupons, product, price)
            for coupon in customer.coupons:
                if coupon.auto_apply and coupon.is_applicable_for(product) and coupon not in used_coupons:
                    price = coupon.apply(price, product)
                    used_coupons.append(coupon)
            final_prices[product.id] = final_price
        return final_prices, used_coupons

       



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