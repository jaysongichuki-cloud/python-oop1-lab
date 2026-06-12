class Book:
    def __init__(self, title, author, total_pages):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = 1  # Standard default start page

    def turn_page(self):
        """Advances the current page by 1, stopping at total_pages."""
        if self.current_page < self.total_pages:
            self.current_page += 1
        return self.current_page

    def read_to(self, page_num):
        """Jumps directly to a specific page number if it is valid."""
        if 1 <= page_num <= self.total_pages:
            self.current_page = page_num
        return self.current_page

    def reset(self):
        """Resets reading progress back to page 1."""
        self.current_page = 1
        return self.current_page