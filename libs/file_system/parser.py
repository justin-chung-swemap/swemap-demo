from .pages import Page

class Parser:
    def parse(self, text: str) -> Page:
        return Page("id", text, "system")
