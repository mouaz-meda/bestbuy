class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def __str__(self):
        return f"**{self.name}, Price: {self.price}, Quantity: {self.quantity}**"

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive.")
        if quantity > self.quantity:
            raise ValueError("Quantity larger than what exists in stock.")
        if not self.active:
            raise Exception("Product is not active.")

        self.set_quantity(self.quantity - quantity)
        return float(self.price * quantity)
