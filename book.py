class Coffee:
    def __init__(self, size, status="ordered"):
        # Validate size before assigning
        if size not in ["Small", "Medium", "Large"]:
            print("size must be Small, Medium, or Large")
        
        self.size = size
        self.status = status
        self.price = 5.00  # Default base price to allow for a tip method

    def tip(self):
        """Adds 1 to the price of the coffee."""
        self.price += 1.00
        return self.price