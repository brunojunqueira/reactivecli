from bin.elements.Menu import Menu
from bin.elements.Input import Input
from bin.elements.Option import Option
from bin.elements.Text import Text
from bin.elements.Title import Title
from bin.elements.Element import Element
from bin.elements.Link import Link
from bin.text import color, background


def create_root(callback, dev=False):
	menu = Menu(callback, dev)
	menu.render()
