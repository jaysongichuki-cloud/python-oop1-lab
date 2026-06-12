class Coffee:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size  # e.g., 'Small', 'Medium', 'Large'
        self.price = float(price)

    def change_size(self, new_size, new_price=None):
        """Changes the size of the coffee and updates the price if provided."""
        self.size = new_size
        if new_price is not None:
            self.price = float(new_price)
        return self.size