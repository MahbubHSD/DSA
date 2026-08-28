# Leetcode Problem 1472: Design Browser History


class BrowserHistory:
    """Browser history supporting visit, back, and forward operations."""

    def __init__(self, homepage):
        self.history = [homepage]
        self.current = 0

    def visit(self, url):
        self.history = self.history[:self.current + 1] + [url]
        self.current += 1

    def back(self, steps):
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps):
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]


if __name__ == "__main__":
    browser = BrowserHistory("leetcode.com")
    browser.visit("google.com")
    print(f"Current page: {browser.back(1)}")