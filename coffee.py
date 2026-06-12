class Coffee:
    def __init__(self, size, price=5.00):
        # Validate size per rubric requirements
        if size not in ["Small", "Medium", "Large"]:
            print("size must be Small, Medium, or Large")
            
        self.size = size
        self.price = float(price)
        self.status = "ordered"

    def tip(self):
        """Adds 1 to the price of the coffee."""
        self.price += 1.00
        return self.price