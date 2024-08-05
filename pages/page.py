from time import sleep


class Page:
    def __init__(self, browser):
        self.browser = browser

    def find_element(self, args):
        return self.browser.find_element(*args)

    def navigate_to(self, url):
        self.browser.get(url)

    def scroll_to_element(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_up(self, delay=0):
        self.browser.execute_script("window.scrollTo(0, 0);")
        sleep(delay)

    def scroll_down(self):
        return self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

