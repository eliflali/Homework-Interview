"""
This module contains a class to
arrange HTML operations.

Author: Elif Lale
"""

from bs4 import BeautifulSoup

class HtmlPage:
  """
  A utility class for creating and rendering HTML pages.

  This class allows you to easily create HTML pages 
  and add content like headings (h1) and paragraphs (p).
  After adding content, you can render the HTML page to a file.

  Args:
      filename (str): The name of the HTML file to be generated.

  Attributes:
      filename (str): The name of the HTML file.
      html (BeautifulSoup): The BeautifulSoup object 
                            representing the HTML content.
      body (Tag): The HTML body tag where content is added.

  Example:
      Create an HtmlPage object, add content, and render the HTML to a file.

      >>> html = HtmlPage("output.html")
      >>> html.add_h1("Welcome to My Website")
      >>> html.add_p("This is a sample paragraph.")
      >>> html.render()
  """

  def __init__(self, filename):
    """
    Initialize a new HtmlPage.

    Args:
        filename (str): The name of the HTML file to be generated.
    """
    self.filename = filename
    self.html = BeautifulSoup('', 'html.parser')
    self.body = self.html.new_tag('body')
    self.html.append(self.body)

  def add_h1(self, text):
    """
    Add an <h1> (heading 1) element to the HTML page.

    Args:
        text (str): The text content of the heading.

    Example:
        >>> html.add_h1("About Me")
    """
    h1 = self.html.new_tag('h1')
    h1.string = text
    self.body.append(h1)

  def add_p(self, text):
    """
    Add a <p> (paragraph) element to the HTML page.

    Args:
        text (str): The text content of the paragraph.

    Example:
        >>> html.add_p("I enjoy programming and writing code.")
    """
    p = self.html.new_tag('p')
    p.string = text
    self.body.append(p)

  def render(self):
    """
    Render the HTML content to the specified file.

    Example:
        >>> html.render()
    """
    with open(self.filename, 'w', encoding='utf-8') as file:
      file.write(str(self.html))
