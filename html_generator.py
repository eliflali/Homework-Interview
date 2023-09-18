from bs4 import BeautifulSoup

class HtmlPage:
    def __init__(self, filename):
        self.filename = filename
        self.html = BeautifulSoup('', 'html.parser')
        self.body = self.html.new_tag('body')
        self.html.append(self.body)

    def add_h1(self, text):
        h1 = self.html.new_tag('h1')
        h1.string = text
        self.body.append(h1)

    def add_p(self, text):
        p = self.html.new_tag('p')
        p.string = text
        self.body.append(p)

    def render(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write(str(self.html))
