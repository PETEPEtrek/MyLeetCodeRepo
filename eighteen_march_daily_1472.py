class BrowserHistory:

    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.current_page = 1

    def visit(self, url: str) -> None:
        if self.current_page == len(self.urls):
            self.urls.append(url)
            self.current_page += 1
        else:
            self.urls = self.urls[:self.current_page]
            self.urls.append(url)
            self.current_page += 1

    def back(self, steps: int) -> str:
        self.current_page -= min(self.current_page - 1, steps)
        return self.urls[self.current_page - 1]

    def forward(self, steps: int) -> str:
        self.current_page += min(len(self.urls) - self.current_page, steps)
        return self.urls[self.current_page - 1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
