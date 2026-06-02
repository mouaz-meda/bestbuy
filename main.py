from products import Product
from store import Store


def create_product_list(products: list[Product]):
    for i, p in enumerate(products, 1):
        print(f"{i}. ", end="")
        p.show()


def make_order(store):
    products = store.get_all_products()
    print("------")
    create_product_list(products)
    print("------")
    print("When you want to finish order, enter empty text.")

    shopping_list = []

    while True:
        product_input = input("Which product # do you want? ").strip()
        if product_input == "":
            break

        quantity_input = input("What amount do you want? ").strip()
        if quantity_input == "":
            break

        try:
            product_num = int(product_input)
            quantity = int(quantity_input)

            if product_num < 1 or product_num > len(products):
                print("Invalid product number, please try again!")
                continue

            selected_product = products[product_num - 1]

            if quantity <= 0:
                print("Quantity must be at least 1, please try again!")
                continue

            if quantity > selected_product.get_quantity():
                print(f"Not enough stock! Only {selected_product.get_quantity()} available.")
                continue

            shopping_list.append((selected_product, quantity))
            print("Product added to list!")

        except ValueError:
            print("Please enter valid numbers!")

    if shopping_list:
        total = store.order(shopping_list)
        print(f"********\nOrder made! Total payment: ${total}")


def start(store):
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ").strip()

        if choice == "1":
            create_product_list(store.get_all_products())
        elif choice == "2":
            print(f"Total of {store.get_total_quantity()} items in store")
        elif choice == "3":
            make_order(store)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", 1450, 100),
        Product("Bose QuietComfort Earbuds", 250, 500),
        Product("Google Pixel 7", 500, 250),
    ]
    best_buy = Store(product_list)
    start(best_buy)
