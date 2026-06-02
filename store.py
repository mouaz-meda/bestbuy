from products import Product


class Store:
    def __init__(self, product_list: list[Product]):
        self.product_list = product_list

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
        self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        total = 0
        for p in self.product_list:
            total += p.get_quantity()
        return total

    def get_all_products(self) -> list[Product]:
        active_products = []
        for p in self.product_list:
            if p.is_active():
                active_products.append(p)
        return active_products

    def order(self, shopping_list) -> float:
        total = 0.0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total


# test
test_product_list: list[Product] = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
]

best_buy = Store(test_product_list)
test_products = best_buy.get_all_products()
print(best_buy.get_total_quantity())
print(best_buy.order([(test_products[0], 1), (test_products[1], 2)]))
